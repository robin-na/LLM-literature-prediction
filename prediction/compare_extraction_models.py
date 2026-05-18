"""Compare GPT-4.1 vs Sonnet 4.6 extractions on every extracted field.

Approach
--------
1.  **Granularity check** — count how many condition rows each model extracted
    per paper.  Papers where the two models disagree on the number of
    conditions are set aside; the mismatch rate is a standalone metric.

2.  **Condition-level comparison** — for papers where the models agree on
    condition count, conditions are aligned within each paper using semantic
    similarity of ``data_id`` strings (Hungarian algorithm on cosine similarity
    of text-embedding-3-small embeddings; falls back to alphabetical sort when
    embeddings are unavailable), then compared field-by-field using type-aware
    rules:

        binary / categorical : exact match after normalisation
        numeric continuous   : within 5 % relative tolerance
        text                 : OpenAI embedding cosine similarity >= 0.95

3.  **Missing handling** — values matching MISSING_TOKENS are treated as
    absent.  Per-field summaries decompose into both-missing, one-missing,
    and both-present so that "trivial N/A agreement" is visible.

Writes (under --output-dir):
    agreement.csv                   — per-field condition-level agreement
    disagreements.csv               — every disagreeing (paper, condition, field)
    disagreement_papers_by_field.md — browsable per-field paper lists
    experiment_counts.csv           — per-paper condition counts per model
    agreement.png                   — per-field agreement bar chart
    granularity_disagreement.png    — condition-count disagreement diagnostics
"""

from __future__ import annotations

import argparse
import os
import pickle
from pathlib import Path

from scipy.optimize import linear_sum_assignment

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DEFAULT_GPT41 = [
    "extraction/output_xlsx/simple_batch_197papers_gpt41.xlsx",
    "extraction/output_xlsx/simple_batch_810papers_v2.xlsx",
]
DEFAULT_SONNET46 = [
    "extraction/output_xlsx/simple_batch_197papers_sonnet46_combined.xlsx",
    "extraction/output_xlsx/simple_batch_810papers_sonnet46_combined.xlsx",
]

BINARY_FIELDS = {
    "METHOD_empirical", "METHOD_experiment", "METHOD_lab",
    "METHOD_simulation", "METHOD_analytical",
    "CONFIG_allOrNothing", "CONFIG_chat",
    "CONFIG_showOtherSummaries", "CONFIG_showPunishmentId",
    "CONFIG_showRewardId", "CONFIG_showNRounds",
    "CONFIG_punishmentExists", "CONFIG_rewardExists",
    "DV_efficiencyReported",
    "source_data", "experiment_environment",
}
NUMERIC_FIELDS = {
    "CONFIG_playerCount", "CONFIG_numRounds",
    "CONFIG_defaultContribProp", "CONFIG_MPCR",
    "CONFIG_punishmentCost", "CONFIG_punishmentTech",
    "CONFIG_rewardCost", "CONFIG_rewardTech",
    "CONFIG_endowment",
    "number_IVs", "number_DVs",
}
TEXT_FIELDS = {
    "data_id", "indep_var", "IVs", "DVs", "DVs_Definitions",
    "participant_country", "participant_age",
    "participant_gender", "participant_education",
    "other_game_info",
}

NUMERIC_TOLERANCE = 0.05
NUMERIC_ABS_FLOOR = 0.01   # values within this absolute diff also agree (protects tiny numbers)
TEXT_COSINE_THRESHOLD = 0.70  # lowered from 0.95: allows paraphrases, blocks genuinely different content
EMBED_MODEL = "text-embedding-3-small"
EMBED_BATCH = 256

MISSING_TOKENS = {"", "nan", "none", "n/a", "n/r", "na", "null"}


def field_type(field: str) -> str:
    if field in BINARY_FIELDS: return "binary"
    if field in NUMERIC_FIELDS: return "numeric"
    if field in TEXT_FIELDS: return "text"
    return "binary"


# ---------------------------------------------------------------------------
# Value normalisation (single cell values)
# ---------------------------------------------------------------------------

