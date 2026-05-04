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
import seaborn as sns
from scipy import stats
from matplotlib.lines import Line2D
from matplotlib.transforms import blended_transform_factory

from paper_figures.plot_figure2_main_text_260415 import (
    BASELINE30_CSV,
    COLLECTION_METRICS_CSV,
    FIG_PNG as OLD_FIG_PNG,
    MODELS,
    MODEL_COLORS,
    NO_AUG_BENCHMARKS_CSV,
    PAPER_METRICS_CSV,
    compute_everything_collection_rows,
    load_noise_ceiling,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

FIG_PNG = PLOTS_DIR / "figure2_heterogeneity_and_cross_model_agreement.png"
ROWS_CSV = RESULTS_DIR / "figure2_heterogeneity_and_cross_model_agreement_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "figure2_heterogeneity_and_cross_model_agreement_summary.csv"
PAIRWISE_CSV = RESULTS_DIR / "figure2_heterogeneity_and_cross_model_agreement_pairwise.csv"
DOC_MD = RESULTS_DIR / "figure2_heterogeneity_and_cross_model_agreement_documentation.md"

KIND_ORDER = ["individual_papers", "metadata_filter_collections"]
KIND_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
ITEM_ID_COLS = {
    "individual_papers": "source_id",
    "metadata_filter_collections": "variant_id",
}
MODEL_DISPLAY = {
    "Claude Sonnet 4.6": "Claude Sonnet 4.6",
    "GPT-4.1": "GPT-4.1",
    "Gemini 2.5 Pro": "Gemini Pro 2.5",
}
HEATMAP_X_LABELS = {
    "Claude Sonnet 4.6": "Claude\nSonnet 4.6",
    "GPT-4.1": "GPT-4.1",
    "Gemini Pro 2.5": "Gemini\nPro 2.5",
}


def load_baseline30() -> dict[str, float]:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODELS), ["model", "correlation_mean_prediction"]].copy()
    return {str(row["model"]): float(row["correlation_mean_prediction"]) for _, row in df.iterrows()}


def build_rows() -> pd.DataFrame:
    paper = pd.read_csv(PAPER_METRICS_CSV)
    paper = paper.loc[paper["model"].isin(MODELS), ["model", "source_id", "correlation"]].copy()
    paper = paper.rename(columns={"source_id": "item_id"})
    paper["kind"] = "individual_papers"

    collections = pd.read_csv(COLLECTION_METRICS_CSV)
    collections = collections.loc[collections["model"].isin(MODELS), ["model", "variant_id", "correlation"]].copy()
    collections = collections.rename(columns={"variant_id": "item_id"})
    collections["kind"] = "metadata_filter_collections"
    everything = compute_everything_collection_rows().loc[:, ["model", "item_id", "correlation"]].copy()
    everything = everything.loc[everything["model"].isin(MODELS)].copy()
    everything["kind"] = "metadata_filter_collections"
    collections = pd.concat([collections, everything], ignore_index=True, sort=False)

    rows = pd.concat([paper, collections], ignore_index=True, sort=False)
    rows["kind_label"] = rows["kind"].map(KIND_LABELS)
    rows["model_short"] = rows["model"].map(MODEL_DISPLAY)
    return rows


def build_summary(rows: pd.DataFrame) -> pd.DataFrame:
    baseline = load_baseline30()
    out_rows: list[dict[str, object]] = []
    for kind in KIND_ORDER:
        for model in MODELS:
            part = rows.loc[(rows["kind"] == kind) & (rows["model"] == model)].copy()
            baseline_value = baseline[model]
            out_rows.append(
                {
                    "kind": kind,
                    "kind_label": KIND_LABELS[kind],
                    "model": model,
                    "model_short": MODEL_DISPLAY[model],
                    "n_items": int(part.shape[0]),
                    "mean_correlation": float(part["correlation"].mean()),
                    "sd_correlation": float(part["correlation"].std(ddof=1)),
                    "min_correlation": float(part["correlation"].min()),
                    "max_correlation": float(part["correlation"].max()),
                    "baseline_correlation_mean30": float(baseline_value),
                    "n_above_baseline": int((part["correlation"] > baseline_value).sum()),
                    "share_above_baseline": float((part["correlation"] > baseline_value).mean()),
                }
            )
    return pd.DataFrame(out_rows)


