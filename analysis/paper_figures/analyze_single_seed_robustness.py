from __future__ import annotations

import os
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from analyze_literature_metadata_supervised_benchmarks import (  # noqa: E402
    COLLECTION_FEATURES as BENCH_COLLECTION_FEATURES,
    COLLECTION_NUMERIC,
    PAPER_FEATURES as BENCH_PAPER_FEATURES,
    PAPER_NUMERIC,
)
from paper_figures.plot_figures_3to8_mean_repeat_correlation import (  # noqa: E402
    FIGURE34_MODEL_ORDER,
    build_alt_benchmark_datasets,
    build_alt_benchmark_tables,
    internal_repeat_ids,
    load_condition_repeat_scores,
)
from plot_cross_model_repeat_rank_ceiling import (  # noqa: E402
    Q_COLS,
    load_collection_repeat_predictions,
    load_paper_repeat_predictions,
    load_truth,
    rowwise_corr,
)
from plot_figure7_metadata_effect_robustness import (  # noqa: E402
    COLLECTION_FEATURES,
    PAPER_FEATURES,
    build_collection_feature_frame,
    build_rows,
    load_paper_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "single_seed_robustness"
REPEATS = [f"rep{i}" for i in range(1, 6)]
PAPER_ITEM_COL = "source_id"
COLLECTION_ITEM_COL = "variant_id"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_single_seed_metrics.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_single_seed_metrics.csv"
PAPER_HETEROGENEITY_CSV = RESULTS_DIR / "figure3_single_seed_heterogeneity_summary.csv"
COLLECTION_HETEROGENEITY_CSV = RESULTS_DIR / "figure4_single_seed_heterogeneity_summary.csv"
RANK_PAIRWISE_CSV = RESULTS_DIR / "figure5_single_seed_rank_pairwise.csv"
RANK_SUMMARY_CSV = RESULTS_DIR / "figure5_single_seed_rank_summary.csv"
FIG6_BEST_CSV = RESULTS_DIR / "figure6_single_seed_metadata_best.csv"
FIG6_SUMMARY_CSV = RESULTS_DIR / "figure6_single_seed_metadata_summary.csv"
FIG7_PAPER_ROWS_CSV = RESULTS_DIR / "figure7_single_seed_paper_rows.csv"
FIG8_COLLECTION_ROWS_CSV = RESULTS_DIR / "figure8_single_seed_collection_rows.csv"
SIGN_SUMMARY_CSV = RESULTS_DIR / "figure7_8_single_seed_sign_summary.csv"
REPORT_MD = RESULTS_DIR / "single_seed_robustness_report.md"


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    mask = np.isfinite(a) & np.isfinite(b)
    if mask.sum() < 3:
        return float("nan")
    return float(spearmanr(a[mask], b[mask]).statistic)


def build_single_seed_metric_tables() -> tuple[pd.DataFrame, pd.DataFrame]:
    truth = load_truth()
    paper_repeat_predictions = load_paper_repeat_predictions()
    collection_repeat_predictions = load_collection_repeat_predictions()
    baseline_repeat_scores, _ = load_condition_repeat_scores()

    paper_rows: list[dict[str, object]] = []
    for model in FIGURE34_MODEL_ORDER:
        repeat_map = paper_repeat_predictions[model]
        ids = internal_repeat_ids(repeat_map)
        baseline_scores = baseline_repeat_scores[model]
        for rep_idx, rep in enumerate(REPEATS, start=1):
            preds = repeat_map[rep].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            corrs = rowwise_corr(preds, truth)
            baseline_corr = float(baseline_scores[rep_idx - 1])
            for item_id, corr in zip(ids.astype(str), corrs):
                paper_rows.append(
                    {
                        "repeat": rep,
                        "repeat_index": rep_idx,
                        "model": model,
                        PAPER_ITEM_COL: str(item_id),
                        "correlation": float(corr),
                        "baseline_correlation": baseline_corr,
                        "delta_correlation": float(corr - baseline_corr) if np.isfinite(corr) else float("nan"),
                    }
                )

    collection_rows: list[dict[str, object]] = []
    for model in FIGURE34_MODEL_ORDER:
        repeat_map = collection_repeat_predictions[model]
        ids = internal_repeat_ids(repeat_map)
        baseline_scores = baseline_repeat_scores[model]
        for rep_idx, rep in enumerate(REPEATS, start=1):
            preds = repeat_map[rep].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            corrs = rowwise_corr(preds, truth)
            baseline_corr = float(baseline_scores[rep_idx - 1])
            for item_id, corr in zip(ids.astype(str), corrs):
                collection_rows.append(
                    {
                        "repeat": rep,
                        "repeat_index": rep_idx,
                        "model": model,
                        COLLECTION_ITEM_COL: str(item_id),
                        "correlation": float(corr),
                        "baseline_correlation": baseline_corr,
                        "delta_correlation": float(corr - baseline_corr) if np.isfinite(corr) else float("nan"),
                    }
                )

    return pd.DataFrame(paper_rows), pd.DataFrame(collection_rows)


def summarize_single_seed_heterogeneity(metric_df: pd.DataFrame, *, item_col: str, item_type: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (repeat, model), part in metric_df.groupby(["repeat", "model"], sort=False):
        corr = pd.to_numeric(part["correlation"], errors="coerce")
        finite = corr[np.isfinite(corr)]
        baseline_corr = float(part["baseline_correlation"].dropna().iloc[0])
        improved = finite > baseline_corr
        rows.append(
            {
                "item_type": item_type,
                "repeat": repeat,
                "model": model,
                "n_items": int(part[item_col].nunique()),
                "n_finite": int(finite.size),
                "baseline_correlation": baseline_corr,
                "mean_augmented_correlation": float(finite.mean()),
                "sd_augmented_correlation": float(finite.std(ddof=1)),
                "p10_augmented_correlation": float(np.quantile(finite, 0.10)),
                "p50_augmented_correlation": float(np.quantile(finite, 0.50)),
                "p90_augmented_correlation": float(np.quantile(finite, 0.90)),
                "n_above_baseline": int(improved.sum()),
                "share_above_baseline": float(improved.mean()),
            }
        )
    return pd.DataFrame(rows)


def build_single_seed_rank_tables(
    paper_metric_df: pd.DataFrame,
    collection_metric_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    pairwise_rows: list[dict[str, object]] = []
    for kind, metric_df, item_col in [
        ("papers", paper_metric_df, PAPER_ITEM_COL),
        ("collections", collection_metric_df, COLLECTION_ITEM_COL),
    ]:
        for repeat in REPEATS:
            wide = (
                metric_df.loc[metric_df["repeat"] == repeat, [item_col, "model", "correlation"]]
                .pivot(index=item_col, columns="model", values="correlation")
                .dropna()
                .reindex(columns=FIGURE34_MODEL_ORDER)
            )
            for model_a, model_b in combinations(FIGURE34_MODEL_ORDER, 2):
                pairwise_rows.append(
                    {
                        "kind": kind,
                        "repeat": repeat,
                        "model_a": model_a,
                        "model_b": model_b,
                        "n_items": int(len(wide)),
                        "observed_spearman": safe_spearman(
                            wide[model_a].to_numpy(dtype=float),
                            wide[model_b].to_numpy(dtype=float),
                        ),
                    }
                )
    pairwise_df = pd.DataFrame(pairwise_rows)
    summary_df = (
        pairwise_df.groupby(["kind", "repeat"], as_index=False)["observed_spearman"]
        .agg(["mean", "min", "max"])
        .reset_index()
        .rename(columns={"mean": "mean_spearman_rho", "min": "min_spearman_rho", "max": "max_spearman_rho"})
    )
    return pairwise_df, summary_df


def build_single_seed_metadata_predictability(
    paper_metric_df: pd.DataFrame,
    collection_metric_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    best_rows: list[pd.DataFrame] = []
    for repeat in REPEATS:
        paper_rep = paper_metric_df.loc[paper_metric_df["repeat"] == repeat].drop(columns=["repeat", "repeat_index"])
        collection_rep = collection_metric_df.loc[collection_metric_df["repeat"] == repeat].drop(columns=["repeat", "repeat_index"])
        alt_paper_bench, alt_collection_bench = build_alt_benchmark_datasets(paper_rep, collection_rep)
        benchmark_results, benchmark_best = build_alt_benchmark_tables(alt_paper_bench, alt_collection_bench)
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

    paper_rows: list[pd.DataFrame] = []
    collection_rows: list[pd.DataFrame] = []
    for repeat in REPEATS:
        paper_rep = paper_metric_df.loc[paper_metric_df["repeat"] == repeat, ["model", PAPER_ITEM_COL, "delta_correlation"]]
        collection_rep = collection_metric_df.loc[collection_metric_df["repeat"] == repeat, ["model", COLLECTION_ITEM_COL, "delta_correlation"]]

        paper_df = base_paper_df.merge(
            paper_rep,
            on=["model", PAPER_ITEM_COL],
            how="inner",
            validate="many_to_one",
        )
        collection_df = base_collection_df.merge(
            collection_rep,
            on=["model", COLLECTION_ITEM_COL],
            how="inner",
            validate="many_to_one",
        )

        paper_coef = build_rows(paper_df, item_type="Individual papers", feature_cols=PAPER_FEATURES)
        paper_coef["repeat"] = repeat
        collection_coef = build_rows(collection_df, item_type="Collections", feature_cols=COLLECTION_FEATURES)
        collection_coef["repeat"] = repeat
        paper_rows.append(paper_coef)
        collection_rows.append(collection_coef)

    return pd.concat(paper_rows, ignore_index=True), pd.concat(collection_rows, ignore_index=True)


def build_sign_summary(
    paper_rows: pd.DataFrame,
    collection_rows: pd.DataFrame,
) -> pd.DataFrame:
    rows = []
    for item_type, df in [("papers", paper_rows), ("collections", collection_rows)]:
        tmp = df.copy()
        tmp["positive"] = tmp["coef"] > 0
        tmp["negative"] = tmp["coef"] < 0
        tmp["signif_positive"] = tmp["ci_low"] > 0
        tmp["signif_negative"] = tmp["ci_high"] < 0
        summary = (
            tmp.groupby("feature_key", as_index=False)
            .agg(
                feature_label=("feature_label", "first"),
                mean_coef=("coef", "mean"),
                n_positive=("positive", "sum"),
                n_negative=("negative", "sum"),
                n_signif_positive=("signif_positive", "sum"),
                n_signif_negative=("signif_negative", "sum"),
                n_total=("coef", "size"),
            )
            .sort_values("feature_key")
            .reset_index(drop=True)
        )
        summary.insert(0, "item_type", item_type)
        rows.append(summary)
    return pd.concat(rows, ignore_index=True)


def format_range(series: pd.Series, digits: int = 3) -> str:
    return f"{series.min():.{digits}f} to {series.max():.{digits}f}"


def write_report(
    paper_heterogeneity: pd.DataFrame,
    collection_heterogeneity: pd.DataFrame,
    rank_summary: pd.DataFrame,
    fig6_summary: pd.DataFrame,
    sign_summary: pd.DataFrame,
) -> None:
    paper_rank = rank_summary.loc[rank_summary["kind"] == "papers", "mean_spearman_rho"]
    collection_rank = rank_summary.loc[rank_summary["kind"] == "collections", "mean_spearman_rho"]
    paper_pred = fig6_summary.loc[fig6_summary["dataset"] == "individual_papers"]
    collection_pred = fig6_summary.loc[fig6_summary["dataset"] == "metadata_filter_collections"]

    def row_for(item_type: str, feature_key: str) -> pd.Series:
        return sign_summary.loc[
            (sign_summary["item_type"] == item_type) & (sign_summary["feature_key"] == feature_key)
        ].iloc[0]

    lines = [
        "# Single-Seed Robustness",
        "",
        "This report summarizes whether the Figures 3-8 qualitative claims survive when each analysis is run on a single repeat instead of the 5-repeat mean.",
        "",
        "## Heterogeneity Across Augmented Inputs",
        f"- Papers: single-seed item SD ranges from {format_range(paper_heterogeneity['sd_augmented_correlation'])}; the share of papers above baseline ranges from {format_range(paper_heterogeneity['share_above_baseline'], 2)}.",
        f"- Collections: single-seed item SD ranges from {format_range(collection_heterogeneity['sd_augmented_correlation'])}; the share of collections above baseline ranges from {format_range(collection_heterogeneity['share_above_baseline'], 2)}.",
        "",
        "## Cross-Model Ranking Agreement",
        f"- Papers: mean pairwise Spearman ranges from {format_range(paper_rank)} across the five single repeats.",
        f"- Collections: mean pairwise Spearman ranges from {format_range(collection_rank)} across the five single repeats.",
        f"- Collections exceed papers in every single repeat: {all(collection_rank.to_numpy() > paper_rank.to_numpy())}.",
        "",
        "## Metadata Predictability",
        f"- Individual papers: grouped-CV R2 ranges from {format_range(paper_pred['cv_r2'])}; grouped-CV Spearman ranges from {format_range(paper_pred['cv_spearman'])}.",
        f"- Collections: grouped-CV R2 ranges from {format_range(collection_pred['cv_r2'])}; grouped-CV Spearman ranges from {format_range(collection_pred['cv_spearman'])}.",
        f"- Collections exceed papers in grouped-CV R2 in every repeat: {all(collection_pred['cv_r2'].to_numpy() > paper_pred['cv_r2'].to_numpy())}.",
        "",
        "## Feature-Direction Trends",
        f"- Paper empirical effect: negative in {int(row_for('papers', 'empirical_share')['n_negative'])}/{int(row_for('papers', 'empirical_share')['n_total'])} model-seed fits; significantly negative in {int(row_for('papers', 'empirical_share')['n_signif_negative'])}/{int(row_for('papers', 'empirical_share')['n_total'])}.",
        f"- Collection empirical-share effect: negative in {int(row_for('collections', 'empirical_share')['n_negative'])}/{int(row_for('collections', 'empirical_share')['n_total'])} model-seed fits; significantly negative in {int(row_for('collections', 'empirical_share')['n_signif_negative'])}/{int(row_for('collections', 'empirical_share')['n_total'])}.",
        f"- Paper citation effect: negative in {int(row_for('papers', 'citation')['n_negative'])}/{int(row_for('papers', 'citation')['n_total'])}; significantly negative in {int(row_for('papers', 'citation')['n_signif_negative'])}/{int(row_for('papers', 'citation')['n_total'])}.",
        f"- Collection citation effect: negative in {int(row_for('collections', 'citation')['n_negative'])}/{int(row_for('collections', 'citation')['n_total'])}; significantly negative in {int(row_for('collections', 'citation')['n_signif_negative'])}/{int(row_for('collections', 'citation')['n_total'])}.",
        f"- Paper journal-impact effect: positive in {int(row_for('papers', 'journal_impact')['n_positive'])}/{int(row_for('papers', 'journal_impact')['n_total'])}; significantly positive in {int(row_for('papers', 'journal_impact')['n_signif_positive'])}/{int(row_for('papers', 'journal_impact')['n_total'])}.",
        f"- Collection journal-impact effect: positive in {int(row_for('collections', 'journal_impact')['n_positive'])}/{int(row_for('collections', 'journal_impact')['n_total'])}; significantly positive in {int(row_for('collections', 'journal_impact')['n_signif_positive'])}/{int(row_for('collections', 'journal_impact')['n_total'])}.",
    ]
    REPORT_MD.write_text("\n".join(lines))


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_metrics, collection_metrics = build_single_seed_metric_tables()
    paper_metrics.to_csv(PAPER_METRICS_CSV, index=False)
    collection_metrics.to_csv(COLLECTION_METRICS_CSV, index=False)

    paper_heterogeneity = summarize_single_seed_heterogeneity(paper_metrics, item_col=PAPER_ITEM_COL, item_type="papers")
    collection_heterogeneity = summarize_single_seed_heterogeneity(collection_metrics, item_col=COLLECTION_ITEM_COL, item_type="collections")
    paper_heterogeneity.to_csv(PAPER_HETEROGENEITY_CSV, index=False)
    collection_heterogeneity.to_csv(COLLECTION_HETEROGENEITY_CSV, index=False)

    rank_pairwise, rank_summary = build_single_seed_rank_tables(paper_metrics, collection_metrics)
    rank_pairwise.to_csv(RANK_PAIRWISE_CSV, index=False)
    rank_summary.to_csv(RANK_SUMMARY_CSV, index=False)

    fig6_best, fig6_summary = build_single_seed_metadata_predictability(paper_metrics, collection_metrics)
    fig6_best.to_csv(FIG6_BEST_CSV, index=False)
    fig6_summary.to_csv(FIG6_SUMMARY_CSV, index=False)

    paper_rows, collection_rows = build_single_seed_metadata_effect_rows(paper_metrics, collection_metrics)
    paper_rows.to_csv(FIG7_PAPER_ROWS_CSV, index=False)
    collection_rows.to_csv(FIG8_COLLECTION_ROWS_CSV, index=False)

    sign_summary = build_sign_summary(paper_rows, collection_rows)
    sign_summary.to_csv(SIGN_SUMMARY_CSV, index=False)

    write_report(paper_heterogeneity, collection_heterogeneity, rank_summary, fig6_summary, sign_summary)


if __name__ == "__main__":
    main()