def normalize_value(v, ftype: str):
    """Normalise a single cell value.  Returns None if missing."""
    if pd.isna(v):
        return None
    s = str(v).strip()
    if s.lower() in MISSING_TOKENS:
        return None
    if ftype == "binary":
        low = s.lower()
        if low in {"true", "yes"}: return "1"
        if low in {"false", "no"}: return "0"
        try:
            f = float(s)
            return str(int(f)) if f.is_integer() else str(f)
        except ValueError:
            return s
    if ftype == "numeric":
        try:
            return float(s)
        except ValueError:
            return s.lower()
    return s if s else None


def compare_values(
    a_raw, b_raw, ftype: str, embeddings: dict | None = None,
    text_threshold: float = TEXT_COSINE_THRESHOLD,
) -> tuple[bool, bool, bool]:
    """Compare two raw cell values.  Returns (ok, a_missing, b_missing)."""
    a = normalize_value(a_raw, ftype)
    b = normalize_value(b_raw, ftype)
    a_miss = a is None
    b_miss = b is None
    if a_miss and b_miss:
        return True, True, True
    if a_miss or b_miss:
        return False, a_miss, b_miss
    if ftype == "binary":
        return a == b, False, False
    if ftype == "numeric":
        if isinstance(a, str) or isinstance(b, str):
            return a == b, False, False
        abs_diff = abs(a - b)
        if abs_diff <= NUMERIC_ABS_FLOOR:
            return True, False, False
        denom = max(abs(a), abs(b), 1e-12)
        return abs_diff / denom <= NUMERIC_TOLERANCE, False, False
    # text: cosine similarity with configurable threshold
    if embeddings and a in embeddings and b in embeddings:
        return cosine(embeddings[a], embeddings[b]) >= text_threshold, False, False
    return a == b, False, False


def display_value(v) -> str:
    if pd.isna(v):
        return "MISSING"
    s = str(v).strip()
    if s.lower() in MISSING_TOKENS:
        return "MISSING"
    return s


# ---------------------------------------------------------------------------
# Loading and condition alignment
# ---------------------------------------------------------------------------

def load_raw_rows(paths: list[str], fields: list[str]) -> dict[str, list[dict]]:
    """Load all extraction rows grouped by custom_id."""
    frames = [pd.read_excel(p, sheet_name="extractions") for p in paths]
    df = pd.concat(frames, ignore_index=True)
    keep = [c for c in ["custom_id"] + fields if c in df.columns]
    result: dict[str, list[dict]] = {}
    for custom_id, group in df[keep].groupby("custom_id", dropna=False):
        result[str(custom_id)] = group.to_dict("records")
    return result


def align_conditions(
    gpt_rows: list[dict], sonnet_rows: list[dict],
    embeddings: dict[str, np.ndarray] | None = None,
) -> list[tuple[dict, dict]]:
    """Pair conditions 1-to-1 using semantic similarity (Hungarian algorithm).

    Falls back to alphabetical data_id sort when embeddings are unavailable
    or when there is only one condition per paper (no choice to make).
    """
    key = lambda r: str(r.get("data_id", "") or "").lower()
    if embeddings is None or len(gpt_rows) <= 1:
        return list(zip(sorted(gpt_rows, key=key), sorted(sonnet_rows, key=key)))

    g_ids = [str(r.get("data_id", "") or "") for r in gpt_rows]
    s_ids = [str(r.get("data_id", "") or "") for r in sonnet_rows]
    n = len(gpt_rows)

    # Build n×n cosine-similarity matrix
    sim = np.zeros((n, n), dtype=np.float32)
    for i, gid in enumerate(g_ids):
        ge = embeddings.get(gid)
        if ge is None:
            continue
        for j, sid in enumerate(s_ids):
            se = embeddings.get(sid)
            if se is not None:
                sim[i, j] = cosine(ge, se)

    # Hungarian algorithm: maximise total similarity (minimise negative)
    row_ind, col_ind = linear_sum_assignment(-sim)
    return [(gpt_rows[r], sonnet_rows[c]) for r, c in zip(row_ind, col_ind)]


# ---------------------------------------------------------------------------
# Comparators
# ---------------------------------------------------------------------------

def cosine(u: np.ndarray, v: np.ndarray) -> float:
    nu = np.linalg.norm(u); nv = np.linalg.norm(v)
    if nu == 0.0 or nv == 0.0: return 0.0
    return float(np.dot(u, v) / (nu * nv))


