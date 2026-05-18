from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_ensemble_gain"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_repeat5_ensemble_gain"
ENSEMBLE_ROWS_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_rows.csv"
SUMMARY_BY_METRIC_CSV = (
    RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_summary_by_metric.csv"
)

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
VARIANT_ORDER = [
    "baseline_no_augmentation",
    "benchmark_pgg_ms",
    "benchmark_pgg_ms_full",
    "broad_all_2011",
    "leaf_a0_b0_c0",
    "leaf_a0_b0_c1",
    "leaf_a0_b1_c0",
    "leaf_a0_b1_c1",
    "leaf_a1_b0_c0",
    "leaf_a1_b0_c1",
    "leaf_a1_b1_c0",
    "leaf_a1_b1_c1",
]
METRICS = ["correlation", "rmse", "r2"]
METRIC_LABELS = {
    "correlation": "Correlation gain from averaging 5 repeats",
    "rmse": "RMSE reduction from averaging 5 repeats",
    "r2": r"$R^2$ gain from averaging 5 repeats",
}


def variant_label(variant_id: str) -> str:
    if variant_id == "baseline_no_augmentation":
        return "Baseline"
    if variant_id == "benchmark_pgg_ms":
        return "Benchmark"
    if variant_id == "benchmark_pgg_ms_full":
        return "Benchmark\n(full)"
    if variant_id == "broad_all_2011":
        return "All papers"
    return variant_id.replace("leaf_", "").replace("_", "\n")


def plot_heatmaps(rows: pd.DataFrame, summary_by_metric: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(3, 1, figsize=(10.8, 12.6), layout="constrained")

    for ax, metric in zip(axes, METRICS):
        part = rows[["variant_id", "model", f"ensemble_gain_{metric}"]].copy()
        part = part.rename(columns={f"ensemble_gain_{metric}": "gain"})
        pivot = (
            part.pivot(index="variant_id", columns="model", values="gain")
            .reindex(index=VARIANT_ORDER, columns=MODEL_ORDER)
            .dropna(how="all")
        )
        vmax = float(pivot.max().max())
        vmin = min(0.0, float(pivot.min().min()))
        sns.heatmap(
            pivot,
            cmap="RdYlGn",
            center=0.0,
            vmin=vmin,
            vmax=vmax,
            annot=True,
            fmt=".3f",
            linewidths=0.6,
            linecolor="#e5e7eb",
            cbar=True,
            ax=ax,
        )
        ax.set_title(METRIC_LABELS[metric])
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_yticklabels([variant_label(idx) for idx in pivot.index], rotation=0)
        ax.tick_params(axis="x", rotation=20)

        stats = summary_by_metric.loc[summary_by_metric["metric"] == metric].iloc[0]
        ax.text(
            1.02,
            1.02,
            f"positive cells: {int(stats['n_positive'])}/{int(stats['n_cells'])}\nmean gain: {float(stats['mean_gain']):.3f}\nmedian gain: {float(stats['median_gain']):.3f}",
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=9,
            color="#374151",
        )

    fig.suptitle(
        "Averaging predictions across 5 repeats improves performance across repeat-5 conditions",
        fontsize=15,
        y=1.01,
    )
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_repeat5_ensemble_gain_heatmaps.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = pd.read_csv(ENSEMBLE_ROWS_CSV)
    summary_by_metric = pd.read_csv(SUMMARY_BY_METRIC_CSV)
    plot_heatmaps(rows, summary_by_metric)


if __name__ == "__main__":
    main()
