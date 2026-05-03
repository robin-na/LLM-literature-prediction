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

from literature_collection_analysis_reports.analyze_validation_collection_analysis_reports_metadata_filters import (
    load_truth_arrays,
)
from paper_figures.plot_collection_linear_metadata_effect_260409 import build_collection_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

BASELINE30_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"
GPT_ALL_COLLECTIONS_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv"
)
ROWS_CSV = RESULTS_DIR / "exploratory_collection_one_filter_barplot_selected4_rows.csv"
FIG_PNG = PLOTS_DIR / "exploratory_collection_one_filter_barplot_selected4.png"
FIG_PDF = PLOTS_DIR / "exploratory_collection_one_filter_barplot_selected4.pdf"

MODELS = ["Claude Sonnet 4.6", "GPT-5.1", "GPT-4.1", "Gemini 2.5 Pro"]
MODEL_TO_LONG_CSV = {
    "Claude Sonnet 4.6": ROOT / "claude_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv",
    "GPT-5.1": ROOT / "openAI_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv",
    "GPT-4.1": ROOT / "openAI_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv",
    "Gemini 2.5 Pro": ROOT / "gemini_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_long.csv",
}

VARIANT_ORDER = [
    "broad_all_2011",
    "type_empirical",
    "type_theoretical",
    "citation_q1_lowest",
    "citation_q2",
    "citation_q3",
    "citation_q4_highest",
    "jcr_q1",
    "jcr_q2",
    "jcr_q3",
    "jcr_q4",
    "year_q1_oldest",
    "year_q2",
    "year_q3",
    "year_q4_newest",
    "discipline_bio_evo",
    "discipline_economics",
    "discipline_math_phys_cs",
    "discipline_multidisciplinary",
    "discipline_other",
    "discipline_psych_social",
]

VARIANT_LABELS = {
    "broad_all_2011": "Everything",
    "type_empirical": "Empirical only",
    "type_theoretical": "Non-empirical only",
    "citation_q1_lowest": "Lowest citation",
    "citation_q2": "Citation Q2",
    "citation_q3": "Citation Q3",
    "citation_q4_highest": "Highest citation",
    "jcr_q1": "JIF Q1",
    "jcr_q2": "JIF Q2",
    "jcr_q3": "JIF Q3",
    "jcr_q4": "JIF Q4",
    "year_q1_oldest": "Oldest",
    "year_q2": "Year Q2",
    "year_q3": "Year Q3",
    "year_q4_newest": "Newest",
    "discipline_bio_evo": "Biology",
    "discipline_economics": "Economics",
    "discipline_math_phys_cs": "Math/physics",
    "discipline_multidisciplinary": "Multidisciplinary",
    "discipline_other": "Other",
    "discipline_psych_social": "Psychology",
}
VARIANT_FAMILY = {
    "broad_all_2011": "all",
    "type_empirical": "type",
    "type_theoretical": "type",
    "citation_q1_lowest": "citation",
    "citation_q2": "citation",
    "citation_q3": "citation",
    "citation_q4_highest": "citation",
    "jcr_q1": "jcr",
    "jcr_q2": "jcr",
    "jcr_q3": "jcr",
    "jcr_q4": "jcr",
    "year_q1_oldest": "year",
    "year_q2": "year",
    "year_q3": "year",
    "year_q4_newest": "year",
    "discipline_bio_evo": "discipline",
    "discipline_economics": "discipline",
    "discipline_math_phys_cs": "discipline",
    "discipline_multidisciplinary": "discipline",
    "discipline_other": "discipline",
    "discipline_psych_social": "discipline",
}
FAMILY_COLORS = {
    "all": "#5f6368",
    "type": "#e59a3a",
    "citation": "#2a9d8f",
    "jcr": "#4c78a8",
    "year": "#7cb342",
    "discipline": "#9c6ade",
}
FAMILY_LABELS = {
    "all": "Everything",
    "type": "Paper type",
    "citation": "Citation",
    "jcr": "Journal impact",
    "year": "Publication year",
    "discipline": "Journal discipline",
}

Q_COLS = [f"Q{i}" for i in range(1, 21)]


def load_baseline30() -> pd.DataFrame:
    df = pd.read_csv(BASELINE30_CSV)
    df = df.loc[df["model"].isin(MODELS), ["model", "correlation_mean_prediction"]].copy()
    return df.rename(columns={"correlation_mean_prediction": "baseline_correlation_mean30"})


