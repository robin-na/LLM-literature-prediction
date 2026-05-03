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
from scipy.stats import spearmanr
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from paper_figures.analyze_single_seed_robustness import (  # noqa: E402
    FIGURE34_MODEL_ORDER,
    REPEATS,
)
from paper_figures.plot_figures_3to8_mean_repeat_correlation import (  # noqa: E402
    build_alt_benchmark_datasets,
    build_alt_benchmark_tables,
)
from plot_figure7_metadata_effect_robustness import (  # noqa: E402
    COLLECTION_FEATURES,
    PAPER_FEATURES,
    build_collection_feature_frame,
    load_paper_df,
)


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "single_seed_robustness"
RESULTS_DIR = ROOT / "results" / "paper" / "single_seed_robustness_summary"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_single_seed_metrics.csv"
COLLECTION_METRICS_CSV = SOURCE_RESULTS_DIR / "collection_single_seed_metrics.csv"
PAPER_HETEROGENEITY_CSV = SOURCE_RESULTS_DIR / "figure3_single_seed_heterogeneity_summary.csv"
COLLECTION_HETEROGENEITY_CSV = SOURCE_RESULTS_DIR / "figure4_single_seed_heterogeneity_summary.csv"
RANK_SUMMARY_CSV = SOURCE_RESULTS_DIR / "figure5_single_seed_rank_summary.csv"

FIG6_BEST_CSV = RESULTS_DIR / "figure6_single_seed_metadata_best.csv"
FIG6_SUMMARY_CSV = RESULTS_DIR / "figure6_single_seed_metadata_summary.csv"
FIG7_PAPER_ROWS_CSV = RESULTS_DIR / "figure7_single_seed_paper_point_rows.csv"
FIG8_COLLECTION_ROWS_CSV = RESULTS_DIR / "figure8_single_seed_collection_point_rows.csv"
SIGN_SUMMARY_CSV = RESULTS_DIR / "figure7_8_single_seed_sign_summary.csv"
REPORT_MD = RESULTS_DIR / "single_seed_robustness_report.md"


def fit_ridge_point(df: pd.DataFrame, feature_cols: list[str], *, y_col: str = "delta_correlation") -> pd.DataFrame:
    part = df[feature_cols + [y_col]].copy()
    y = pd.to_numeric(part[y_col], errors="coerce")
    X = part[feature_cols].apply(pd.to_numeric, errors="coerce")
    valid = y.notna()
    X = X.loc[valid].reset_index(drop=True)
    y = y.loc[valid].to_numpy(dtype=float)

    pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", RidgeCV(alphas=np.logspace(-3, 3, 13))),
        ]
    )
    pipe.fit(X, y)
    coef = pipe.named_steps["model"].coef_.astype(float)
    return pd.DataFrame({"feature_key": feature_cols, "coef": coef, "n": int(len(y))})


