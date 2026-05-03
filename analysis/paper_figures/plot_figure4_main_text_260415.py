from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

PARAMETER_ROWS_CSV = RESULTS_DIR / "figure4_design_parameter_mention_variation_rows.csv"
COUNT_DISTRIBUTION_CSV = RESULTS_DIR / "figure4_design_parameter_count_distribution_rows.csv"
HEATMAP_PERCENT_CSV = RESULTS_DIR / "figure4_group_size_rounds_heatmap_percent.csv"
HEATMAP_COUNTS_CSV = RESULTS_DIR / "figure4_group_size_rounds_heatmap_counts.csv"
DOC_MD = RESULTS_DIR / "figure4_empirical_design_limitations_documentation.md"
LEGACY_DOC_MD = RESULTS_DIR / "figure4_empirical_config_limitations_documentation.md"

OUT_STEM = "figure4_empirical_design_limitations"
LEGACY_OUT_STEM = "figure4_empirical_config_limitations"

REPORTED_COLOR = "#4c78a8"
VARIED_COLOR = "#f58518"
GRID_COLOR = "#e8ebef"
TEXT_COLOR = "#30343b"


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 8.5,
            "ytick.labelsize": 9,
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.dpi": 300,
        }
    )


def panel_title(ax: plt.Axes, letter: str, title: str) -> None:
    ax.set_title(rf"$\bf{{{letter}}}$  {title}", loc="left", pad=8)


def annotate_sample_size(
    ax: plt.Axes,
    text: str,
    x: float = 0.995,
    y: float = 0.98,
    va: str = "top",
) -> None:
    ax.text(
        x,
        y,
        text,
        transform=ax.transAxes,
        ha="right",
        va=va,
        fontsize=8.2,
        color="#555555",
    )