def compute_all_collections_rows() -> pd.DataFrame:
    truth = load_truth_arrays()[0]
    rows: list[dict[str, object]] = []

    gpt_avg = pd.read_csv(GPT_ALL_COLLECTIONS_AVG_CSV)
    gpt_avg = gpt_avg.loc[
        gpt_avg["model"].isin(MODELS) & gpt_avg["variant_id"].eq("broad_all_2011")
    ].copy()
    if not gpt_avg.empty:
        for _, row in gpt_avg.iterrows():
            pred = pd.to_numeric(row[Q_COLS], errors="coerce").to_numpy(dtype=float)
            corr = float(np.corrcoef(pred, truth)[0, 1])
            rows.append(
                {
                    "model": str(row["model"]),
                    "variant_id": "broad_all_2011",
                    "variant_label": VARIANT_LABELS["broad_all_2011"],
                    "family": VARIANT_FAMILY["broad_all_2011"],
                    "count": 2011,
                    "correlation": corr,
                    "n_aug_runs": int(pd.to_numeric(row.get("n_runs", np.nan), errors="coerce")),
                }
            )

    usecols = [
        "model_label",
        "augmented_input_id",
        "repeat_index",
        "question_index",
        "prediction",
    ]
    cache: dict[Path, pd.DataFrame] = {}

    for model in MODELS:
        if model in set(gpt_avg["model"]):
            continue
        path = MODEL_TO_LONG_CSV[model]
        if path not in cache:
            cache[path] = pd.read_csv(path, usecols=usecols, low_memory=False)
        df = cache[path]
        part = df.loc[
            (df["model_label"] == model)
            & (df["augmented_input_id"] == "broad_all_2011")
            & (pd.to_numeric(df["repeat_index"], errors="coerce").between(1, 5))
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
        corr = float(np.corrcoef(mean_pred, truth)[0, 1])
        rows.append(
            {
                "model": model,
                "variant_id": "broad_all_2011",
                "variant_label": VARIANT_LABELS["broad_all_2011"],
                "family": VARIANT_FAMILY["broad_all_2011"],
                "count": 2011,
                "correlation": corr,
                "n_aug_runs": int(pivot.shape[0]),
            }
        )
    return pd.DataFrame(rows)


def load_one_filter_rows() -> pd.DataFrame:
    feature_df = build_collection_df()
    feature_df = (
        feature_df.loc[feature_df["model"] == "GPT-4.1", ["variant_id", "count", "n_filters"]]
        .drop_duplicates("variant_id")
        .copy()
    )
    metrics_df = pd.read_csv(COLLECTION_METRICS_CSV)
    df = metrics_df.merge(feature_df, on="variant_id", how="left", validate="many_to_one")
    df = df.loc[df["model"].isin(MODELS) & (pd.to_numeric(df["n_filters"], errors="coerce") == 1)].copy()
    df = df.loc[df["variant_id"].isin(VARIANT_ORDER)].copy()
    df["variant_label"] = df["variant_id"].map(VARIANT_LABELS)
    df["family"] = df["variant_id"].map(VARIANT_FAMILY)
    df["count"] = pd.to_numeric(df["count"], errors="coerce")
    return df.loc[:, ["model", "variant_id", "variant_label", "family", "count", "correlation", "n_aug_runs"]]


def build_plot_rows() -> pd.DataFrame:
    all_rows = compute_all_collections_rows()
    one_filter = load_one_filter_rows()
    baseline = load_baseline30()

    rows = pd.concat([all_rows, one_filter], ignore_index=True, sort=False)
    rows = rows.drop_duplicates(["model", "variant_id"], keep="first").copy()
    rows["variant_order"] = rows["variant_id"].map({name: idx for idx, name in enumerate(VARIANT_ORDER)})
    rows = rows.sort_values(["model", "variant_order"]).reset_index(drop=True)
    rows = rows.merge(baseline, on="model", how="left", validate="many_to_one")
    rows["delta_vs_baseline_mean30"] = rows["correlation"] - rows["baseline_correlation_mean30"]
    return rows


def draw_plot(rows: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(15.8, 8.8), sharex=True, sharey=True)
    axes = axes.ravel()

    x = np.arange(len(VARIANT_ORDER))
    y_min = min(rows["correlation"].min(), rows["baseline_correlation_mean30"].min()) - 0.05
    y_max = max(rows["correlation"].max(), rows["baseline_correlation_mean30"].max()) + 0.05

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
        ax.bar(x, part["correlation"], color=colors, width=0.82, edgecolor="none", zorder=2)
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

    axes[0].set_ylabel("Correlation performance")
    axes[2].set_ylabel("Correlation performance")

    handles = [Patch(facecolor=FAMILY_COLORS[key], edgecolor="none", label=label) for key, label in FAMILY_LABELS.items()]
    handles.append(Line2D([0], [0], color="#222222", lw=1.3, ls=(0, (5, 3)), label="Unaugmented baseline"))
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=4,
        frameon=False,
        bbox_to_anchor=(0.5, 0.99),
        columnspacing=1.2,
        handlelength=1.8,
    )
    fig.suptitle("Collection augmentation performance by one-filter report", fontsize=15, y=0.995)
    fig.subplots_adjust(top=0.88, left=0.08, right=0.99, bottom=0.23, wspace=0.12, hspace=0.25)
    fig.savefig(FIG_PNG, dpi=300)
    fig.savefig(FIG_PDF)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = build_plot_rows()
    rows.to_csv(ROWS_CSV, index=False)
    draw_plot(rows)


if __name__ == "__main__":
    main()
