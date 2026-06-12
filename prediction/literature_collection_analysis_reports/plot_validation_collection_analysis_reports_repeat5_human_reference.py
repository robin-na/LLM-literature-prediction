from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_human_reference"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_repeat5_human_reference"
ROWS_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_comparison_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_comparison_summary.csv"
FULL_CROWD_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_full_crowd_summary.csv"

CATEGORY_ORDER = [
    "Humans: laypeople vs laypeople",
    "Humans: experts vs laypeople",
    "Humans: experts vs experts",
    "Human subcrowds (5): laypeople vs laypeople",
    "Human subcrowds (5): experts vs laypeople",
    "Human subcrowds (5): experts vs experts",
    "LLM baseline: different model",
    "LLM baseline: same model, different repeat",
    "LLM benchmark: different model",
    "LLM benchmark: same model, different repeat",
]
PALETTE = {
    "Humans: laypeople vs laypeople": "#9c6644",
    "Humans: experts vs laypeople": "#b08968",
    "Humans: experts vs experts": "#7f5539",
    "Human subcrowds (5): laypeople vs laypeople": "#6c757d",
    "Human subcrowds (5): experts vs laypeople": "#495057",
    "Human subcrowds (5): experts vs experts": "#343a40",
    "LLM baseline: different model": "#94a3b8",
    "LLM baseline: same model, different repeat": "#64748b",
    "LLM benchmark: different model": "#f59e0b",
    "LLM benchmark: same model, different repeat": "#d97706",
}


def plot_comparison(rows: pd.DataFrame, summary: pd.DataFrame, full_crowd: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.6, 7.4), layout="constrained")

    sns.boxplot(
        data=rows,
        x="value",
        y="category",
        hue="category",
        order=CATEGORY_ORDER,
        orient="h",
        palette=PALETTE,
        showfliers=False,
        dodge=False,
        width=0.62,
        ax=ax,
    )
    if ax.legend_ is not None:
        ax.legend_.remove()

    summary = summary.set_index("category").reindex(CATEGORY_ORDER).reset_index()
    for _, row in summary.iterrows():
        ax.plot(
            [row["q10"], row["q90"]],
            [row["category"], row["category"]],
            color="#111827",
            linewidth=1.4,
            alpha=0.7,
            solid_capstyle="round",
            zorder=3,
        )
        ax.scatter(
            row["mean"],
            row["category"],
            marker="D",
            s=34,
            color="white",
            edgecolor="#111827",
            linewidth=0.9,
            zorder=4,
        )
        ax.text(
            min(row["mean"] + 0.012, 0.995),
            row["category"],
            f"{row['mean']:.3f}",
            va="center",
            ha="left",
            fontsize=8.5,
            color="#111827",
        )

    full_crowd_value = float(full_crowd["value"].iloc[0])
    ax.axvline(full_crowd_value, color="#047857", linewidth=1.6, linestyle="--", alpha=0.9)
    ax.text(
        full_crowd_value,
        -0.7,
        f"Full expert-crowd vs lay-crowd corr = {full_crowd_value:.3f}",
        ha="left",
        va="bottom",
        fontsize=9,
        color="#065f46",
    )

    ax.set_xlim(-0.15, 1.02)
    ax.set_xlabel("Pairwise correlation across the 20 validation questions")
    ax.set_ylabel("")
    ax.set_title("LLM repeat stability and cross-model convergence against human prediction baselines")

    fig.text(
        0.5,
        0.01,
        "Boxes show pairwise-correlation distributions; black diamonds mark means and horizontal segments mark the 10th-90th percentile range.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )

    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_reference_comparison.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = pd.read_csv(ROWS_CSV)
    summary = pd.read_csv(SUMMARY_CSV)
    full_crowd = pd.read_csv(FULL_CROWD_CSV)
    plot_comparison(rows, summary, full_crowd)


if __name__ == "__main__":
    main()
