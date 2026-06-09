"""
Compare Claude vs human extractions on the 25-paper out-of-sample test set.

Aligns conditions per paper (greedy best-similarity), then computes per-field
exact-match agreement. Numeric fields use ±5% tolerance.

Outputs:
    results/extraction_model_comparison/test_set_field_accuracy.csv
    results/extraction_model_comparison/test_set_per_paper.csv
    results/extraction_model_comparison/test_set_disagreements.csv
"""
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
HUMAN_CSV = REPO_ROOT / "evaluator" / "inputs" / "human" / "human_out_of_sample.csv"
CLAUDE_CSV = REPO_ROOT / "evaluator" / "inputs" / "llm" / "claude_out_of_sample.csv"
OUT_DIR = REPO_ROOT / "results" / "extraction_model_comparison"

# Fields evaluated for agreement. Skip free-text / metadata columns.
EVAL_FIELDS = [
    "Empirical", "Controled_Or_Observational", "Lab_Or_Field",
    "Simulation", "Analytical", "Review",
    "CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp", "CONFIG_MPCR",
    "CONFIG_chat", "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId", "CONFIG_showRewardId", "CONFIG_showNRounds",
    "CONFIG_punishmentExists", "CONFIG_punishmentCost", "CONFIG_punishmentTech",
    "CONFIG_rewardExists", "CONFIG_rewardCost", "CONFIG_rewardTech",
    "Independent Variables", "Dependent Variables",
]

NUMERIC_FIELDS = {
    "CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_MPCR",
    "CONFIG_punishmentCost", "CONFIG_punishmentTech",
    "CONFIG_rewardCost", "CONFIG_rewardTech",
    "Independent Variables", "Dependent Variables",
}

NA_TOKENS = {"n/a", "na", "n/r", "nr", ""}


def normalize(v) -> str:
    if pd.isna(v):
        return ""
    return str(v).strip().lower().replace('"', "")


def as_number(v: str):
    if v in NA_TOKENS:
        return None
    try:
        return float(v.replace(",", ""))
    except ValueError:
        return None


def values_match(field: str, h: str, c: str) -> str:
    """Returns: 'match' / 'mismatch' / 'both_na' / 'one_na'."""
    h_na = h in NA_TOKENS
    c_na = c in NA_TOKENS
    if h_na and c_na:
        return "both_na"
    if h_na or c_na:
        return "one_na"
    if field in NUMERIC_FIELDS:
        hn, cn = as_number(h), as_number(c)
        if hn is not None and cn is not None:
            denom = max(abs(hn), abs(cn), 1e-9)
            if abs(hn - cn) / denom <= 0.05:
                return "match"
        # Fall through to string match if number parse fails
    return "match" if h == c else "mismatch"


# ── Alignment ─────────────────────────────────────────────────────────────────


def label_tokens(row: dict) -> set[str]:
    text = " ".join([
        str(row.get("Experiment Name", "") or ""),
        str(row.get("Topic", "") or ""),
        str(row.get("Misc", "") or "")[:200],
    ])
    text = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    toks = {t for t in text.split() if len(t) > 3}
    return toks


def align(human_rows: list[dict], claude_rows: list[dict]) -> list[tuple[dict | None, dict | None]]:
    """Greedy best-Jaccard alignment, preserving human order. Unmatched Claude rows trail."""
    if not human_rows:
        return [(None, r) for r in claude_rows]
    if not claude_rows:
        return [(r, None) for r in human_rows]

    used = set()
    pairs: list[tuple[dict | None, dict | None]] = []
    h_tokens = [label_tokens(r) for r in human_rows]
    c_tokens = [label_tokens(r) for r in claude_rows]

    for hi, h in enumerate(human_rows):
        best_ci, best_score = None, -1.0
        ht = h_tokens[hi]
        for ci, c in enumerate(claude_rows):
            if ci in used:
                continue
            ct = c_tokens[ci]
            if not ht and not ct:
                # No info — fall back to positional
                score = 1.0 if hi == ci else 0.0
            elif not ht or not ct:
                score = 0.0
            else:
                inter = len(ht & ct)
                union = len(ht | ct)
                score = inter / union if union else 0.0
            if score > best_score:
                best_score = score
                best_ci = ci
        if best_ci is not None:
            used.add(best_ci)
            pairs.append((h, claude_rows[best_ci]))
        else:
            pairs.append((h, None))

    for ci, c in enumerate(claude_rows):
        if ci not in used:
            pairs.append((None, c))
    return pairs


