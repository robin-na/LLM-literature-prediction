from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, MaxNLocator


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

INDIVIDUAL_ROWS_CSV = RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv"
COLLECTION_ROWS_CSV = RESULTS_DIR / "figure8_collection_metadata_effect_robustness_rows.csv"
COMBINED_ROWS_CSV = RESULTS_DIR / "figure7_8_metadata_effect_side_by_side_rows.csv"
OUT_PNG = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected_models.png"
OUT_PDF = PLOTS_DIR / "figure7_8_metadata_effect_side_by_side_selected_models.pdf"

MODELS = ["GPT-4.1", "GPT-5.1", "Claude Sonnet 4.6"]
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-5.1": "#d95f02",
    "Claude Sonnet 4.6": "#9c755f",
}


def ordered_features_from_individual(df: pd.DataFrame) -> list[str]:
    ordered = (
        df.groupby("feature_label", as_index=False)
        .agg(mean_coef=("coef", "mean"))
        .sort_values("mean_coef", ascending=False)
    )
    features = ordered["feature_label"].tolist()
    if "Number of Papers" in features:
        features = [f for f in features if f != "Number of Papers"]
    return features + ["Number of Papers"]


def draw_panel(
    ax: plt.Axes,
    df: pd.DataFrame,
    features: list[str],
    title: str,
    *,
    show_ylabels: bool,
) -> None:
    base_y = np.arange(len(features))[::-1].astype(float)
    y_map = dict(zip(features, base_y))
    offsets = np.linspace(-0.22, 0.22, len(MODELS))

    xabs = float(np.nanmax(np.abs(df[["coef", "ci_low", "ci_high"]].to_numpy(dtype=float))))
    xlim = max(0.01, xabs * 1.18)

    ax.axvline(0.0, color="#777777", lw=1.0, ls=(0, (4, 3)), zorder=1)
    for offset, model in zip(offsets, MODELS):
        part = df.loc[df["model"] == model].copy()
        ys = [y_map[label] + offset for label in part["feature_label"]]
        ax.errorbar(
            part["coef"],
            ys,
            xerr=[part["coef"] - part["ci_low"], part["ci_high"] - part["coef"]],
            fmt="o",
            ms=5.2,
            lw=0,
            elinewidth=1.15,
            capsize=2.5,
            color=MODEL_COLORS[model],
            ecolor=MODEL_COLORS[model],
            alpha=0.96,
            zorder=3,
        )

    ax.set_title(title, fontsize=13, pad=8)
    ax.set_yticks(base_y)
    if show_ylabels:
        ax.set_yticklabels(features)
    else:
        ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfcf")
    ax.set_xlim(-xlim, xlim)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.tick_params(axis="x", labelsize=9.5, rotation=0, pad=2)
    ax.set_xlabel("")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    individual = pd.read_csv(INDIVIDUAL_ROWS_CSV)
    collection = pd.read_csv(COLLECTION_ROWS_CSV)

    individual = individual.loc[individual["model"].isin(MODELS)].copy()
    collection = collection.loc[collection["model"].isin(MODELS)].copy()

    features = ordered_features_from_individual(individual)
    individual["panel"] = "Individual papers"
    collection["panel"] = "Collections"
    pd.concat([individual, collection], ignore_index=True).to_csv(COMBINED_ROWS_CSV, index=False)

    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.8), sharey=True)
    draw_panel(axes[0], individual, features, "Individual Papers", show_ylabels=True)
    draw_panel(axes[1], collection, features, "Collections", show_ylabels=False)

    handles = [
        Line2D([0], [0], marker="o", linestyle="none", markersize=6, color=MODEL_COLORS[model], label=model)
        for model in MODELS
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.985),
        columnspacing=1.4,
        handletextpad=0.4,
    )
    fig.supxlabel("Coefficient on correlation gain", fontsize=11, y=0.06)
    fig.subplots_adjust(left=0.35, right=0.985, top=0.84, bottom=0.16, wspace=0.20)
    fig.savefig(OUT_PNG, dpi=300)
    fig.savefig(OUT_PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
