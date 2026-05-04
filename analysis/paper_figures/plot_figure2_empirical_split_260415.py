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

from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df


SOURCE_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

PAPER_METRICS_CSV = SOURCE_RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
BASELINE30_CSV = SOURCE_RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)
PAPER_FEATURE_DATA_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "paper_feature_analysis_dataset_repeat5.csv"
)

FIG_PNG = PLOTS_DIR / "figure2_empirical_split_density.png"
ROWS_CSV = RESULTS_DIR / "figure2_empirical_split_density_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "figure2_empirical_split_density_summary.csv"
DOC_MD = RESULTS_DIR / "figure2_empirical_split_density_documentation.md"

MODELS = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
GROUP_ORDER = ["Empirical", "Non-empirical"]
GROUP_COLORS = {
    "Empirical": "#d95f02",
    "Non-empirical": "#1f9fb5",
}
MODEL_LABEL_COLORS = {
    "Claude Sonnet 4.6": "#9c755f",
    "GPT-4.1": "#2b8cbe",
    "Gemini 2.5 Pro": "#17becf",
}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_baseline30() -> dict[str, float]:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODELS), ["model", "correlation_mean_prediction"]].copy()
    return {str(row["model"]): float(row["correlation_mean_prediction"]) for _, row in df.iterrows()}


def build_paper_split_rows() -> pd.DataFrame:
    metrics_df = pd.read_csv(PAPER_METRICS_CSV)
    metrics_df = metrics_df.loc[metrics_df["model"].isin(MODELS), ["model", "source_id", "correlation"]].copy()

    feature_df = pd.read_csv(PAPER_FEATURE_DATA_CSV, usecols=["source_id", "empirical"]).drop_duplicates()
    feature_df["group"] = feature_df["empirical"].map({True: "Empirical", False: "Non-empirical"})
    feature_df = feature_df.loc[feature_df["group"].notna(), ["source_id", "group"]].copy()

    out = metrics_df.merge(feature_df, on="source_id", how="inner", validate="many_to_one")
    out["kind"] = "individual_papers"
    out["item_id"] = out["source_id"]
    return out.loc[:, ["model", "kind", "item_id", "group", "correlation"]]


def build_collection_split_rows() -> pd.DataFrame:
    collection_df = build_collection_df().loc[lambda x: x["model"].isin(MODELS)].copy()
    collection_df["group"] = collection_df["type_value"].map({"empirical": "Empirical", "theoretical": "Non-empirical"})
    collection_df = collection_df.loc[collection_df["group"].notna(), ["model", "variant_id", "group", "correlation", "count"]].copy()
    collection_df["kind"] = "type_filtered_collections"
    collection_df["item_id"] = collection_df["variant_id"]
    return collection_df.loc[:, ["model", "kind", "item_id", "group", "correlation", "count"]]


def build_rows() -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = pd.concat([build_paper_split_rows(), build_collection_split_rows()], ignore_index=True, sort=False)
    baseline_map = load_baseline30()

    summary_rows: list[dict[str, object]] = []
    for model in MODELS:
        for kind in ["individual_papers", "type_filtered_collections"]:
            for group in GROUP_ORDER:
                part = rows.loc[
                    (rows["model"] == model)
                    & (rows["kind"] == kind)
                    & (rows["group"] == group)
                ].copy()
                summary_rows.append(
                    {
                        "model": model,
                        "kind": kind,
                        "group": group,
                        "n_items": int(part.shape[0]),
                        "mean_correlation": float(part["correlation"].mean()),
                        "sd_correlation": float(part["correlation"].std(ddof=1)),
                        "share_above_baseline": float((part["correlation"] > baseline_map[model]).mean()),
                        "baseline_correlation_mean30": float(baseline_map[model]),
                    }
                )
    return rows, pd.DataFrame(summary_rows)


