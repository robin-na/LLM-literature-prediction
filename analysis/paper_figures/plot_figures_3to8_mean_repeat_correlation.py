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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
from scipy import stats

from analyze_literature_metadata_supervised_benchmarks import (
    COLLECTION_FEATURES as BENCH_COLLECTION_FEATURES,
    COLLECTION_NUMERIC,
    PAPER_FEATURES as BENCH_PAPER_FEATURES,
    PAPER_NUMERIC,
    evaluate_models,
    summarize_best,
)
from plot_cross_model_repeat_rank_ceiling import (
    MODELS as FIVE_MODEL_ORDER,
    Q_COLS,
    load_collection_repeat_predictions,
    load_paper_repeat_predictions,
    load_truth,
    rowwise_corr,
)
from plot_figure7_metadata_effect_robustness import (
    PAPER_FEATURES as FIG7_PAPER_FEATURES,
    build_rows as build_ridge_rows,
    draw_figure as draw_ridge_figure,
    load_paper_df as load_current_figure7_paper_df,
)
from plot_figure8_collection_feature_importance_gpt41 import (
    FEATURE_KEYS as FIG8_FEATURE_KEYS,
    NONLINEAR_MODELS,
    compute_permutation_importance,
    compute_shap_tables,
    draw_figure as draw_feature_importance_figure,
    load_collection_feature_frame as load_current_figure8_collection_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_mean_repeat_correlation"

REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
PAPER_FEATURE_DATA_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "paper_feature_analysis_dataset_repeat5.csv"
)
CURRENT_COLLECTION_REL_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)
CURRENT_FIG5_PAIRWISE_CSV = ROOT / "results" / "paper" / "robustness" / "cross_model_repeat_rank_ceiling_pairwise.csv"
CURRENT_FIG5_RELIABILITY_CSV = ROOT / "results" / "paper" / "robustness" / "cross_model_repeat_rank_ceiling_reliability.csv"

FIGURE34_MODEL_ORDER = ["GPT-5.1", "GPT-4.1 Mini", "GPT-4.1", "GPT-5 Nano", "GPT-5 Mini"]
FIGURE6_MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
FIGURE5_EPSILON = 0.06

MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
FIGURE6_DATASET_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
FIGURE6_DATASET_COLORS = {
    "individual_papers": "#73808f",
    "metadata_filter_collections": "#e59a3a",
}


def internal_repeat_ids(repeat_map: dict[str, pd.DataFrame]) -> pd.Index:
    shared: set[str] | None = None
    for df in repeat_map.values():
        ids = set(df.index.astype(str).tolist())
        shared = ids if shared is None else (shared & ids)
    assert shared is not None
    return pd.Index(sorted(shared))


def load_condition_repeat_scores() -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    baseline: dict[str, np.ndarray] = {}
    benchmark: dict[str, np.ndarray] = {}
    for model in FIVE_MODEL_ORDER:
        base_scores = (
            repeat_rows.loc[
                (repeat_rows["model"] == model) & (repeat_rows["condition"] == "baseline"),
                ["repeat", "correlation"],
            ]
            .sort_values("repeat")["correlation"]
            .to_numpy(dtype=float)
        )
        benchmark_scores = (
            repeat_rows.loc[
                (repeat_rows["model"] == model) & (repeat_rows["condition"] == "benchmark"),
                ["repeat", "correlation"],
            ]
            .sort_values("repeat")["correlation"]
            .to_numpy(dtype=float)
        )
        baseline[model] = base_scores
        benchmark[model] = benchmark_scores
    return baseline, benchmark


def summarize_repeat_vector(values: np.ndarray) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    mean = float(np.mean(arr)) if n else float("nan")
    if n <= 1:
        return {"n": n, "mean": mean, "sd": float("nan"), "se": float("nan")}
    sd = float(np.std(arr, ddof=1))
    return {"n": n, "mean": mean, "sd": sd, "se": float(sd / np.sqrt(n))}