def draw_panel_a(ax: plt.Axes, parameter_rows: pd.DataFrame, n_papers: int) -> None:
    y = np.arange(len(parameter_rows))
    bar_h = 0.34
    ax.barh(
        y - bar_h / 2,
        parameter_rows["percent_papers_mentioned"],
        height=bar_h,
        color=REPORTED_COLOR,
        alpha=0.86,
        label="Reported",
    )
    ax.barh(
        y + bar_h / 2,
        parameter_rows["percent_papers_varied"],
        height=bar_h,
        color=VARIED_COLOR,
        alpha=0.92,
        label="Varied",
    )

    ax.set_yticks(y)
    ax.set_yticklabels(parameter_rows["label"])
    ax.invert_yaxis()
    ax.set_xlim(0, 105)
    ax.set_xlabel("% of papers")
    panel_title(ax, "A", "Uneven reporting and variation across design parameters")
    annotate_sample_size(ax, f"n={n_papers} papers")
    ax.grid(axis="x", color=GRID_COLOR, linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", frameon=False, fontsize=8.5)


def draw_panel_b(ax: plt.Axes, count_rows: pd.DataFrame, n_papers: int) -> None:
    count_rows = count_rows.copy()
    count_rows["percent_papers_reported"] = count_rows["n_papers_mentioned"] / n_papers * 100.0
    count_rows["percent_papers_varied"] = count_rows["n_papers_varied"] / n_papers * 100.0

    x = count_rows["n_design_parameters"].to_numpy(dtype=float)
    width = 0.38
    ax.bar(
        x - width / 2,
        count_rows["percent_papers_reported"],
        width=width,
        color=REPORTED_COLOR,
        alpha=0.82,
        label="Reported",
    )
    ax.bar(
        x + width / 2,
        count_rows["percent_papers_varied"],
        width=width,
        color=VARIED_COLOR,
        alpha=0.92,
        label="Varied",
    )

    ax.set_xlim(-0.75, int(x.max()) + 0.75)
    ax.set_ylim(0, max(70, float(count_rows[["percent_papers_reported", "percent_papers_varied"]].max().max()) * 1.12))
    ax.set_xticks(x)
    ax.set_xlabel("Number of design parameters")
    ax.set_ylabel("% of papers")
    panel_title(ax, "B", "Limited reporting and variation of design parameters")
    annotate_sample_size(ax, f"n={n_papers} papers", y=0.68)
    ax.grid(axis="y", color=GRID_COLOR, linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", frameon=False, fontsize=8.5)


def draw_panel_c(ax: plt.Axes, heat_percent: pd.DataFrame, heat_counts: pd.DataFrame) -> None:
    values = heat_percent.to_numpy(dtype=float)
    counts = heat_counts.to_numpy(dtype=float)
    n_experiments = int(np.nansum(counts))

    vmax = float(np.nanmax(values))
    im = ax.imshow(values, cmap="Blues", origin="lower", vmin=0.0, vmax=vmax, aspect="auto")
    ax.set_xticks(range(len(heat_percent.columns)))
    ax.set_xticklabels(list(heat_percent.columns))
    ax.set_yticks(range(len(heat_percent.index)))
    ax.set_yticklabels(list(heat_percent.index))
    ax.set_xlabel("Group size")
    ax.set_ylabel("Number of rounds")
    panel_title(ax, "C", "Confounded variations across design parameters")
    annotate_sample_size(ax, f"n={n_experiments} experiments", x=0.985, y=0.965)

    for row_i in range(values.shape[0]):
        for col_i in range(values.shape[1]):
            val = float(values[row_i, col_i])
            if val <= 0:
                continue
            color = "white" if val >= 0.45 * vmax else "#1f2933"
            ax.text(
                col_i,
                row_i,
                f"{val:.1f}",
                ha="center",
                va="center",
                fontsize=7.2,
                color=color,
            )

    cbar = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.018)
    cbar.set_label("% of experiments", fontsize=9)
    cbar.ax.tick_params(labelsize=8)


def draw_figure() -> None:
    set_style()
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    parameter_rows = pd.read_csv(PARAMETER_ROWS_CSV)
    count_rows = pd.read_csv(COUNT_DISTRIBUTION_CSV)
    heat_percent = pd.read_csv(HEATMAP_PERCENT_CSV, index_col=0)
    heat_counts = pd.read_csv(HEATMAP_COUNTS_CSV, index_col=0)

    n_papers = int(parameter_rows["n_papers_total"].iloc[0])

    fig = plt.figure(figsize=(11.4, 6.35))
    gs = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.15, 1.05],
        height_ratios=[0.82, 1.18],
        left=0.17,
        right=0.97,
        bottom=0.10,
        top=0.91,
        wspace=0.19,
        hspace=0.38,
    )
    ax_a = fig.add_subplot(gs[:, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, 1])

    draw_panel_a(ax_a, parameter_rows, n_papers)
    draw_panel_b(ax_b, count_rows, n_papers)
    draw_panel_c(ax_c, heat_percent, heat_counts)

    for stem in [OUT_STEM, LEGACY_OUT_STEM]:
        fig.savefig(PLOTS_DIR / f"{stem}.png", bbox_inches="tight")
        fig.savefig(PLOTS_DIR / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)

    doc_text = "\n".join(
        [
            "# Figure 4: Empirical Design Limitations",
            "",
            "Input: `batch_processing/output_csv/simple_batch_197papers.xlsx`, sheet `extractions`.",
            "",
            f"Rows included: `METHOD_lab == True` grouped by `custom_id` ({n_papers} papers).",
            "",
            "Design parameter definition: 14 design parameters. Punishment-ID and reward-ID visibility are merged into one ID-visibility parameter. Punishment-existence and endowment variables are excluded.",
            "",
            "Panel A: Percent of lab papers where each design parameter is reported at least once, and percent where it varies within paper.",
            "",
            "Panel B: Paper-level distribution. Reported means every lab-condition row in that paper reports the parameter. Varied means the parameter takes more than one value across lab-condition rows in that paper.",
            "",
            "Panel C: Percent of experiments by group-size and number-of-rounds bins. The heatmap uses 705 rows with numeric group size >= 2 and number of rounds >= 1.",
            "",
        ]
    )
    DOC_MD.write_text(doc_text)
    LEGACY_DOC_MD.write_text(doc_text)


if __name__ == "__main__":
    draw_figure()