# ---------------------------------------------------------------------------
# Embedding helpers
# ---------------------------------------------------------------------------

def load_dotenv() -> None:
    env_path = Path(".env")
    if not env_path.exists():
        env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists(): return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k, v = line.split("=", 1)
        k = k.strip(); v = v.strip().strip('"').strip("'")
        if k and k not in os.environ: os.environ[k] = v


def get_embeddings(texts: list[str], cache_path: Path) -> dict[str, np.ndarray]:
    cache: dict[str, np.ndarray] = {}
    if cache_path.exists():
        with cache_path.open("rb") as fh:
            cache = pickle.load(fh)
    needed = sorted({t for t in texts if t and t not in cache})
    if not needed:
        return cache
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set; needed to embed text fields.")
    from openai import OpenAI
    client = OpenAI()
    print(f"Embedding {len(needed)} new texts via {EMBED_MODEL}...")
    for i in range(0, len(needed), EMBED_BATCH):
        chunk = needed[i:i + EMBED_BATCH]
        resp = client.embeddings.create(model=EMBED_MODEL, input=chunk)
        for text, item in zip(chunk, resp.data):
            cache[text] = np.array(item.embedding, dtype=np.float32)
        print(f"  {min(i + EMBED_BATCH, len(needed))}/{len(needed)}")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("wb") as fh:
        pickle.dump(cache, fh)
    return cache


# ---------------------------------------------------------------------------
# Diagnostics: per-paper experiment counts
# ---------------------------------------------------------------------------

def experiment_counts(paths: list[str]) -> pd.DataFrame:
    """Per-paper number of condition rows pooled across the model's workbooks."""
    frames = [pd.read_excel(p, sheet_name="extractions")[["custom_id"]] for p in paths]
    df = pd.concat(frames, ignore_index=True)
    return df.groupby("custom_id").size().reset_index(name="n_experiments")


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

TYPE_COLORS = {"binary": "#4c78a8", "numeric": "#f58518", "text": "#54a24b"}


