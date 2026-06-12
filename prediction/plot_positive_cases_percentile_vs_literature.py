#!/usr/bin/env python3
"""Plot positive-case percentile vs 1398 literature retrieved cases."""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from plot_paths import POSITIVE_CASE_PLOTS, ensure_plot_dir


@dataclass
class MetricSpec:
    delta_col: str
    title: str
    better_direction: str  # "lower" or "higher"


@dataclass
class RunRow:
    source_label: str
    variation: str
    n: int
    values: dict[str, float]

    @property
    def y_label(self) -> str:
        return f"{self.source_label}: {self.variation} (n={self.n})"


METRICS = [
    MetricSpec("delta_rmse", "RMSE Percentile\n(higher percentile is better)", "lower"),
    MetricSpec(
        "delta_correlation",
        "Correlation Percentile\n(higher percentile is better)",
        "higher",
    ),
    MetricSpec(
        "delta_directional_accuracy",
        "Directional Accuracy Percentile\n(higher percentile is better)",
        "higher",
    ),
]

POSITIVE_CASE_FILES = [
    ("PC-M41", "prediction_positive_cases_merged_41_metrics_delta.csv"),
    ("PC-R41", "prediction_positive_cases_reasoning_merged_41_metrics_delta.csv"),
    ("PC-R-GPT51", "prediction_positive_cases_reasoning_merged_gpt51_metrics_delta.csv"),
    ("PC-OP46", "prediction_positive_cases_anthropic_merged_opus46_metrics_delta.csv"),
    (
        "PC-R-OP46",
        "prediction_positive_cases_reasoning_anthropic_merged_opus46_metrics_delta.csv",
    ),
]

REFERENCE_FILE = "prediction_251105_individual_report_41_metrics_delta.csv"
EXCLUDED_N = {1, 7}

SOURCE_COLORS = {
    "PC-M41": "#1f77b4",
    "PC-R41": "#ff7f0e",
    "PC-R-GPT51": "#2ca02c",
    "PC-OP46": "#9467bd",
    "PC-R-OP46": "#8c564b",
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


def load_reference_rows(results_dir: Path) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    with (results_dir / REFERENCE_FILE).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            row = {metric.delta_col: parse_float(raw.get(metric.delta_col)) for metric in METRICS}
            rows.append(row)
    return rows


def load_positive_rows(results_dir: Path) -> list[RunRow]:
    rows: list[RunRow] = []
    for source_label, filename in POSITIVE_CASE_FILES:
        with (results_dir / filename).open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                try:
                    n = int(float(raw.get("n", "")))
                except (TypeError, ValueError):
                    continue
                if n in EXCLUDED_N:
                    continue
                values = {metric.delta_col: parse_float(raw.get(metric.delta_col)) for metric in METRICS}
                rows.append(
                    RunRow(
                        source_label=source_label,
                        variation=raw.get("variation", "unknown"),
                        n=n,
                        values=values,
                    )
                )
    return rows


def percentile_vs_reference(value: float, reference_values: list[float], better_direction: str) -> float:
    valid = [x for x in reference_values if not math.isnan(x)]
    if math.isnan(value) or not valid:
        return math.nan
    n = len(valid)
    if better_direction == "lower":
        # Lower delta is better for RMSE.
        return 100.0 * sum(x >= value for x in valid) / n
    # Higher delta is better for correlation and directional accuracy.
    return 100.0 * sum(x <= value for x in valid) / n


def draw_percentile_plot(
    positive_rows: list[RunRow], reference_rows: list[dict[str, float]], output_path: Path
) -> None:
    if not positive_rows:
        raise RuntimeError("No positive-case rows available after filtering.")
    if not reference_rows:
        raise RuntimeError("No reference rows found.")

    y_positions = list(range(len(positive_rows)))
    labels = [row.y_label for row in positive_rows]
    fig_height = max(5.8, 0.42 * len(positive_rows) + 1.5)
    fig, axes = plt.subplots(1, 3, figsize=(15.2, fig_height), sharey=True)
    fig.subplots_adjust(left=0.41, right=0.98, top=0.86, bottom=0.16, wspace=0.16)

    for idx, metric in enumerate(METRICS):
        ax = axes[idx]
        reference_values = [row[metric.delta_col] for row in reference_rows]
        baseline_pct = percentile_vs_reference(0.0, reference_values, metric.better_direction)
        ax.axvline(
            baseline_pct,
            color="#111111",
            linestyle="--",
            linewidth=1.2,
            zorder=1,
        )

        for y, row in zip(y_positions, positive_rows):
            value = row.values[metric.delta_col]
            pct = percentile_vs_reference(value, reference_values, metric.better_direction)
            if math.isnan(pct):
                continue
            color = SOURCE_COLORS.get(row.source_label, "#4d4d4d")
            ax.scatter(pct, y, color=color, s=42, zorder=3, edgecolors="white", linewidths=0.5)

        ax.set_xlim(0, 100)
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.set_xlabel("Percentile", fontsize=10)
        ax.set_title(metric.title, fontsize=11)
        ax.grid(axis="x", color="#e8e8e8", linestyle="-", linewidth=0.8)
        ax.set_axisbelow(True)
        ax.set_ylim(-1, len(positive_rows))
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
            color="#111111",
            linestyle="--",
            linewidth=1.2,
            label="Baseline GPT-4.1 (Δ=0) percentile",
        )
    ]
    legend_handles.extend(
        [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markerfacecolor=color,
            markeredgecolor="white",
            markeredgewidth=0.5,
            label=label,
            markersize=7,
        )
        for label, color in SOURCE_COLORS.items()
        ]
    )
    fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.03),
        frameon=False,
        ncol=3,
        fontsize=9,
    )
    fig.suptitle(
        "Positive Cases vs Literature Retrieved Cases (Reference: 1398 individual report rows)",
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

    reference_rows = load_reference_rows(results_dir)
    positive_rows = load_positive_rows(results_dir)

    out_png = plots_dir / "positive_cases_percentile_vs_literature_1398.png"
    out_pdf = plots_dir / "positive_cases_percentile_vs_literature_1398.pdf"

    draw_percentile_plot(positive_rows, reference_rows, out_png)
    draw_percentile_plot(positive_rows, reference_rows, out_pdf)

    print(f"Saved: {out_png}")
    print(f"Saved: {out_pdf}")
    print(f"Reference rows: {len(reference_rows)}")
    print(f"Positive-case rows plotted: {len(positive_rows)}")


if __name__ == "__main__":
    main()
