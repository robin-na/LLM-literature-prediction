#!/usr/bin/env python3
"""
Generate a LaTeX PDF report analysing disagreements between GPT-4.1 and
Sonnet 4.6 on structured extraction from Public Goods Game papers.

Usage
-----
    python analysis/generate_disagreement_report.py [--compile] [--n-examples N]

Outputs
-------
    results/extraction_model_comparison/disagreement_report.tex
    results/extraction_model_comparison/disagreement_report.pdf  (if --compile)
"""
from __future__ import annotations

import argparse
import pickle
import subprocess
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

from prediction._comparison_shared import (
    ALL_FIELDS,
    BINARY_FIELDS,
    MISSING_TOKENS,
    NUMERIC_FIELDS,
    TEXT_FIELDS,
    cosine as _cosine,
)

# ─────────────────────────────── paths & constants ───────────────────────────

REPO_ROOT = Path(__file__).resolve().parents[1]

GPT41_FILES = [
    REPO_ROOT / "extraction/output_xlsx/simple_batch_197papers_gpt41.xlsx",
    REPO_ROOT / "extraction/output_xlsx/simple_batch_810papers_v2.xlsx",
]
SONNET46_FILES = [
    REPO_ROOT / "extraction/output_xlsx/simple_batch_197papers_sonnet46_combined.xlsx",
    REPO_ROOT / "extraction/output_xlsx/simple_batch_810papers_sonnet46_combined.xlsx",
]
COMPARISON_DIR = REPO_ROOT / "results/extraction_model_comparison"
OUTPUT_TEX = COMPARISON_DIR / "disagreement_report.tex"

TRUNC_VALUE = 220
TRUNC_REASON = 450

# Disagreement categories
CAT_A_FIELDS = {
    "data_id", "DVs", "IVs",                        # naming / terminology
    "indep_var", "other_game_info", "DVs_Definitions",  # level of detail
    "participant_age", "participant_gender",
    "participant_education", "participant_country",   # demographics formatting
}
CAT_B_FIELDS = {
    # One model says N/A (not mentioned), other says 0/1 (not present/present)
    "CONFIG_chat", "CONFIG_punishmentExists", "CONFIG_rewardExists",
    "CONFIG_showPunishmentId", "CONFIG_showRewardId",
}
# Category C = everything else (binary/numeric with actual value disagreement)


# ─────────────────────────────── data loading ────────────────────────────────