def build_single_seed_metadata_predictability(
    paper_metric_df: pd.DataFrame,
    collection_metric_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    best_rows: list[pd.DataFrame] = []
    for repeat in REPEATS:
        paper_rep = paper_metric_df.loc[paper_metric_df["repeat"] == repeat].drop(columns=["repeat", "repeat_index"])
        collection_rep = collection_metric_df.loc[collection_metric_df["repeat"] == repeat].drop(columns=["repeat", "repeat_index"])
        alt_paper_bench, alt_collection_bench = build_alt_benchmark_datasets(paper_rep, collection_rep)
        _, benchmark_best = build_alt_benchmark_tables(alt_paper_bench, alt_collection_bench)
        best_rep = benchmark_best.loc[
            (benchmark_best["target"] == "correlation")
            & (benchmark_best["scope"] == "within_model")
            & (benchmark_best["scope_name"].isin(FIGURE34_MODEL_ORDER))
            & (benchmark_best["dataset"].isin(["individual_papers", "metadata_filter_collections"]))
        ].copy()
        best_rep["repeat"] = repeat
        best_rows.append(best_rep)

    best_df = pd.concat(best_rows, ignore_index=True)
    summary_df = (
        best_df.groupby(["dataset", "repeat"], as_index=False)[["cv_r2", "cv_spearman", "mean_fold_r2", "mean_fold_spearman"]]
        .mean()
        .sort_values(["dataset", "repeat"])
        .reset_index(drop=True)
    )
    return best_df, summary_df


def build_single_seed_metadata_effect_rows(
    paper_metric_df: pd.DataFrame,
    collection_metric_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    base_paper_df = load_paper_df().drop(columns=["delta_correlation"])
    base_collection_df = build_collection_feature_frame().drop(columns=["delta_correlation"])

    paper_rows: list[dict[str, object]] = []
    collection_rows: list[dict[str, object]] = []
    for repeat in REPEATS:
        paper_rep = paper_metric_df.loc[paper_metric_df["repeat"] == repeat, ["model", "source_id", "delta_correlation"]]
        collection_rep = collection_metric_df.loc[collection_metric_df["repeat"] == repeat, ["model", "variant_id", "delta_correlation"]]

        paper_df = base_paper_df.merge(
            paper_rep,
            on=["model", "source_id"],
            how="inner",
            validate="many_to_one",
        )
        collection_df = base_collection_df.merge(
            collection_rep,
            on=["model", "variant_id"],
            how="inner",
            validate="many_to_one",
        )

        paper_coef = fit_ridge_point(paper_df, PAPER_FEATURES)
        paper_coef["feature_label"] = paper_coef["feature_key"]
        paper_coef["repeat"] = repeat
        paper_coef["item_type"] = "papers"
        for row in paper_coef.itertuples(index=False):
            paper_rows.append(row._asdict())

        collection_coef = fit_ridge_point(collection_df, COLLECTION_FEATURES)
        collection_coef["feature_label"] = collection_coef["feature_key"]
        collection_coef["repeat"] = repeat
        collection_coef["item_type"] = "collections"
        for row in collection_coef.itertuples(index=False):
            collection_rows.append(row._asdict())

    return pd.DataFrame(paper_rows), pd.DataFrame(collection_rows)


def build_sign_summary(paper_rows: pd.DataFrame, collection_rows: pd.DataFrame) -> pd.DataFrame:
    all_rows = pd.concat([paper_rows, collection_rows], ignore_index=True)
    all_rows["positive"] = all_rows["coef"] > 0
    all_rows["negative"] = all_rows["coef"] < 0
    summary = (
        all_rows.groupby(["item_type", "feature_key"], as_index=False)
        .agg(
            mean_coef=("coef", "mean"),
            n_positive=("positive", "sum"),
            n_negative=("negative", "sum"),
            n_total=("coef", "size"),
        )
        .sort_values(["item_type", "feature_key"])
        .reset_index(drop=True)
    )
    return summary


def format_range(series: pd.Series, digits: int = 3) -> str:
    return f"{series.min():.{digits}f} to {series.max():.{digits}f}"


def row_for(sign_summary: pd.DataFrame, item_type: str, feature_key: str) -> pd.Series:
    return sign_summary.loc[
        (sign_summary["item_type"] == item_type) & (sign_summary["feature_key"] == feature_key)
    ].iloc[0]


def write_report(
    paper_heterogeneity: pd.DataFrame,
    collection_heterogeneity: pd.DataFrame,
    rank_summary: pd.DataFrame,
    fig6_summary: pd.DataFrame,
    sign_summary: pd.DataFrame,
) -> None:
    paper_rank = rank_summary.loc[rank_summary["kind"] == "papers", "mean_spearman_rho"].reset_index(drop=True)
    collection_rank = rank_summary.loc[rank_summary["kind"] == "collections", "mean_spearman_rho"].reset_index(drop=True)
    paper_pred = fig6_summary.loc[fig6_summary["dataset"] == "individual_papers", ["repeat", "cv_r2", "cv_spearman"]].reset_index(drop=True)
    collection_pred = fig6_summary.loc[fig6_summary["dataset"] == "metadata_filter_collections", ["repeat", "cv_r2", "cv_spearman"]].reset_index(drop=True)

    lines = [
        "# Single-Seed Robustness Summary",
        "",
        "This report uses one repeat at a time and asks whether the Figures 3-8 qualitative claims still hold.",
        "",
        "## Heterogeneity Across Inputs",
        f"- Papers: item SD ranges from {format_range(paper_heterogeneity['sd_augmented_correlation'])}; share above baseline ranges from {format_range(paper_heterogeneity['share_above_baseline'], 2)}.",
        f"- Collections: item SD ranges from {format_range(collection_heterogeneity['sd_augmented_correlation'])}; share above baseline ranges from {format_range(collection_heterogeneity['share_above_baseline'], 2)}.",
        "",
        "## Cross-Model Ranking Agreement",
        f"- Papers: mean pairwise Spearman ranges from {format_range(paper_rank)}.",
        f"- Collections: mean pairwise Spearman ranges from {format_range(collection_rank)}.",
        f"- Collections exceed papers in every repeat: {all(collection_rank.to_numpy() > paper_rank.to_numpy())}.",
        "",
        "## Metadata Predictability",
        f"- Papers: grouped-CV R2 ranges from {format_range(paper_pred['cv_r2'])}; grouped-CV Spearman ranges from {format_range(paper_pred['cv_spearman'])}.",
        f"- Collections: grouped-CV R2 ranges from {format_range(collection_pred['cv_r2'])}; grouped-CV Spearman ranges from {format_range(collection_pred['cv_spearman'])}.",
        f"- Collections exceed papers in grouped-CV R2 in every repeat: {all(collection_pred['cv_r2'].to_numpy() > paper_pred['cv_r2'].to_numpy())}.",
        "",
        "## Feature Direction Trends (Point Estimates)",
        f"- Paper empirical effect is negative in {int(row_for(sign_summary, 'papers', 'empirical_share')['n_negative'])}/{int(row_for(sign_summary, 'papers', 'empirical_share')['n_total'])} model-seed fits.",
        f"- Collection empirical-share effect is negative in {int(row_for(sign_summary, 'collections', 'empirical_share')['n_negative'])}/{int(row_for(sign_summary, 'collections', 'empirical_share')['n_total'])} model-seed fits.",
        f"- Paper citation effect is negative in {int(row_for(sign_summary, 'papers', 'citation')['n_negative'])}/{int(row_for(sign_summary, 'papers', 'citation')['n_total'])} model-seed fits.",
        f"- Collection citation effect is negative in {int(row_for(sign_summary, 'collections', 'citation')['n_negative'])}/{int(row_for(sign_summary, 'collections', 'citation')['n_total'])} model-seed fits.",
        f"- Paper journal-impact effect is positive in {int(row_for(sign_summary, 'papers', 'journal_impact')['n_positive'])}/{int(row_for(sign_summary, 'papers', 'journal_impact')['n_total'])} model-seed fits.",
        f"- Collection journal-impact effect is positive in {int(row_for(sign_summary, 'collections', 'journal_impact')['n_positive'])}/{int(row_for(sign_summary, 'collections', 'journal_impact')['n_total'])} model-seed fits.",
    ]
    REPORT_MD.write_text("\n".join(lines))


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_metric_df = pd.read_csv(PAPER_METRICS_CSV)
    collection_metric_df = pd.read_csv(COLLECTION_METRICS_CSV)
    paper_heterogeneity = pd.read_csv(PAPER_HETEROGENEITY_CSV)
    collection_heterogeneity = pd.read_csv(COLLECTION_HETEROGENEITY_CSV)
    rank_summary = pd.read_csv(RANK_SUMMARY_CSV)

    fig6_best, fig6_summary = build_single_seed_metadata_predictability(paper_metric_df, collection_metric_df)
    fig6_best.to_csv(FIG6_BEST_CSV, index=False)
    fig6_summary.to_csv(FIG6_SUMMARY_CSV, index=False)

    paper_rows, collection_rows = build_single_seed_metadata_effect_rows(paper_metric_df, collection_metric_df)
    paper_rows.to_csv(FIG7_PAPER_ROWS_CSV, index=False)
    collection_rows.to_csv(FIG8_COLLECTION_ROWS_CSV, index=False)

    sign_summary = build_sign_summary(paper_rows, collection_rows)
    sign_summary.to_csv(SIGN_SUMMARY_CSV, index=False)

    write_report(paper_heterogeneity, collection_heterogeneity, rank_summary, fig6_summary, sign_summary)


if __name__ == "__main__":
    main()
