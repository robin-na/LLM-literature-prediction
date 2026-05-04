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
from matplotlib.lines import Line2D

from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_metadata_filters import (
    load_truth_arrays,
)


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = SOURCE_RESULTS_DIR / "collection_repeat_correlation_metrics.csv"
BASELINE30_CSV = SOURCE_RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)
GPT_ALL_COLLECTIONS_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv"
)
CLAUDE_LONG_CSV = ROOT / "claude_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv"
GEMINI_LONG_CSV = ROOT / "gemini_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv"

ROWS_CSV = RESULTS_DIR / "figure2_individual_collection_density_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "figure2_individual_collection_density_summary.csv"
DOC_MD = RESULTS_DIR / "figure2_individual_collection_density_documentation.md"
FIG_PNG = PLOTS_DIR / "figure2_individual_collection_density.png"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
MODELS = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}
PANEL_LABELS = {
    "individual_papers": "2,011 individual papers",
    "metadata_filter_collections": "717 collections",
}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_baseline30() -> dict[str, float]:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODELS), ["model", "correlation_mean_prediction"]].copy()
    return {str(row["model"]): float(row["correlation_mean_prediction"]) for _, row in df.iterrows()}


def compute_everything_collection_rows() -> pd.DataFrame:
    truth = load_truth_arrays()[0]
    rows: list[dict[str, object]] = []

    gpt_avg = pd.read_csv(GPT_ALL_COLLECTIONS_AVG_CSV)
    gpt_avg = gpt_avg.loc[
        gpt_avg["model"].isin(MODELS) & gpt_avg["variant_id"].eq("broad_all_2011")
    ].copy()
    for _, row in gpt_avg.iterrows():
        pred = pd.to_numeric(row[Q_COLS], errors="coerce").to_numpy(dtype=float)
        rows.append(
            {
                "model": str(row["model"]),
                "kind": "everything_collection",
                "item_id": "broad_all_2011",
                "correlation": float(np.corrcoef(pred, truth)[0, 1]),
                "n_items": 2011,
                "n_aug_runs": int(pd.to_numeric(row.get("n_runs", np.nan), errors="coerce")),
            }
        )

    for model, long_csv in [
        ("Claude Sonnet 4.6", CLAUDE_LONG_CSV),
        ("Gemini 2.5 Pro", GEMINI_LONG_CSV),
    ]:
        long_df = pd.read_csv(
            long_csv,
            usecols=["model_label", "augmented_input_id", "repeat_index", "question_index", "prediction"],
            low_memory=False,
        )
        part = long_df.loc[
            (long_df["model_label"] == model)
            & (long_df["augmented_input_id"] == "broad_all_2011")
            & (pd.to_numeric(long_df["repeat_index"], errors="coerce").between(1, 5))
        ].copy()
        if part.empty:
            continue
        part["question_index"] = pd.to_numeric(part["question_index"], errors="coerce").astype(int)
        part["prediction"] = pd.to_numeric(part["prediction"], errors="coerce")
        pivot = (
            part.pivot_table(
                index="repeat_index",
                columns="question_index",
                values="prediction",
                aggfunc="mean",
            )
            .reindex(columns=range(1, 21))
            .sort_index()
        )
        mean_pred = pivot.mean(axis=0, skipna=True).to_numpy(dtype=float)
        rows.append(
            {
                "model": model,
                "kind": "everything_collection",
                "item_id": "broad_all_2011",
                "correlation": float(np.corrcoef(mean_pred, truth)[0, 1]),
                "n_items": 2011,
                "n_aug_runs": int(pivot.shape[0]),
            }
        )

    out = pd.DataFrame(rows)
    return out.sort_values("model").reset_index(drop=True)