def build_paper_repeat_metrics(truth: np.ndarray, baseline_repeat_scores: dict[str, np.ndarray]) -> tuple[pd.DataFrame, pd.DataFrame]:
    repeat_predictions = load_paper_repeat_predictions()
    metric_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for model in FIGURE34_MODEL_ORDER:
        repeat_map = repeat_predictions[model]
        ids = internal_repeat_ids(repeat_map)
        score_list = []
        for rep in sorted(repeat_map):
            preds = repeat_map[rep].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            score_list.append(rowwise_corr(preds, truth))
        score_mat = np.stack(score_list, axis=1)

        baseline_scores = baseline_repeat_scores[model]
        baseline_summary = summarize_repeat_vector(baseline_scores)
        delta_mat = score_mat - baseline_scores[None, :]

        for i, source_id in enumerate(ids):
            corr_summary = summarize_repeat_vector(score_mat[i])
            delta_summary = summarize_repeat_vector(delta_mat[i])
            metric_rows.append(
                {
                    "model": model,
                    "source_id": str(source_id),
                    "n_aug_runs": corr_summary["n"],
                    "n_baseline_runs": baseline_summary["n"],
                    "correlation": corr_summary["mean"],
                    "correlation_repeat_sd": corr_summary["sd"],
                    "correlation_repeat_se": corr_summary["se"],
                    "baseline_correlation": baseline_summary["mean"],
                    "baseline_repeat_sd": baseline_summary["sd"],
                    "baseline_repeat_se": baseline_summary["se"],
                    "delta_correlation": delta_summary["mean"],
                    "delta_correlation_repeat_sd": delta_summary["sd"],
                    "delta_correlation_repeat_se": delta_summary["se"],
                }
            )

        summary_rows.append(
            {
                "model": model,
                "n_items": int(len(ids)),
                "baseline_correlation": baseline_summary["mean"],
                "baseline_repeat_sd": baseline_summary["sd"],
                "baseline_repeat_se": baseline_summary["se"],
                "mean_augmented_correlation": float(np.mean(score_mat.mean(axis=1))),
            }
        )

    metric_df = pd.DataFrame(metric_rows).sort_values(["model", "source_id"]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows).sort_values("model").reset_index(drop=True)
    return metric_df, summary_df


def build_collection_repeat_metrics(truth: np.ndarray, baseline_repeat_scores: dict[str, np.ndarray]) -> tuple[pd.DataFrame, pd.DataFrame]:
    repeat_predictions = load_collection_repeat_predictions()
    metric_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for model in FIGURE34_MODEL_ORDER:
        repeat_map = repeat_predictions[model]
        ids = internal_repeat_ids(repeat_map)
        score_list = []
        for rep in sorted(repeat_map):
            preds = repeat_map[rep].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            score_list.append(rowwise_corr(preds, truth))
        score_mat = np.stack(score_list, axis=1)

        baseline_scores = baseline_repeat_scores[model]
        baseline_summary = summarize_repeat_vector(baseline_scores)
        delta_mat = score_mat - baseline_scores[None, :]

        for i, variant_id in enumerate(ids):
            corr_summary = summarize_repeat_vector(score_mat[i])
            delta_summary = summarize_repeat_vector(delta_mat[i])
            metric_rows.append(
                {
                    "model": model,
                    "variant_id": str(variant_id),
                    "n_runs": corr_summary["n"],
                    "correlation": corr_summary["mean"],
                    "correlation_repeat_sd": corr_summary["sd"],
                    "correlation_repeat_se": corr_summary["se"],
                    "baseline_correlation": baseline_summary["mean"],
                    "baseline_repeat_sd": baseline_summary["sd"],
                    "baseline_repeat_se": baseline_summary["se"],
                    "delta_correlation": delta_summary["mean"],
                    "delta_correlation_repeat_sd": delta_summary["sd"],
                    "delta_correlation_repeat_se": delta_summary["se"],
                }
            )

        summary_rows.append(
            {
                "model": model,
                "n_items": int(len(ids)),
                "baseline_correlation": baseline_summary["mean"],
                "baseline_repeat_sd": baseline_summary["sd"],
                "baseline_repeat_se": baseline_summary["se"],
                "mean_augmented_correlation": float(np.mean(score_mat.mean(axis=1))),
            }
        )

    metric_df = pd.DataFrame(metric_rows).sort_values(["model", "variant_id"]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows).sort_values("model").reset_index(drop=True)
    return metric_df, summary_df