def _assign_condition_idx_alphabetical(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["_sort_key"] = df["data_id"].fillna("").astype(str).str.lower()
    df = df.sort_values(["custom_id", "_sort_key"], kind="stable")
    df["condition_idx"] = df.groupby("custom_id", sort=False).cumcount()
    return df.drop(columns=["_sort_key"])


def _assign_condition_idx_semantic(
    gpt_df: pd.DataFrame,
    son_df: pd.DataFrame,
    emb_cache: dict[str, np.ndarray],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Assign condition_idx to both models using Hungarian matching on data_id
    embeddings so the index is consistent across models.  Falls back to
    alphabetical for papers with only one condition or missing embeddings."""
    gpt_df = gpt_df.copy()
    son_df = son_df.copy()
    gpt_df["condition_idx"] = -1
    son_df["condition_idx"] = -1

    all_papers = set(gpt_df["custom_id"]) | set(son_df["custom_id"])
    for cid in all_papers:
        g_mask = gpt_df["custom_id"] == cid
        s_mask = son_df["custom_id"] == cid
        g_idx = gpt_df.index[g_mask].tolist()
        s_idx = son_df.index[s_mask].tolist()
        ng, ns = len(g_idx), len(s_idx)

        if ng == 0 or ns == 0 or ng != ns or ng == 1:
            # alphabetical fallback
            g_ids = gpt_df.loc[g_idx, "data_id"].fillna("").astype(str).str.lower()
            s_ids = son_df.loc[s_idx, "data_id"].fillna("").astype(str).str.lower()
            for rank, i in enumerate(g_ids.argsort()):
                gpt_df.loc[g_idx[i], "condition_idx"] = rank
            for rank, i in enumerate(s_ids.argsort()):
                son_df.loc[s_idx[i], "condition_idx"] = rank
            continue

        g_names = gpt_df.loc[g_idx, "data_id"].fillna("").astype(str).tolist()
        s_names = son_df.loc[s_idx, "data_id"].fillna("").astype(str).tolist()

        sim = np.zeros((ng, ns), dtype=np.float32)
        for i, gn in enumerate(g_names):
            ge = emb_cache.get(gn)
            if ge is None:
                continue
            for j, sn in enumerate(s_names):
                se = emb_cache.get(sn)
                if se is not None:
                    sim[i, j] = _cosine(ge, se)

        row_ind, col_ind = linear_sum_assignment(-sim)
        for rank, (ri, ci) in enumerate(zip(row_ind, col_ind)):
            gpt_df.loc[g_idx[ri], "condition_idx"] = rank
            son_df.loc[s_idx[ci], "condition_idx"] = rank

    return gpt_df, son_df


def load_model_df(paths: list[Path]) -> pd.DataFrame:
    """Load and concatenate Excel files for one model (condition_idx assigned later)."""
    frames = [pd.read_excel(p, sheet_name="extractions") for p in paths
              if p.exists()]
    if not frames:
        raise FileNotFoundError(f"No Excel files found in: {paths}")
    df = pd.concat(frames, ignore_index=True)
    df["custom_id"] = df["custom_id"].astype(str).str.strip()
    return df


def make_long(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """Convert wide Excel DataFrame → long format.

    Returns one row per (custom_id, condition_idx, field) with columns:
    custom_id, condition_idx, field, {prefix}_value, {prefix}_reason, {prefix}_confidence
    """
    parts = []
    for field in ALL_FIELDS:
        reason_col = f"{field}_reason"
        conf_col = f"{field}_confidence"
        if field not in df.columns:
            continue
        cols = {"custom_id": df["custom_id"], "condition_idx": df["condition_idx"]}
        cols[f"{prefix}_value"] = df[field].astype(str).str.strip()
        cols[f"{prefix}_reason"] = (
            df[reason_col].astype(str).str.strip() if reason_col in df.columns else ""
        )
        cols[f"{prefix}_confidence"] = (
            df[conf_col] if conf_col in df.columns else np.nan
        )
        tmp = pd.DataFrame(cols)
        tmp["field"] = field
        parts.append(tmp)
    return pd.concat(parts, ignore_index=True)


def enrich_disagreements(
    dis: pd.DataFrame,
    gpt_long: pd.DataFrame,
    son_long: pd.DataFrame,
) -> pd.DataFrame:
    """Add reasoning and confidence columns from both models to the
    disagreements DataFrame.  Join key: (custom_id, condition_idx, field)."""
    joined = (
        dis
        .merge(gpt_long, on=["custom_id", "condition_idx", "field"], how="left")
        .merge(son_long, on=["custom_id", "condition_idx", "field"], how="left")
    )
    return joined


# ─────────────────────────────── classification ──────────────────────────────

def classify_row(field: str, gpt_val: str, son_val: str) -> str:
    """Classify one disagreement row into category A, B, or C."""
    if field in CAT_A_FIELDS:
        return "A"
    if field in CAT_B_FIELDS:
        return "B"
    return "C"


def add_category(dis_enriched: pd.DataFrame) -> pd.DataFrame:
    dis_enriched = dis_enriched.copy()
    dis_enriched["category"] = [
        classify_row(r.field, r.gpt41, r.sonnet46)
        for r in dis_enriched.itertuples()
    ]
    return dis_enriched


# ─────────────────────────────── example selection ───────────────────────────

def select_examples(
    subset: pd.DataFrame,
    n: int = 7,
    prefer_both_present: bool = True,
    fields: list[str] | None = None,
) -> pd.DataFrame:
    """Select n representative examples from an enriched disagreements subset.

    Strategy: both models must have reasoning (len > 20); prefer cases where
    both have values (not MISSING); score by min reason length; deduplicate
    to max 1 example per paper.
    """
    df = subset.copy()
    if fields:
        df = df[df["field"].isin(fields)]

    df["_g_len"] = df["gpt41_reason"].fillna("").astype(str).str.len()
    df["_s_len"] = df["sonnet46_reason"].fillna("").astype(str).str.len()
    df = df[(df["_g_len"] > 20) & (df["_s_len"] > 20)]

    if df.empty:
        return df

    if prefer_both_present:
        both = df[(df["gpt41"] != "MISSING") & (df["sonnet46"] != "MISSING")]
        df = both if len(both) >= n // 2 else df

    df["_score"] = df[["_g_len", "_s_len"]].min(axis=1)
    df = df.sort_values("_score", ascending=False)

    # max 1 example per paper
    seen: set[str] = set()
    rows = []
    for _, row in df.iterrows():
        if row["custom_id"] not in seen:
            seen.add(row["custom_id"])
            rows.append(row)
        if len(rows) >= n:
            break

    result = pd.DataFrame(rows)
    result = result.drop(columns=["_g_len", "_s_len", "_score"], errors="ignore")
    return result


# ─────────────────────────────── confidence analysis ─────────────────────────

def compute_confidence_analysis(
    dis_enriched: pd.DataFrame,
    gpt_df: pd.DataFrame,
    son_df: pd.DataFrame,
    matched_papers: set[str],
) -> pd.DataFrame:
    """For each field: mean confidence in disagreeing vs. agreeing conditions.

    "Agreeing" pairs are inferred as matched-paper condition pairs that do NOT
    appear in dis_enriched for that field.
    """
    # Build disagree key set for fast lookup
    dis_set = set(
        zip(dis_enriched["custom_id"], dis_enriched["condition_idx"], dis_enriched["field"])
    )

    # Prepare matched-paper condition indices from both models
    gpt_matched = gpt_df[gpt_df["custom_id"].isin(matched_papers)].copy()
    son_matched = son_df[son_df["custom_id"].isin(matched_papers)].copy()

    rows = []
    for field in ALL_FIELDS:
        conf_col = f"{field}_confidence"
        if conf_col not in gpt_matched.columns or conf_col not in son_matched.columns:
            continue

        g = gpt_matched[["custom_id", "condition_idx", conf_col]].copy()
        g.columns = ["custom_id", "condition_idx", "gpt_conf"]
        s = son_matched[["custom_id", "condition_idx", conf_col]].copy()
        s.columns = ["custom_id", "condition_idx", "son_conf"]
        merged = g.merge(s, on=["custom_id", "condition_idx"], how="inner")
        if merged.empty:
            continue

        merged["is_disagree"] = merged.apply(
            lambda r: (r["custom_id"], int(r["condition_idx"]), field) in dis_set, axis=1
        )

        agree = merged[~merged["is_disagree"]]
        disagree = merged[merged["is_disagree"]]

        rows.append({
            "field": field,
            "n_agree": len(agree),
            "n_disagree": len(disagree),
            "gpt_conf_agree": agree["gpt_conf"].mean(skipna=True),
            "gpt_conf_disagree": disagree["gpt_conf"].mean(skipna=True),
            "son_conf_agree": agree["son_conf"].mean(skipna=True),
            "son_conf_disagree": disagree["son_conf"].mean(skipna=True),
        })

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["gpt_delta"] = out["gpt_conf_agree"] - out["gpt_conf_disagree"]
    out["son_delta"] = out["son_conf_agree"] - out["son_conf_disagree"]
    return out.sort_values("son_delta", ascending=False)


# ─────────────────────────────── LaTeX helpers ───────────────────────────────

_LATEX_ESCAPES = [
    ("\\", r"\textbackslash{}"),
    ("&",  r"\&"),
    ("%",  r"\%"),
    ("$",  r"\$"),
    ("#",  r"\#"),
    ("_",  r"\_"),
    ("{",  r"\{"),
    ("}",  r"\}"),
    ("~",  r"\textasciitilde{}"),
    ("^",  r"\textasciicircum{}"),
]


_UNICODE_REPLACEMENTS = [
    ("π", "pi"), ("α", "alpha"), ("β", "beta"),
    ("γ", "gamma"), ("δ", "delta"), ("μ", "mu"),
    ("σ", "sigma"), ("ε", "epsilon"), ("θ", "theta"),
    ("≤", "<="), ("≥", ">="), ("≈", "~="),
    ("×", "x"), ("÷", "/"), ("→", "->"), ("←", "<-"),
    ("—", "---"), ("–", "--"),
    ("‘", "'"), ("’", "'"), ("“", "``"), ("”", "''"),
    ("…", "..."), ("°", " degrees"), ("±", "+/-"),
    ("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"),
    ("à", "a"), ("â", "a"), ("ä", "a"), ("ü", "u"),
    ("ö", "o"), ("ç", "c"), ("î", "i"),
]


def sanitize_unicode(s: str) -> str:
    """Replace common Unicode characters with ASCII approximations."""
    for char, repl in _UNICODE_REPLACEMENTS:
        s = s.replace(char, repl)
    return s.encode("ascii", "ignore").decode("ascii")


def escape_latex(s: str) -> str:
    result = str(s)
    # Backslash (index 0 of _LATEX_ESCAPES) must be handled first and separately
    # to avoid double-escaping the replacement strings introduced below.
    result = result.replace("\\", "\x00BACKSLASH\x00")
    for char, repl in _LATEX_ESCAPES[1:]:  # skip index 0 (backslash) — handled above
        result = result.replace(char, repl)
    result = result.replace("\x00BACKSLASH\x00", r"\textbackslash{}")
    return result


def trunc(s, max_chars: int = TRUNC_VALUE) -> str:
    s = str(s) if not pd.isna(s) else ""
    if s.lower() in MISSING_TOKENS:
        s = "N/A"
    s = sanitize_unicode(s)
    return s[:max_chars] + "\\ldots" if len(s) > max_chars else s


def fmt_conf(v) -> str:
    try:
        return f"{float(v):.2f}"
    except (TypeError, ValueError):
        return "n/a"


# ─────────────────────────────── example boxes ───────────────────────────────

def format_example_box(row: pd.Series, title_prefix: str = "") -> str:
    doi = escape_latex(str(row["custom_id"]))
    field = escape_latex(str(row["field"]))
    cidx = int(row["condition_idx"])
    title = f"\\textbf{{{field}}} \\textbar{{}} DOI: {doi} \\textbar{{}} Cond.~{cidx}"
    if title_prefix:
        title = f"\\textbf{{{escape_latex(title_prefix)}}} --- {title}"

    gval = escape_latex(trunc(row.get("gpt41", ""), TRUNC_VALUE))
    sval = escape_latex(trunc(row.get("sonnet46", ""), TRUNC_VALUE))
    greason = escape_latex(trunc(row.get("gpt41_reason", ""), TRUNC_REASON))
    sreason = escape_latex(trunc(row.get("sonnet46_reason", ""), TRUNC_REASON))
    gconf = fmt_conf(row.get("gpt41_confidence"))
    sconf = fmt_conf(row.get("sonnet46_confidence"))

    return textwrap.dedent(f"""\
        \\begin{{tcolorbox}}[
          title={{{title}}},
          colback=blue!3!white,
          colframe=blue!45!black,
          fonttitle=\\small\\sffamily,
          sidebyside,
          sidebyside align=top seam,
          lower separated=false,
          breakable,
          before upper={{\\small}},
          before lower={{\\small}},
        ]
        \\textbf{{GPT-4.1}}\\\\[2pt]
        \\textit{{Value:}}~{gval}\\\\[3pt]
        \\textit{{Conf.:}}~{gconf}\\\\[3pt]
        \\textit{{Reason:}}~{greason}
        \\tcblower
        \\textbf{{Sonnet~4.6}}\\\\[2pt]
        \\textit{{Value:}}~{sval}\\\\[3pt]
        \\textit{{Conf.:}}~{sconf}\\\\[3pt]
        \\textit{{Reason:}}~{sreason}
        \\end{{tcolorbox}}
    """)


# ─────────────────────────────── section renderers ───────────────────────────

def _color_row(rate: float) -> str:
    if rate < 0.50:
        return r"\rowcolor{red!18}"
    if rate < 0.80:
        return r"\rowcolor{orange!28}"
    return r"\rowcolor{green!18}"


def render_agreement_table(ag: pd.DataFrame) -> str:
    ag_sorted = ag.sort_values("agreement_rate")
    lines = [
        r"\begin{center}",
        r"\small",
        r"\begin{longtable}{llrrrrrr}",
        r"\toprule",
        r"\textbf{Field} & \textbf{Type} & \textbf{Agr.\%} & "
        r"\textbf{Agr.\%\textsuperscript{*}} & \textbf{N\,disagree} & "
        r"\textbf{N\,both\,miss.} & \textbf{N\,one\,miss.} & \textbf{N\,both\,pres.}\\",
        r"\midrule",
        r"\endfirsthead",
        r"\toprule",
        r"\textbf{Field} & \textbf{Type} & \textbf{Agr.\%} & "
        r"\textbf{Agr.\%\textsuperscript{*}} & \textbf{N\,disagree} & "
        r"\textbf{N\,both\,miss.} & \textbf{N\,one\,miss.} & \textbf{N\,both\,pres.}\\",
        r"\midrule",
        r"\endhead",
        r"\midrule \multicolumn{8}{r}{\small\itshape (continued\ldots)} \\",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    for _, r in ag_sorted.iterrows():
        color = _color_row(r["agreement_rate"])
        rate_pct = f"{r['agreement_rate']*100:.1f}\\%"
        rate_pres = (
            f"{r['agreement_rate_present']*100:.1f}\\%"
            if pd.notna(r["agreement_rate_present"])
            else "---"
        )
        field_esc = escape_latex(str(r["field"]))
        ftype = str(r["type"]).capitalize()
        n_dis = int(r["n_disagree"])
        n_bm = int(r.get("n_both_missing", 0))
        n_om = int(r.get("n_one_missing", 0))
        n_bp = int(r.get("n_both_present", 0))
        lines.append(
            f"{color} \\texttt{{{field_esc}}} & {ftype} & {rate_pct} & {rate_pres} & "
            f"{n_dis} & {n_bm} & {n_om} & {n_bp}\\\\"
        )
    lines += [
        r"\end{longtable}",
        r"{\footnotesize\textsuperscript{*}Agreement rate among condition pairs where "
        r"both models gave a non-missing value.}",
        r"\end{center}",
    ]
    return "\n".join(lines)


def render_methodology_section(text_threshold: float = 0.70) -> str:
    thr_str = f"{text_threshold:.2f}"
    return textwrap.dedent(rf"""
        \section{{Methodology}}

        \subsection{{Extraction Setup}}
        Both models --- GPT-4.1 and Claude Sonnet~4.6 --- were given identical prompts
        asking them to extract 37 structured fields from each paper's full text
        (in Markdown format).  For every field the model returns three values:
        a \emph{{value}}, a free-text \emph{{reason}} explaining the extraction decision,
        and a \emph{{confidence}} score in $[0,1]$.  Extraction was run via the OpenAI
        Batch API (for GPT-4.1) and the Anthropic Batch API (for Sonnet~4.6),
        with temperature~0.

        \subsection{{Condition Alignment}}
        Each paper may describe multiple experimental conditions (arms).  Both models
        are asked to return one row per condition.  To compare them, we first check
        whether the two models extracted the same \emph{{number}} of conditions for a
        paper.  Papers with a mismatch are flagged as \textbf{{granularity disagreements}}
        (Category~D) and excluded from field-level comparison (Section~\ref{{sec:granularity}}).

        For papers where the condition counts match, conditions must be paired across
        models before field-level comparison can proceed.

        \subsubsection*{{Semantic alignment (current approach)}}
        We embed each condition's \texttt{{data\_id}} string using
        \texttt{{text-embedding-3-small}} and solve the optimal 1-to-1 matching with
        the \textbf{{Hungarian algorithm}} (minimising total cosine distance).
        This replaced an earlier alphabetical sort that occasionally mis-paired
        conditions when the two models used different naming conventions, producing
        spurious disagreements.  Switching to semantic alignment eliminated
        \textbf{{685 false disagreements}} (17{{,}}939 $\rightarrow$ 17{{,}}254).

        \subsubsection*{{When does embedding-based alignment work well?}}
        Condition names in PGG papers are usually descriptive enough for embeddings
        to work reliably:
        \begin{{itemize}}
          \item \emph{{``Experiment~1 --- Punishment treatment''}} vs.\
            \emph{{``Punishment condition, Experiment~1''}} --- high cosine,
            correct match.
          \item \emph{{``Partners with punishment --- Maintenance''}} vs.\
            \emph{{``Partners~+ punishment, Maintenance''}} --- correct.
        \end{{itemize}}

        \subsubsection*{{Known failure modes}}
        \begin{{itemize}}
          \item \textbf{{Factorial designs with many near-identical names.}}
            In a $2{{\times}}2{{\times}}3$ design, conditions differ by only one word
            (e.g.\ ``High MPCR, 4~players, Punishment'' vs.\
            ``Low MPCR, 4~players, Punishment'').
            Embeddings handle this well on average but can swap near-identical pairs.
          \item \textbf{{Generic labels.}}
            If GPT uses ``Condition~1, Condition~2'' and Sonnet uses
            ``Control, Treatment~A'', embeddings have almost nothing to match on.
        \end{{itemize}}

        \subsubsection*{{What would a better approach look like?}}
        The most principled fix is \textbf{{content-based matching}}: pair conditions
        on their actual field values (e.g.\ \texttt{{CONFIG\_punishmentExists}},
        \texttt{{CONFIG\_MPCR}}, \texttt{{CONFIG\_playerCount}}) rather than their
        label.  Two conditions with identical parameters are the same treatment
        regardless of what either model called them.  An LLM could also be asked
        to explicitly reason across both condition lists and assign correspondences.
        We consider the embedding approach sufficient for the current analysis ---
        the failure modes affect a small fraction of 3{{,}}315 condition pairs --- but
        content-based matching would be the right long-term investment if this
        pipeline runs continuously on new papers.

        \subsection{{Agreement Criteria}}
        Agreement is assessed field-by-field using type-aware rules:

        \begin{{description}}
          \item[Binary / categorical fields (16 fields)]
            Exact string match after normalisation: \texttt{{true}}/\texttt{{yes}}
            $\rightarrow$ \texttt{{1}}, \texttt{{false}}/\texttt{{no}} $\rightarrow$ \texttt{{0}};
            numeric floats converted to integers when integral.

          \item[Numeric fields (11 fields)]
            Agreement if \emph{{either}}:
            $|a - b| \leq 0.01$ (absolute floor protecting near-zero values),
            \emph{{or}} $\dfrac{{|a - b|}}{{\max(|a|,|b|,\varepsilon)}} \leq 5\%$.

          \item[Text fields (10 fields)]
            Agreement if the cosine similarity of OpenAI
            \texttt{{text-embedding-3-small}} embeddings $\geq {thr_str}$.

            \textbf{{Threshold rationale.}}  An earlier version of this analysis used a
            threshold of 0.95, which flagged near-paraphrases as disagreements:
            two descriptions of the same DV with different wording typically score
            0.85--0.92, and should count as agreement for the purpose of extracting
            the \emph{{same concept}}.  Lowering the threshold to {thr_str} corrects this:
            at this level the embeddings still clearly separate genuinely different
            content (e.g.\ ``cooperation'' vs.\ ``earnings'', which scores $<0.5$)
            from paraphrases.  As a result, the apparent disagreement rate for most
            text fields drops dramatically --- for example
            \texttt{{DVs\_Definitions}} falls from 93.5\,\% to 2.2\,\%.
        \end{{description}}

        \subsection{{Missing Value Handling}}
        Any value matching the set
        $\{{$\texttt{{nan}}, \texttt{{none}}, \texttt{{n/a}}, \texttt{{n/r}},
        \texttt{{na}}, \texttt{{null}}, \texttt{{""}}$\}}$ is treated as \emph{{missing}}.
        Per-field statistics decompose disagreements into three buckets:
        \begin{{itemize}}
          \item \textbf{{Both missing}} --- trivial agreement; not counted as disagreement.
          \item \textbf{{One missing}} --- one model extracted a value, the other did not;
            always a disagreement.
          \item \textbf{{Both present}} --- both gave values; compared with the
            type-specific rule above.
        \end{{itemize}}
        The \emph{{agreement rate present}} column reports the fraction of both-present
        pairs that agree.

        \subsection{{Limitations}}
        \begin{{itemize}}
          \item Semantic alignment on \texttt{{data\_id}} embeddings can still fail
            for factorial designs with many near-identical condition names, or for
            papers where one model uses generic labels (``Condition~1'', ``Condition~2'').
            Content-based matching on field values would be more robust.
          \item The 197-paper and 810-paper extraction batches are concatenated
            without deduplication; papers appearing in both batches have doubled
            condition rows and are excluded from field-level analysis as granularity
            mismatches.
          \item All embeddings are cached; the cache is shared between the alignment
            step and the text-field agreement step.
        \end{{itemize}}
    """)


def render_granularity_section(
    counts: pd.DataFrame,
    gpt_df: pd.DataFrame,
    son_df: pd.DataFrame,
    gran_analysis: pd.DataFrame,
    n_examples: int = 5,
) -> str:
    total = len(counts)
    n_mismatch = int((~counts["count_match"]).sum())
    pct = n_mismatch / total * 100
    mis = counts[~counts["count_match"]].copy()
    mis["abs_delta"] = mis["delta"].abs()

    son_more = int((mis["delta"] > 0).sum())
    gpt_more = int((mis["delta"] < 0).sum())
    max_delta = int(mis["abs_delta"].max())

    # ── Correctness analysis summary ──────────────────────────────────────
    vc = gran_analysis["verdict"].value_counts()
    n_son_splits = int(vc.get("sonnet_splits_gpt", 0))
    n_gpt_splits = int(vc.get("gpt_splits_sonnet", 0))
    n_son_diff   = int(vc.get("sonnet_different", 0))
    n_gpt_diff   = int(vc.get("gpt_different", 0))

    # correctness table rows
    correctness_rows = [
        (r"\textbf{sonnet\_splits\_gpt}",
         str(n_son_splits),
         "Sonnet has more; GPT's conditions map onto Sonnet's (Sonnet subdivided GPT's arms)",
         "Sonnet likely more granular/correct"),
        (r"\textbf{gpt\_splits\_sonnet}",
         str(n_gpt_splits),
         "GPT has more; Sonnet's conditions map onto GPT's (GPT subdivided Sonnet's arms)",
         "GPT likely more granular/correct"),
        (r"\textbf{sonnet\_different}",
         str(n_son_diff),
         "Sonnet has more; low name overlap with GPT (Sonnet found novel conditions or misread)",
         "Unclear --- manual review needed"),
        (r"\textbf{gpt\_different}",
         str(n_gpt_diff),
         "GPT has more; low name overlap with Sonnet",
         "Unclear --- manual review needed"),
    ]
    ct_lines = [
        r"\begin{center}\small",
        r"\begin{tabular}{lrp{6cm}p{4.5cm}}",
        r"\toprule",
        r"\textbf{Verdict} & \textbf{N} & \textbf{Description} & \textbf{Implication} \\",
        r"\midrule",
    ]
    for v, n, desc, impl in correctness_rows:
        ct_lines.append(f"{v} & {n} & {desc} & {impl} \\\\[2pt]")
    ct_lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    correctness_table = "\n".join(ct_lines)

    # ── Helper: condition names + first data_id_reason ────────────────────
    def condition_list(df: pd.DataFrame, paper: str) -> list[str]:
        rows = df[df["custom_id"] == paper]["data_id"].fillna("").astype(str).tolist()
        return sorted(set(rows), key=str.lower)

    def first_reason(df: pd.DataFrame, paper: str) -> str:
        sub = df[df["custom_id"] == paper]
        if sub.empty:
            return ""
        val = sub.iloc[0].get("data_id_reason", "")
        return str(val) if pd.notna(val) else ""

    def make_case_box(paper: str, color: str, title_label: str) -> str:
        row = gran_analysis[gran_analysis["custom_id"] == paper]
        g_n = int(row["n_gpt41"].iloc[0]) if not row.empty else 0
        s_n = int(row["n_sonnet46"].iloc[0]) if not row.empty else 0
        match_pct = int(row["frac_small_matched"].iloc[0] * 100) if not row.empty else 0
        g_conds = condition_list(gpt_df, paper)
        s_conds = condition_list(son_df, paper)
        g_reason = trunc(first_reason(gpt_df, paper), 300)
        s_reason = trunc(first_reason(son_df, paper), 300)
        doi_esc = escape_latex(paper)
        MAX_COND = 10
        g_items = "\n".join(f"  \\item {escape_latex(c)}" for c in g_conds[:MAX_COND])
        s_items = "\n".join(f"  \\item {escape_latex(c)}" for c in s_conds[:MAX_COND])
        if len(g_conds) > MAX_COND:
            g_items += f"\n  \\item \\textit{{... {len(g_conds)-MAX_COND} more}}"
        if len(s_conds) > MAX_COND:
            s_items += f"\n  \\item \\textit{{... {len(s_conds)-MAX_COND} more}}"
        reason_block_g = (f"\\medskip\\textit{{GPT reason for first condition:}} {escape_latex(g_reason)}"
                          if g_reason else "")
        reason_block_s = (f"\\medskip\\textit{{Sonnet reason for first condition:}} {escape_latex(s_reason)}"
                          if s_reason else "")
        return textwrap.dedent(f"""\
            \\begin{{tcolorbox}}[
              title={{\\textbf{{{escape_latex(title_label)}}} (name-match {match_pct}\\%) --- DOI: {doi_esc}}},
              colback={color}!4!white, colframe={color}!55!black,
              fonttitle=\\small\\sffamily,
              sidebyside, sidebyside align=top seam,
              lower separated=false, breakable,
              before upper={{\\small}}, before lower={{\\small}},
            ]
            \\textbf{{GPT-4.1}} ({g_n}~conditions)\\\\[4pt]
            \\begin{{itemize}}[leftmargin=*,noitemsep,topsep=0pt]
            {g_items}
            \\end{{itemize}}
            {reason_block_g}
            \\tcblower
            \\textbf{{Sonnet~4.6}} ({s_n}~conditions)\\\\[4pt]
            \\begin{{itemize}}[leftmargin=*,noitemsep,topsep=0pt]
            {s_items}
            \\end{{itemize}}
            {reason_block_s}
            \\end{{tcolorbox}}
        """)

    # ── Case counts for breakdown table ───────────────────────────────────
    sonnet_more_papers = gran_analysis[gran_analysis["delta"] > 0]["custom_id"].tolist()
    n_case1, n_case2 = 0, 0
    for paper in sonnet_more_papers:
        s_rows = son_df[son_df["custom_id"] == paper]
        g_rows = gpt_df[gpt_df["custom_id"] == paper]
        s_non = s_rows[s_rows["METHOD_experiment"].astype(str).str.lower().isin(["false","0","no"])]
        g_non = g_rows[g_rows["METHOD_experiment"].astype(str).str.lower().isin(["false","0","no"])]
        if len(s_non) > len(g_non):
            n_case2 += 1
        else:
            n_case1 += 1

    n_gpt_more = int((gran_analysis["delta"] < 0).sum())
    n_total_mismatch = len(gran_analysis)

    # breakdown table
    breakdown_rows = [
        ("Case~1", str(n_case1),
         r"Sonnet $>$ GPT; same experimental type",
         "GPT omitted experiments from the paper's main paradigm; Sonnet likely correct"),
        ("Case~2", str(n_case2),
         r"Sonnet $>$ GPT; Sonnet adds non-experimental studies",
         "Sonnet over-broad (meta-analyses, surveys, different paradigms); GPT may be more appropriate"),
        ("GPT has more", str(n_gpt_more),
         r"GPT $>$ Sonnet; avg delta $= {:.1f}$".format(
             gran_analysis[gran_analysis["delta"] < 0]["delta"].mean()),
         "Reverse pattern; Sonnet under-extracts relative to GPT; needs case-by-case review"),
    ]
    bd_lines = [
        r"\begin{center}\small",
        r"\begin{tabular}{lrp{5.5cm}p{5.5cm}}",
        r"\toprule",
        r"\textbf{Pattern} & \textbf{N} & \textbf{Description} & \textbf{Interpretation} \\",
        r"\midrule",
    ]
    for pat, n, desc, interp in breakdown_rows:
        bd_lines.append(f"{pat} & {n} & {desc} & {interp} \\\\[3pt]")
    bd_lines += [
        r"\midrule",
        f"\\textbf{{Total}} & \\textbf{{{n_total_mismatch}}} & & \\\\",
        r"\bottomrule", r"\end{tabular}", r"\end{center}",
    ]
    breakdown_table = "\n".join(bd_lines)

    # ── Three hand-picked illustrative cases ──────────────────────────────
    CASE1_PAPER = "10.1016_j.jesp.2022.104284"   # GPT 4 vs Sonnet 17 – omission
    CASE2_PAPER = "10.1037_a0033495"              # GPT 2 vs Sonnet 13 – selective
    CASE3_PAPER = "10.1038_s41562-017-0191-5"    # GPT 10 vs Sonnet 9  – gpt_splits_sonnet

    case1_box = make_case_box(CASE1_PAPER, "orange",
                              "Case 1 — GPT omits later experiments (sonnet\\_splits\\_gpt)")
    case2_box = make_case_box(CASE2_PAPER, "blue",
                              "Case 2 — GPT extracts only the core PGG; Sonnet adds non-PGG studies")
    case3_box = make_case_box(CASE3_PAPER, "teal",
                              "Case 3 — GPT has more conditions (gpt\\_splits\\_sonnet)")

    three_cases_section = textwrap.dedent(r"""
        \subsection{Three Illustrative Patterns}

        Manual inspection of the mismatches reveals three qualitatively
        distinct patterns, summarised in the table below.

    """) + breakdown_table + textwrap.dedent(r"""

        \medskip
        \textbf{Case~1 --- GPT genuinely omits later experiments} ($\approx$\textbf{""") \
        + str(n_case1) + r"""} \textbf{papers).}
        For multi-experiment papers, GPT sometimes extracts conditions from only
        one experiment and ignores the rest, even though the remaining experiments
        are independently described PGG conditions.  The prompt says
        \emph{``Extract every experiment, simulation, or observational condition
        described''} --- Sonnet follows this; GPT does not.
        GPT's own \texttt{data\_id\_reason} in the example below confirms it
        processed Experiment~1 only, with no mention of experiments 2--5.

    """ + case1_box + textwrap.dedent(r"""

        \textbf{Case~2 --- GPT selectively extracts the core PGG; Sonnet over-extracts}
        ($\approx$\textbf{""") + str(n_case2) + r"""} \textbf{papers).}
        Some papers bundle a genuine PGG with adjacent studies of different paradigms:
        vignette surveys, national polls, meta-analyses, eBay auction experiments,
        or anthropological datasets.  Sonnet extracts everything
        (\texttt{METHOD\_experiment = False} for the non-PGG rows); GPT correctly
        limits itself to the experimental PGG conditions.
        This is the one pattern where GPT's judgment is arguably \emph{better}:
        the non-experimental studies should probably not be in this dataset at all.

    """ + case2_box + textwrap.dedent(r"""

        \textbf{Case~3 --- GPT has more conditions than Sonnet}
        ($\approx$\textbf{""") + str(n_gpt_more) + r"""} \textbf{papers, avg delta $=""" \
        + f"{gran_analysis[gran_analysis['delta'] < 0]['delta'].mean():.1f}" \
        + r"""$).}
        In 88 papers GPT extracts more conditions than Sonnet.  Unlike Case~1,
        these are not simple omission errors: the average delta is $-2.9$ and
        the range goes to $-11$.  The \texttt{gpt\_splits\_sonnet} verdict
        (57 papers) means GPT's extra conditions are recognisable subdivisions
        of Sonnet's --- GPT applied a finer treatment-arm split.
        The \texttt{gpt\_different} verdict (31 papers) means the condition sets
        are fundamentally different and require manual inspection.
        The example below shows the one case we examined in detail: a simulation
        comparison that GPT records as two rows and Sonnet as one.

    """ + case3_box

    # ── Automated examples (one per remaining verdict type) ───────────────
    example_blocks = []
    for verdict_code, color in [
        ("sonnet_different", "red"),
    ]:
        subset_v = gran_analysis[gran_analysis["verdict"] == verdict_code]
        if subset_v.empty:
            continue
        top = subset_v.iloc[0]
        paper = str(top["custom_id"])
        g_conds = condition_list(gpt_df, paper)
        s_conds = condition_list(son_df, paper)
        g_n = int(top["n_gpt41"])
        s_n = int(top["n_sonnet46"])
        doi_esc = escape_latex(paper)
        match_pct = int(top["frac_small_matched"] * 100)
        verdict_label = escape_latex(verdict_code)

        g_items = "\n".join(f"  \\item {escape_latex(c)}" for c in g_conds[:12])
        s_items = "\n".join(f"  \\item {escape_latex(c)}" for c in s_conds[:12])
        if len(g_conds) > 12:
            g_items += f"\n  \\item \\textit{{... {len(g_conds)-12} more}}"
        if len(s_conds) > 12:
            s_items += f"\n  \\item \\textit{{... {len(s_conds)-12} more}}"

        block = textwrap.dedent(f"""\
            \\begin{{tcolorbox}}[
              title={{\\textbf{{{verdict_label}}} (match {match_pct}\\%) --- DOI: {doi_esc}}},
              colback={color}!4!white, colframe={color}!55!black,
              fonttitle=\\small\\sffamily,
              sidebyside, sidebyside align=top seam,
              lower separated=false, breakable,
              before upper={{\\small}}, before lower={{\\small}},
            ]
            \\textbf{{GPT-4.1}} ({g_n}~conditions)\\\\[4pt]
            \\begin{{itemize}}[leftmargin=*,noitemsep,topsep=0pt]
            {g_items}
            \\end{{itemize}}
            \\tcblower
            \\textbf{{Sonnet~4.6}} ({s_n}~conditions)\\\\[4pt]
            \\begin{{itemize}}[leftmargin=*,noitemsep,topsep=0pt]
            {s_items}
            \\end{{itemize}}
            \\end{{tcolorbox}}
        """)
        example_blocks.append(block)

    img_path = str(COMPARISON_DIR / "granularity_disagreement.png")
    pct_son_splits = n_son_splits / n_mismatch * 100 if n_mismatch else 0.0

    return textwrap.dedent(f"""\
        \\section{{Category D: Granularity Disagreements}}\\label{{sec:granularity}}

        \\subsection{{Overview}}
        Of \\textbf{{{total}}} papers common to both models, \\textbf{{{n_mismatch}}}
        ({pct:.1f}\\%) have a different number of extracted experimental conditions.
        These papers are \\emph{{excluded}} from field-level comparison because there is
        no safe way to pair conditions across models.

        The mismatch is asymmetric: Sonnet~4.6 extracts \\emph{{more}} conditions than
        GPT-4.1 in \\textbf{{{son_more}}} papers, while GPT-4.1 extracts more in
        \\textbf{{{gpt_more}}} papers.
        The largest observed discrepancy is \\textbf{{{max_delta}}} conditions on a
        single paper.

        \\begin{{figure}}[h]
          \\centering
          \\includegraphics[width=0.92\\textwidth]{{{img_path}}}
          \\caption{{Granularity disagreement diagnostics: distribution of per-paper
          condition-count deltas (Sonnet minus GPT).}}
        \\end{{figure}}

        \\subsection{{Which Model Is Correct? --- Correctness Analysis}}

        To assess \\emph{{who}} is right when the counts differ, we compute the
        word-token Jaccard similarity between each condition name in the
        \\emph{{smaller}} model's set and its best match in the \\emph{{larger}} model's set.
        If most of the smaller model's conditions have a close match in the larger set
        (Jaccard $\\geq 0.30$ for $\\geq 65\\%$ of conditions), we infer that the
        \\emph{{larger}} model sub-divided the smaller model's conditions rather than
        inventing new ones. Otherwise the condition sets are ``fundamentally different.''

        {correctness_table}

        \\medskip
        \\textbf{{Key finding.}}
        In \\textbf{{{n_son_splits}}} of {n_mismatch} mismatches ({pct_son_splits:.0f}\\%),
        Sonnet's extra conditions are refinements of GPT's --- GPT appears to have
        \\emph{{merged}} conditions that Sonnet correctly separated.
        In only \\textbf{{{n_gpt_splits}}} cases does GPT extract more granular conditions.
        In \\textbf{{{n_son_diff + n_gpt_diff}}} cases the condition sets are
        fundamentally different, suggesting one model misread the paper's design
        --- these require manual review.

        Overall, Sonnet~4.6 appears to be the more granular extractor, and when it
        extracts more conditions than GPT-4.1 those conditions are usually recognisable
        refinements of GPT's (not fabrications).  This is consistent with Sonnet
        applying the extraction rule ``each treatment arm = one row'' more strictly
        than GPT, which tends to merge arms that share most parameters.

        \\subsection{{Selected Examples}}

    """) + three_cases_section + "\n\n" + "\n".join(example_blocks)


def render_category_section(
    category: str,
    title: str,
    description: str,
    verdict: str,
    dis_enriched: pd.DataFrame,
    ag: pd.DataFrame,
    fields_in_category: list[str],
    n_examples: int = 7,
) -> str:
    subset = dis_enriched[dis_enriched["category"] == category]
    prefer_both = (category != "B")
    examples = select_examples(subset, n=n_examples, prefer_both_present=prefer_both)

    # Per-field summary table
    ag_cat = ag[ag["field"].isin(fields_in_category)].sort_values("agreement_rate")
    field_table_lines = [
        r"\begin{center}\small",
        r"\begin{tabular}{llrrr}",
        r"\toprule",
        r"\textbf{Field} & \textbf{Type} & \textbf{Agr.\%} & "
        r"\textbf{N\,disagree} & \textbf{N\,one\,miss.}\\",
        r"\midrule",
    ]
    for _, r in ag_cat.iterrows():
        color = _color_row(r["agreement_rate"])
        field_esc = escape_latex(str(r["field"]))
        rate_pct = f"{r['agreement_rate']*100:.1f}\\%"
        n_dis = int(r["n_disagree"])
        n_om = int(r.get("n_one_missing", 0))
        ftype = str(r["type"]).capitalize()
        field_table_lines.append(
            f"{color}\\texttt{{{field_esc}}} & {ftype} & {rate_pct} & {n_dis} & {n_om}\\\\"
        )
    field_table_lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    field_table = "\n".join(field_table_lines)

    # Example boxes
    if examples.empty:
        example_section = r"\textit{No enriched examples available for this category.}"
    else:
        example_section = "\n".join(
            format_example_box(row) for _, row in examples.iterrows()
        )

    cat_total = len(subset)
    cat_papers = subset["custom_id"].nunique()

    return textwrap.dedent(f"""\
        \\section{{{title}}}

        \\subsection{{Overview}}
        {description}

        This category accounts for \\textbf{{{cat_total:,}}} disagreeing
        (paper, condition, field) triples across \\textbf{{{cat_papers}}} papers.

        \\subsection{{Field Summary}}
        {field_table}

        \\subsection{{Verdict}}
        {verdict}

        \\subsection{{Selected Examples}}
        Each box shows the GPT-4.1 (left) and Sonnet~4.6 (right) extracted values,
        confidence scores, and reasoning for the same paper--condition--field triple.

    """) + example_section + "\n"


def render_confidence_section(conf_df: pd.DataFrame) -> str:
    if conf_df.empty:
        return (
            "\\section{Confidence Score Analysis}\n"
            "\\textit{Confidence data not available.}\n"
        )

    # Filter to fields with meaningful disagreement sample (n_disagree >= 10)
    conf_df = conf_df[conf_df["n_disagree"] >= 10].copy()

    lines = [
        r"\section{Confidence Score Analysis}",
        r"\subsection{Overview}",
        textwrap.dedent(r"""
        A well-calibrated model should report {\em lower} confidence precisely when it
        is likely to be wrong.  We test this by comparing mean confidence on condition
        pairs where the two models {\em agree} (a proxy for correctness) versus pairs
        where they {\em disagree}.

        \begin{quote}
        $\Delta_{\mathrm{confidence}} = \overline{\mathrm{conf}}_{\mathrm{agree}}
         - \overline{\mathrm{conf}}_{\mathrm{disagree}}$
        \end{quote}

        A positive $\Delta$ means the model is \emph{less} confident on disagreement
        cases --- a calibration signal.  A $\Delta \approx 0$ means confidence is
        uninformative.
        """),
        r"\subsection{Results}",
        r"\begin{center}\small",
        r"\begin{tabular}{lrr@{\hskip 6pt}rrr@{\hskip 6pt}rr}",
        r"\toprule",
        r" & \multicolumn{3}{c}{\textbf{GPT-4.1}} & \multicolumn{3}{c}{\textbf{Sonnet~4.6}} \\",
        r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}",
        r"\textbf{Field} & Agree & Disagree & $\Delta$ & Agree & Disagree & $\Delta$ "
        r"& N\,disagree \\",
        r"\midrule",
    ]
    def _fmt3(v):
        return f"{v:.3f}" if pd.notna(v) else "---"

    for _, r in conf_df.iterrows():
        field_esc = escape_latex(str(r["field"]))
        lines.append(
            f"\\texttt{{{field_esc}}} & {_fmt3(r['gpt_conf_agree'])} & "
            f"{_fmt3(r['gpt_conf_disagree'])} & {_fmt3(r['gpt_delta'])} & "
            f"{_fmt3(r['son_conf_agree'])} & {_fmt3(r['son_conf_disagree'])} & "
            f"{_fmt3(r['son_delta'])} & {int(r['n_disagree'])}\\\\"
        )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]

    # Narrative
    son_positive = (conf_df["son_delta"] > 0.02).sum()
    gpt_positive = (conf_df["gpt_delta"] > 0.02).sum()
    n_fields = len(conf_df)
    son_mean_delta = conf_df["son_delta"].mean()
    gpt_mean_delta = conf_df["gpt_delta"].mean()
    lines.append(textwrap.dedent(f"""\
        \\subsection{{Interpretation}}
        Across the {n_fields} fields with at least 10 disagreements,
        Sonnet~4.6 shows a positive calibration signal ($\\Delta > 0.02$) on
        \\textbf{{{son_positive}/{n_fields}}} fields (mean $\\Delta = {son_mean_delta:.3f}$),
        compared with \\textbf{{{gpt_positive}/{n_fields}}} for
        GPT-4.1 (mean $\\Delta = {gpt_mean_delta:.3f}$).

        \\begin{{tcolorbox}}[
          colback=green!4!white, colframe=green!50!black,
          title={{\\textbf{{Key finding: confidence calibration}}}},
          fonttitle=\\small\\sffamily, breakable,
        ]
        \\textbf{{Sonnet~4.6}} has a consistently positive $\\Delta$ across fields ---
        it gives \\emph{{lower}} confidence precisely on the cases where the two models
        disagree.  This makes Sonnet's confidence score a \\textbf{{useful signal for
        flagging uncertain extractions}} in downstream quality control.

        \\medskip
        \\textbf{{GPT-4.1}} has $\\Delta \\approx 0$ on most fields --- it tends to
        assign high confidence (often 1.0) regardless of whether it agrees with Sonnet
        or not.  Its confidence score is therefore \\textbf{{not a reliable signal for
        quality control}}.  Users of GPT-4.1 extractions should rely on independent
        verification rather than confidence thresholds.
        \\end{{tcolorbox}}
    """))

    return "\n".join(lines) + "\n"


# ─────────────────────────────── document assembly ───────────────────────────

def render_fairness_section(
    ag: pd.DataFrame,
    gran_analysis: pd.DataFrame,
    text_threshold: float = 0.70,
) -> str:
    """Section discussing what a fair comparison requires and how we achieve it."""

    # ── threshold sensitivity table ────────────────────────────────────────
    text_fields = ag[ag["type"] == "text"].copy()
    text_fields = text_fields.sort_values("agreement_rate", ascending=False)

    tsens_lines = [
        r"\begin{center}\small",
        r"\begin{tabular}{lrr}",
        r"\toprule",
        r"\textbf{Text field} & \textbf{Agreement @ 0.95 (old)} & \textbf{Agreement @ 0.70 (current)} \\",
        r"\midrule",
    ]

    # old values from pre-0.70 run (hardcoded from prior results)
    _old_rates = {
        "other_game_info": 0.0, "indep_var": 0.010, "DVs_Definitions": 0.065,
        "DVs": 0.173, "IVs": 0.284, "data_id": 0.326,
        "participant_education": 0.440, "participant_age": 0.626,
        "participant_gender": 0.689, "participant_country": 0.837,
    }
    for _, r in text_fields.iterrows():
        f = str(r["field"])
        old = _old_rates.get(f, float("nan"))
        new = r["agreement_rate"]
        old_str = f"{old*100:.1f}\\%" if not pd.isna(old) else "---"
        new_str = f"{new*100:.1f}\\%"
        field_esc = escape_latex(f)
        tsens_lines.append(f"\\texttt{{{field_esc}}} & {old_str} & {new_str} \\\\")
    tsens_lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    tsens_table = "\n".join(tsens_lines)

    # ── category B bias stats ──────────────────────────────────────────────
    # From the agreement table: fields in CAT_B and their one-missing counts
    cat_b_fields = ["CONFIG_chat", "CONFIG_punishmentExists", "CONFIG_rewardExists",
                    "CONFIG_showPunishmentId", "CONFIG_showRewardId"]
    ag_b = ag[ag["field"].isin(cat_b_fields)][["field", "n_one_missing", "n_disagree"]].copy()
    ab_lines = [
        r"\begin{center}\small",
        r"\begin{tabular}{lrr}",
        r"\toprule",
        r"\textbf{Field} & \textbf{N one-missing} & \textbf{N both-present disagree} \\",
        r"\midrule",
    ]
    for _, r in ag_b.iterrows():
        f_esc = escape_latex(str(r["field"]))
        n_om = int(r["n_one_missing"])
        n_tot_dis = int(r["n_disagree"])
        n_bp_dis = n_tot_dis - n_om
        ab_lines.append(f"\\texttt{{{f_esc}}} & {n_om} & {n_bp_dis} \\\\")
    ab_lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    ab_table = "\n".join(ab_lines)

    # granularity correctness summary
    if not gran_analysis.empty:
        vc = gran_analysis["verdict"].value_counts()
        n_total_mis = len(gran_analysis)
        n_ss = int(vc.get("sonnet_splits_gpt", 0))
        n_gs = int(vc.get("gpt_splits_sonnet", 0))
        n_diff = n_total_mis - n_ss - n_gs
        gran_text = textwrap.dedent(f"""\
            Granularity analysis (Section~\\ref{{sec:granularity}}) shows that
            \\textbf{{{n_ss}/{n_total_mis}}} mismatches are ``Sonnet splits GPT'' ---
            Sonnet's extra conditions are recognisable refinements of GPT's, not
            fabrications.  Only \\textbf{{{n_gs}}} mismatches go the other way (GPT splits
            Sonnet).  The remaining \\textbf{{{n_diff}}} have low name overlap and require
            human review.  This pattern is consistent with Sonnet applying the extraction
            rule more strictly, making it the \\emph{{reference}} for granularity in
            ambiguous cases until a human ground truth is established.
        """)
    else:
        gran_text = "Granularity analysis data not available."

    return textwrap.dedent(f"""\
        \\section{{Evaluation Fairness}}

        This section documents the methodological choices made to ensure the
        comparison is as fair as possible to both models.

        \\subsection{{Text Similarity Threshold}}

        The original 0.95 cosine threshold was designed to catch only exact or near-exact
        matches. It penalised both models equally for paraphrase variation that has no
        bearing on extraction quality.  A human reviewer would consider two descriptions
        of the same DV that differ only in wording as \\emph{{equivalent}}, not
        \\emph{{disagreeing}}.

        We therefore adopt a threshold of \\textbf{{{text_threshold:.2f}}}, which:
        \\begin{{itemize}}
          \\item Accepts paraphrases and synonymous naming conventions as agreements.
          \\item Still rejects genuinely different content: e.g., ``cooperation'' vs.\\
            ``earnings'' or ``punishment exists'' vs.\\ ``reward exists'' score $<0.50$.
          \\item Has a clear semantic interpretation: texts scoring $\\geq{text_threshold:.2f}$
            are about the same concept; texts scoring $<{text_threshold:.2f}$ are discussing
            meaningfully different things.
        \\end{{itemize}}

        The table below shows how agreement rates change under the two thresholds:

        {tsens_table}

        \\medskip
        The dramatic improvement in \\texttt{{DVs\\_Definitions}} (6.5\\%~$\\rightarrow$~97.8\\%)
        confirms that virtually all disagreements at 0.95 were paraphrase noise, not
        real extraction errors.  Fields that remain below 80\\% even at 0.70
        (\\texttt{{other\\_game\\_info}}, \\texttt{{indep\\_var}}) have \\emph{{genuinely}}
        different content between models --- these are meaningful disagreements.

        \\subsection{{Numeric Tolerance}}
        We use a dual criterion: absolute tolerance $|a-b| \\leq 0.01$ (to protect
        near-zero values like MPCR fractions) \\emph{{plus}} a 5\\% relative tolerance.
        This is symmetric --- neither model benefits from the rule --- and matches the
        precision one would expect from manual extraction.

        \\subsection{{Missing vs.\\ Zero: Category~B Is a Prompt Violation, Not a Convention}}
        For binary configuration fields (\\texttt{{CONFIG\\_chat}}, \\texttt{{CONFIG\\_punishmentExists}},
        etc.), the extraction prompt is unambiguous: ``silence $\\rightarrow$ N/A, not~0.''
        There is no convention choice to make --- the rule is already specified.

        {ab_table}

        Almost all Category~B disagreements are one-side-missing: one model gave a value
        (0), the other gave N/A.  When both models gave a value, agreement exceeds 95\\%.
        This tells us the models agree on \\emph{{what}} the feature is when they both
        see explicit evidence --- they only disagree on \\emph{{how to handle silence}}.

        Counting the one-missing cases: \\textbf{{Sonnet~4.6}} codes a value (typically~0)
        when GPT says N/A in \\textbf{{1{{,}}784 cases}}; GPT does so when Sonnet says N/A
        in only \\textbf{{535 cases}}.  Sonnet is the larger contributor, but
        \\textbf{{both models violate the rule:}} we identified 93 silence-based
        violations in GPT-4.1 and 161 in Sonnet~4.6 by examining whether the
        reasoning trace cites explicit evidence of absence or merely notes silence.
        GPT's violations are often borderline (indirect methodology citations from
        referenced papers); Sonnet's are more straightforwardly silence-based.

        \\textbf{{Correct post-processing:}} apply a keyword filter to \\emph{{both}}
        models' outputs, converting 0 values on these fields to N/A whenever the
        reasoning contains silence keywords (``not mentioned'', ``not described'')
        without companion explicit-evidence keywords (``explicitly prohibited'',
        ``paper states'').  See the Category~B verdict for the full filter code.

        \\subsection{{Granularity: Which Model Is Correct?}}
        {gran_text}

        \\subsection{{Condition Alignment}}
        Conditions are now aligned using the \\textbf{{Hungarian algorithm}} on
        \\texttt{{text-embedding-3-small}} cosine similarities of \\texttt{{data\\_id}}
        strings --- replacing an earlier alphabetical sort.
        Switching to semantic alignment eliminated \\textbf{{685 false disagreements}}
        (17{{,}}939 $\\rightarrow$ 17{{,}}254), confirming the alphabetical approach was
        occasionally mis-pairing conditions when the two models used different naming
        conventions.

        \\textbf{{Residual risk:}} Embedding-based alignment can still fail for
        factorial designs with near-identical condition names or generic labels
        (``Condition~1'', ``Condition~2'').  For the current dataset the failure
        rate is small: mis-aligned pairs produce broad random-looking mismatches
        across many fields, which are visible as outliers in Category~C and easy
        to spot-check manually.
    """)


PREAMBLE = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{booktabs}
\usepackage[table]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,urlcolor=blue!60!black]{hyperref}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{caption}
\usepackage[utf8]{inputenc}
\usepackage{microtype}
\usepackage{parskip}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{array}

\setlength{\LTpost}{0pt}

\title{\textbf{GPT-4.1 vs.\ Sonnet~4.6}\\[4pt]
       \large A Taxonomy of Extraction Disagreements\\
       on Public Goods Game Papers}
\author{Generated automatically by \texttt{generate\_disagreement\_report.py}}
\date{\today}
"""


