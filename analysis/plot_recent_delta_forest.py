#!/usr/bin/env python3
"""Create a 3-panel forest plot of metric deltas vs baseline.

The plot focuses on recent positive-cases and experiment-data runs, while
excluding pgg_CONFIGmerged_validation because it behaves like lookup.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


@dataclass
class MetricSpec:
    key: str
    delta_col: str
    ci_low_col: str
    ci_high_col: str
    title: str
    better_direction: str  # "lower" or "higher"


@dataclass
class Row:
    source_label: str
    variation: str
    n: str
    values: dict[str, float]

    @property
    def y_label(self) -> str:
        return f"{self.source_label}: {self.variation} (n={self.n})"


METRICS = [
    MetricSpec(
        key="rmse",
        delta_col="delta_rmse",
        ci_low_col="delta_rmse_ci_low",
        ci_high_col="delta_rmse_ci_high",
        title="Delta RMSE (left is better)",
        better_direction="lower",
    ),
    MetricSpec(
        key="correlation",
        delta_col="delta_correlation",
        ci_low_col="delta_correlation_ci_low",
        ci_high_col="delta_correlation_ci_high",
        title="Delta Correlation (right is better)",
        better_direction="higher",
    ),
    MetricSpec(
        key="directional_accuracy",
        delta_col="delta_directional_accuracy",
        ci_low_col="delta_directional_accuracy_ci_low",
        ci_high_col="delta_directional_accuracy_ci_high",
        title="Delta Directional Accuracy (right is better)",
        better_direction="higher",
    ),
]


SOURCE_FILES = [
    ("PC-M41", "prediction_positive_cases_merged_41_metrics_delta.csv"),
    ("PC-R41", "prediction_positive_cases_reasoning_merged_41_metrics_delta.csv"),
    ("PC-R-GPT51", "prediction_positive_cases_reasoning_merged_gpt51_metrics_delta.csv"),
    ("PC-OP46", "prediction_positive_cases_anthropic_merged_opus46_metrics_delta.csv"),
    (
        "PC-R-OP46",
        "prediction_positive_cases_reasoning_anthropic_merged_opus46_metrics_delta.csv",
    ),
    ("EXP-M41", "prediction_experiment_data_merged_41_metrics_delta.csv"),
    ("EXP-R41", "prediction_experiment_data_reasoning_merged_41_metrics_delta.csv"),
]

EXCLUDED_VARIATIONS = {"pgg_CONFIGmerged_validation"}
EXCLUDED_N = {1, 7}

COLORS = {
    "better": "#1a9850",
    "uncertain": "#4d4d4d",
    "worse": "#d73027",
    "missing": "#999999",
}


def parse_float(value: str | None) -> float:
    if value is None:
        return math.nan
    value = value.strip()
    if not value:
        return math.nan
    try:
        return float(value)
    except ValueError:
        return math.nan


def ci_verdict(metric: MetricSpec, ci_low: float, ci_high: float) -> str:
    if math.isnan(ci_low) or math.isnan(ci_high):
        return "missing"
    if metric.better_direction == "lower":
        if ci_high < 0:
            return "better"
        if ci_low > 0:
            return "worse"
        return "uncertain"
    if ci_low > 0:
        return "better"
    if ci_high < 0:
        return "worse"
    return "uncertain"


def load_rows(results_dir: Path) -> list[Row]:
    rows: list[Row] = []
    for source_label, filename in SOURCE_FILES:
        file_path = results_dir / filename
        with file_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                if raw.get("variation") in EXCLUDED_VARIATIONS:
                    continue
                n_raw = raw.get("n", "")
                try:
                    n_int = int(float(n_raw))
                except (TypeError, ValueError):
                    n_int = None
                if n_int in EXCLUDED_N:
                    continue
                values: dict[str, float] = {}
                for metric in METRICS:
                    values[metric.delta_col] = parse_float(raw.get(metric.delta_col))
                    values[metric.ci_low_col] = parse_float(raw.get(metric.ci_low_col))
                    values[metric.ci_high_col] = parse_float(raw.get(metric.ci_high_col))
                rows.append(
                    Row(
                        source_label=source_label,
                        variation=raw.get("variation", "unknown"),
                        n=raw.get("n", ""),
                        values=values,
                    )
                )
    return rows


def draw_plot(rows: list[Row], output_path: Path) -> None:
    if not rows:
        raise RuntimeError("No rows available after filtering.")

    y_positions = list(range(len(rows)))
    labels = [row.y_label for row in rows]
    fig_height = max(6.0, 0.42 * len(rows) + 1.6)
    fig, axes = plt.subplots(1, 3, figsize=(16, fig_height), sharey=True)
    fig.subplots_adjust(left=0.42, right=0.98, top=0.88, bottom=0.14, wspace=0.14)

    for idx, metric in enumerate(METRICS):
        ax = axes[idx]
        ax.axvline(0, color="#7a7a7a", linestyle="--", linewidth=1.0, zorder=1)
        for y, row in zip(y_positions, rows):
            x = row.values[metric.delta_col]
            lo = row.values[metric.ci_low_col]
            hi = row.values[metric.ci_high_col]
            if math.isnan(x):
                continue

            verdict = ci_verdict(metric, lo, hi)
            color = COLORS[verdict]

            if math.isnan(lo) or math.isnan(hi):
                ax.plot(x, y, marker="x", markersize=6, color=color, zorder=4)
            else:
                xerr = [[x - lo], [hi - x]]
                ax.errorbar(
                    x,
                    y,
                    xerr=xerr,
                    fmt="o",
                    color=color,
                    ecolor=color,
                    elinewidth=1.2,
                    capsize=2.8,
                    markersize=5,
                    zorder=3,
                )

        ax.set_title(metric.title, fontsize=11)
        ax.grid(axis="x", color="#e8e8e8", linestyle="-", linewidth=0.8)
        ax.set_axisbelow(True)
        ax.set_ylim(-1, len(rows))
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
        loc="lower center",
        bbox_to_anchor=(0.5, 0.03),
        frameon=False,
        ncol=2,
        fontsize=9,
    )
    fig.suptitle(
        "Recent Non-Validation Runs: Deltas vs Baseline (95% CIs)",
        fontsize=13,
        fontweight="bold",
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"
    plots_dir = repo_root / "plots"

    rows = load_rows(results_dir)
    png_path = plots_dir / "recent_nonvalidation_delta_forest.png"
    pdf_path = plots_dir / "recent_nonvalidation_delta_forest.pdf"

    draw_plot(rows, png_path)
    draw_plot(rows, pdf_path)

    print(f"Saved: {png_path}")
    print(f"Saved: {pdf_path}")
    print(f"Rows plotted (after filtering): {len(rows)}")


if __name__ == "__main__":
    main()
