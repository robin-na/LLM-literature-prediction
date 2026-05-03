from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]

EXISTING_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
GEMINI_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "gemini_literature_baseline_benchmark_repeat5"
    / "gemini_literature_baseline_benchmark_repeat_rows.csv"
)
CLAUDE_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "claude_literature_baseline_benchmark_repeat5"
    / "claude_literature_baseline_benchmark_repeat_rows.csv"
)

EXISTING_COMPARISON_CSV = (
    ROOT
    / "results"
    / "paper"
    / "main_text_figures_mean_repeat_correlation"
    / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction.csv"
)
GEMINI_COMPARISON_CSV = (
    ROOT
    / "results"
    / "validation"
    / "gemini_literature_baseline_benchmark_repeat5"
    / "gemini_literature_baseline_benchmark_comparison_vs_avg_prediction.csv"
)
CLAUDE_COMPARISON_CSV = (
    ROOT
    / "results"
    / "validation"
    / "claude_literature_baseline_benchmark_repeat5"
    / "claude_literature_baseline_benchmark_comparison_vs_avg_prediction.csv"
)
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_median_repeat_correlation"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_median_repeat_correlation"

CONDITION_COLORS = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
CONDITION_LABELS = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}
CEILING_COLOR = "#0f766e"


def _noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def summarize_repeat_distribution(values: pd.Series) -> dict[str, float]:
    arr = values.to_numpy(dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return {
            "count": 0,
            "median": float("nan"),
            "q1": float("nan"),
            "q3": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        }
    return {
        "count": int(arr.size),
        "median": float(np.median(arr)),
        "q1": float(np.quantile(arr, 0.25)),
        "q3": float(np.quantile(arr, 0.75)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
    }


def build_median_figure2_tables(
    all_repeat_rows: pd.DataFrame,
    all_comparison_rows: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    plot_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    model_order = (
        all_repeat_rows.loc[all_repeat_rows["condition"] == "baseline"]
        .groupby("model", observed=False)["correlation"]
        .median()
        .sort_values(ascending=False)
        .index.tolist()
    )

    for model in model_order:
        sub = all_repeat_rows.loc[all_repeat_rows["model"] == model].copy()
        by_condition: dict[str, dict[str, float]] = {}
        paired = (
            sub.loc[:, ["repeat", "condition", "correlation"]]
            .pivot(index="repeat", columns="condition", values="correlation")
            .dropna()
            .sort_index()
        )
        for condition in ["baseline", "benchmark"]:
            cond_summary = summarize_repeat_distribution(sub.loc[sub["condition"] == condition, "correlation"])
            by_condition[condition] = cond_summary
            plot_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "median_repeat_correlation": cond_summary["median"],
                    "repeat_q1": cond_summary["q1"],
                    "repeat_q3": cond_summary["q3"],
                    "repeat_min": cond_summary["min"],
                    "repeat_max": cond_summary["max"],
                    "n_repeats": cond_summary["count"],
                }
            )

        paired_diffs = paired["benchmark"] - paired["baseline"]
        paired_diff_summary = summarize_repeat_distribution(paired_diffs)
        summary_rows.append(
            {
                "model": model,
                "baseline_median_repeat_correlation": by_condition["baseline"]["median"],
                "benchmark_median_repeat_correlation": by_condition["benchmark"]["median"],
                "delta_median_repeat_correlation": (
                    by_condition["benchmark"]["median"] - by_condition["baseline"]["median"]
                ),
                "median_paired_repeat_difference": paired_diff_summary["median"],
                "paired_difference_q1": paired_diff_summary["q1"],
                "paired_difference_q3": paired_diff_summary["q3"],
                "n_repeats": paired_diff_summary["count"],
            }
        )

    plot_df = pd.DataFrame(plot_rows)
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=model_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    summary_df = pd.DataFrame(summary_rows)
    summary_df["model"] = pd.Categorical(summary_df["model"], categories=model_order, ordered=True)
    summary_df = summary_df.sort_values("model").reset_index(drop=True)

    comparison_df = all_comparison_rows.loc[
        :,
        [
            "model",
            "baseline_avg_prediction_correlation",
            "benchmark_avg_prediction_correlation",
            "delta_avg_prediction_correlation",
        ],
    ].copy()
    comparison_df = comparison_df.merge(summary_df, on="model", how="inner")
    comparison_df["baseline_shift_median_repeat_minus_avg_prediction"] = (
        comparison_df["baseline_median_repeat_correlation"] - comparison_df["baseline_avg_prediction_correlation"]
    )
    comparison_df["benchmark_shift_median_repeat_minus_avg_prediction"] = (
        comparison_df["benchmark_median_repeat_correlation"] - comparison_df["benchmark_avg_prediction_correlation"]
    )
    comparison_df["delta_shift_median_repeat_minus_avg_prediction"] = (
        comparison_df["delta_median_repeat_correlation"] - comparison_df["delta_avg_prediction_correlation"]
    )
    comparison_df["model"] = pd.Categorical(comparison_df["model"], categories=model_order, ordered=True)
    comparison_df = comparison_df.sort_values("model").reset_index(drop=True)

    repeat_detail = all_repeat_rows.loc[:, ["model", "condition", "repeat", "correlation"]].copy()
    repeat_detail["model"] = pd.Categorical(repeat_detail["model"], categories=model_order, ordered=True)
    repeat_detail = repeat_detail.sort_values(["model", "condition", "repeat"]).reset_index(drop=True)

    return plot_df, summary_df, comparison_df, repeat_detail


def plot_figure2_median(
    plot_df: pd.DataFrame,
    repeat_detail: pd.DataFrame,
    *,
    ceiling: float,
    output_stem: str,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(11.2, 7.0))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}

    ax.axvline(ceiling, color=CEILING_COLOR, linestyle="--", linewidth=1.4, zorder=1)

    for condition in ["baseline", "benchmark"]:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        center = part["median_repeat_correlation"].to_numpy(dtype=float)
        q1 = part["repeat_q1"].to_numpy(dtype=float)
        q3 = part["repeat_q3"].to_numpy(dtype=float)

        ax.barh(
            y,
            center,
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.32,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack([center - q1, q3 - center])
        ax.errorbar(
            center,
            y,
            xerr=xerr,
            fmt="none",
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.35),
            elinewidth=1.0,
            capsize=2.8,
            zorder=4,
        )

        for idx, model in enumerate(model_order):
            repeats = repeat_detail.loc[
                (repeat_detail["model"] == model) & (repeat_detail["condition"] == condition),
                "correlation",
            ].to_numpy(dtype=float)
            if repeats.size == 0:
                continue
            jitter = np.linspace(-0.08, 0.08, repeats.size) if repeats.size > 1 else np.array([0.0])
            ax.scatter(
                repeats,
                np.full(repeats.size, y_positions[idx] + offsets[condition]) + jitter,
                s=18,
                color="#111827",
                alpha=0.65,
                linewidths=0.0,
                zorder=5,
            )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Median correlation with true treatment outcome across 5 repeats")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["benchmark"], linewidth=8, label=CONDITION_LABELS["benchmark"]),
        Line2D([0], [0], marker="o", linestyle="", color="#111827", markersize=5, alpha=0.65, label="Individual repeats"),
        Line2D([0], [0], color=CEILING_COLOR, linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.01,
        0.02,
        "Error bars show the repeat interquartile range; dots show the five individual repeat correlations.",
        ha="left",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.22, right=0.97)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{output_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    all_repeat_rows = pd.concat(
        [
            pd.read_csv(EXISTING_REPEAT_ROWS_CSV),
            pd.read_csv(GEMINI_REPEAT_ROWS_CSV),
            pd.read_csv(CLAUDE_REPEAT_ROWS_CSV),
        ],
        ignore_index=True,
    )
    all_comparison_rows = pd.concat(
        [
            pd.read_csv(EXISTING_COMPARISON_CSV),
            pd.read_csv(GEMINI_COMPARISON_CSV),
            pd.read_csv(CLAUDE_COMPARISON_CSV),
        ],
        ignore_index=True,
    )

    plot_df, summary_df, comparison_df, repeat_detail = build_median_figure2_tables(
        all_repeat_rows,
        all_comparison_rows,
    )

    plot_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows_with_gemini_claude.csv",
        index=False,
    )
    summary_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary_with_gemini_claude.csv",
        index=False,
    )
    comparison_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction_with_gemini_claude.csv",
        index=False,
    )
    repeat_detail.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_repeat_rows_with_gemini_claude.csv",
        index=False,
    )

    plot_figure2_median(
        plot_df,
        repeat_detail,
        ceiling=_noise_ceiling(),
        output_stem="figure2_benchmark_report_vs_baseline_correlation_with_gemini_claude",
    )


if __name__ == "__main__":
    main()