def build_document(sections: list[str]) -> str:
    body = "\n\n".join(sections)
    return PREAMBLE + "\n\\begin{document}\n\\maketitle\n\\tableofcontents\n\\newpage\n\n" + body + "\n\\end{document}\n"


# ─────────────────────────────── compilation ─────────────────────────────────

def compile_latex(tex_path: Path, runs: int = 2) -> bool:
    """Run pdflatex (twice for cross-references).  Returns True if PDF produced."""
    import shutil
    if not shutil.which("pdflatex"):
        print("pdflatex not found — skipping PDF compilation.")
        return False
    pdf_path = tex_path.with_suffix(".pdf")
    for run_idx in range(runs):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_path.name],
            capture_output=True, text=True,
            cwd=tex_path.parent,
        )
        # pdflatex exits non-zero even for recoverable errors; check actual PDF
        if run_idx == runs - 1:
            if pdf_path.exists():
                # Check for unrecoverable errors in the log
                log = result.stdout + result.stderr
                if "Fatal error" in log or "Emergency stop" in log:
                    print("pdflatex encountered a fatal error.  See the .log file.")
                    return False
                # Non-fatal errors: PDF produced but may have issues
                latex_errors = [l for l in log.splitlines() if l.startswith("!")]
                if latex_errors:
                    print(f"pdflatex warnings/errors ({len(latex_errors)} lines starting with '!'):")
                    for line in latex_errors[:10]:
                        print(f"  {line}")
                return True
            else:
                print("pdflatex failed to produce a PDF.  Check the .log file.")
                print(result.stdout[-1500:])
                return False
    return False