def build_density_rows() -> tuple[pd.DataFrame, pd.DataFrame]:
    paper_df = pd.read_csv(PAPER_METRICS_CSV)
    paper_df = paper_df.loc[
        paper_df["model"].isin(MODELS),
        ["model", "source_id", "correlation", "n_aug_runs"],
    ].copy()
    paper_df["kind"] = "individual_papers"
    paper_df = paper_df.rename(columns={"source_id": "item_id"})
    paper_df["n_items"] = 1

    collection_df = pd.read_csv(COLLECTION_METRICS_CSV)
    collection_df = collection_df.loc[
        collection_df["model"].isin(MODELS),
        ["model", "variant_id", "correlation", "n_aug_runs"],
    ].copy()
    collection_df["kind"] = "metadata_filter_collections"
    collection_df = collection_df.rename(columns={"variant_id": "item_id"})
    collection_df["n_items"] = np.nan

    density_rows = pd.concat([paper_df, collection_df], ignore_index=True, sort=False)
    density_rows["panel_label"] = density_rows["kind"].map(PANEL_LABELS)

    baseline_map = load_baseline30()
    everything_rows = compute_everything_collection_rows()

    summary_rows: list[dict[str, object]] = []
    for model in MODELS:
        for kind in ["individual_papers", "metadata_filter_collections"]:
            part = density_rows.loc[(density_rows["model"] == model) & (density_rows["kind"] == kind)].copy()
            baseline_value = baseline_map[model]
            summary_rows.append(
                {
                    "model": model,
                    "kind": kind,
                    "panel_label": PANEL_LABELS[kind],
                    "n_items_shown": int(part.shape[0]),
                    "mean_augmented_correlation": float(part["correlation"].mean()),
                    "sd_augmented_correlation": float(part["correlation"].std(ddof=1)),
                    "share_above_baseline": float((part["correlation"] > baseline_value).mean()),
                    "n_above_baseline": int((part["correlation"] > baseline_value).sum()),
                    "baseline_correlation_mean30": float(baseline_value),
                }
            )

    summary_df = pd.DataFrame(summary_rows)
    everything_map = everything_rows.set_index("model")["correlation"].to_dict()
    summary_df["everything_collection_correlation"] = summary_df["model"].map(everything_map)
    return density_rows, summary_df