def build_pairwise(rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for kind in KIND_ORDER:
        wide = rows.loc[rows["kind"] == kind].pivot(index="item_id", columns="model", values="correlation")
        wide = wide.reindex(columns=MODELS).dropna()
        for i, model_a in enumerate(MODELS):
            for model_b in MODELS[i + 1 :]:
                a = wide[model_a].to_numpy(dtype=float)
                b = wide[model_b].to_numpy(dtype=float)
                try:
                    pearson = stats.pearsonr(a, b, alternative="greater")
                    pearson_r = float(pearson.statistic)
                    pearson_p_greater = float(pearson.pvalue)
                except TypeError:
                    pearson_r, pearson_p_two_sided = stats.pearsonr(a, b)
                    pearson_r = float(pearson_r)
                    pearson_p_greater = float(pearson_p_two_sided / 2.0 if pearson_r >= 0 else 1.0 - pearson_p_two_sided / 2.0)
                out_rows.append(
                    {
                        "kind": kind,
                        "kind_label": KIND_LABELS[kind],
                        "model_a": model_a,
                        "model_b": model_b,
                        "model_a_short": MODEL_DISPLAY[model_a],
                        "model_b_short": MODEL_DISPLAY[model_b],
                        "n_shared_items": int(wide.shape[0]),
                        "pearson_r": pearson_r,
                        "pearson_p_greater_than_zero_parametric": pearson_p_greater,
                    }
                )
    return pd.DataFrame(out_rows)


def matrix_from_pairwise(pairwise: pd.DataFrame, kind: str, value_col: str) -> pd.DataFrame:
    labels = [MODEL_DISPLAY[model] for model in MODELS]
    matrix = pd.DataFrame(np.eye(len(MODELS)), index=labels, columns=labels)
    sub = pairwise.loc[pairwise["kind"] == kind]
    for row in sub.itertuples(index=False):
        value = float(getattr(row, value_col))
        matrix.loc[row.model_a_short, row.model_b_short] = value
        matrix.loc[row.model_b_short, row.model_a_short] = value
    return matrix


def draw_boxplot(
    ax: plt.Axes,
    rows: pd.DataFrame,
    summary: pd.DataFrame,
    kind: str,
    noise_ceiling: float,
    *,
    label_noise: bool = False,
) -> None:
    values = [
        rows.loc[(rows["kind"] == kind) & (rows["model"] == model), "correlation"].dropna().to_numpy(dtype=float)
        for model in MODELS
    ]
    positions = np.arange(1, len(MODELS) + 1)
    box = ax.boxplot(
        values,
        vert=False,
        positions=positions,
        widths=0.54,
        patch_artist=True,
        showfliers=True,
        whis=(5, 95),
        medianprops={"color": "#111827", "linewidth": 1.25},
        whiskerprops={"color": "#6b7280", "linewidth": 0.9},
        capprops={"color": "#6b7280", "linewidth": 0.9},
        flierprops={
            "marker": "o",
            "markersize": 1.7,
            "markerfacecolor": "#6b7280",
            "markeredgecolor": "none",
            "alpha": 0.18,
        },
    )

    for patch, model in zip(box["boxes"], MODELS):
        patch.set_facecolor(MODEL_COLORS[model])
        patch.set_edgecolor(MODEL_COLORS[model])
        patch.set_alpha(0.32)
        patch.set_linewidth(1.2)

    for idx, model in enumerate(MODELS, start=1):
        baseline_value = float(
            summary.loc[(summary["kind"] == kind) & (summary["model"] == model), "baseline_correlation_mean30"].iloc[0]
        )
        ax.scatter(
            baseline_value,
            idx,
            marker="D",
            s=42,
            facecolor="white",
            edgecolor="#111827",
            linewidth=1.1,
            zorder=6,
        )
        ax.text(
            baseline_value + 0.019,
            idx,
            f"{baseline_value:.2f}",
            ha="left",
            va="center",
            fontsize=8.1,
            color="#111827",
            zorder=7,
            bbox={"boxstyle": "round,pad=0.10", "facecolor": "white", "edgecolor": "none", "alpha": 0.74},
        )

    ax.axvline(noise_ceiling, color="#111827", linewidth=1.2, linestyle=":", zorder=0)
    if label_noise:
        trans = blended_transform_factory(ax.transData, ax.transAxes)
        ax.text(
            noise_ceiling + 0.012,
            0.97,
            "Noise ceiling",
            transform=trans,
            ha="left",
            va="top",
            rotation=90,
            fontsize=8.8,
            color="#111827",
            bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.82},
        )

    ax.set_xlim(0.0, 0.88)
    ax.set_ylim(0.45, len(MODELS) + 0.55)
    ax.set_xticks(np.arange(0.0, 0.81, 0.2))
    ax.set_xticks(np.arange(0.0, 0.86, 0.1), minor=True)
    ax.set_yticks(positions)
    ax.set_yticklabels([MODEL_DISPLAY[model] for model in MODELS], fontsize=9.4)
    ax.invert_yaxis()
    ax.grid(axis="x", which="minor", color="#e5e7eb", linewidth=0.8)
    ax.grid(axis="x", which="major", color="#d1d5db", linewidth=0.9)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_heatmap(
    ax: plt.Axes,
    matrix: pd.DataFrame,
    title: str,
    *,
    cbar: bool = False,
    show_xlabels: bool = True,
) -> None:
    mask = np.triu(np.ones_like(matrix, dtype=bool), k=1)
    sns.heatmap(
        matrix,
        ax=ax,
        mask=mask,
        cmap="YlGnBu",
        vmin=0.0,
        vmax=1.0,
        annot=True,
        fmt=".2f",
        cbar=cbar,
        square=True,
        linewidths=0.8,
        linecolor="white",
        annot_kws={"fontsize": 9.5},
    )
    ax.set_title(title, fontsize=11.2, pad=7)
    ax.set_xlabel("")
    ax.set_ylabel("")
    if show_xlabels:
        ax.set_xticklabels(
            [HEATMAP_X_LABELS.get(label.get_text(), label.get_text()) for label in ax.get_xticklabels()],
            rotation=0,
            ha="center",
        )
        ax.tick_params(axis="x", labelsize=8.7, pad=4)
    else:
        ax.tick_params(axis="x", labelbottom=False, bottom=False)
    ax.tick_params(axis="y", rotation=0, labelsize=8.7)


