from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnnotationBbox, HPacker, TextArea, VPacker


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

BEST_CSV = RESULTS_DIR / "literature_metadata_supervised_model_best.csv"
ROWS_CSV = RESULTS_DIR / "figure6_metadata_predictability_correlation_selected_models_rows.csv"
OUT_PNG = PLOTS_DIR / "figure6_metadata_predictability_correlation_selected_models.png"
OUT_PDF = PLOTS_DIR / "figure6_metadata_predictability_correlation_selected_models.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
DATASET_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
DATASET_COLORS = {
    "individual_papers": "#73808f",
    "metadata_filter_collections": "#e59a3a",
}


def pretty_estimator(name: str) -> str:
    return str(name).replace("_", " ").title()


def build_rows() -> pd.DataFrame:
    best = pd.read_csv(BEST_CSV)
    rows = best.loc[(best["target"] == "correlation") & (best["scope"] == "within_model")].copy()
    rows = rows.loc[rows["scope_name"].isin(MODELS)].copy()
    rows["scope_order"] = rows["scope_name"].map({name: idx for idx, name in enumerate(MODELS)})
    rows["dataset_label"] = rows["dataset"].map(DATASET_LABELS)
    rows["estimator_label"] = rows["model_name"].map(pretty_estimator)
    rows["se_fold_r2"] = rows["sd_fold_r2"] / np.sqrt(5.0)
    rows["se_fold_spearman"] = rows["sd_fold_spearman"] / np.sqrt(5.0)
    return rows.sort_values(["scope_order", "dataset"]).reset_index(drop=True)


def draw_panel(ax: plt.Axes, rows: pd.DataFrame, metric: str, err: str, xlabel: str, *, show_ylabels: bool) -> None:
    row_y = np.arange(len(MODELS))[::-1].astype(float) * 1.35
    y_map = dict(zip(MODELS, row_y))
    offsets = {"individual_papers": 0.23, "metadata_filter_collections": -0.23}
    height = 0.36

    for dataset in ["individual_papers", "metadata_filter_collections"]:
        part = rows.loc[rows["dataset"] == dataset].copy()
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
    ax.tick_params(axis="y", labelleft=False)
    ax.tick_params(axis="y", length=0, pad=10)
    ax.grid(axis="x", color="#e6e6e6", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cfcfcf")
    ax.spines["bottom"].set_color("#cfcfcf")

    if show_ylabels:
        trans = ax.get_yaxis_transform()
        for model in MODELS:
            part = rows.loc[rows["scope_name"] == model].copy()
            ind = part.loc[part["dataset"] == "individual_papers", "estimator_label"].iloc[0]
            coll = part.loc[part["dataset"] == "metadata_filter_collections", "estimator_label"].iloc[0]
            label_box = VPacker(
                children=[
                    TextArea(
                        model,
                        textprops={"fontsize": 12.0, "color": "#222222", "ha": "right", "va": "center"},
                    ),
                    HPacker(
                        children=[
                            TextArea(
                                ind,
                                textprops={
                                    "fontsize": 10.4,
                                    "color": DATASET_COLORS["individual_papers"],
                                    "ha": "right",
                                    "va": "center",
                                },
                            ),
                            TextArea(
                                " | ",
                                textprops={"fontsize": 10.4, "color": "#555555", "ha": "center", "va": "center"},
                            ),
                            TextArea(
                                coll,
                                textprops={
                                    "fontsize": 10.4,
                                    "color": DATASET_COLORS["metadata_filter_collections"],
                                    "ha": "left",
                                    "va": "center",
                                },
                            ),
                        ],
                        align="center",
                        pad=0,
                        sep=0,
                    ),
                ],
                align="right",
                pad=0,
                sep=2,
            )
            ax.add_artist(
                AnnotationBbox(
                    label_box,
                    (-0.08, y_map[model]),
                    xycoords=trans,
                    frameon=False,
                    box_alignment=(1.0, 0.5),
                    pad=0.0,
                    annotation_clip=False,
                )
            )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    rows.to_csv(ROWS_CSV, index=False)

    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.4), sharey=True)
    draw_panel(axes[0], rows, "mean_fold_r2", "se_fold_r2", "Grouped-CV R^2", show_ylabels=True)
    draw_panel(axes[1], rows, "mean_fold_spearman", "se_fold_spearman", "Grouped-CV Spearman", show_ylabels=False)

    axes[0].set_xlim(-0.02, max(0.26, rows["mean_fold_r2"].max() + rows["se_fold_r2"].max() + 0.02))
    axes[1].set_xlim(-0.02, max(0.54, rows["mean_fold_spearman"].max() + rows["se_fold_spearman"].max() + 0.03))

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

    fig.subplots_adjust(top=0.78, left=0.43, right=0.985, bottom=0.18, wspace=0.18)
    fig.savefig(OUT_PNG, dpi=300)
    fig.savefig(OUT_PDF)
    plt.close(fig)


if __name__ == "__main__":
    main()