def draw_figure(density_rows: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(
        len(MODELS),
        2,
        figsize=(10.8, 6.95),
        sharex=True,
        gridspec_kw={"hspace": 0.08, "wspace": 0.12},
    )

    x_min, x_max = 0.0, 0.90

    for row_idx, model in enumerate(MODELS):
        for col_idx, kind in enumerate(["individual_papers", "metadata_filter_collections"]):
            ax = axes[row_idx, col_idx]
            part = density_rows.loc[(density_rows["model"] == model) & (density_rows["kind"] == kind)].copy()
            refs = summary_df.loc[(summary_df["model"] == model) & (summary_df["kind"] == kind)].iloc[0]

            sns.kdeplot(
                x=part["correlation"].to_numpy(dtype=float),
                ax=ax,
                color=MODEL_COLORS[model],
                fill=False,
                linewidth=1.9,
                bw_adjust=0.9,
                cut=0,
                clip=(x_min, x_max),
                warn_singular=False,
            )
            kde_line = ax.lines[-1]
            x_kde = np.asarray(kde_line.get_xdata(), dtype=float)
            y_kde = np.asarray(kde_line.get_ydata(), dtype=float)
            baseline_value = float(refs["baseline_correlation_mean30"])
            mask = x_kde >= baseline_value
            if mask.any():
                ax.fill_between(
                    x_kde[mask],
                    y_kde[mask],
                    0.0,
                    color=MODEL_COLORS[model],
                    alpha=0.18,
                    zorder=1,
                )

            ax.axvline(
                float(refs["mean_augmented_correlation"]),
                color=MODEL_COLORS[model],
                linewidth=1.45,
                alpha=0.96,
                zorder=3,
            )
            ax.axvline(
                baseline_value,
                color=MODEL_COLORS[model],
                linewidth=1.2,
                linestyle="--",
                alpha=0.95,
                zorder=3,
            )
            if kind == "metadata_filter_collections":
                everything_value = float(refs["everything_collection_correlation"])
                ax.axvline(
                    everything_value,
                    color="#374151",
                    linewidth=1.75,
                    linestyle=(0, (4, 2, 1.2, 2)),
                    alpha=0.98,
                    zorder=4,
                )
                label_y = 0.20 if row_idx != 1 else 0.24
                label_x = everything_value + 0.014 if everything_value < 0.62 else everything_value - 0.014
                label_ha = "left" if everything_value < 0.62 else "right"
                ax.text(
                    label_x,
                    label_y,
                    "Collection of all papers",
                    transform=ax.get_xaxis_transform(),
                    ha=label_ha,
                    va="center",
                    fontsize=8.1,
                    color="#374151",
                    bbox={"boxstyle": "round,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.88},
                )

            if col_idx == 0:
                ax.text(
                    0.01,
                    0.84,
                    model,
                    transform=ax.transAxes,
                    ha="left",
                    va="center",
                    fontsize=11.2,
                    color=MODEL_COLORS[model],
                    fontweight="semibold",
                )
            ax.annotate(
                "",
                xy=(float(refs["mean_augmented_correlation"]), 0.83),
                xytext=(baseline_value, 0.83),
                xycoords=("data", "axes fraction"),
                textcoords=("data", "axes fraction"),
                annotation_clip=False,
                zorder=5,
                arrowprops={
                    "arrowstyle": "-|>",
                    "lw": 1.1,
                    "color": MODEL_COLORS[model],
                    "alpha": 0.92,
                    "mutation_scale": 10,
                    "shrinkA": 0,
                    "shrinkB": 0,
                },
            )
            ax.text(
                0.985,
                0.82,
                f"{100.0 * float(refs['share_above_baseline']):.0f}% above baseline",
                transform=ax.transAxes,
                ha="right",
                va="top",
                fontsize=8.8,
                color=MODEL_COLORS[model],
                bbox={"boxstyle": "round,pad=0.16", "facecolor": "white", "edgecolor": "none", "alpha": 0.88},
            )
            ax.set_xlim(x_min, x_max)
            ax.set_xticks(np.arange(0.0, 0.91, 0.2))
            ax.set_xticks(np.arange(0.0, 0.91, 0.1), minor=True)
            ax.grid(axis="x", which="minor", color="#e5e7eb", linewidth=0.8)
            ax.grid(axis="x", which="major", color="#e5e7eb", linewidth=0.0)
            ax.grid(axis="y", visible=False)
            ax.set_xlabel("")
            ax.set_ylabel("")
            ax.set_yticks([])
            ax.spines["right"].set_visible(False)
            ax.spines["top"].set_visible(False)

    axes[0, 0].set_title("2,011 individual papers", fontsize=12.0, pad=10)
    axes[0, 1].set_title("717 collections", fontsize=12.0, pad=10)
    fig.text(0.5, 0.04, r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$", ha="center", va="center")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")
    fig.subplots_adjust(bottom=0.10, left=0.08, top=0.93, right=0.98)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)


def write_documentation(density_rows: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    collection_counts = (
        summary_df.loc[summary_df["kind"] == "metadata_filter_collections", ["model", "n_items_shown"]]
        .copy()
        .sort_values("model")
    )
    collection_count_lines = "\n".join(
        f"- `{row.model}`: {int(row.n_items_shown)} metadata-filter collections in the corrected density table"
        for row in collection_counts.itertuples(index=False)
    )

    doc = f"""# Figure 2: Individual Papers and Collections

Output:
- Figure: `{FIG_PNG}`
- Density rows: `{ROWS_CSV}`
- Summary table: `{SUMMARY_CSV}`

How the figure is constructed:
- Rows are the three main-text models, in this order: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`.
- Left column shows the distribution of augmented correlation across the `2,011` individual-paper reports.
- Right column shows the distribution of augmented correlation across the collection reports, with the panel titled `717 collections`.
- The density itself comes from the corrected metadata-filter collection table, and a separate vertical reference line marks the `Collection of all papers` entry (`broad_all_2011`), which contains all `2,011` papers.
- The x-axis is the performance scale, `Corr(y_true, y_pred)`.
- Each panel includes:
  - a solid vertical line for the mean augmented correlation within that panel
  - a dashed vertical line for the model's unaugmented baseline
  - on the collection side only, a heavier dash-dot vertical line for the `Collection of all papers`

Primary data sources:
- Individual-paper density values: `{PAPER_METRICS_CSV}`
- Collection density values: `{COLLECTION_METRICS_CSV}`
- Unaugmented baseline lines (`corr(mean across 30 runs, truth)`): `{BASELINE30_CSV}`
- `Everything` collection:
  - GPT-4.1: `{GPT_ALL_COLLECTIONS_AVG_CSV}`
  - Claude Sonnet 4.6: `{CLAUDE_LONG_CSV}`
  - Gemini 2.5 Pro: `{GEMINI_LONG_CSV}`

Metric definition:
- All augmented density values come from the corrected `260409` pipeline and use `corr(mean prediction across repeats, truth)`, not mean of repeat-level correlations.
- The baseline line uses the same estimand, but with the mean prediction across `30` baseline runs.

Collection count note:
{collection_count_lines}
- The old metadata-filter design space contains `716` report-indexed collections plus the separate `Everything` collection. In the corrected `260409` repeat-intersection table, GPT-4.1 is missing one metadata-filter collection, so its right-panel density uses `715` values.
"""
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    density_rows, summary_df = build_density_rows()
    density_rows.to_csv(ROWS_CSV, index=False)
    summary_df.to_csv(SUMMARY_CSV, index=False)
    draw_figure(density_rows, summary_df)
    write_documentation(density_rows, summary_df)


if __name__ == "__main__":
    main()
