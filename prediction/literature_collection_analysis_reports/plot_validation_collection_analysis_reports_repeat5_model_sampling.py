from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_model_sampling"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_repeat5_model_sampling"
REPEAT_ROWS_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
REPEAT_METRIC_SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_metric_summary.csv"
QUESTION_SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_question_summary.csv"
PREDICTION_CORR_SUMMARY_CSV = RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_prediction_corr_summary.csv"

MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
CONDITION_ORDER = ["baseline", "benchmark"]
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
CONDITION_LABELS = {
    "baseline": "No-augmentation baseline",
    "benchmark": "Benchmark paper report",
}


def plot_model_sampling_summary(
    repeat_rows: pd.DataFrame,
    repeat_metric_summary: pd.DataFrame,
    question_summary: pd.DataFrame,
    prediction_corr_summary: pd.DataFrame,
) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig = plt.figure(figsize=(14.2, 8.8), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.1, 0.9], hspace=0.35, wspace=0.24)
    axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[1, 1]),
    ]

    for ax, condition in zip(axes[:2], CONDITION_ORDER):
        part = repeat_rows.loc[repeat_rows["condition"] == condition].copy()
        sns.stripplot(
            data=part,
            x="model",
            y="correlation",
            hue="model",
            order=MODEL_ORDER,
            palette=MODEL_COLORS,
            size=7,
            alpha=0.75,
            jitter=0.12,
            dodge=False,
            legend=False,
            ax=ax,
        )
        means = part.groupby("model", observed=True)["correlation"].mean().reindex(MODEL_ORDER)
        for idx, (model, mean_val) in enumerate(means.items()):
            ax.scatter(idx, mean_val, marker="_", s=520, linewidths=2.4, color="black", zorder=5)
        summary_row = repeat_metric_summary.loc[
            (repeat_metric_summary["condition"] == condition) & (repeat_metric_summary["metric"] == "correlation")
        ].iloc[0]
        ax.text(
            0.02,
            0.97,
            f"eta_model={float(summary_row['eta_model']):.2f}\nmodel SD={float(summary_row['between_sd_model_means']):.03f}\nrepeat SD={float(summary_row['mean_within_model_sd']):.03f}",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=9,
            color="#374151",
            bbox={"facecolor": "white", "alpha": 0.9, "edgecolor": "none", "pad": 2.0},
        )
        ax.set_title(CONDITION_LABELS[condition])
        ax.set_xlabel("")
        ax.set_ylabel("Repeat-level correlation to truth")
        ax.tick_params(axis="x", rotation=18)

    bar_ax = axes[2]
    metrics_plot = [
        ("correlation", "Repeat-level corr eta"),
        ("r2", "Repeat-level R2 eta"),
        ("prediction", "20-question pred eta"),
    ]
    x = np.arange(len(metrics_plot))
    width = 0.34
    baseline_vals = []
    benchmark_vals = []
    for metric_key, _ in metrics_plot:
        if metric_key == "prediction":
            baseline_vals.append(float(question_summary.loc[question_summary["condition"] == "baseline", "eta_model_across_questions"].iloc[0]))
            benchmark_vals.append(float(question_summary.loc[question_summary["condition"] == "benchmark", "eta_model_across_questions"].iloc[0]))
        else:
            baseline_vals.append(float(repeat_metric_summary.loc[(repeat_metric_summary["condition"] == "baseline") & (repeat_metric_summary["metric"] == metric_key), "eta_model"].iloc[0]))
            benchmark_vals.append(float(repeat_metric_summary.loc[(repeat_metric_summary["condition"] == "benchmark") & (repeat_metric_summary["metric"] == metric_key), "eta_model"].iloc[0]))
    bar_ax.bar(x - width / 2, baseline_vals, width=width, color="#9ca3af", label="Baseline")
    bar_ax.bar(x + width / 2, benchmark_vals, width=width, color="#f28e2b", label="Benchmark report")
    bar_ax.set_xticks(x, [label for _, label in metrics_plot])
    bar_ax.set_ylabel("Share of heterogeneity attributable to model")
    bar_ax.set_ylim(0.0, max(baseline_vals + benchmark_vals) + 0.15)
    bar_ax.legend(frameon=False, loc="upper right")
    bar_ax.set_title("Model effect on performance drops after benchmark augmentation")

    corr_ax = axes[3]
    corr_plot = prediction_corr_summary.melt(
        id_vars="condition",
        value_vars=[
            "mean_within_model_repeat_prediction_corr",
            "mean_between_model_repeat_prediction_corr",
            "mean_pairwise_corr_of_model_mean_predictions",
        ],
        var_name="corr_type",
        value_name="value",
    )
    corr_labels = {
        "mean_within_model_repeat_prediction_corr": "Within-model\nrepeat corr",
        "mean_between_model_repeat_prediction_corr": "Between-model\nrepeat corr",
        "mean_pairwise_corr_of_model_mean_predictions": "Model-mean\npairwise corr",
    }
    sns.barplot(
        data=corr_plot,
        x="corr_type",
        y="value",
        hue="condition",
        order=list(corr_labels.keys()),
        hue_order=CONDITION_ORDER,
        palette={"baseline": "#9ca3af", "benchmark": "#f28e2b"},
        ax=corr_ax,
    )
    corr_ax.set_xticks(np.arange(len(corr_labels)))
    corr_ax.set_xticklabels([corr_labels[key] for key in corr_labels.keys()])
    corr_ax.set_ylim(0.75, 1.0)
    corr_ax.set_ylabel("Prediction correlation across 20 questions")
    corr_ax.set_xlabel("")
    corr_ax.legend(frameon=False, title="")
    corr_ax.set_title("Benchmark augmentation raises repeat stability and cross-model convergence")

    fig.suptitle("Repeat-5 model-versus-sampling comparison for baseline and benchmark report augmentation", fontsize=15, y=0.99)
    fig.text(
        0.5,
        0.02,
        "Top: repeat-level correlation to truth for each model. Bottom-left: ANOVA-style eta values comparing model differences to repeat noise. Bottom-right: convergence across the 20-question prediction vectors.",
        ha="center",
        fontsize=9,
        color="#4b5563",
    )
    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_repeat5_model_sampling_summary.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    repeat_metric_summary = pd.read_csv(REPEAT_METRIC_SUMMARY_CSV)
    question_summary = pd.read_csv(QUESTION_SUMMARY_CSV)
    prediction_corr_summary = pd.read_csv(PREDICTION_CORR_SUMMARY_CSV)
    plot_model_sampling_summary(repeat_rows, repeat_metric_summary, question_summary, prediction_corr_summary)


if __name__ == "__main__":
    main()