def plot(
    summary: pd.DataFrame,
    n_papers: int,
    n_conditions: int,
    output: Path,
    text_threshold: float = TEXT_COSINE_THRESHOLD,
) -> None:
    """Two bars per field: overall agreement (lighter) and present-only (darker)."""
    s = summary.sort_values("agreement_rate", ascending=True).reset_index(drop=True)
    colors = [TYPE_COLORS[t] for t in s["type"]]
    fig, ax = plt.subplots(figsize=(15, max(6, 0.45 * len(s) + 1.5)))
    y = np.arange(len(s))
    bar_h = 0.38
    overall = s["agreement_rate"].to_numpy()
    present = s["agreement_rate_present"].fillna(0.0).to_numpy()
    ax.barh(y + bar_h / 2, overall, height=bar_h, color=colors, alpha=0.45)
    ax.barh(y - bar_h / 2, present, height=bar_h, color=colors)
    ax.set_yticks(y)
    ax.set_yticklabels(s["field"], fontsize=10)
    ax.set_ylim(-0.7, len(s) - 0.3)
    ax.set_xlim(0, 1.32)
    ax.set_xticks(np.linspace(0, 1, 6))
    ax.set_xlabel("Fraction of condition pairs where GPT-4.1 and Sonnet 4.6 agree")
    ax.set_title(
        f"GPT-4.1 vs Sonnet 4.6 — field-level agreement across {n_conditions} condition pairs "
        f"({n_papers} papers)\n"
        f"binary: exact match | numeric: ±5% or ±{NUMERIC_ABS_FLOOR} abs | "
        f"text: cosine ≥ {text_threshold} (semantic similarity)",
    )
    ax.axvline(1.0, color="gray", linewidth=0.5, linestyle="--")
    for i, row in s.iterrows():
        present_str = (
            f"{row['agreement_rate_present']:.2f}"
            if pd.notna(row["agreement_rate_present"]) else "n/a"
        )
        ax.text(
            max(row["agreement_rate"], row["agreement_rate_present"] or 0) + 0.01,
            i,
            f"{row['agreement_rate']:.2f} → {present_str} "
            f"({row['pct_both_missing']*100:.0f}% N/A)",
            va="center", fontsize=9,
        )
    # Legend 1: bar shade — place below the axes, outside the plot
    shade_handles = [
        plt.Rectangle((0, 0), 1, 1, color="gray", alpha=0.45),
        plt.Rectangle((0, 0), 1, 1, color="gray"),
    ]
    leg1 = ax.legend(
        shade_handles,
        [
            "Top bar: agreement across ALL pairs (N/A+N/A counts as agreement — "
            "can look inflated for sparse fields)",
            "Bottom bar: agreement when BOTH models gave a value — "
            "the more meaningful number",
        ],
        loc="upper center", bbox_to_anchor=(0.5, -0.04),
        ncol=1, framealpha=0.9, fontsize=9,
        title="What each bar shows",
    )
    ax.add_artist(leg1)
    # Legend 2: field type — also below, to the right of leg1
    type_handles = [plt.Rectangle((0, 0), 1, 1, color=TYPE_COLORS[t])
                    for t in ("binary", "numeric", "text")]
    ax.legend(type_handles, ["Binary (yes/no)", "Numeric", "Text (semantic)"],
              loc="upper center", bbox_to_anchor=(0.5, -0.09),
              ncol=3, framealpha=0.9, fontsize=9, title="Field type")
    fig.subplots_adjust(left=0.28, right=0.97, top=0.88, bottom=0.14)
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_experiment_count_disagreement(counts: pd.DataFrame, output: Path) -> None:
    """Visualize how often models disagree on per-paper condition counts."""
    delta = counts["delta"].astype(int)
    abs_delta = delta.abs()
    n = len(counts)

    delta_counts = delta.value_counts().sort_index()

    bins = ["0", "1", "2", "3-5", "6-10", "11+"]
    bucket_values = {
        "0": int((abs_delta == 0).sum()),
        "1": int((abs_delta == 1).sum()),
        "2": int((abs_delta == 2).sum()),
        "3-5": int(((abs_delta >= 3) & (abs_delta <= 5)).sum()),
        "6-10": int(((abs_delta >= 6) & (abs_delta <= 10)).sum()),
        "11+": int((abs_delta >= 11).sum()),
    }

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 5.5))

    colors = ["#d95f02" if x < 0 else "#7570b3" if x > 0 else "#7f7f7f"
              for x in delta_counts.index]
    ax_left.bar(delta_counts.index.astype(str), delta_counts.values, color=colors)
    ax_left.set_xlabel("delta = sonnet46_conditions − gpt41_conditions")
    ax_left.set_ylabel("Number of papers")
    ax_left.set_title("Signed condition-count differences")
    ax_left.axvline(x=str(0), color="black", linewidth=0.8, linestyle="--", alpha=0.6)

    bar_vals = [bucket_values[b] for b in bins]
    bar_colors = ["#7f7f7f", "#4c78a8", "#4c78a8", "#f58518", "#e45756", "#b279a2"]
    ax_right.bar(bins, bar_vals, color=bar_colors)
    ax_right.set_xlabel("|delta| bucket")
    ax_right.set_ylabel("Number of papers")
    ax_right.set_title("Magnitude of granularity disagreement")
    for i, v in enumerate(bar_vals):
        ax_right.text(i, v + max(1, int(0.01 * n)), f"{v} ({v / n:.0%})",
                      ha="center", va="bottom", fontsize=9)

    n_match = int((delta == 0).sum())
    n_son_more = int((delta > 0).sum())
    n_gpt_more = int((delta < 0).sum())
    fig.suptitle(
        "GPT-4.1 vs Sonnet 4.6 — extraction granularity disagreement\n"
        f"same count: {n_match}/{n} ({n_match / n:.1%}) | "
        f"sonnet more: {n_son_more}/{n} ({n_son_more / n:.1%}) | "
        f"gpt more: {n_gpt_more}/{n} ({n_gpt_more / n:.1%})",
        y=1.03,
    )
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

NOISY_PRESENT_RATE_THRESHOLD = 0.10
MAX_PAPERS_PER_BUCKET = 50


