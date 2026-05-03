from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df
from paper_figures.plot_collection_one_filter_barplot_260413 import (
    FAMILY_COLORS,
    FAMILY_LABELS,
    MODELS,
    VARIANT_FAMILY,
    VARIANT_LABELS,
    VARIANT_ORDER,
    compute_all_collections_rows,
    load_baseline30,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"

ROWS_CSV = RESULTS_DIR / "exploratory_collection_filter_value_average_barplot_selected4_rows.csv"
FIG_PNG = PLOTS_DIR / "exploratory_collection_filter_value_average_barplot_selected4.png"
FIG_PDF = PLOTS_DIR / "exploratory_collection_filter_value_average_barplot_selected4.pdf"

FILTER_SPECS = {
    "type_empirical": ("type_value", "empirical"),
    "type_theoretical": ("type_value", "theoretical"),
    "citation_q1_lowest": ("citation_value", "Q1_lowest"),
    "citation_q2": ("citation_value", "Q2"),
    "citation_q3": ("citation_value", "Q3"),
    "citation_q4_highest": ("citation_value", "Q4_highest"),
    "jcr_q1": ("jcr_value", "Q1"),
    "jcr_q2": ("jcr_value", "Q2"),
    "jcr_q3": ("jcr_value", "Q3"),
    "jcr_q4": ("jcr_value", "Q4"),
    "year_q1_oldest": ("year_value", "Q1_oldest"),
    "year_q2": ("year_value", "Q2"),
    "year_q3": ("year_value", "Q3"),
    "year_q4_newest": ("year_value", "Q4_newest"),
    "discipline_bio_evo": ("discipline_value", "bio_evo"),
    "discipline_economics": ("discipline_value", "economics"),
    "discipline_math_phys_cs": ("discipline_value", "math_phys_cs"),
    "discipline_multidisciplinary": ("discipline_value", "multidisciplinary"),
    "discipline_other": ("discipline_value", "other"),
    "discipline_psych_social": ("discipline_value", "psych_social"),
}


def build_average_rows() -> pd.DataFrame:
    feature_df = build_collection_df()
    feature_df = feature_df.loc[
        feature_df["model"] == "GPT-4.1",
        ["variant_id", "count", "n_filters", "type_value", "citation_value", "jcr_value", "year_value", "discipline_value"],
    ].drop_duplicates("variant_id")
    metrics_df = pd.read_csv(COLLECTION_METRICS_CSV)
    df = metrics_df.merge(feature_df, on="variant_id", how="left", validate="many_to_one")
    df = df.loc[df["model"].isin(MODELS)].copy()
    baseline_df = load_baseline30()
    all_rows = compute_all_collections_rows()

    rows: list[dict[str, object]] = []
    for model in MODELS:
        model_df = df.loc[df["model"] == model].copy()
        for variant_id in VARIANT_ORDER[1:]:
            column, value = FILTER_SPECS[variant_id]
            part = model_df.loc[model_df[column] == value].copy()
            if part.empty:
                continue
            rows.append(
                {
                    "model": model,
                    "variant_id": variant_id,
                    "variant_label": VARIANT_LABELS[variant_id],
                    "family": VARIANT_FAMILY[variant_id],
                    "n_matching_variants": int(len(part)),
                    "mean_correlation": float(part["correlation"].mean()),
                    "median_correlation": float(part["correlation"].median()),
                    "sd_correlation": float(part["correlation"].std(ddof=1)) if len(part) > 1 else 0.0,
                    "mean_count": float(pd.to_numeric(part["count"], errors="coerce").mean()),
                }
            )

    avg_rows = pd.DataFrame(rows)
    all_rows = all_rows.rename(
        columns={
            "correlation": "mean_correlation",
            "count": "mean_count",
            "n_aug_runs": "n_matching_variants",
        }
    )
    all_rows["median_correlation"] = all_rows["mean_correlation"]
    all_rows["sd_correlation"] = 0.0
    all_rows = all_rows.loc[
        :, ["model", "variant_id", "variant_label", "family", "n_matching_variants", "mean_correlation", "median_correlation", "sd_correlation", "mean_count"]
    ]

    plot_rows = pd.concat([all_rows, avg_rows], ignore_index=True, sort=False)
    plot_rows["variant_order"] = plot_rows["variant_id"].map({name: idx for idx, name in enumerate(VARIANT_ORDER)})
    plot_rows = plot_rows.sort_values(["model", "variant_order"]).reset_index(drop=True)
    plot_rows = plot_rows.merge(baseline_df, on="model", how="left", validate="many_to_one")
    plot_rows["delta_vs_baseline_mean30"] = plot_rows["mean_correlation"] - plot_rows["baseline_correlation_mean30"]
    return plot_rows


def draw_plot(rows: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(15.8, 8.8), sharex=True, sharey=True)
    axes = axes.ravel()

    x = np.arange(len(VARIANT_ORDER))
    y_min = min(rows["mean_correlation"].min(), rows["baseline_correlation_mean30"].min()) - 0.05
    y_max = max(rows["mean_correlation"].max(), rows["baseline_correlation_mean30"].max()) + 0.05

    family_breaks = []
    prev_family = None
    for idx, variant_id in enumerate(VARIANT_ORDER):
        family = VARIANT_FAMILY[variant_id]
        if prev_family is not None and family != prev_family:
            family_breaks.append(idx - 0.5)
        prev_family = family

    for ax, model in zip(axes, MODELS):
        part = rows.loc[rows["model"] == model].set_index("variant_id").reindex(VARIANT_ORDER).reset_index()
        colors = [FAMILY_COLORS[VARIANT_FAMILY[v]] for v in part["variant_id"]]
        vals = part["mean_correlation"].to_numpy(dtype=float)
        errs = part["sd_correlation"].to_numpy(dtype=float)
        ax.bar(x, vals, color=colors, width=0.82, edgecolor="none", zorder=2)
        ax.errorbar(
            x,
            vals,
            yerr=errs,
            fmt="none",
            ecolor="#555555",
            elinewidth=0.9,
            alpha=0.5,
            capsize=2.0,
            zorder=3,
        )
        baseline_value = float(part["baseline_correlation_mean30"].dropna().iloc[0])
        ax.axhline(baseline_value, color="#222222", lw=1.3, ls=(0, (5, 3)), zorder=3)
        ax.set_title(model, fontsize=13, pad=9)
        ax.grid(axis="y", color="#e6e6e6", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cfcfcf")
        ax.spines["bottom"].set_color("#cfcfcf")
        ax.set_ylim(y_min, y_max)
        for boundary in family_breaks:
            ax.axvline(boundary, color="#efefef", lw=1.0, zorder=1)
        ax.text(
            0.985,
            0.94,
            f"Unaugmented = {baseline_value:.3f}",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=9.6,
            color="#333333",
            bbox={"facecolor": "white", "alpha": 0.82, "edgecolor": "none", "pad": 2.0},
        )

    labels = [VARIANT_LABELS[v] for v in VARIANT_ORDER]
    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=55, ha="right")

    axes[0].set_ylabel("Mean correlation performance")
    axes[2].set_ylabel("Mean correlation performance")

    handles = [Patch(facecolor=FAMILY_COLORS[key], edgecolor="none", label=label) for key, label in FAMILY_LABELS.items()]
    handles.append(Line2D([0], [0], color="#222222", lw=1.3, ls=(0, (5, 3)), label="Unaugmented baseline"))
    handles.append(Line2D([0], [0], color="#555555", lw=1.0, label="SD across matching reports"))
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=4,
        frameon=False,
        bbox_to_anchor=(0.5, 0.99),
        columnspacing=1.2,
        handlelength=1.8,
    )
    fig.suptitle("Average collection augmentation performance by filter value", fontsize=15, y=0.995)
    fig.text(
        0.5,
        0.955,
        "Each bar averages over all matching collection reports that include the indicated filter value",
        ha="center",
        va="center",
        fontsize=10.0,
        color="#555555",
    )
    fig.subplots_adjust(top=0.88, left=0.08, right=0.99, bottom=0.23, wspace=0.12, hspace=0.25)
    fig.savefig(FIG_PNG, dpi=300)
    fig.savefig(FIG_PDF)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = build_average_rows()
    rows.to_csv(ROWS_CSV, index=False)
    draw_plot(rows)


if __name__ == "__main__":
    main()