def draw_figure(rows: pd.DataFrame, summary: pd.DataFrame, pairwise: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    noise_ceiling = load_noise_ceiling()

    fig = plt.figure(figsize=(11.4, 6.7))
    gs = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.35, 1.0],
        height_ratios=[1.0, 1.0],
        wspace=0.33,
        hspace=0.55,
    )

    box_axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])]
    pearson_axes = [fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])]

    for row_idx, (ax, kind) in enumerate(zip(box_axes, KIND_ORDER)):
        draw_boxplot(ax, rows, summary, kind, noise_ceiling, label_noise=row_idx == 0)
        ax.set_title(KIND_LABELS[kind], fontsize=12.0, pad=8)
        ax.text(
            0.02,
            0.94,
            f"n = {int(rows.loc[rows['kind'].eq(kind), 'item_id'].nunique()):,}",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=8.7,
            color="#374151",
            bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.86},
        )

    no_aug_handle = Line2D(
        [0],
        [0],
        marker="D",
        color="#111827",
        markerfacecolor="white",
        lw=0,
        markersize=5.4,
        label="No augmentation",
    )
    box_axes[0].tick_params(axis="x", labelbottom=False)
    box_axes[1].set_xlabel(r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$", fontsize=11.5)

    for row_idx, kind in enumerate(KIND_ORDER):
        draw_heatmap(
            pearson_axes[row_idx],
            matrix_from_pairwise(pairwise, kind, "pearson_r"),
            f"{KIND_LABELS[kind]}",
            cbar=False,
            show_xlabels=True,
        )

    fig.text(0.02, 0.965, "A", fontsize=14, fontweight="bold")
    fig.text(0.075, 0.965, "Heterogeneity across augmented papers", ha="left", fontsize=12.2)
    fig.text(0.59, 0.965, "B", fontsize=14, fontweight="bold")
    fig.text(0.645, 0.965, "Cross-LLM agreement on augmented performance", ha="left", fontsize=12.2)

    fig.subplots_adjust(left=0.18, right=0.985, top=0.88, bottom=0.11)
    top_box_pos = box_axes[0].get_position()
    bottom_box_pos = box_axes[1].get_position()
    fig.legend(
        handles=[no_aug_handle],
        loc="center left",
        bbox_to_anchor=(
            top_box_pos.x0 + 0.02,
            bottom_box_pos.y1 + (top_box_pos.y0 - bottom_box_pos.y1) / 2.0,
        ),
        frameon=False,
        fontsize=8.8,
        handletextpad=0.5,
        borderaxespad=0.0,
    )
    top_pos = pearson_axes[0].get_position()
    bottom_pos = pearson_axes[1].get_position()
    cbar_width = 0.010
    cbar_height = 0.22
    cbar_x = top_pos.x1 + 0.018
    cbar_y = (bottom_pos.y0 + top_pos.y1 - cbar_height) / 2.0
    cbar_ax = fig.add_axes([cbar_x, cbar_y, cbar_width, cbar_height])
    scalar_map = plt.cm.ScalarMappable(cmap="YlGnBu", norm=plt.Normalize(vmin=0.0, vmax=1.0))
    scalar_map.set_array([])
    colorbar = fig.colorbar(scalar_map, cax=cbar_ax, orientation="vertical")
    colorbar.set_label(r"$r$", fontsize=9.5, labelpad=3)
    colorbar.ax.tick_params(labelsize=8.0, length=2.5, pad=1)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)