def write_disagreements_markdown(
    disagreements_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    n_papers_total: int,
    n_papers_matching: int,
    n_papers_mismatching: int,
    n_condition_pairs: int,
    output_path: Path,
) -> None:
    lines: list[str] = [
        "# Condition-level LLM disagreement, by field",
        "",
        f"- **Total common papers:** {n_papers_total}",
        f"- **Granularity match** (same # conditions): "
        f"{n_papers_matching} ({n_papers_matching / n_papers_total:.1%})",
        f"- **Granularity mismatch** (excluded from field comparison): "
        f"{n_papers_mismatching} ({n_papers_mismatching / n_papers_total:.1%})",
        f"- **Condition pairs compared:** {n_condition_pairs}",
        "",
        "Conditions within each paper are aligned by sorting on `data_id`. "
        "Only papers with matching condition counts are compared.",
        "",
        f"Bullet lists are capped at {MAX_PAPERS_PER_BUCKET} papers per bucket; "
        "see `disagreements.csv` for the full record.",
        "",
    ]

    if disagreements_df.empty:
        lines.append("No disagreements found.")
        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    summary_lookup = summary_df.set_index("field")
    fields_with_dis = set(disagreements_df["field"].unique())

    def is_noisy(field: str) -> bool:
        meta = summary_lookup.loc[field]
        return (meta["type"] == "text"
                and pd.notna(meta["agreement_rate_present"])
                and meta["agreement_rate_present"] < NOISY_PRESENT_RATE_THRESHOLD)

    ranked = (
        summary_df.sort_values(
            ["agreement_rate_present", "agreement_rate"],
            ascending=[True, True],
            na_position="last",
        )["field"]
        .tolist()
    )
    ordered_fields = [f for f in ranked if f in fields_with_dis and not is_noisy(f)]
    noisy_fields = [f for f in ranked if f in fields_with_dis and is_noisy(f)]

    # ---- Summary table -----------------------------------------------------
    lines.append("## Summary")
    lines.append("")
    lines.append(
        "| Field | Type | Overall | Both-present | "
        "Condition-pair disagr. | One-missing | Both-missing |"
    )
    lines.append("|---|---|---:|---:|---:|---:|---:|")

    def _fmt(v: float) -> str:
        return f"{v:.2f}" if pd.notna(v) else "n/a"

    for field in ordered_fields + noisy_fields:
        meta = summary_lookup.loc[field]
        lines.append(
            f"| `{field}` | {meta['type']} | "
            f"{meta['agreement_rate']:.2f} | "
            f"{_fmt(meta['agreement_rate_present'])} | "
            f"{int(meta['n_disagree'])} | "
            f"{int(meta['n_one_missing'])} | "
            f"{int(meta['n_both_missing'])} |"
        )
    lines.append("")

    # ---- Per-field sections -----------------------------------------------
    def _emit_section(field: str) -> None:
        sub = disagreements_df[disagreements_df["field"] == field]
        meta = summary_lookup.loc[field]
        n_papers_with_dis = sub["custom_id"].nunique()
        lines.append(
            f"### {field} "
            f"({int(meta['n_disagree'])} disagreeing condition pairs "
            f"across {n_papers_with_dis} papers; "
            f"agreement {meta['agreement_rate']:.2f} overall, "
            f"{_fmt(meta['agreement_rate_present'])} on both-present)"
        )
        lines.append("")

        one_missing = sub[(sub["gpt41"] == "MISSING") | (sub["sonnet46"] == "MISSING")]
        both_present = sub.drop(one_missing.index)

        if not one_missing.empty:
            papers = sorted(one_missing["custom_id"].astype(str).unique())
            lines.append(
                f"**One-side missing ({len(one_missing)} condition pairs "
                f"across {len(papers)} papers)**"
            )
            lines.append("")
            for cid in papers[:MAX_PAPERS_PER_BUCKET]:
                n = int((one_missing["custom_id"] == cid).sum())
                lines.append(f"- `{cid}.md` ({n} conditions)")
            if len(papers) > MAX_PAPERS_PER_BUCKET:
                lines.append(
                    f"- _…and {len(papers) - MAX_PAPERS_PER_BUCKET} more "
                    "— see disagreements.csv_"
                )
            lines.append("")

        if not both_present.empty:
            papers = sorted(both_present["custom_id"].astype(str).unique())
            lines.append(
                f"**Both present, value differs ({len(both_present)} condition pairs "
                f"across {len(papers)} papers)**"
            )
            lines.append("")
            for cid in papers[:MAX_PAPERS_PER_BUCKET]:
                n = int((both_present["custom_id"] == cid).sum())
                lines.append(f"- `{cid}.md` ({n} conditions)")
            if len(papers) > MAX_PAPERS_PER_BUCKET:
                lines.append(
                    f"- _…and {len(papers) - MAX_PAPERS_PER_BUCKET} more "
                    "— see disagreements.csv_"
                )
            lines.append("")

    lines.append("## Fields by reliability (worst first)")
    lines.append("")
    for field in ordered_fields:
        _emit_section(field)

    if noisy_fields:
        lines.append(
            "## Free-text fields with near-zero both-present agreement"
        )
        lines.append("")
        lines.append(
            "These fields are unconstrained free text where exact or near-exact "
            "matching is structurally rare. Listed last since the disagreements "
            "are mostly paraphrase noise, not extraction errors."
        )
        lines.append("")
        for field in noisy_fields:
            _emit_section(field)

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Granularity correctness analysis
# ---------------------------------------------------------------------------

