from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch


RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_metadata_filters"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_metadata_filters"
ROWS_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_summary.csv"
CONVERGENCE_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_convergence_dataset.csv"
CONVERGENCE_SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_convergence_summary.csv"
BASELINE_MATRIX_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_baseline_pairwise_corr.csv"
ALL_PAPERS_MATRIX_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_all_papers_pairwise_corr.csv"
BASELINE_EFFECT_MATRIX_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_baseline_treatment_effect_pairwise_corr.csv"
ALL_PAPERS_EFFECT_MATRIX_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_all_papers_treatment_effect_pairwise_corr.csv"

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
METRICS = ["correlation", "r2", "rmse"]
METRIC_LABELS = {
    "correlation": "Raw correlation",
    "r2": r"Raw $R^2$ vs learning-wave mean",
    "rmse": "Raw RMSE",
}
LOWER_IS_BETTER = {"rmse"}
ALL_PAPERS_VARIANT_ID = "broad_all_2011"
BENCHMARK_VARIANT_ID = "benchmark_pgg_ms"


def _model_list(rows: pd.DataFrame) -> list[str]:
    return [model for model in MODEL_ORDER if model in set(rows["model"].astype(str))]


def plot_performance(rows: pd.DataFrame, summary: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    available_models = _model_list(rows)
    metadata_rows = rows.loc[rows["variant_group"] == "metadata_filter"].copy()
    all_papers = rows.loc[rows["variant_id"] == ALL_PAPERS_VARIANT_ID].copy()
    benchmark = rows.loc[rows["variant_id"] == BENCHMARK_VARIANT_ID].copy()

    fig, axes = plt.subplots(1, 3, figsize=(16.0, 5.4))
    for ax, metric in zip(axes, METRICS):
        sns.boxplot(
            data=metadata_rows,
            x="model",
            y=metric,
            hue="model",
            order=available_models,
            palette=MODEL_COLORS,
            width=0.58,
            showfliers=False,
            dodge=False,
            legend=False,
            ax=ax,
        )

        for idx, model in enumerate(available_models):
            summary_row = summary.loc[summary["model"] == model].iloc[0]
            baseline_value = float(summary_row[f"baseline_{metric}"])
            ax.scatter(
                idx,
                baseline_value,
                marker="_",
                s=320,
                color="black",
                linewidths=2.4,
                zorder=5,
            )

            all_papers_part = all_papers.loc[all_papers["model"] == model]
            if not all_papers_part.empty:
                ax.scatter(
                    idx,
                    float(all_papers_part[metric].iloc[0]),
                    marker="^",
                    s=58,
                    color="#7a3db8",
                    edgecolor="black",
                    linewidth=0.6,
                    zorder=6,
                )

            benchmark_part = benchmark.loc[benchmark["model"] == model]
            if not benchmark_part.empty:
                ax.scatter(
                    idx,
                    float(benchmark_part[metric].iloc[0]),
                    marker="D",
                    s=58,
                    color="#f28e2b",
                    edgecolor="black",
                    linewidth=0.6,
                    zorder=6,
                )

            model_meta = metadata_rows.loc[metadata_rows["model"] == model].copy()
            if not model_meta.empty:
                ascending = metric in LOWER_IS_BETTER
                best_row = model_meta.sort_values(metric, ascending=ascending).iloc[0]
                ax.scatter(
                    idx,
                    float(best_row[metric]),
                    marker="*",
                    s=120,
                    color="#2ca25f",
                    edgecolor="black",
                    linewidth=0.6,
                    zorder=7,
                )
                share_improved = float(summary_row[f"metadata_share_improved_{metric}"])
                n_sig_improve = int(summary_row[f"metadata_n_sig_improved_{metric}"])
                n_sig_worsen = int(summary_row[f"metadata_n_sig_worsened_{metric}"])
                direction_label = "below" if metric in LOWER_IS_BETTER else "above"
                ax.text(
                    idx,
                    0.02,
                    f"{share_improved:.0%} {direction_label}\nsig +{n_sig_improve} / -{n_sig_worsen}",
                    transform=ax.get_xaxis_transform(),
                    ha="center",
                    va="bottom",
                    fontsize=8.2,
                    color="#4b5563",
                )

        ax.set_xlabel("")
        ax.set_ylabel(METRIC_LABELS[metric])
        ax.set_title(METRIC_LABELS[metric])
        ax.tick_params(axis="x", rotation=20)

    handles = [
        Line2D([], [], color="#9ca3af", linewidth=8, alpha=0.8, label="Metadata-filter distribution"),
        Line2D([], [], color="black", marker="_", linestyle="None", markersize=16, label="No-augmentation baseline"),
        Line2D([], [], color="#f28e2b", marker="D", markeredgecolor="black", linestyle="None", markersize=7, label="Benchmark paper"),
        Line2D([], [], color="#7a3db8", marker="^", markeredgecolor="black", linestyle="None", markersize=7, label="All papers"),
        Line2D([], [], color="#2ca25f", marker="*", markeredgecolor="black", linestyle="None", markersize=10, label="Best metadata filter"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 0.02))
    fig.suptitle(
        "Metadata-filter collection augmentations vs each model's no-augmentation baseline",
        fontsize=15,
        y=0.99,
    )
    fig.text(
        0.5,
        0.08,
        "Boxes show the metadata-filter sweep only. Text under each model gives the share of metadata filters that beat baseline plus the number with paired-bootstrap 95% CI significant improvement/worsening. Orange diamonds mark the benchmark paper report, purple triangles mark the all-papers collection report, and stars mark the best metadata-filter variant per model.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )
    fig.tight_layout(rect=[0.02, 0.12, 1, 0.93])
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_metadata_filters_performance.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def _scatter_limits(values: np.ndarray, extra_values: list[float]) -> tuple[float, float]:
    finite = values[np.isfinite(values)]
    lo = float(np.nanquantile(finite, 0.01))
    hi = float(np.nanquantile(finite, 0.99))
    for val in extra_values:
        if np.isfinite(val):
            lo = min(lo, float(val))
            hi = max(hi, float(val))
    pad = 0.08 * (hi - lo + 1e-9)
    return lo - pad, hi + pad


def plot_convergence(
    convergence_df: pd.DataFrame,
    convergence_summary: pd.DataFrame,
    baseline_matrix: pd.DataFrame,
    all_papers_matrix: pd.DataFrame,
    *,
    metric_space: str,
) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    metadata_conv = convergence_df.loc[convergence_df["variant_group"] == "metadata_filter"].copy()
    all_papers = convergence_df.loc[convergence_df["variant_id"] == ALL_PAPERS_VARIANT_ID].iloc[0]
    benchmark = convergence_df.loc[convergence_df["variant_id"] == BENCHMARK_VARIANT_ID].iloc[0]
    if metric_space == "effect":
        delta_col = "delta_mean_pairwise_corr_effect_vs_baseline"
        truth_col = "delta_mean_corr_to_truth_effect_vs_baseline"
        best_accuracy_col = "best_metadata_accuracy_effect_variant_id"
        rho_col = "spearman_metadata_delta_corr_effect_vs_delta_truth_corr_effect"
        pearson_col = "pearson_metadata_delta_corr_effect_vs_delta_truth_corr_effect"
        axis_suffix = "predicted treatment effect"
        truth_suffix = "predicted treatment effect"
        panel_title = "Metadata-filter collection reports usually make the available models agree more on the predicted treatment effect"
        hist_title = "Most metadata filters increase cross-model agreement on treatment effect"
        scatter_title = "More treatment-effect convergence is moderately associated with better effect accuracy"
        output_name = "validation_literature_collection_analysis_report_metadata_filters_treatment_effect_convergence.png"
        base_heatmap_title = "Baseline pairwise correlations\n(predicted treatment effect)"
        all_heatmap_title = "All-papers pairwise correlations\n(predicted treatment effect)"
    else:
        delta_col = "delta_mean_pairwise_corr_raw_vs_baseline"
        truth_col = "delta_mean_corr_to_truth_raw_vs_baseline"
        best_accuracy_col = "best_metadata_accuracy_variant_id"
        rho_col = "spearman_metadata_delta_corr_raw_vs_delta_truth_corr_raw"
        pearson_col = "pearson_metadata_delta_corr_raw_vs_delta_truth_corr_raw"
        axis_suffix = "predicted outcome"
        truth_suffix = "predicted outcome"
        panel_title = "Metadata-filter collection reports usually make the available models agree more on the predicted outcome"
        hist_title = "Most metadata filters increase cross-model agreement"
        scatter_title = "More convergence is moderately associated with better accuracy"
        output_name = "validation_literature_collection_analysis_report_metadata_filters_convergence.png"
        base_heatmap_title = "Baseline pairwise correlations\n(predicted outcome)"
        all_heatmap_title = "All-papers pairwise correlations\n(predicted outcome)"

    best_accuracy_id = str(convergence_summary[best_accuracy_col].iloc[0])
    best_accuracy = metadata_conv.loc[metadata_conv["variant_id"] == best_accuracy_id].iloc[0]

    delta_vals = metadata_conv[delta_col].to_numpy(dtype=float)
    truth_vals = metadata_conv[truth_col].to_numpy(dtype=float)
    all_papers_delta = float(all_papers[delta_col])
    all_papers_truth = float(all_papers[truth_col])
    benchmark_delta = float(benchmark[delta_col])
    benchmark_truth = float(benchmark[truth_col])
    best_accuracy_delta = float(best_accuracy[delta_col])
    best_accuracy_truth = float(best_accuracy[truth_col])

    fig, axes = plt.subplots(2, 2, figsize=(13.2, 10.2))
    ax_hist, ax_scatter, ax_base, ax_all = axes.flat

    ax_hist.hist(delta_vals, bins=34, color="#9ca3af", edgecolor="white", linewidth=0.5)
    ax_hist.axvline(0.0, color="black", linewidth=1.3, label="No change vs baseline")
    ax_hist.axvline(float(np.mean(delta_vals)), color="#2b8cbe", linewidth=1.4, label="Mean metadata filter")
    ax_hist.axvline(float(np.median(delta_vals)), color="#6b7280", linestyle=":", linewidth=1.4, label="Median metadata filter")
    ax_hist.axvline(benchmark_delta, color="#f28e2b", linestyle="-.", linewidth=1.6, label="Benchmark paper")
    ax_hist.axvline(all_papers_delta, color="#7a3db8", linestyle="-.", linewidth=1.6, label="All papers")
    ax_hist.axvline(best_accuracy_delta, color="#2ca25f", linestyle="--", linewidth=1.5, label="Best metadata accuracy")
    ax_hist.set_xlabel(f"Change in mean pairwise model correlation\non {axis_suffix}")
    ax_hist.set_ylabel("Number of metadata-filter variants")
    ax_hist.set_title(hist_title)
    ax_hist.text(
        0.98,
        0.98,
        (
            f"Variants with Δ > 0: {float((delta_vals > 0).mean()):.1%}\n"
            f"Mean Δ: {float(np.mean(delta_vals)):+.3f}\n"
            f"Median Δ: {float(np.median(delta_vals)):+.3f}"
        ),
        transform=ax_hist.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d1d5db", "boxstyle": "round,pad=0.3"},
    )
    ax_hist.legend(loc="upper left", frameon=False)

    ax_scatter.scatter(delta_vals, truth_vals, s=16, color="#9ca3af", alpha=0.3, linewidth=0)
    ax_scatter.scatter(
        benchmark_delta,
        benchmark_truth,
        marker="D",
        s=72,
        color="#f28e2b",
        edgecolor="black",
        linewidth=0.6,
        zorder=4,
    )
    ax_scatter.scatter(
        all_papers_delta,
        all_papers_truth,
        marker="^",
        s=72,
        color="#7a3db8",
        edgecolor="black",
        linewidth=0.6,
        zorder=4,
    )
    ax_scatter.scatter(
        best_accuracy_delta,
        best_accuracy_truth,
        marker="*",
        s=140,
        color="#2ca25f",
        edgecolor="black",
        linewidth=0.6,
        zorder=5,
    )
    ax_scatter.annotate("Benchmark", xy=(benchmark_delta, benchmark_truth), xytext=(7, 6), textcoords="offset points", fontsize=9)
    ax_scatter.annotate("All papers", xy=(all_papers_delta, all_papers_truth), xytext=(7, 6), textcoords="offset points", fontsize=9)
    ax_scatter.annotate("Best metadata", xy=(best_accuracy_delta, best_accuracy_truth), xytext=(7, -12), textcoords="offset points", fontsize=9)
    ax_scatter.axvline(0.0, color="black", linestyle="--", linewidth=1.1)
    ax_scatter.axhline(0.0, color="black", linestyle=":", linewidth=1.0)
    ax_scatter.set_xlim(*_scatter_limits(delta_vals, [0.0, benchmark_delta, all_papers_delta, best_accuracy_delta]))
    ax_scatter.set_ylim(*_scatter_limits(truth_vals, [benchmark_truth, all_papers_truth, best_accuracy_truth]))
    ax_scatter.set_xlabel(f"Change in mean pairwise model correlation\non {axis_suffix}")
    ax_scatter.set_ylabel(f"Change in mean model correlation to truth\non {truth_suffix}")
    ax_scatter.set_title(scatter_title)
    ax_scatter.text(
        0.02,
        0.98,
        (
            f"Spearman ρ = {float(convergence_summary[rho_col].iloc[0]):.2f}\n"
            f"Pearson r = {float(convergence_summary[pearson_col].iloc[0]):.2f}"
        ),
        transform=ax_scatter.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d1d5db", "boxstyle": "round,pad=0.3"},
    )

    combined_heatmap_vals = np.concatenate(
        [baseline_matrix.to_numpy(dtype=float).ravel(), all_papers_matrix.to_numpy(dtype=float).ravel()]
    )
    combined_heatmap_vals = combined_heatmap_vals[np.isfinite(combined_heatmap_vals)]
    heatmap_vmin = max(0.0, float(combined_heatmap_vals.min()) - 0.03)
    heatmap_kwargs = dict(
        vmin=heatmap_vmin,
        vmax=1.0,
        cmap="magma",
        annot=True,
        fmt=".2f",
        square=True,
        cbar=False,
    )
    sns.heatmap(baseline_matrix, ax=ax_base, **heatmap_kwargs)
    ax_base.set_title(base_heatmap_title)
    ax_base.tick_params(axis="x", rotation=35)
    ax_base.tick_params(axis="y", rotation=0)

    sns.heatmap(all_papers_matrix, ax=ax_all, **heatmap_kwargs)
    ax_all.set_title(all_heatmap_title)
    ax_all.tick_params(axis="x", rotation=35)
    ax_all.tick_params(axis="y", rotation=0)

    fig.suptitle(panel_title, fontsize=15, y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    base_pos = ax_base.get_position()
    all_pos = ax_all.get_position()
    y_arrow = max(base_pos.y1, all_pos.y1) + 0.01
    x_start = base_pos.x1 + 0.015
    x_end = all_pos.x0 - 0.015
    arrow = FancyArrowPatch(
        (x_start, y_arrow),
        (x_end, y_arrow),
        transform=fig.transFigure,
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.5,
        color="#4b5563",
    )
    fig.add_artist(arrow)
    fig.text(
        (x_start + x_end) / 2,
        y_arrow + 0.012,
        "augment with all-papers report",
        ha="center",
        va="bottom",
        fontsize=10,
        color="#374151",
    )

    fig.savefig(
        PLOTS_DIR / output_name,
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = pd.read_csv(ROWS_CSV)
    summary = pd.read_csv(SUMMARY_CSV)
    convergence_df = pd.read_csv(CONVERGENCE_CSV)
    convergence_summary = pd.read_csv(CONVERGENCE_SUMMARY_CSV)
    baseline_matrix = pd.read_csv(BASELINE_MATRIX_CSV, index_col=0)
    all_papers_matrix = pd.read_csv(ALL_PAPERS_MATRIX_CSV, index_col=0)
    baseline_effect_matrix = pd.read_csv(BASELINE_EFFECT_MATRIX_CSV, index_col=0)
    all_papers_effect_matrix = pd.read_csv(ALL_PAPERS_EFFECT_MATRIX_CSV, index_col=0)

    plot_performance(rows, summary)
    plot_convergence(
        convergence_df,
        convergence_summary,
        baseline_matrix,
        all_papers_matrix,
        metric_space="raw",
    )
    plot_convergence(
        convergence_df,
        convergence_summary,
        baseline_effect_matrix,
        all_papers_effect_matrix,
        metric_space="effect",
    )


if __name__ == "__main__":
    main()