def write_documentation(rows: pd.DataFrame, summary: pd.DataFrame, pairwise: pd.DataFrame) -> None:
    doc = f"""# Figure 2: Heterogeneity and Cross-LLM Agreement

Output:
- Figure: `{FIG_PNG}`
- Rows: `{ROWS_CSV}`
- Summary: `{SUMMARY_CSV}`
- Pairwise agreement: `{PAIRWISE_CSV}`

Purpose:
- Panel A shows that augmented performance varies substantially depending on which paper or collection is supplied.
- Panel B shows whether the three main-text LLMs agree on which augmented papers or collections perform better or worse using Pearson r.

Construction:
- LLMs: `Claude Sonnet 4.6`, `GPT-4.1`, and `Gemini 2.5 Pro` (displayed as `Gemini Pro 2.5` in the figure).
- Input types:
  - Individual papers: n = 2,011.
  - Collections: n = 717, operationalized as the corrected metadata-filter collection rows in `{COLLECTION_METRICS_CSV}` plus the separate `Collection of all papers` row.
- Metric: `Corr(y_true, y_pred)`.
- Panel A boxplots use item-level augmented correlations from the corrected `260409` tables.
- Panel A boxes show median and interquartile range; whiskers span the 5th to 95th percentiles; outliers are plotted as faint points.
- Panel A diamond markers show each LLM's no-augmentation 30-run performance and are labeled as `No augmentation`.
- Panel A vertical dotted black line marks the noise ceiling from `{NO_AUG_BENCHMARKS_CSV}`.
- Panel B heatmaps use pairwise complete items for the three displayed LLMs.
- Panel B masks the upper triangle because each agreement matrix is symmetric.
- Panel B uses one shared vertical colorbar centered between the individual-paper and collection heatmaps.
- Pearson r is computed across item-level augmented correlations.
- Pairwise table includes a standard one-sided parametric Pearson test of `r > 0`.

Data sources:
- Individual-paper correlations: `{PAPER_METRICS_CSV}`
- Collection correlations: `{COLLECTION_METRICS_CSV}`, with `Collection of all papers` reconstructed from the same source path used in `{OLD_FIG_PNG}`.
- Unaugmented baseline table: `{BASELINE30_CSV}`
- Noise ceiling table: `{NO_AUG_BENCHMARKS_CSV}`

Notes:
- All augmented values use `corr(mean prediction across repeats, truth)`, not mean of repeat-level correlations.
- Pairwise paper agreement uses {int(pairwise.loc[pairwise["kind"].eq("individual_papers"), "n_shared_items"].iloc[0])} shared papers.
- Pairwise collection agreement uses {int(pairwise.loc[pairwise["kind"].eq("metadata_filter_collections"), "n_shared_items"].iloc[0])} shared collections.
- The parametric Pearson p-values are descriptive. They assume independent item rows, which is not strictly true for overlapping metadata-filter collections.
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = build_rows()
    summary = build_summary(rows)
    pairwise = build_pairwise(rows)
    rows.to_csv(ROWS_CSV, index=False)
    summary.to_csv(SUMMARY_CSV, index=False)
    pairwise.to_csv(PAIRWISE_CSV, index=False)
    draw_figure(rows, summary, pairwise)
    write_documentation(rows, summary, pairwise)


if __name__ == "__main__":
    main()