def _word_jaccard(a: str, b: str) -> float:
    """Token-level Jaccard similarity between two strings."""
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def analyze_granularity_mismatches(
    mismatching_ids: list[str],
    gpt_rows: dict[str, list[dict]],
    sonnet_rows: dict[str, list[dict]],
) -> pd.DataFrame:
    """For each granularity-mismatched paper, classify the nature of the mismatch.

    Uses word-Jaccard similarity between data_id strings to detect whether one
    model sub-divided the other's conditions (merging/splitting) or whether the
    condition lists are fundamentally different.

    Verdict codes
    -------------
    sonnet_splits_gpt   Sonnet has more conditions; GPT's names have close
                        matches in Sonnet's list (Sonnet split GPT's arms).
    gpt_splits_sonnet   GPT has more conditions; Sonnet's names have close
                        matches in GPT's list.
    sonnet_different    Sonnet has more conditions but the extra conditions
                        don't map onto GPT's (Sonnet found novel arms or
                        GPT missed them entirely).
    gpt_different       GPT has more conditions with no mapping to Sonnet's.
    """
    MATCH_THR = 0.30   # min Jaccard to count a condition as "matched"
    FRAC_THR  = 0.65   # fraction of smaller-set conditions that must be matched

    records = []
    for cid in mismatching_ids:
        g_ids = [str(r.get("data_id", "") or "").strip() for r in gpt_rows[cid]]
        s_ids = [str(r.get("data_id", "") or "").strip() for r in sonnet_rows[cid]]
        n_g, n_s = len(g_ids), len(s_ids)
        delta = n_s - n_g

        if n_g <= n_s:
            smaller, larger = g_ids, s_ids
            smaller_model = "gpt41"
        else:
            smaller, larger = s_ids, g_ids
            smaller_model = "sonnet46"

        # For each condition in the smaller set, best match score in the larger set
        best_scores = []
        for sc in smaller:
            best = max((_word_jaccard(sc, lc) for lc in larger), default=0.0)
            best_scores.append(best)

        frac_matched = (
            sum(1 for s in best_scores if s >= MATCH_THR) / len(best_scores)
            if best_scores else 0.0
        )
        avg_score = sum(best_scores) / len(best_scores) if best_scores else 0.0

        if frac_matched >= FRAC_THR:
            verdict = (
                "sonnet_splits_gpt" if smaller_model == "gpt41"
                else "gpt_splits_sonnet"
            )
        else:
            verdict = (
                "sonnet_different" if delta > 0
                else "gpt_different"
            )

        records.append({
            "custom_id": cid,
            "n_gpt41": n_g,
            "n_sonnet46": n_s,
            "delta": delta,
            "smaller_model": smaller_model,
            "frac_small_matched": round(frac_matched, 3),
            "avg_match_score": round(avg_score, 3),
            "verdict": verdict,
        })

    df = pd.DataFrame(records)
    return df.sort_values("delta", ascending=False)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gpt41", nargs="+", default=DEFAULT_GPT41)
    p.add_argument("--sonnet46", nargs="+", default=DEFAULT_SONNET46)
    p.add_argument("--output-dir", default="results/extraction_model_comparison")
    p.add_argument("--skip-text", action="store_true",
                   help="Skip text-field comparison (no embedding API calls).")
    p.add_argument("--text-threshold", type=float, default=TEXT_COSINE_THRESHOLD,
                   help=f"Cosine similarity threshold for text-field agreement "
                        f"(default {TEXT_COSINE_THRESHOLD}).")
    args = p.parse_args()
    text_threshold = args.text_threshold

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    # ---- Determine fields --------------------------------------------------
    sample = pd.read_excel(args.gpt41[0], sheet_name="extractions", nrows=1)
    fields = [c for c in sample.columns
              if c != "custom_id"
              and not c.endswith("_reason")
              and not c.endswith("_confidence")]
    if args.skip_text:
        fields = [f for f in fields if field_type(f) != "text"]

    print(f"Comparing {len(fields)} fields "
          f"({sum(field_type(f)=='binary' for f in fields)} binary, "
          f"{sum(field_type(f)=='numeric' for f in fields)} numeric, "
          f"{sum(field_type(f)=='text' for f in fields)} text)")

    # ---- Load raw rows (ungrouped) ----------------------------------------
    gpt_rows = load_raw_rows(args.gpt41, fields)
    sonnet_rows = load_raw_rows(args.sonnet46, fields)
    common_ids = sorted(set(gpt_rows) & set(sonnet_rows))
    print(f"Loaded: gpt41={len(gpt_rows)} papers, "
          f"sonnet46={len(sonnet_rows)} papers, common={len(common_ids)}")

    # ---- Granularity -------------------------------------------------------
    matching_ids = [cid for cid in common_ids
                    if len(gpt_rows[cid]) == len(sonnet_rows[cid])]
    mismatching_ids = [cid for cid in common_ids
                       if len(gpt_rows[cid]) != len(sonnet_rows[cid])]
    n_total = len(common_ids)
    n_match = len(matching_ids)
    n_mismatch = len(mismatching_ids)
    n_condition_pairs = sum(len(gpt_rows[cid]) for cid in matching_ids)
    print(f"Granularity: {n_match}/{n_total} papers match "
          f"({n_mismatch} excluded), {n_condition_pairs} condition pairs")

    # ---- Embed data_id strings for semantic alignment ----------------------
    cache_path = out / ".embedding_cache.pkl"
    all_data_ids: list[str] = []
    for cid in matching_ids:
        for r in gpt_rows[cid] + sonnet_rows[cid]:
            did = str(r.get("data_id", "") or "")
            if did:
                all_data_ids.append(did)
    print(f"Embedding {len(set(all_data_ids))} unique data_id strings for semantic alignment…")
    id_embeddings = get_embeddings(list(set(all_data_ids)), cache_path)

    # ---- Align conditions semantically -------------------------------------
    aligned: dict[str, list[tuple[dict, dict]]] = {}
    for cid in matching_ids:
        aligned[cid] = align_conditions(gpt_rows[cid], sonnet_rows[cid], id_embeddings)

    # ---- Collect text field values for embedding ---------------------------
    text_fields = [f for f in fields if field_type(f) == "text"]
    embeddings: dict[str, np.ndarray] = {}
    if text_fields:
        all_texts: list[str] = []
        for cid in matching_ids:
            for g, s in aligned[cid]:
                for f in text_fields:
                    gv = normalize_value(g.get(f), "text")
                    sv = normalize_value(s.get(f), "text")
                    if gv: all_texts.append(gv)
                    if sv: all_texts.append(sv)
        embeddings = get_embeddings(all_texts, cache_path)

    # ---- Compare each (paper, condition, field) ----------------------------
    # Accumulators per field
    field_stats: dict[str, dict] = {f: {
        "n": 0, "n_agree": 0, "n_disagree": 0,
        "n_both_missing": 0, "n_one_missing": 0,
        "n_both_present": 0, "n_agree_present": 0,
    } for f in fields}

    disagreement_rows: list[dict] = []

    for cid in matching_ids:
        for cond_idx, (g, s) in enumerate(aligned[cid]):
            for f in fields:
                ftype = field_type(f)
                ok, a_miss, b_miss = compare_values(
                    g.get(f), s.get(f), ftype, embeddings,
                    text_threshold=text_threshold,
                )
                st = field_stats[f]
                st["n"] += 1
                if ok:
                    st["n_agree"] += 1
                else:
                    st["n_disagree"] += 1

                if a_miss and b_miss:
                    st["n_both_missing"] += 1
                elif a_miss or b_miss:
                    st["n_one_missing"] += 1
                else:
                    st["n_both_present"] += 1
                    if ok:
                        st["n_agree_present"] += 1

                if not ok:
                    disagreement_rows.append({
                        "custom_id": cid,
                        "condition_idx": cond_idx,
                        "field": f,
                        "type": ftype,
                        "gpt41": display_value(g.get(f)),
                        "sonnet46": display_value(s.get(f)),
                    })

    # ---- Build summary -----------------------------------------------------
    summary_records = []
    for f in fields:
        st = field_stats[f]
        n = st["n"]
        bp = st["n_both_present"]
        summary_records.append({
            "field": f,
            "type": field_type(f),
            "n_condition_pairs": n,
            "n_agree": st["n_agree"],
            "n_disagree": st["n_disagree"],
            "agreement_rate": st["n_agree"] / n if n else np.nan,
            "n_both_missing": st["n_both_missing"],
            "n_one_missing": st["n_one_missing"],
            "n_both_present": bp,
            "n_agree_present": st["n_agree_present"],
            "agreement_rate_present": st["n_agree_present"] / bp if bp else np.nan,
            "pct_both_missing": st["n_both_missing"] / n if n else np.nan,
        })

    summary_df = pd.DataFrame(summary_records).sort_values(
        "agreement_rate", ascending=False,
    )
    disagreements_df = pd.DataFrame(disagreement_rows).sort_values(
        ["custom_id", "condition_idx", "field"],
    ) if disagreement_rows else pd.DataFrame(
        columns=["custom_id", "condition_idx", "field", "type", "gpt41", "sonnet46"],
    )

    # ---- Experiment counts -------------------------------------------------
    counts_gpt = experiment_counts(args.gpt41).rename(
        columns={"n_experiments": "n_experiments_gpt41"},
    )
    counts_son = experiment_counts(args.sonnet46).rename(
        columns={"n_experiments": "n_experiments_sonnet46"},
    )
    counts = counts_gpt.merge(counts_son, on="custom_id", how="inner")
    counts["count_match"] = (
        counts["n_experiments_gpt41"] == counts["n_experiments_sonnet46"]
    )
    counts["delta"] = counts["n_experiments_sonnet46"] - counts["n_experiments_gpt41"]
    counts = counts.sort_values(["count_match", "delta"], ascending=[True, False])

    # ---- Write outputs -----------------------------------------------------
    summary_df.to_csv(out / "agreement.csv", index=False)
    disagreements_df.to_csv(out / "disagreements.csv", index=False)
    counts.to_csv(out / "experiment_counts.csv", index=False)
    write_disagreements_markdown(
        disagreements_df, summary_df,
        n_papers_total=n_total,
        n_papers_matching=n_match,
        n_papers_mismatching=n_mismatch,
        n_condition_pairs=n_condition_pairs,
        output_path=out / "disagreement_papers_by_field.md",
    )
    plot(summary_df, n_match, n_condition_pairs, out / "agreement.png",
         text_threshold=text_threshold)
    plot_experiment_count_disagreement(counts, out / "granularity_disagreement.png")

    # ---- Granularity correctness analysis ------------------------------------
    gran_df = analyze_granularity_mismatches(mismatching_ids, gpt_rows, sonnet_rows)
    gran_df.to_csv(out / "granularity_analysis.csv", index=False)

    print(
        f"Wrote {out / 'agreement.csv'}, {out / 'disagreements.csv'}, "
        f"{out / 'experiment_counts.csv'}, "
        f"{out / 'granularity_analysis.csv'}, "
        f"{out / 'disagreement_papers_by_field.md'}, "
        f"{out / 'agreement.png'}, {out / 'granularity_disagreement.png'}"
    )


if __name__ == "__main__":
    main()
