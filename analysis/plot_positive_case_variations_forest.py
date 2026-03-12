#!/usr/bin/env python3
"""Create a forest plot for positive-case variation deltas vs baseline."""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


SUMMARY_FILE = "prediction_positive_case_variations_ranked_summary.csv"
OUTPUT_PNG = "positive_case_variations_delta_forest.png"
OUTPUT_PDF = "positive_case_variations_delta_forest.pdf"


@dataclass
class MetricSpec:
    delta_col: str
    ci_low_col: str
    ci_high_col: str
    verdict_col: str
    title: str


METRICS = [
    MetricSpec(
        delta_col="delta_rmse",
        ci_low_col="delta_rmse_ci_low",
        ci_high_col="delta_rmse_ci_high",
        verdict_col="rmse_ci_verdict",
        title="Delta RMSE (left is better)",
    ),
    MetricSpec(
        delta_col="delta_correlation",
        ci_low_col="delta_correlation_ci_low",
        ci_high_col="delta_correlation_ci_high",
        verdict_col="correlation_ci_verdict",
        title="Delta Correlation (right is better)",
    ),
    MetricSpec(
        delta_col="delta_directional_accuracy",
        ci_low_col="delta_directional_accuracy_ci_low",
        ci_high_col="delta_directional_accuracy_ci_high",
        verdict_col="directional_accuracy_ci_verdict",
        title="Delta Directional Accuracy (right is better)",
    ),
]


MODE_LABELS = {
    "single": "single",
    "reasoning": "reasoning",
    "joint": "joint",
    "joint_reasoning": "joint+reasoning",
}

COLORS = {
    "better": "#1a9850",
    "uncertain": "#4d4d4d",
    "worse": "#d73027",
    "missing": "#999999",
}


def draw_plot(summary_df: pd.DataFrame, output_path: Path) -> None:
    if summary_df.empty:
        raise RuntimeError("No rows available for plotting.")

    labels = [
        f"{row.family} [{MODE_LABELS.get(row.mode, row.mode)}]"
        for row in summary_df.itertuples(index=False)
    ]
    y_positions = list(range(len(summary_df)))

    fig_height = max(9.0, 0.28 * len(summary_df) + 1.8)
    fig, axes = plt.subplots(1, 3, figsize=(16, fig_height), sharey=True)
    fig.subplots_adjust(left=0.38, right=0.98, top=0.92, bottom=0.08, wspace=0.14)

    for idx, metric in enumerate(METRICS):
        ax = axes[idx]
        ax.axvline(0, color="#7a7a7a", linestyle="--", linewidth=1.0, zorder=1)

        for y, row in zip(y_positions, summary_df.itertuples(index=False)):
            x = getattr(row, metric.delta_col)
            lo = getattr(row, metric.ci_low_col)
            hi = getattr(row, metric.ci_high_col)
            verdict = getattr(row, metric.verdict_col)
            color = COLORS.get(verdict, COLORS["missing"])

            if math.isnan(x):
                continue
            if math.isnan(lo) or math.isnan(hi):
                ax.plot(x, y, marker="x", markersize=5, color=color, zorder=3)
                continue

            ax.errorbar(
                x,
                y,
                xerr=[[x - lo], [hi - x]],
                fmt="o",
                color=color,
                ecolor=color,
                elinewidth=1.0,
                capsize=2.5,
                markersize=4.5,
                zorder=3,
            )

        ax.set_title(metric.title, fontsize=11)
        ax.grid(axis="x", color="#e8e8e8", linestyle="-", linewidth=0.8)
        ax.set_axisbelow(True)
        ax.set_ylim(-1, len(summary_df))
        ax.invert_yaxis()

        if idx == 0:
            ax.set_yticks(y_positions)
            ax.set_yticklabels(labels, fontsize=8)
        else:
            ax.tick_params(axis="y", which="both", left=False, labelleft=False)

    legend_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markerfacecolor=COLORS["better"],
            markeredgecolor=COLORS["better"],
            label="Better vs baseline (CI excludes 0)",
            markersize=6,
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markerfacecolor=COLORS["uncertain"],
            markeredgecolor=COLORS["uncertain"],
            label="Uncertain (CI crosses 0)",
            markersize=6,
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markerfacecolor=COLORS["worse"],
            markeredgecolor=COLORS["worse"],
            label="Worse vs baseline (CI excludes 0)",
            markersize=6,
        ),
        Line2D(
            [0],
            [0],
            marker="x",
            linestyle="",
            color=COLORS["missing"],
            label="Missing CI",
            markersize=6,
        ),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.03),
        frameon=False,
        ncol=2,
        fontsize=9,
    )
    fig.suptitle(
        "Positive-Case Variants: Deltas vs GPT-4.1 Baseline (95% CIs)",
        fontsize=13,
        fontweight="bold",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    summary_path = repo_root / "results" / SUMMARY_FILE
    plots_dir = repo_root / "plots"

    summary_df = pd.read_csv(summary_path)
    summary_df = summary_df.sort_values(
        by=[
            "overall_rank_mean",
            "delta_rmse",
            "delta_correlation",
            "delta_directional_accuracy",
        ],
        ascending=[True, True, False, False],
    )

    out_png = plots_dir / OUTPUT_PNG
    out_pdf = plots_dir / OUTPUT_PDF
    draw_plot(summary_df, out_png)
    draw_plot(summary_df, out_pdf)

    print(f"Saved: {out_png}")
    print(f"Saved: {out_pdf}")
    print(f"Rows plotted: {len(summary_df)}")


if __name__ == "__main__":
    main()
