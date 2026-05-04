from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import numpy as np
import pandas as pd
from scipy.stats import linregress
from statsmodels.stats.multitest import multipletests

from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
FULL_CSV = RESULTS_DIR / "metadata_univariate_significance_selected4.csv"
SUMMARY_CSV = RESULTS_DIR / "metadata_univariate_significance_selected4_summary.csv"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
FEATURE_LABELS = {
    "empirical_share": "Empirical papers",
    "citation": "Citation",
    "journal_impact": "Journal Impact Factor",
    "recent": "Publication Year",
    "biology_share": "Biology Journals",
    "economics_share": "Economics Journals",
    "psychology_share": "Psychology Journals",
    "mathphysics_share": "Math/Physics Journals",
    "multidisciplinary_share": "Multidisciplinary Journals",
}
FEATURE_FAMILY = {
    "empirical_share": "paper_type",
    "citation": "citation",
    "journal_impact": "journal_impact",
    "recent": "publication_year",
    "biology_share": "journal_discipline",
    "economics_share": "journal_discipline",
    "psychology_share": "journal_discipline",
    "mathphysics_share": "journal_discipline",
    "multidisciplinary_share": "journal_discipline",
}
FEATURE_KEYS = list(FEATURE_LABELS)
PAPER_META_CSV = (
    ROOT
    / "literature"
    / "output"
    / "evidence_cards"
    / "literature_evidence_cards_cleaned"
    / "collection_metadata_sets"
    / "collection_metadata_catalog.csv"
)
PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"


def load_paper_df() -> pd.DataFrame:
    meta = pd.read_csv(PAPER_META_CSV).copy()
    meta["source_id"] = meta["custom_id"].astype(str).str.removesuffix(".md")
    meta = meta.drop_duplicates("source_id", keep="first")
    meta["journal_impact"] = np.log1p(pd.to_numeric(meta["jif_value"], errors="coerce"))
    meta["citation"] = np.log1p(pd.to_numeric(meta["Times Cited, All Databases"], errors="coerce").clip(lower=0))
    meta["empirical_share"] = meta["paper_type_primary"].map({"theory": 0.0, "empirical": 1.0})
    meta["recent"] = pd.to_numeric(meta["Publication Year"], errors="coerce")

    disc = meta["discipline_coarse"].fillna("").astype(str)
    meta["biology_share"] = disc.str.contains("bio_evo", regex=False).astype(float)
    meta["economics_share"] = disc.str.contains("economics", regex=False).astype(float)
    meta["psychology_share"] = disc.str.contains("psych_social", regex=False).astype(float)
    meta["mathphysics_share"] = disc.str.contains("math_phys_cs", regex=False).astype(float)
    meta["multidisciplinary_share"] = disc.str.contains("multidisciplinary", regex=False).astype(float)

    metrics = pd.read_csv(PAPER_METRICS_CSV)
    merged = metrics.merge(
        meta[["source_id", *FEATURE_KEYS]],
        on="source_id",
        how="left",
        validate="many_to_one",
    )
    return merged.loc[merged["model"].isin(MODELS)].copy()