def build_figure3_tables(
    paper_metrics_df: pd.DataFrame,
    benchmark_repeat_scores: dict[str, np.ndarray],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    plot_df = (
        paper_metrics_df.loc[:, ["model", "source_id", "correlation", "baseline_correlation"]]
        .copy()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=FIGURE34_MODEL_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)

    summary_rows: list[dict[str, object]] = []
    for model in FIGURE34_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        benchmark_summary = summarize_repeat_vector(benchmark_repeat_scores[model])
        baseline = float(sub["baseline_correlation"].iloc[0])
        mean_aug = float(sub["correlation"].mean())
        count_above = int((sub["correlation"] > baseline).sum())
        count_below_or_equal = int(sub.shape[0] - count_above)
        share_below = float(count_below_or_equal / sub.shape[0])
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline,
                "mean_augmented_correlation": mean_aug,
                "sd_augmented_correlation": float(sub["correlation"].std(ddof=1)),
                "n_above_baseline": count_above,
                "n_below_or_equal_baseline": count_below_or_equal,
                "share_augmented_papers_below_baseline": share_below,
                "share_augmented_papers_above_baseline": 1.0 - share_below,
                "n_papers": int(sub.shape[0]),
                "benchmark_correlation": benchmark_summary["mean"],
            }
        )
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=FIGURE34_MODEL_ORDER, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def build_figure4_tables(
    collection_metrics_df: pd.DataFrame,
    benchmark_repeat_scores: dict[str, np.ndarray],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    base_cols = ["model", "variant_id", "correlation", "baseline_correlation"]
    plot_df = collection_metrics_df.loc[:, base_cols].copy()
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=FIGURE34_MODEL_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "correlation"]).reset_index(drop=True)

    summary_rows: list[dict[str, object]] = []
    for model in FIGURE34_MODEL_ORDER:
        sub = plot_df.loc[plot_df["model"] == model].copy()
        benchmark_summary = summarize_repeat_vector(benchmark_repeat_scores[model])
        baseline = float(sub["baseline_correlation"].iloc[0])
        count_above = int((sub["correlation"] > baseline).sum())
        count_below_or_equal = int(sub.shape[0] - count_above)
        summary_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline,
                "mean_augmented_correlation": float(sub["correlation"].mean()),
                "sd_augmented_correlation": float(sub["correlation"].std(ddof=1)),
                "n_above_baseline": count_above,
                "n_below_or_equal_baseline": count_below_or_equal,
                "share_augmented_collections_above_baseline": float(count_above / sub.shape[0]),
                "share_augmented_collections_below_or_equal_baseline": float(count_below_or_equal / sub.shape[0]),
                "n_collections": int(sub.shape[0]),
                "benchmark_correlation": benchmark_summary["mean"],
            }
        )
    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=FIGURE34_MODEL_ORDER, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)
    return plot_df, summary_df