def main() -> None:
    human_df = pd.read_csv(HUMAN_CSV)
    claude_df = pd.read_csv(CLAUDE_CSV)

    # Group by paper
    human_by_paper = {pid: g.to_dict("records") for pid, g in human_df.groupby("Filename")}
    claude_by_paper = {pid: g.to_dict("records") for pid, g in claude_df.groupby("Filename")}

    # Align every paper
    aligned_pairs: list[tuple[str, dict | None, dict | None]] = []
    granularity_rows: list[dict] = []
    for pid in sorted(set(human_by_paper) | set(claude_by_paper)):
        h_rows = human_by_paper.get(pid, [])
        c_rows = claude_by_paper.get(pid, [])
        granularity_rows.append({
            "paper_id": pid,
            "n_human_conds": len(h_rows),
            "n_claude_conds": len(c_rows),
            "diff": len(c_rows) - len(h_rows),
        })
        for h, c in align(h_rows, c_rows):
            aligned_pairs.append((pid, h, c))

    # Per-field agreement
    field_counter: dict[str, Counter] = defaultdict(Counter)
    disagreements: list[dict] = []
    per_paper: dict[str, Counter] = defaultdict(Counter)

    for pid, h, c in aligned_pairs:
        if h is None or c is None:
            # Unmatched row — count every field as "one_na" if Claude over-/under-extracted
            for f in EVAL_FIELDS:
                field_counter[f]["unmatched_row"] += 1
                per_paper[pid]["unmatched_row"] += 1
            continue
        for f in EVAL_FIELDS:
            hv = normalize(h.get(f))
            cv = normalize(c.get(f))
            outcome = values_match(f, hv, cv)
            field_counter[f][outcome] += 1
            per_paper[pid][outcome] += 1
            if outcome == "mismatch":
                disagreements.append({
                    "paper_id": pid,
                    "field": f,
                    "human": h.get(f),
                    "claude": c.get(f),
                    "human_cond": h.get("Granularity", ""),
                    "claude_cond": c.get("Granularity", ""),
                })

    # ── Save ──────────────────────────────────────────────────────────────────
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Per-field accuracy
    field_rows = []
    for f in EVAL_FIELDS:
        c = field_counter[f]
        n_compared = c["match"] + c["mismatch"]
        n_both_na = c["both_na"]
        n_one_na = c["one_na"]
        n_unmatched = c["unmatched_row"]
        n_total_pairs = n_compared + n_both_na + n_one_na
        acc = c["match"] / n_compared if n_compared else float("nan")
        acc_with_na = (c["match"] + n_both_na) / n_total_pairs if n_total_pairs else float("nan")
        field_rows.append({
            "field": f,
            "n_pairs": n_total_pairs,
            "n_match": c["match"],
            "n_mismatch": c["mismatch"],
            "n_both_na": n_both_na,
            "n_one_na": n_one_na,
            "n_unmatched_row": n_unmatched,
            "accuracy_excl_na": round(acc, 3) if n_compared else None,
            "accuracy_incl_na": round(acc_with_na, 3) if n_total_pairs else None,
        })
    field_df = pd.DataFrame(field_rows).sort_values("accuracy_incl_na", ascending=False, na_position="last")
    field_df.to_csv(OUT_DIR / "test_set_field_accuracy.csv", index=False)

    # 2. Per-paper summary
    per_paper_rows = []
    for r in granularity_rows:
        pid = r["paper_id"]
        c = per_paper[pid]
        n_compared = c["match"] + c["mismatch"]
        per_paper_rows.append({
            **r,
            "n_match": c["match"],
            "n_mismatch": c["mismatch"],
            "n_both_na": c["both_na"],
            "n_one_na": c["one_na"],
            "accuracy_excl_na": round(c["match"] / n_compared, 3) if n_compared else None,
        })
    per_paper_df = pd.DataFrame(per_paper_rows).sort_values("accuracy_excl_na", ascending=False, na_position="last")
    per_paper_df.to_csv(OUT_DIR / "test_set_per_paper.csv", index=False)

    # 3. Raw disagreements
    pd.DataFrame(disagreements).to_csv(OUT_DIR / "test_set_disagreements.csv", index=False)

    # ── Print summary ─────────────────────────────────────────────────────────
    total_match = sum(field_counter[f]["match"] for f in EVAL_FIELDS)
    total_mismatch = sum(field_counter[f]["mismatch"] for f in EVAL_FIELDS)
    total_both_na = sum(field_counter[f]["both_na"] for f in EVAL_FIELDS)
    total_one_na = sum(field_counter[f]["one_na"] for f in EVAL_FIELDS)
    total_unmatched = sum(field_counter[f]["unmatched_row"] for f in EVAL_FIELDS)
    total_compared = total_match + total_mismatch

    granularity_correct = sum(1 for r in granularity_rows if r["diff"] == 0)

    print("\n" + "=" * 70)
    print("Claude vs Human — Out-of-Sample Test Set (25 papers)")
    print("=" * 70)
    print(f"Papers with matching condition count: {granularity_correct}/{len(granularity_rows)}")
    print(f"Total cell pairs evaluated: {total_compared:,} (+ {total_both_na:,} both-N/A, {total_one_na:,} one-N/A, {total_unmatched:,} unmatched-row)")
    print(f"\nOverall accuracy (excl N/A pairs): {total_match / total_compared:.1%}")
    print(f"Overall accuracy (incl both-N/A as match): {(total_match + total_both_na) / (total_compared + total_both_na + total_one_na):.1%}")
    print(f"\nTop 5 fields by accuracy:")
    for _, r in field_df.head(5).iterrows():
        print(f"  {r['field']:<35} {r['accuracy_incl_na'] or 0:.1%}  ({r['n_match']}/{r['n_pairs']})")
    print(f"\nBottom 5 fields by accuracy:")
    for _, r in field_df.tail(5).iterrows():
        print(f"  {r['field']:<35} {r['accuracy_incl_na'] or 0:.1%}  ({r['n_match']}/{r['n_pairs']})")
    print(f"\nOutputs written to {OUT_DIR}/")
    print(f"  - test_set_field_accuracy.csv ({len(EVAL_FIELDS)} fields)")
    print(f"  - test_set_per_paper.csv (25 papers)")
    print(f"  - test_set_disagreements.csv ({len(disagreements)} disagreements)")


if __name__ == "__main__":
    main()