def draw_figure(rows: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(
        len(MODELS),
        2,
        figsize=(10.8, 7.35),
        sharex=True,
        gridspec_kw={"hspace": 0.10, "wspace": 0.12},
    )

    x_min, x_max = 0.0, 0.90
    ceiling = load_noise_ceiling()

    for row_idx, model in enumerate(MODELS):
        for col_idx, kind in enumerate(["individual_papers", "type_filtered_collections"]):
            ax = axes[row_idx, col_idx]
            baseline_value = float(
                summary_df.loc[
                    (summary_df["model"] == model)
                    & (summary_df["kind"] == kind)
                    & (summary_df["group"] == GROUP_ORDER[0]),
                    "baseline_correlation_mean30",
                ].iloc[0]
            )

            for group in GROUP_ORDER:
                part = rows.loc[
                    (rows["model"] == model)
                    & (rows["kind"] == kind)
                    & (rows["group"] == group)
                ].copy()
                vals = part["correlation"].to_numpy(dtype=float)
                sns.kdeplot(
                    x=vals,
                    ax=ax,
                    color=GROUP_COLORS[group],
                    fill=False,
                    linewidth=1.7,
                    bw_adjust=0.95,
                    cut=0,
                    clip=(x_min, x_max),
                    warn_singular=False,
                )
                kde_line = ax.lines[-1]
                x_kde = np.asarray(kde_line.get_xdata(), dtype=float)
                y_kde = np.asarray(kde_line.get_ydata(), dtype=float)
                ax.fill_between(x_kde, y_kde, 0.0, color=GROUP_COLORS[group], alpha=0.13, zorder=1)
                mean_value = float(summary_df.loc[
                    (summary_df["model"] == model)
                    & (summary_df["kind"] == kind)
                    & (summary_df["group"] == group),
                    "mean_correlation",
                ].iloc[0])
                ax.axvline(mean_value, color=GROUP_COLORS[group], linewidth=1.1, alpha=0.92, zorder=3)

            ax.axvline(baseline_value, color="#4b5563", linewidth=1.05, linestyle="--", alpha=0.95, zorder=2)
            ax.axvline(ceiling, color="#111111", linewidth=1.0, linestyle=":", alpha=0.95, zorder=2)

            if col_idx == 0:
                ax.text(
                    0.01,
                    0.84,
                    model,
                    transform=ax.transAxes,
                    ha="left",
                    va="center",
                    fontsize=11.2,
                    color=MODEL_LABEL_COLORS[model],
                    fontweight="semibold",
                )

            emp_mean = float(summary_df.loc[
                (summary_df["model"] == model) & (summary_df["kind"] == kind) & (summary_df["group"] == "Empirical"),
                "mean_correlation",
            ].iloc[0])
            non_mean = float(summary_df.loc[
                (summary_df["model"] == model) & (summary_df["kind"] == kind) & (summary_df["group"] == "Non-empirical"),
                "mean_correlation",
            ].iloc[0])
            ax.text(
                0.985,
                0.84,
                f"Empirical mean = {emp_mean:.3f}\nNon-empirical mean = {non_mean:.3f}",
                transform=ax.transAxes,
                ha="right",
                va="top",
                fontsize=8.6,
                color="#374151",
                bbox={"boxstyle": "round,pad=0.16", "facecolor": "white", "edgecolor": "none", "alpha": 0.86},
            )
            emp_n = int(summary_df.loc[
                (summary_df["model"] == model) & (summary_df["kind"] == kind) & (summary_df["group"] == "Empirical"),
                "n_items",
            ].iloc[0])
            non_n = int(summary_df.loc[
                (summary_df["model"] == model) & (summary_df["kind"] == kind) & (summary_df["group"] == "Non-empirical"),
                "n_items",
            ].iloc[0])
            unit = "papers" if kind == "individual_papers" else "collections"
            ax.text(
                0.985,
                0.60,
                f"n = {emp_n} empirical, {non_n} non-empirical {unit}",
                transform=ax.transAxes,
                ha="right",
                va="top",
                fontsize=8.5,
                color="#4b5563",
                bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.86},
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
            if row_idx == 0:
                ax.text(
                    ceiling + 0.008,
                    0.93,
                    "Estimated ceiling",
                    transform=ax.get_xaxis_transform(),
                    ha="left",
                    va="center",
                    fontsize=8.5,
                    color="#111111",
                    bbox={"boxstyle": "round,pad=0.14", "facecolor": "white", "edgecolor": "none", "alpha": 0.78},
                )

    axes[0, 0].set_title("2,011 individual papers", fontsize=12.0, pad=10)
    axes[0, 1].set_title("Type-filtered collections", fontsize=12.0, pad=10)
    fig.text(0.5, 0.04, r"$\mathrm{Corr}(y_{\mathrm{true}}, y_{\mathrm{pred}})$", ha="center", va="center")
    fig.text(0.03, 0.5, "Probability density", rotation=90, va="center", ha="center")

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Empirical"], linewidth=1.7, label="Empirical"),
        Line2D([0], [0], color=GROUP_COLORS["Non-empirical"], linewidth=1.7, label="Non-empirical"),
        Line2D([0], [0], color="#4b5563", linewidth=1.05, linestyle="--", label="No augmentation"),
    ]
    fig.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.34, 0.985),
        ncol=3,
        frameon=False,
        columnspacing=1.5,
        handlelength=2.5,
        borderaxespad=0.0,
    )
    fig.subplots_adjust(bottom=0.10, left=0.08, top=0.92, right=0.98)
    fig.savefig(FIG_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)


def write_documentation(rows: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    doc = f"""# Exploratory empirical split density

Output:
- Figure: `{FIG_PNG}`
- Rows: `{ROWS_CSV}`
- Summary: `{SUMMARY_CSV}`

Construction:
- Same three models as the main-text Figure 2: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`.
- Left column: augmented individual-paper correlations split by paper-level empirical label.
- Right column: augmented collection correlations split only across the subset of collection reports with an explicit type filter:
  - `type_value = empirical`
  - `type_value = theoretical`
- Collections with `type_value = ANY` are excluded from the split overlay, because they are not cleanly classifiable as empirical or non-empirical.

Data sources:
- Individual-paper correlations: `{PAPER_METRICS_CSV}`
- Individual-paper empirical labels: `{PAPER_FEATURE_DATA_CSV}`
- Collection correlations and type labels: constructed through `build_collection_df()` in `/Users/robinna/Documents/projects/academic-llm/LLM-literature-prediction/analysis/paper_figures/plot_collection_linear_metadata_effect_260409.py`
- No-augmentation baseline line: `{BASELINE30_CSV}`
- Estimated ceiling: `{NO_AUG_BENCHMARKS_CSV}`

Counts:
"""
    count_lines = []
    for model in MODELS:
        for kind in ["individual_papers", "type_filtered_collections"]:
            part = summary_df.loc[summary_df["model"].eq(model) & summary_df["kind"].eq(kind), ["group", "n_items"]]
            unit = "papers" if kind == "individual_papers" else "collections"
            emp = int(part.loc[part["group"].eq("Empirical"), "n_items"].iloc[0])
            non = int(part.loc[part["group"].eq("Non-empirical"), "n_items"].iloc[0])
            count_lines.append(f"- `{model}` / `{kind}`: {emp} empirical and {non} non-empirical {unit}")
    doc += "\n".join(count_lines) + "\n"
    DOC_MD.write_text(doc, encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows, summary_df = build_rows()
    rows.to_csv(ROWS_CSV, index=False)
    summary_df.to_csv(SUMMARY_CSV, index=False)
    draw_figure(rows, summary_df)
    write_documentation(rows, summary_df)


if __name__ == "__main__":
    main()