def plot_density_figure(
    plot_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    *,
    mean_label: str,
    out_stem: str,
    item_label: str,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(
        len(FIGURE34_MODEL_ORDER),
        1,
        figsize=(8.8, 7.6),
        sharex=True,
        gridspec_kw={"hspace": 0.08},
    )

    x_min, x_max = 0.0, 0.90
    for ax, model in zip(axes, FIGURE34_MODEL_ORDER):
        sub = plot_df.loc[plot_df["model"] == model]
        refs = summary_df.loc[summary_df["model"] == model].iloc[0]
        vals = sub["correlation"].to_numpy(dtype=float)
        baseline_value = float(refs["baseline_correlation"])

        sns.kdeplot(
            x=vals,
            ax=ax,
            color=MODEL_COLORS[model],
            fill=False,
            linewidth=1.8,
            bw_adjust=0.9,
            cut=0,
            clip=(x_min, x_max),
        )
        kde_line = ax.lines[-1]
        x_kde = np.asarray(kde_line.get_xdata(), dtype=float)
        y_kde = np.asarray(kde_line.get_ydata(), dtype=float)
        mask = x_kde >= baseline_value
        if mask.any():
            ax.fill_between(
                x_kde[mask],
                y_kde[mask],
                0.0,
                color=MODEL_COLORS[model],
                alpha=0.18,
                zorder=1,
            )
        ax.axvline(
            float(refs["mean_augmented_correlation"]),
            color=MODEL_COLORS[model],
            linewidth=1.4,
            alpha=0.95,
        )
        ax.annotate(
            "",
            xy=(float(refs["mean_augmented_correlation"]), 0.84),
            xytext=(float(refs["baseline_correlation"]), 0.84),
            xycoords=("data", "axes fraction"),
            textcoords=("data", "axes fraction"),
            annotation_clip=False,
            zorder=5,
            arrowprops={
                "arrowstyle": "-|>",
                "lw": 1.15,
                "color": MODEL_COLORS[model],
                "alpha": 0.9,
                "mutation_scale": 10,
                "shrinkA": 0,
                "shrinkB": 0,
            },
        )
        ax.axvline(
            baseline_value,
            color=MODEL_COLORS[model],
            linewidth=1.1,
            linestyle="--",
            alpha=0.95,
        )
        ax.text(
            0.01,
            0.82,
            model,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=11.0,
            color=MODEL_COLORS[model],
        )
        ax.text(
            0.01,
            0.66,
            f"mean={float(refs['mean_augmented_correlation']):.3f}, SD={float(refs['sd_augmented_correlation']):.3f}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=8.9,
            color="#4b5563",
        )
        ax.text(
            0.01,
            0.53,
            f"no augmentation={baseline_value:.3f}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=8.9,
            color="#4b5563",
        )
        total_inputs = int(refs["n_papers"]) if "n_papers" in refs.index else int(refs["n_collections"])
        count_above = int(refs["n_above_baseline"])
        pct_above = 100.0 * float(count_above / total_inputs)
        ax.text(
            0.985,
            0.84,
            f"{pct_above:.0f}% improve prediction",
            transform=ax.transAxes,
            ha="right",
            va="center",
            fontsize=9.7,
            fontweight="semibold",
            color=MODEL_COLORS[model],
            bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "none", "alpha": 0.92},
        )
        ax.text(
            0.985,
            0.70,
            f"{count_above:,} / {total_inputs:,} {item_label}",
            transform=ax.transAxes,
            ha="right",
            va="center",
            fontsize=8.9,
            color="#4b5563",
            bbox={"boxstyle": "round,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.92},
        )
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.set_xticks(np.arange(0.0, 0.91, 0.2))
        ax.set_xticks(np.arange(0.0, 0.91, 0.1), minor=True)
        ax.grid(axis="x", which="minor", color="#e5e7eb", linewidth=0.8)
        ax.grid(axis="x", which="major", color="#e5e7eb", linewidth=0.0)
        ax.grid(axis="y", visible=False)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)

    axes[-1].set_xlim(x_min, x_max)
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.2))
    axes[-1].set_xticks(np.arange(0.0, 0.91, 0.1), minor=True)
    axes[-1].set_xlabel(r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")

    legend_items = [
        Line2D([0], [0], color="#4b5563", linewidth=1.4, label=mean_label),
        Line2D([0], [0], color="#4b5563", linewidth=1.1, linestyle="--", label="No augmentation"),
    ]
    fig.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.45, 0.995),
        ncol=2,
        frameon=False,
        columnspacing=1.6,
        handlelength=2.6,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.09, left=0.08, top=0.93, right=0.98)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{out_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def build_figure5_pairwise_rows(
    metric_df: pd.DataFrame,
    *,
    kind: str,
    item_id_col: str,
    epsilon: float,
) -> pd.DataFrame:
    wide = (
        metric_df.pivot(index=item_id_col, columns="model", values="correlation")
        .dropna()
        .reindex(columns=FIGURE34_MODEL_ORDER)
    )
    upper_idx = np.triu_indices(len(wide), k=1)
    values = {model: wide[model].to_numpy(dtype=np.float32) for model in FIGURE34_MODEL_ORDER}

    rows: list[dict[str, float | str | int]] = []
    for model_a, model_b in combinations(FIGURE34_MODEL_ORDER, 2):
        scores_a = values[model_a]
        scores_b = values[model_b]
        diff_a = scores_a[upper_idx[0]] - scores_a[upper_idx[1]]
        diff_b = scores_b[upper_idx[0]] - scores_b[upper_idx[1]]
        informative_mask = (np.abs(diff_a) > epsilon) & (np.abs(diff_b) > epsilon)
        informative_agreement = float(np.mean(np.sign(diff_a[informative_mask]) == np.sign(diff_b[informative_mask])))
        rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": int(len(wide)),
                "epsilon": float(epsilon),
                "observed_spearman": float(stats.spearmanr(scores_a, scores_b).statistic),
                "order_agreement_excluding_near_ties": informative_agreement,
                "informative_pair_coverage": float(informative_mask.mean()),
            }
        )
    return pd.DataFrame(rows)