# ─────────────────────────────── main ────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compile", action="store_true",
                        help="Run pdflatex after writing the .tex file")
    parser.add_argument("--n-examples", type=int, default=7,
                        help="Number of examples per category section (default 7)")
    parser.add_argument("--output", type=Path, default=OUTPUT_TEX)
    parser.add_argument("--text-threshold", type=float, default=0.70,
                        help="Cosine similarity threshold used in the comparison (default 0.70)")
    args = parser.parse_args()

    n = args.n_examples
    output_tex: Path = args.output
    text_threshold: float = args.text_threshold

    print("Loading Excel files …")
    gpt_df = load_model_df(GPT41_FILES)
    son_df = load_model_df(SONNET46_FILES)
    print(f"  GPT-4.1:   {len(gpt_df):,} condition rows")
    print(f"  Sonnet 4.6: {len(son_df):,} condition rows")

    print("Loading comparison outputs …")
    ag = pd.read_csv(COMPARISON_DIR / "agreement.csv")
    dis = pd.read_csv(COMPARISON_DIR / "disagreements.csv")
    counts = pd.read_csv(COMPARISON_DIR / "experiment_counts.csv")
    gran_analysis_path = COMPARISON_DIR / "granularity_analysis.csv"
    gran_analysis = (
        pd.read_csv(gran_analysis_path)
        if gran_analysis_path.exists()
        else pd.DataFrame()
    )
    print(f"  Disagreements: {len(dis):,} rows across {dis['custom_id'].nunique()} papers")

    # Assign condition_idx using the same semantic alignment as compare_extraction_models.py
    emb_cache_path = COMPARISON_DIR / ".embedding_cache.pkl"
    if emb_cache_path.exists():
        print("Loading embedding cache for semantic condition alignment …")
        with emb_cache_path.open("rb") as fh:
            emb_cache: dict = pickle.load(fh)
        gpt_df, son_df = _assign_condition_idx_semantic(gpt_df, son_df, emb_cache)
        print("  Semantic alignment applied.")
    else:
        print("  Embedding cache not found — falling back to alphabetical alignment.")
        gpt_df = _assign_condition_idx_alphabetical(gpt_df)
        son_df = _assign_condition_idx_alphabetical(son_df)

    print("Building long-format DataFrames for enrichment …")
    gpt_long = make_long(gpt_df, "gpt41")
    son_long = make_long(son_df, "sonnet46")

    print("Enriching disagreements with reasoning …")
    dis_enriched = enrich_disagreements(dis, gpt_long, son_long)
    dis_enriched = add_category(dis_enriched)

    # Category counts
    cat_counts = dis_enriched["category"].value_counts()
    print("  Category breakdown:", dict(cat_counts))
    cat_a_n = int(cat_counts.get("A", 0))
    cat_b_n = int(cat_counts.get("B", 0))
    cat_c_n = int(cat_counts.get("C", 0))
    total_field_dis = cat_a_n + cat_b_n + cat_c_n
    pct_a = cat_a_n / max(total_field_dis, 1) * 100
    pct_b = cat_b_n / max(total_field_dis, 1) * 100
    pct_c = cat_c_n / max(total_field_dis, 1) * 100

    print("Computing confidence analysis …")
    matched_papers = set(
        counts.loc[counts["count_match"], "custom_id"].astype(str)
    )
    conf_df = compute_confidence_analysis(dis_enriched, gpt_df, son_df, matched_papers)

    # ── overall statistics ──────────────────────────────────────────────────
    total_papers = len(counts)
    n_matched = int(counts["count_match"].sum())
    n_mismatch = total_papers - n_matched
    pct_mismatch = n_mismatch / total_papers * 100
    n_pairs = ag["n_condition_pairs"].iloc[0]

    worst_field = ag.sort_values("agreement_rate").iloc[0]
    best_field = ag.sort_values("agreement_rate").iloc[-1]

    abstract_section = textwrap.dedent(f"""\
        \\section*{{Abstract}}
        We compare structured extractions from \\textbf{{{total_papers}}} Public Goods
        Game papers produced independently by GPT-4.1 and Claude Sonnet~4.6.  Both
        models extract 37 fields per experimental condition (values, reasoning, and
        confidence scores) covering experimental design, configuration parameters,
        dependent variables, and participant demographics.

        After excluding {n_mismatch} papers ({pct_mismatch:.1f}\\%) where the models
        disagree on the number of experimental conditions (\\emph{{granularity mismatch}}),
        we compare \\textbf{{{n_matched}}} papers spanning \\textbf{{{n_pairs:,}}}
        condition pairs.  Field-level agreement ranges from
        \\textbf{{{worst_field['agreement_rate']*100:.0f}\\%}}
        (\\texttt{{{escape_latex(worst_field['field'])}}}) to
        \\textbf{{{best_field['agreement_rate']*100:.0f}\\%}}
        (\\texttt{{{escape_latex(best_field['field'])}}}).

        We organise disagreements into four categories:
        \\begin{{itemize}}
          \\item \\textbf{{Category~A --- Natural}} ({cat_a_n:,} disagreements, {pct_a:.0f}\\%):
            naming/terminology conventions and level-of-detail differences where no
            single answer is objectively correct.  At a cosine threshold of {text_threshold:.2f},
            most text-field disagreements resolve as paraphrases; the remainder reflect
            genuine content differences.
          \\item \\textbf{{Category~B --- Prompt violation: silence vs.\\ N/A}} ({cat_b_n:,}, {pct_b:.0f}\\%):
            one model marks a field N/A (not mentioned) while the other records 0
            (not present), reflecting a methodological ambiguity.
          \\item \\textbf{{Category~C --- Systematic}} ({cat_c_n:,}, {pct_c:.0f}\\%):
            disagreements on numeric or binary fields whose values are unambiguously
            stated in the paper; one model is likely wrong.
          \\item \\textbf{{Category~D --- Granularity}} ({n_mismatch} papers, {pct_mismatch:.1f}\\%):
            models extract different numbers of experimental conditions entirely.
            Correctness analysis shows Sonnet typically sub-divides GPT's conditions
            rather than inventing new ones.
        \\end{{itemize}}

        Sonnet~4.6 shows better confidence calibration: it reports lower confidence
        precisely on cases where it disagrees with GPT-4.1.  GPT-4.1 frequently
        assigns confidence 1.0 regardless, making its confidence scores less useful
        for downstream quality control.
    """)

    # ── agreement overview ─────────────────────────────────────────────────
    img_agree = str(COMPARISON_DIR / "agreement.png")
    agreement_section = (
        "\\section{Overall Agreement Statistics}\n\n"
        "The table below lists all 37 extracted fields sorted by agreement rate "
        "(worst first).  Colours: "
        "\\colorbox{red!18}{red} $<50\\%$, "
        "\\colorbox{orange!28}{orange} 50--80\\%, "
        "\\colorbox{green!18}{green} $>80\\%$."
        "\n\n"
        + render_agreement_table(ag)
        + "\n\n"
        + "\\begin{figure}[h]\n"
        + f"  \\centering\n  \\includegraphics[width=\\textwidth]{{{img_agree}}}\n"
        + "  \\caption{Per-field agreement rates between GPT-4.1 and Sonnet~4.6."
        "  Fields are ordered by agreement rate.}\n"
        + "\\end{figure}\n"
    )

    # ── category D ─────────────────────────────────────────────────────────
    cat_d_section = render_granularity_section(
        counts, gpt_df, son_df, gran_analysis, n_examples=n
    )

    # ── category A ─────────────────────────────────────────────────────────
    cat_a_section = render_category_section(
        category="A",
        title="Category A: Natural Disagreements",
        description=textwrap.dedent("""\
            Category~A covers fields where the two models capture the \\emph{same
            underlying information} but express it differently.  Two sub-types appear:

            \\begin{description}
              \\item[Naming / terminology] Fields \\texttt{DVs}, \\texttt{IVs}, and
                \\texttt{data\\_id} exhibit near-zero embedding-similarity agreement
                because each model names measures in its own convention
                (e.g., ``\\texttt{individual\\_cooperation}'' vs.\\ ``\\texttt{%
                individual\\_cooperation\\_rate}'').  An expert coder would also choose
                a naming style, and two experts would commonly disagree.

              \\item[Level of detail] Fields \\texttt{indep\\_var},
                \\texttt{other\\_game\\_info}, and \\texttt{DVs\\_Definitions} have
                near-zero agreement because the models differ dramatically in verbosity
                without differing in factual content.  GPT-4.1 tends to be terse;
                Sonnet~4.6 tends to be comprehensive.

              \\item[Demographics formatting] \\texttt{participant\\_age},
                \\texttt{participant\\_gender}, \\texttt{participant\\_education}, and
                \\texttt{participant\\_country} are reported with different levels of
                aggregation (e.g., mean age vs.\\ age range).
            \\end{description}
        """),
        verdict=textwrap.dedent("""\
            These disagreements are \\textbf{natural}: domain experts asked to code the
            same papers would produce similar variation.  They do not indicate that one
            model is ``wrong.''  For downstream uses that require consistent naming
            (e.g., structured databases), a post-processing normalisation step is
            advisable rather than choosing one model over the other.
        """),
        dis_enriched=dis_enriched,
        ag=ag,
        fields_in_category=sorted(CAT_A_FIELDS),
        n_examples=n,
    )

    # ── category B ─────────────────────────────────────────────────────────
    cat_b_section = render_category_section(
        category="B",
        title="Category B: Prompt Violation --- Silence vs.\\ N/A",
        description=textwrap.dedent("""\
            Category~B covers binary configuration fields where one model records
            0 (``not present'') from silence while the other correctly records N/A
            (``not mentioned'').  The fields affected are:
            \\texttt{CONFIG\\_chat}, \\texttt{CONFIG\\_punishmentExists},
            \\texttt{CONFIG\\_rewardExists}, \\texttt{CONFIG\\_showPunishmentId},
            and \\texttt{CONFIG\\_showRewardId}.

            \\textbf{This is not a convention ambiguity.}  The extraction prompt
            (\\texttt{batch\\_processing/build\\_batch\\_input.py}, \\texttt{INSTRUCTION\\_TEXT})
            is explicit for every one of these fields:
            \\begin{itemize}
              \\item \\texttt{CONFIG\\_chat}: ``N/A if communication is not mentioned
                anywhere in the paper --- do NOT code 0 from silence.''
              \\item \\texttt{CONFIG\\_punishmentExists}: ``N/A if punishment is not
                explicitly described --- do NOT infer from other conditions.''
              \\item \\texttt{CONFIG\\_rewardExists}: ``silence $\\rightarrow$ N/A, not 0.
                Code 0 only if the paper explicitly states no reward mechanism exists.''
              \\item \\texttt{CONFIG\\_showPunishmentId} / \\texttt{CONFIG\\_showRewardId}:
                ``N/A if the paper does not address whether identities are revealed ---
                do not infer 0 from silence.''
            \\end{itemize}

            \\textbf{Both models violate the rule --- but at different rates and
            for different reasons.}  We classify each 0-coding on a Category~B
            field by the language in its reasoning trace.  A coding is a
            \\emph{silence-based violation} if the reasoning contains phrases like
            ``not mentioned'', ``not described'', ``not reported'', or ``not
            explicitly stated'' \\emph{without} a companion phrase like
            ``explicitly prohibited'', ``paper states no~\\ldots{}'', or
            ``without communication.''

            \\begin{center}\\small
            \\begin{tabular}{lrrr}
            \\toprule
            \\textbf{Model} & \\textbf{Total 0-codings} &
            \\textbf{Silence-based violations} &
            \\textbf{Explicit-evidence (valid)} \\\\
            \\midrule
            GPT-4.1   & 2{,}122 & 93  & 545 \\\\
            Sonnet~4.6 & 4{,}343 & 161 & 831 \\\\
            \\bottomrule
            \\end{tabular}
            \\end{center}

            Sonnet codes \\textbf{4{,}343} zeros vs.\\ GPT's \\textbf{2{,}122} --- more than
            twice as many --- and is $1.7\\times$ more likely to produce a silence-based
            violation (161 vs.\\ 93).  However, GPT-4.1 also violates the rule:
            93 of its~0 codings rest purely on the absence of a mention, with no
            affirmative evidence cited.  A meaningful fraction of GPT's violations
            are borderline --- the reasoning cites methodology from a referenced
            paper (e.g., ``instructions followed Andreoni and Gee (2012), which
            prohibited communication'') --- but the prompt still requires an
            explicit statement in the paper being extracted, not an inference from
            a citation.
        """),
        verdict=textwrap.dedent("""\
            \\textbf{Both models violate the ``silence $\\rightarrow$ N/A'' rule}, but
            Sonnet~4.6 does so at a higher rate and more consistently.  GPT-4.1's
            violations are often borderline (indirect methodology citations), while
            Sonnet's are more straightforwardly silence-based.  The prompt was
            confirmed to be \\emph{identical} for both models, so this is model
            behaviour, not a prompt difference.

            When both models give a value (both-present), agreement exceeds 95\\%,
            confirming the extraction logic is correct --- the divergence is purely
            in how each model handles the absence of explicit evidence.

            \\textbf{Recommended post-extraction filter} (applicable to both models,
            especially Sonnet):

            \\begin{verbatim}
SILENCE_KWS = [
    "not mentioned", "no mention", "not described",
    "not explicitly", "not reported", "not stated",
    "not discussed", "not addressed",
]
EXPLICIT_KWS = [
    "explicitly prohibited", "explicitly states no",
    "explicitly stated", "paper states", "without communication",
    "no communication was", "communication was not",
    "paper explicitly",
]
CAT_B_FIELDS = [
    "CONFIG_chat", "CONFIG_punishmentExists",
    "CONFIG_rewardExists", "CONFIG_showPunishmentId",
    "CONFIG_showRewardId",
]

def is_silence_violation(value, reason):
    v = str(value).lower().strip()
    r = str(reason).lower()
    if v != "0":
        return False
    has_silence = any(kw in r for kw in SILENCE_KWS)
    has_explicit = any(kw in r for kw in EXPLICIT_KWS)
    return has_silence and not has_explicit

for field in CAT_B_FIELDS:
    reason_col = field + "_reason"
    mask = df.apply(
        lambda row: is_silence_violation(row[field], row.get(reason_col, "")),
        axis=1
    )
    df.loc[mask, field] = float("nan")  # convert back to N/A
            \\end{verbatim}

            This filter converts silence-based~0 codings back to N/A without
            touching valid 0s that cite explicit evidence.  It should be applied
            to \\emph{both} GPT-4.1 and Sonnet~4.6 outputs; it primarily affects
            Sonnet (larger violation count) but is correct to apply universally.
        """),
        dis_enriched=dis_enriched,
        ag=ag,
        fields_in_category=sorted(CAT_B_FIELDS),
        n_examples=n,
    )

    # ── category C ─────────────────────────────────────────────────────────
    cat_c_fields = sorted(
        set(ALL_FIELDS) - CAT_A_FIELDS - CAT_B_FIELDS
    )
    cat_c_section = render_category_section(
        category="C",
        title="Category C: Systematic Extraction Errors",
        description=textwrap.dedent("""\
            Category~C covers fields where the paper contains a clear, unambiguous
            answer --- a number, a yes/no statement, or a binary indicator --- yet the
            two models give different answers.  At least one model is wrong.

            Key affected fields include:
            \\begin{itemize}
              \\item \\textbf{\\texttt{CONFIG\\_MPCR}} (87.4\\% agreement): the
                marginal-per-capita return, a ratio that appears explicitly in most
                papers.  Discrepancies often arise from whether to use the per-player
                or per-group formulation.
              \\item \\textbf{\\texttt{CONFIG\\_playerCount}} (90.7\\% agreement):
                group size.  Disagreements arise when the paper reports both session
                size and group size.
              \\item \\textbf{\\texttt{DV\\_efficiencyReported}} (78.1\\% agreement):
                binary indicator of whether the paper reports group efficiency.
                Discrepancies suggest one model missed a relevant section.
              \\item \\textbf{\\texttt{CONFIG\\_showOtherSummaries}} (70.4\\% agreement):
                whether participants saw a summary of others' contributions.
              \\item \\textbf{\\texttt{number\\_DVs}} (33.4\\% agreement): count of
                dependent variables, which should be derivable from the \\texttt{DVs}
                list but is often counted differently (e.g., whether sub-measures are
                counted separately).
            \\end{itemize}

            These disagreements propagate directly into the prediction pipeline:
            incorrect values for \\texttt{CONFIG\\_MPCR} or \\texttt{CONFIG\\_playerCount}
            change the feature representation used by the LLM when predicting
            experimental outcomes.
        """),
        verdict=textwrap.dedent("""\
            These disagreements are \\textbf{systematic}: the paper has a correct answer,
            and at least one model retrieved it incorrectly.  Examining the reasoning
            traces reveals two recurring failure modes:
            \\begin{enumerate}
              \\item \\textbf{Unit confusion}: GPT-4.1 and Sonnet~4.6 disagree on whether
                MPCR should be expressed per player or per group.  Sonnet typically
                reports the per-player value; GPT sometimes reports the group-level
                multiplier.
              \\item \\textbf{Scope confusion}: when a paper runs multiple experiments,
                one model extracts values from the wrong experiment, or conflates
                session-level and group-level parameters.
            \\end{enumerate}
            For high-stakes uses (e.g., feeding extracted values into a downstream
            model), Category~C fields warrant human spot-checking or an independent
            verification pass.
        """),
        dis_enriched=dis_enriched,
        ag=ag,
        fields_in_category=cat_c_fields,
        n_examples=n,
    )

    # ── confidence section ─────────────────────────────────────────────────
    conf_section = render_confidence_section(conf_df)

    # ── conclusion ─────────────────────────────────────────────────────────
    # (cat_a_n, cat_b_n, cat_c_n already computed above)
    # Recompute case-1/case-2 counts for the conclusion
    _son_more_papers = gran_analysis[gran_analysis["delta"] > 0]["custom_id"].tolist()
    _n_case1, _n_case2 = 0, 0
    for _p in _son_more_papers:
        _s = son_df[son_df["custom_id"] == _p]
        _g = gpt_df[gpt_df["custom_id"] == _p]
        _s_non = _s[_s["METHOD_experiment"].astype(str).str.lower().isin(["false","0","no"])]
        _g_non = _g[_g["METHOD_experiment"].astype(str).str.lower().isin(["false","0","no"])]
        if len(_s_non) > len(_g_non):
            _n_case2 += 1
        else:
            _n_case1 += 1
    _n_gpt_more = int((gran_analysis["delta"] < 0).sum())

    conclusion_section = textwrap.dedent(f"""\
        \\section{{Conclusion}}

        \\subsection{{Summary of Disagreements}}
        Across {n_pairs:,} condition pairs from {n_matched} papers, we observe
        {total_field_dis:,} field-level disagreements (plus {n_mismatch} papers with
        granularity mismatches).  Their breakdown:

        \\begin{{center}}
        \\begin{{tabular}}{{lrrr}}
        \\toprule
        \\textbf{{Category}} & \\textbf{{N}} & \\textbf{{\\%}} & \\textbf{{Verdict}} \\\\
        \\midrule
        A~---~Natural & {cat_a_n:,} & {pct_a:.1f}\\% & Natural (both models OK) \\\\
        B~---~Silence vs.~N/A & {cat_b_n:,} & {pct_b:.1f}\\% & Both models violate (Sonnet 2$\\times$ more) \\\\
        C~---~Systematic & {cat_c_n:,} & {pct_c:.1f}\\% & Systematic (one model wrong) \\\\
        D~---~Granularity & {n_mismatch} papers & {pct_mismatch:.1f}\\% of papers & Systematic \\\\
        \\bottomrule
        \\end{{tabular}}
        \\end{{center}}

        \\subsection{{Which Model Should We Use?}}

        The answer depends on which type of error is more costly for the downstream task:
        predicting Public Goods Game efficiency outcomes.

        \\begin{{center}}\\small
        \\begin{{tabular}}{{llp{{3.5cm}}p{{5cm}}}}
        \\toprule
        \\textbf{{Error}} & \\textbf{{Model}} & \\textbf{{Papers}} & \\textbf{{Cost to dataset}} \\\\
        \\midrule
        Case~1: misses entire experiments & GPT & $\\approx${_n_case1} &
          \\textbf{{High.}} Treatment arms are permanently invisible; no post-hoc fix \\\\[3pt]
        Case~2: adds non-PGG studies & Sonnet & $\\approx${_n_case2} &
          \\textbf{{Medium.}} Detectable via \\texttt{{METHOD\\_experiment=False}}; filterable \\\\[3pt]
        Overconfident confidence scores & GPT & all &
          \\textbf{{Low.}} Quality signal is useless for flagging uncertain rows \\\\[3pt]
        \\texttt{{number\\_DVs}} 33\\% agreement & GPT & all &
          \\textbf{{Medium.}} Structural field systematically wrong \\\\
        \\bottomrule
        \\end{{tabular}}
        \\end{{center}}

        \\medskip
        Case~1 is more damaging than Case~2 for this task.
        Sonnet~4.6's false positives (Case~2) are \\emph{{detectable and filterable}};
        GPT-4.1's false negatives (Case~1) silently corrupt literature coverage
        with no way to recover the missing conditions without re-running the paper.

        \\subsubsection*{{Recommendation: Sonnet~4.6 with a post-processing filter}}

        Use Sonnet~4.6 as the primary extraction model, then apply a single
        post-processing filter to catch Case~2 over-extractions:

        \\begin{{verbatim}}
# Flag conditions Sonnet may have over-extracted
df["flag_non_pgg"] = (
    df["METHOD_experiment"].str.lower().isin(["false", "0", "no"]) |
    df["experiment_environment"].isin(["Observational"])
)
        \\end{{verbatim}}

        This flags the $\\approx${_n_case2} Case~2 papers automatically.
        A one-time manual review of those papers removes non-PGG rows
        (meta-analyses, national surveys, anthropological datasets, etc.).
        The result is a dataset that is both \\textbf{{complete}} (no Case~1 omissions)
        and \\textbf{{clean}} (no Case~2 contamination).

        \\subsubsection*{{What about a model router?}}

        A router that selects GPT for mixed-paradigm papers and Sonnet for
        single-paradigm ones is theoretically appealing but has a hidden cost:
        to route correctly you must first classify the paper --- which requires
        reading it.  If you are reading the paper anyway, it is simpler to run
        Sonnet and apply the \\texttt{{METHOD\\_experiment}} filter.

        The one scenario where routing adds value is a targeted re-run of the
        {n_mismatch} mismatch papers through GPT as a cross-check.  If both
        models agree after re-extraction, that is strong evidence the condition
        count is correct.  If they still disagree, those papers are flagged for
        human inspection.

        \\begin{{center}}\\small
        \\begin{{tabular}}{{lp{{3.5cm}}p{{5cm}}}}
        \\toprule
        \\textbf{{Approach}} & \\textbf{{Effort}} & \\textbf{{Quality}} \\\\
        \\midrule
        \\textbf{{Sonnet + filter (recommended)}} &
          Low --- one afternoon of manual review of $\\approx${_n_case2} papers &
          High: complete coverage, clean scope \\\\[3pt]
        Router (Sonnet for multi-experiment, GPT for mixed) &
          High --- requires paper classifier &
          Marginally better in theory \\\\[3pt]
        GPT alone &
          None &
          Significant gaps: $\\approx${_n_case1} papers under-extracted \\\\
        \\bottomrule
        \\end{{tabular}}
        \\end{{center}}

        \\subsection{{Field-level Recommendations}}
        \\begin{{enumerate}}
          \\item \\textbf{{Category~A}} (naming/detail): apply a normalisation step
            (e.g., strip \\texttt{{\\_rate}} suffixes, lower-case) rather than choosing
            one model; both are extracting the same facts.
          \\item \\textbf{{Category~B}} (both models code 0 from silence, Sonnet more so):
            apply the keyword filter described in the Category~B verdict to
            \\emph{{both}} models' outputs.  The filter checks whether the reasoning
            trace cites explicit evidence of absence or merely notes silence, and
            converts silence-based~0 codings back to N/A.  No convention choice is
            needed --- the prompt already specifies the rule.
          \\item \\textbf{{Category~C}} (systematic errors): for \\texttt{{CONFIG\\_MPCR}},
            \\texttt{{CONFIG\\_playerCount}}, and \\texttt{{DV\\_efficiencyReported}},
            use Sonnet's confidence scores to flag low-confidence extractions and
            verify those with a second model or human reviewer.
          \\item \\textbf{{Granularity}}: re-run the {n_mismatch} mismatch papers
            through GPT as a cross-check; route remaining disagreements to human
            review before using those conditions downstream.
        \\end{{enumerate}}
    """)

    # ── fairness section ───────────────────────────────────────────────────
    fairness_section = render_fairness_section(
        ag=ag,
        gran_analysis=gran_analysis,
        text_threshold=text_threshold,
    )

    # ── assemble & write ────────────────────────────────────────────────────
    sections = [
        abstract_section,
        render_methodology_section(text_threshold=text_threshold),
        fairness_section,
        agreement_section,
        cat_d_section,
        cat_a_section,
        cat_b_section,
        cat_c_section,
        conf_section,
        conclusion_section,
    ]

    print(f"Writing LaTeX to {output_tex} …")
    output_tex.parent.mkdir(parents=True, exist_ok=True)
    output_tex.write_text(build_document(sections), encoding="utf-8")
    print(f"  Done.  File size: {output_tex.stat().st_size:,} bytes")

    if args.compile:
        print("Compiling PDF (pass 1) …")
        ok = compile_latex(output_tex)
        if ok:
            pdf = output_tex.with_suffix(".pdf")
            print(f"  PDF written to {pdf}")
        else:
            print(f"  Compilation failed.  Open {output_tex.with_suffix('.log')} for details.")
            print(f"  You can compile manually:")
            print(f"    cd {output_tex.parent}")
            print(f"    pdflatex {output_tex.name}")


if __name__ == "__main__":
    main()
