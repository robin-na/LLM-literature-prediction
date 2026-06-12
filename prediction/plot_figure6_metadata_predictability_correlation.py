from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
BEST_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_metadata_supervised_benchmarks"
    / "literature_metadata_supervised_model_best.csv"
)
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"

FIGURE_CSV = RESULTS_DIR / "figure6_metadata_predictability_correlation_rows.csv"
FIGURE_PNG = PLOTS_DIR / "figure6_metadata_predictability_correlation.png"
FIGURE_PDF = PLOTS_DIR / "figure6_metadata_predictability_correlation.pdf"

KEEP_MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
ROW_ORDER = KEEP_MODELS
DATASET_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
DATASET_COLORS = {
    "individual_papers": "#73808f",
    "metadata_filter_collections": "#e59a3a",
}

def load_rows() -> pd.DataFrame:
    best = pd.read_csv(BEST_CSV)
    best = best.loc[(best["target"] == "correlation") & (best["scope"] == "within_model")].copy()
    best = best.loc[best["scope_name"].isin(KEEP_MODELS)].copy()
    rows = best.copy()
    rows["dataset_label"] = rows["dataset"].map(DATASET_LABELS)
    rows["scope_order"] = rows["scope_name"].map({name: idx for idx, name in enumerate(ROW_ORDER)})
    rows = rows.sort_values(["scope_order", "dataset_label"]).reset_index(drop=True)

    # Fold-based descriptive uncertainty.
    rows["se_fold_r2"] = rows["sd_fold_r2"] / np.sqrt(5)
    rows["se_fold_spearman"] = rows["sd_fold_spearman"] / np.sqrt(5)
    return rows


def draw_panel(ax: plt.Axes, df: pd.DataFrame, metric: str, err: str, xlabel: str, show_ylabels: bool) -> None:
    row_y = np.arange(len(ROW_ORDER))[::-1].astype(float)
    y_map = dict(zip(ROW_ORDER, row_y))
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
            color=DATASET_COLORS[dataset],
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
        ax.set_yticklabels(ROW_ORDER)
    else:
        ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cfcfcf")
    ax.spines["bottom"].set_color("#cfcfcf")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = load_rows()
    rows.to_csv(FIGURE_CSV, index=False)

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.35), sharey=True)
    draw_panel(axes[0], rows, "mean_fold_r2", "se_fold_r2", "Grouped-CV $R^2$", show_ylabels=True)
    draw_panel(
        axes[1],
        rows,
        "mean_fold_spearman",
        "se_fold_spearman",
        "Grouped-CV Spearman",
        show_ylabels=False,
    )

    axes[0].set_xlim(-0.02, max(0.24, rows["mean_fold_r2"].max() + rows["se_fold_r2"].max() + 0.02))
    axes[1].set_xlim(
        -0.03,
        max(0.52, rows["mean_fold_spearman"].max() + rows["se_fold_spearman"].max() + 0.03),
    )

    handles = [
        Line2D([0], [0], color=DATASET_COLORS[key], lw=10, solid_capstyle="round", label=label)
        for key, label in DATASET_LABELS.items()
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
    fig.savefig(FIGURE_PNG, dpi=300)
    fig.savefig(FIGURE_PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