def write_figure5_outputs(paper_metrics_df: pd.DataFrame, collection_metrics_df: pd.DataFrame) -> None:
    sns.set_theme(style="white", context="talk")

    plot_pairwise = pd.concat(
        [
            build_figure5_pairwise_rows(
                paper_metrics_df,
                kind="papers",
                item_id_col="source_id",
                epsilon=FIGURE5_EPSILON,
            ),
            build_figure5_pairwise_rows(
                collection_metrics_df,
                kind="collections",
                item_id_col="variant_id",
                epsilon=FIGURE5_EPSILON,
            ),
        ],
        ignore_index=True,
    )

    summary = (
        plot_pairwise.groupby("kind", as_index=False)[["observed_spearman", "order_agreement_excluding_near_ties", "informative_pair_coverage"]]
        .mean()
        .rename(
            columns={
                "observed_spearman": "mean_spearman_rho",
                "order_agreement_excluding_near_ties": "mean_order_agreement_excluding_near_ties",
                "informative_pair_coverage": "mean_informative_pair_coverage",
            }
        )
    )
    coverage = plot_pairwise.loc[:, ["kind", "model_a", "model_b", "epsilon", "informative_pair_coverage"]].copy()

    plot_pairwise.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_pairwise.csv", index=False)
    summary.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_summary.csv", index=False)
    coverage.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_epsilon_coverage.csv", index=False)

    def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
        matrix = pd.DataFrame(np.eye(len(FIGURE34_MODEL_ORDER)), index=FIGURE34_MODEL_ORDER, columns=FIGURE34_MODEL_ORDER)
        for row in df.itertuples(index=False):
            value = float(getattr(row, value_col))
            matrix.loc[row.model_a, row.model_b] = value
            matrix.loc[row.model_b, row.model_a] = value
        return matrix

    def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str, ylabel: str = "") -> None:
        sns.heatmap(
            matrix,
            ax=ax,
            cmap="YlGnBu",
            vmin=0.0,
            vmax=1.0,
            annot=True,
            fmt=".2f",
            cbar=False,
            square=True,
            linewidths=0.6,
            linecolor="white",
            annot_kws={"fontsize": 9},
        )
        ax.set_title(title, fontsize=12, pad=8)
        ax.set_xlabel("")
        ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
        ax.tick_params(axis="x", rotation=45, labelsize=9)
        ax.tick_params(axis="y", rotation=0, labelsize=9)

    def add_footnote(fig: plt.Figure) -> None:
        fig.text(
            0.5,
            0.02,
            f"ε = {FIGURE5_EPSILON:.2f}. Order agreement excludes item pairs whose score gap is at most ε in either model; the left panel remains exact Spearman ρ.",
            ha="center",
            fontsize=10,
        )

    fig, axes = plt.subplots(2, 2, figsize=(10.6, 8.1))
    specs = [
        ("papers", "observed_spearman", "Spearman ρ", "Individual papers"),
        ("papers", "order_agreement_excluding_near_ties", "Order agreement\n(excluding near-ties)", ""),
        ("collections", "observed_spearman", "Spearman ρ", "Collections"),
        ("collections", "order_agreement_excluding_near_ties", "Order agreement\n(excluding near-ties)", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = plot_pairwise.loc[plot_pairwise["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, value_col), title, ylabel)

    add_footnote(fig)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure5_cross_model_rank_robustness.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)

    for kind, ylabel, out_stems in [
        (
            "papers",
            "Individual papers",
            [
                "figure5_cross_model_rank_robustness_individual_papers",
                "figure5_1_cross_model_rank_robustness_individual_papers",
            ],
        ),
        (
            "collections",
            "Collections",
            [
                "figure5_cross_model_rank_robustness_collections",
                "figure5_2_cross_model_rank_robustness_collections",
            ],
        ),
    ]:
        sub = plot_pairwise.loc[plot_pairwise["kind"] == kind]
        kind_fig, kind_axes = plt.subplots(1, 2, figsize=(10.2, 4.9))
        draw_heatmap(kind_axes[0], build_matrix(sub, "observed_spearman"), "Spearman ρ", ylabel)
        draw_heatmap(
            kind_axes[1],
            build_matrix(sub, "order_agreement_excluding_near_ties"),
            "Order agreement\n(excluding near-ties)",
            "",
        )
        add_footnote(kind_fig)
        kind_fig.tight_layout(rect=[0, 0.06, 1, 1])
        for out_stem in out_stems:
            for ext in ["png", "pdf"]:
                kind_fig.savefig(PLOTS_DIR / f"{out_stem}.{ext}", dpi=300, bbox_inches="tight")
        plt.close(kind_fig)


def build_alt_benchmark_datasets(
    paper_metrics_df: pd.DataFrame,
    collection_metrics_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    paper_feature_df = pd.read_csv(PAPER_FEATURE_DATA_CSV)
    paper_metric_cols = paper_metrics_df.loc[:, ["model", "source_id", "correlation", "baseline_correlation", "delta_correlation"]]
    alt_paper_bench = (
        paper_feature_df.drop(columns=[col for col in ["correlation", "baseline_correlation", "delta_correlation"] if col in paper_feature_df.columns])
        .merge(paper_metric_cols, on=["model", "source_id"], how="left", validate="many_to_one")
    )

    collection_rel_df = pd.read_csv(CURRENT_COLLECTION_REL_CSV)
    collection_rel_df = collection_rel_df.loc[
        (collection_rel_df["variant_group"] == "metadata_filter") & (collection_rel_df["model"].isin(FIGURE6_MODEL_ORDER))
    ].copy()
    metric_cols = [
        "correlation",
        "baseline_correlation",
        "delta_correlation",
    ]
    alt_collection_bench = (
        collection_rel_df.drop(columns=[col for col in metric_cols if col in collection_rel_df.columns])
        .merge(
            collection_metrics_df.loc[:, ["model", "variant_id", *metric_cols]],
            on=["model", "variant_id"],
            how="left",
            validate="many_to_one",
        )
    )
    return alt_paper_bench, alt_collection_bench


def build_alt_benchmark_tables(
    alt_paper_bench: pd.DataFrame,
    alt_collection_bench: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    results = pd.concat(
        [
            evaluate_models(
                alt_paper_bench,
                dataset_name="individual_papers",
                features=BENCH_PAPER_FEATURES,
                numeric_cols=PAPER_NUMERIC,
                group_col="source_id",
                within_model=True,
            ),
            evaluate_models(
                alt_collection_bench,
                dataset_name="metadata_filter_collections",
                features=BENCH_COLLECTION_FEATURES,
                numeric_cols=COLLECTION_NUMERIC,
                group_col="variant_id",
                within_model=True,
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    best = summarize_best(results)
    return results, best


def write_figure6_outputs(best: pd.DataFrame) -> None:
    rows = best.loc[(best["target"] == "correlation") & (best["scope"] == "within_model")].copy()
    rows = rows.loc[rows["scope_name"].isin(FIGURE6_MODEL_ORDER)].copy()
    rows["dataset_label"] = rows["dataset"].map(FIGURE6_DATASET_LABELS)
    rows["model_label"] = (
        rows["model_name"]
        .astype(str)
        .str.replace("_", " ", regex=False)
        .str.title()
    )
    rows["scope_order"] = rows["scope_name"].map({name: idx for idx, name in enumerate(FIGURE6_MODEL_ORDER)})
    rows = rows.sort_values(["scope_order", "dataset_label"]).reset_index(drop=True)
    rows["se_fold_r2"] = rows["sd_fold_r2"] / np.sqrt(5)
    rows["se_fold_spearman"] = rows["sd_fold_spearman"] / np.sqrt(5)
    rows.to_csv(RESULTS_DIR / "figure6_metadata_predictability_correlation_rows.csv", index=False)

    def draw_panel(ax: plt.Axes, df: pd.DataFrame, metric: str, err: str, xlabel: str, show_ylabels: bool) -> None:
        row_y = np.arange(len(FIGURE6_MODEL_ORDER))[::-1].astype(float)
        y_map = dict(zip(FIGURE6_MODEL_ORDER, row_y))
        offsets = {"individual_papers": 0.18, "metadata_filter_collections": -0.18}
        height = 0.33

        for dataset in ["individual_papers", "metadata_filter_collections"]:
            part = df.loc[df["dataset"] == dataset].copy()
            ys = [y_map[name] + offsets[dataset] for name in part["scope_name"]]
            xs = part[metric].to_numpy(dtype=float)
            xerr = part[err].to_numpy(dtype=float)

            ax.barh(
                ys,
                xs,
                height=height,
                color=FIGURE6_DATASET_COLORS[dataset],
                alpha=0.86,
                edgecolor="none",
                zorder=2,
            )
            ax.errorbar(
                xs,
                ys,
                xerr=xerr,
                fmt="none",
                ecolor="#46505d",
                elinewidth=1.0,
                alpha=0.45,
                capsize=2.3,
                zorder=3,
            )

        ax.axvline(0.0, color="#777777", lw=1.1, ls=(0, (4, 3)), zorder=1)
        ax.set_xlabel(xlabel)
        ax.set_yticks(row_y)
        if show_ylabels:
            ax.set_yticklabels(FIGURE6_MODEL_ORDER)
        else:
            ax.tick_params(axis="y", labelleft=False)
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", color="#e6e6e6", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cfcfcf")
        ax.spines["bottom"].set_color("#cfcfcf")

    def annotate_models(ax: plt.Axes, df: pd.DataFrame, x_pos: float) -> None:
        row_y = np.arange(len(FIGURE6_MODEL_ORDER))[::-1].astype(float)
        y_map = dict(zip(FIGURE6_MODEL_ORDER, row_y))
        offsets = {"individual_papers": 0.18, "metadata_filter_collections": -0.18}
        for dataset in ["individual_papers", "metadata_filter_collections"]:
            part = df.loc[df["dataset"] == dataset].copy()
            for row in part.itertuples(index=False):
                ax.text(
                    x_pos,
                    y_map[row.scope_name] + offsets[dataset],
                    str(row.model_label),
                    ha="left",
                    va="center",
                    fontsize=8.6,
                    color=FIGURE6_DATASET_COLORS[dataset],
                )

    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.55), sharey=True)
    draw_panel(axes[0], rows, "mean_fold_r2", "se_fold_r2", "Grouped-CV $R^2$", show_ylabels=True)
    draw_panel(axes[1], rows, "mean_fold_spearman", "se_fold_spearman", "Grouped-CV Spearman", show_ylabels=False)

    axes[0].set_xlim(-0.075, max(0.24, rows["mean_fold_r2"].max() + rows["se_fold_r2"].max() + 0.02))
    axes[1].set_xlim(-0.03, max(0.52, rows["mean_fold_spearman"].max() + rows["se_fold_spearman"].max() + 0.03))
    annotate_models(axes[0], rows, x_pos=-0.072)

    handles = [
        Line2D([0], [0], color=FIGURE6_DATASET_COLORS[key], lw=10, solid_capstyle="round", label=label)
        for key, label in FIGURE6_DATASET_LABELS.items()
    ]
    handles.append(Line2D([0], [0], color="#777777", lw=1.1, ls=(0, (4, 3)), label="No signal"))
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.985),
        columnspacing=1.2,
        handlelength=2.0,
    )

    fig.subplots_adjust(top=0.78, left=0.24, right=0.985, bottom=0.19, wspace=0.16)
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure6_metadata_predictability_correlation.{ext}", dpi=300)
    plt.close(fig)


def write_figure7_outputs(paper_metrics_df: pd.DataFrame) -> None:
    current_df = load_current_figure7_paper_df().drop(columns=["delta_correlation"])
    alt_df = current_df.merge(
        paper_metrics_df.loc[:, ["model", "source_id", "delta_correlation"]],
        on=["model", "source_id"],
        how="inner",
        validate="many_to_one",
    )
    rows = build_ridge_rows(alt_df, item_type="Individual papers", feature_cols=FIG7_PAPER_FEATURES)
    rows.to_csv(RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv", index=False)
    draw_ridge_figure(
        rows,
        None,
        PLOTS_DIR / "figure7_individual_metadata_effect_robustness.png",
        PLOTS_DIR / "figure7_individual_metadata_effect_robustness.pdf",
    )


def write_figure8_outputs(
    collection_metrics_df: pd.DataFrame,
    benchmark_results: pd.DataFrame,
) -> pd.DataFrame:
    current_df = load_current_figure8_collection_df().drop(columns=["delta_correlation"])
    alt_df = current_df.merge(
        collection_metrics_df.loc[:, ["model", "variant_id", "delta_correlation"]],
        on=["model", "variant_id"],
        how="inner",
        validate="many_to_one",
    )

    nonlinear = benchmark_results.loc[
        (benchmark_results["dataset"] == "metadata_filter_collections")
        & (benchmark_results["target"] == "delta_correlation")
        & (benchmark_results["scope"] == "within_model")
        & (benchmark_results["scope_name"].isin(FIGURE6_MODEL_ORDER))
        & (benchmark_results["model_name"].isin(NONLINEAR_MODELS))
    ].copy()
    best_nonlinear = (
        nonlinear.sort_values(
            ["scope_name", "cv_r2", "cv_spearman"],
            ascending=[True, False, False],
        )
        .groupby("scope_name", as_index=False)
        .head(1)
        .reset_index(drop=True)
    )
    best_nonlinear.to_csv(RESULTS_DIR / "figure8_collection_best_nonlinear_model_by_model.csv", index=False)

    estimator_name = str(best_nonlinear.loc[best_nonlinear["scope_name"] == "GPT-4.1", "model_name"].iloc[0])
    df = alt_df.loc[alt_df["model"] == "GPT-4.1"].sort_values("variant_id").reset_index(drop=True)
    X = df[FIG8_FEATURE_KEYS].apply(pd.to_numeric, errors="coerce")
    y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
    groups = df["variant_id"].astype(str).to_numpy()

    perm_df = compute_permutation_importance(X, y, groups, estimator_name)
    shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)

    perm_df.to_csv(RESULTS_DIR / "figure8_collection_feature_importance_gpt41_permutation.csv", index=False)
    shap_points.to_csv(RESULTS_DIR / "figure8_collection_feature_importance_gpt41_shap_points.csv", index=False)
    shap_summary.to_csv(RESULTS_DIR / "figure8_collection_feature_importance_gpt41_shap_summary.csv", index=False)
    draw_feature_importance_figure(
        "GPT-4.1",
        estimator_name,
        perm_df,
        shap_points,
        PLOTS_DIR / "figure8_collection_feature_importance_gpt41.png",
        PLOTS_DIR / "figure8_collection_feature_importance_gpt41.pdf",
    )
    return best_nonlinear


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    truth = load_truth()
    baseline_repeat_scores, benchmark_repeat_scores = load_condition_repeat_scores()

    paper_metrics_df, paper_summary_df = build_paper_repeat_metrics(truth, baseline_repeat_scores)
    collection_metrics_df, collection_summary_df = build_collection_repeat_metrics(truth, baseline_repeat_scores)

    paper_metrics_df.to_csv(RESULTS_DIR / "paper_mean_repeat_correlation_metrics.csv", index=False)
    paper_summary_df.to_csv(RESULTS_DIR / "paper_mean_repeat_correlation_model_summary.csv", index=False)
    collection_metrics_df.to_csv(RESULTS_DIR / "collection_mean_repeat_correlation_metrics.csv", index=False)
    collection_summary_df.to_csv(RESULTS_DIR / "collection_mean_repeat_correlation_model_summary.csv", index=False)

    figure3_rows, figure3_summary = build_figure3_tables(paper_metrics_df, benchmark_repeat_scores)
    figure4_rows, figure4_summary = build_figure4_tables(collection_metrics_df, benchmark_repeat_scores)
    figure3_rows.to_csv(RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_rows.csv", index=False)
    figure3_summary.to_csv(RESULTS_DIR / "figure3_individual_paper_augmentation_cdf_baselines.csv", index=False)
    figure4_rows.to_csv(RESULTS_DIR / "figure4_collection_augmentation_density_rows.csv", index=False)
    figure4_summary.to_csv(RESULTS_DIR / "figure4_collection_augmentation_density_summary.csv", index=False)

    plot_density_figure(
        figure3_rows,
        figure3_summary,
        mean_label="Average augmented paper",
        out_stem="figure3_individual_paper_augmentation_density_correlation",
        item_label="papers",
    )
    plot_density_figure(
        figure4_rows,
        figure4_summary,
        mean_label="Average augmented collection",
        out_stem="figure4_collection_augmentation_density_correlation",
        item_label="collections",
    )

    write_figure5_outputs(paper_metrics_df, collection_metrics_df)

    alt_paper_bench, alt_collection_bench = build_alt_benchmark_datasets(paper_metrics_df, collection_metrics_df)
    alt_paper_bench.to_csv(RESULTS_DIR / "figure6_paper_metadata_benchmark_dataset.csv", index=False)
    alt_collection_bench.to_csv(RESULTS_DIR / "figure6_collection_metadata_benchmark_dataset.csv", index=False)

    benchmark_results, benchmark_best = build_alt_benchmark_tables(alt_paper_bench, alt_collection_bench)
    benchmark_results.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_benchmark.csv", index=False)
    benchmark_best.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_best.csv", index=False)
    write_figure6_outputs(benchmark_best)

    write_figure7_outputs(paper_metrics_df)
    write_figure8_outputs(collection_metrics_df, benchmark_results)


if __name__ == "__main__":
    main()