def run_univariate_tests(df: pd.DataFrame, *, dataset_name: str, feature_keys: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for model in MODELS:
        part = df.loc[df["model"] == model].copy()
        y = pd.to_numeric(part["correlation"], errors="coerce")
        for feature_key in feature_keys:
            x = pd.to_numeric(part[feature_key], errors="coerce")
            valid = x.notna() & y.notna()
            xv = x.loc[valid].to_numpy(dtype=float)
            yv = y.loc[valid].to_numpy(dtype=float)
            n = len(xv)

            if n < 3 or np.nanstd(xv) == 0 or np.nanstd(yv) == 0:
                rows.append(
                    {
                        "dataset": dataset_name,
                        "model": model,
                        "feature_key": feature_key,
                        "feature_label": FEATURE_LABELS[feature_key],
                        "feature_family": FEATURE_FAMILY[feature_key],
                        "n": n,
                        "slope": np.nan,
                        "intercept": np.nan,
                        "rvalue": np.nan,
                        "r_squared": np.nan,
                        "p_value": np.nan,
                        "stderr": np.nan,
                        "x_mean": float(np.nanmean(xv)) if n else np.nan,
                        "x_sd": float(np.nanstd(xv, ddof=1)) if n > 1 else np.nan,
                        "y_mean": float(np.nanmean(yv)) if n else np.nan,
                        "sign": "NA",
                        "sig_raw_0_05": False,
                    }
                )
                continue

            fit = linregress(xv, yv)
            rows.append(
                {
                    "dataset": dataset_name,
                    "model": model,
                    "feature_key": feature_key,
                    "feature_label": FEATURE_LABELS[feature_key],
                    "feature_family": FEATURE_FAMILY[feature_key],
                    "n": n,
                    "slope": float(fit.slope),
                    "intercept": float(fit.intercept),
                    "rvalue": float(fit.rvalue),
                    "r_squared": float(fit.rvalue**2),
                    "p_value": float(fit.pvalue),
                    "stderr": float(fit.stderr),
                    "x_mean": float(np.mean(xv)),
                    "x_sd": float(np.std(xv, ddof=1)),
                    "y_mean": float(np.mean(yv)),
                    "sign": "positive" if fit.slope > 0 else "negative" if fit.slope < 0 else "zero",
                    "sig_raw_0_05": bool(fit.pvalue < 0.05),
                }
            )
    return pd.DataFrame(rows)


def add_bh_fdr(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["q_value_bh_within_dataset"] = np.nan
    for _, idx in out.groupby("dataset").groups.items():
        pvals = out.loc[idx, "p_value"].to_numpy(dtype=float)
        ok = np.isfinite(pvals)
        qvals = np.full_like(pvals, np.nan, dtype=float)
        if ok.any():
            qvals[ok] = multipletests(pvals[ok], method="fdr_bh")[1]
        out.loc[idx, "q_value_bh_within_dataset"] = qvals
    out["sig_bh_0_05_within_dataset"] = out["q_value_bh_within_dataset"] < 0.05
    return out


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (dataset_name, family, label), part in df.groupby(
        ["dataset", "feature_family", "feature_label"], dropna=False
    ):
        rows.append(
            {
                "dataset": dataset_name,
                "feature_family": family,
                "feature_label": label,
                "n_models_tested": int(part["model"].nunique()),
                "n_negative_raw_p_lt_0_05": int(((part["sign"] == "negative") & part["sig_raw_0_05"]).sum()),
                "n_positive_raw_p_lt_0_05": int(((part["sign"] == "positive") & part["sig_raw_0_05"]).sum()),
                "n_negative_bh_q_lt_0_05": int(
                    ((part["sign"] == "negative") & part["sig_bh_0_05_within_dataset"]).sum()
                ),
                "n_positive_bh_q_lt_0_05": int(
                    ((part["sign"] == "positive") & part["sig_bh_0_05_within_dataset"]).sum()
                ),
                "mean_slope": float(part["slope"].mean()),
                "mean_r_squared": float(part["r_squared"].mean()),
            }
        )
    return pd.DataFrame(rows).sort_values(["dataset", "feature_family", "feature_label"]).reset_index(drop=True)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_df = load_paper_df()
    collection_df = build_collection_df()
    collection_df = collection_df.loc[collection_df["model"].isin(MODELS)].copy()

    parts = [
        run_univariate_tests(paper_df, dataset_name="individual_papers", feature_keys=FEATURE_KEYS),
        run_univariate_tests(
            collection_df,
            dataset_name="collections",
            feature_keys=collection_df.columns.intersection(FEATURE_KEYS).tolist(),
        ),
    ]
    full = add_bh_fdr(pd.concat(parts, ignore_index=True))
    summary = build_summary(full)

    full.to_csv(FULL_CSV, index=False)
    summary.to_csv(SUMMARY_CSV, index=False)

    print(f"Wrote {FULL_CSV}")
    print(f"Wrote {SUMMARY_CSV}")


if __name__ == "__main__":
    main()
