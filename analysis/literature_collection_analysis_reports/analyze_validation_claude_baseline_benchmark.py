from __future__ import annotations

import os
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from analyze_validation_collection_analysis_reports_repeat5 import (
    Q_COLS,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)
from analyze_validation_gemini_baseline_benchmark import build_figure2_tables, summarize_series
from jsonl_parser import jsonl_to_dataframe


CLAUDE_BATCH_OUTPUT = ROOT / "claude_batch_output"
RESULTS_DIR = ROOT / "results" / "validation" / "claude_literature_baseline_benchmark_repeat5"
GEMINI_RESULTS_DIR = ROOT / "results" / "validation" / "gemini_literature_baseline_benchmark_repeat5"
FIGURE2_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_mean_repeat_correlation"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_mean_repeat_correlation"
EXISTING_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
EXISTING_COMPARISON_CSV = (
    ROOT
    / "results"
    / "paper"
    / "main_text_figures_mean_repeat_correlation"
    / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction.csv"
)
GEMINI_REPEAT_ROWS_CSV = GEMINI_RESULTS_DIR / "gemini_literature_baseline_benchmark_repeat_rows.csv"
GEMINI_COMPARISON_CSV = GEMINI_RESULTS_DIR / "gemini_literature_baseline_benchmark_comparison_vs_avg_prediction.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

MODEL_SPECS = [
    {
        "model": "Claude Opus 4.6",
        "tag": "opus46",
    },
    {
        "model": "Claude Sonnet 4.6",
        "tag": "sonnet46",
    },
    {
        "model": "Claude Haiku 4.5",
        "tag": "haiku45",
    },
]

CONDITION_COLORS = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
CONDITION_LABELS = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}
BENCHMARK_POSITIVE = "#f28e2b"
BENCHMARK_NEGATIVE = "#b23a48"
BRACKET_COLOR = "#6b7280"
CEILING_COLOR = "#0f766e"


def _sanitize_custom_id(custom_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", custom_id)
    if len(safe) <= 64:
        return safe
    head, _, tail = safe.rpartition("_")
    if not tail:
        return safe[:64]
    max_head_len = max(1, 64 - len(tail) - 1)
    return f"{head[:max_head_len]}_{tail}"


def _merged_row_id(base_id: str, tag: str) -> str:
    return _sanitize_custom_id(f"{base_id}__{tag}")


def _baseline_ids(tag: str) -> list[str]:
    return [_merged_row_id(f"baseline_joint_reasoning_rep{i}", tag) for i in range(1, 6)]


def _benchmark_ids(tag: str) -> list[str]:
    return [_merged_row_id(f"paper_analysis_report_joint_rep{i}/PGG_MS_202502", tag) for i in range(1, 6)]


def _mean_prediction_metrics(rows: pd.DataFrame) -> dict[str, float]:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    mean_row = rows.loc[:, Q_COLS].mean(axis=0)
    metrics = compute_metrics(mean_row, treatment, control, learning_mean)
    return {key: float(value) for key, value in metrics.items() if key != "n"}


def load_claude_repeat_rows() -> pd.DataFrame:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    path = CLAUDE_BATCH_OUTPUT / "prediction_literature_baseline-benchmark_reasoning_anthropic_merged_allmodels.jsonl"
    if not path.exists():
        raise FileNotFoundError(path)

    source_df = jsonl_to_dataframe(path, platform="claude").reindex(columns=Q_COLS)
    rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        for condition, row_ids in [
            ("baseline", _baseline_ids(spec["tag"])),
            ("benchmark", _benchmark_ids(spec["tag"])),
        ]:
            missing = [row_id for row_id in row_ids if row_id not in source_df.index]
            if missing:
                raise KeyError(f"Missing {condition} rows for {spec['model']}: {missing}")
            for repeat_index, row_id in enumerate(row_ids, start=1):
                pred_row = pd.to_numeric(source_df.loc[row_id], errors="coerce").reindex(Q_COLS)
                metrics = compute_metrics(pred_row, treatment, control, learning_mean)
                row: dict[str, object] = {
                    "model": spec["model"],
                    "condition": condition,
                    "repeat": repeat_index,
                    "row_id": row_id,
                    **metrics,
                }
                row.update({q: float(pred_row[q]) for q in Q_COLS})
                rows.append(row)

    out = pd.DataFrame(rows)
    return out.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def build_claude_condition_summary(repeat_rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    plot_rows: list[dict[str, object]] = []
    comparison_rows: list[dict[str, object]] = []

    for model in [str(spec["model"]) for spec in MODEL_SPECS]:
        sub = repeat_rows.loc[repeat_rows["model"] == model].copy()
        by_condition: dict[str, dict[str, float]] = {}
        avg_metrics: dict[str, dict[str, float]] = {}
        for condition in ["baseline", "benchmark"]:
            cond_rows = sub.loc[sub["condition"] == condition].copy()
            cond_summary = summarize_series(cond_rows["correlation"])
            by_condition[condition] = cond_summary
            avg_metrics[condition] = _mean_prediction_metrics(cond_rows)
            plot_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "correlation": cond_summary["mean"],
                    "repeat_sd": cond_summary["sd"],
                    "repeat_se": cond_summary["se"],
                    "ci_low": cond_summary["ci_low"],
                    "ci_high": cond_summary["ci_high"],
                    "n_repeats": cond_summary["count"],
                }
            )

        paired = (
            sub.loc[:, ["repeat", "condition", "correlation"]]
            .pivot(index="repeat", columns="condition", values="correlation")
            .dropna()
        )
        diff = paired["benchmark"] - paired["baseline"]
        diff_summary = summarize_series(diff)
        comparison_rows.append(
            {
                "model": model,
                "baseline_avg_prediction_correlation": avg_metrics["baseline"]["correlation"],
                "baseline_mean_repeat_correlation": by_condition["baseline"]["mean"],
                "baseline_shift_mean_repeat_minus_avg_prediction": (
                    by_condition["baseline"]["mean"] - avg_metrics["baseline"]["correlation"]
                ),
                "benchmark_avg_prediction_correlation": avg_metrics["benchmark"]["correlation"],
                "benchmark_mean_repeat_correlation": by_condition["benchmark"]["mean"],
                "benchmark_shift_mean_repeat_minus_avg_prediction": (
                    by_condition["benchmark"]["mean"] - avg_metrics["benchmark"]["correlation"]
                ),
                "delta_avg_prediction_correlation": (
                    avg_metrics["benchmark"]["correlation"] - avg_metrics["baseline"]["correlation"]
                ),
                "delta_mean_repeat_correlation": diff_summary["mean"],
                "delta_shift_mean_repeat_minus_avg_prediction": (
                    float(diff_summary["mean"])
                    - (avg_metrics["benchmark"]["correlation"] - avg_metrics["baseline"]["correlation"])
                ),
            }
        )

    return pd.DataFrame(plot_rows), pd.DataFrame(comparison_rows)


def _noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def plot_figure2_extended(
    plot_df: pd.DataFrame,
    delta_df: pd.DataFrame,
    repeat_detail: pd.DataFrame,
    *,
    ceiling: float,
    output_stem: str,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(11.2, 7.2))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}
    delta_lookup = delta_df.set_index("model")

    ax.axvline(ceiling, color=CEILING_COLOR, linestyle="--", linewidth=1.4, zorder=1)

    for condition in ["baseline", "benchmark"]:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        ax.barh(
            y,
            part["correlation"].to_numpy(dtype=float),
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.32,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack(
            [
                part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
                part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
            ]
        )
        ax.errorbar(
            part["correlation"].to_numpy(dtype=float),
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

    bracket_x = 0.944
    bracket_left = 0.929
    for idx, model in enumerate(model_order):
        row = delta_lookup.loc[model]
        y0 = y_positions[idx] + offsets["baseline"]
        y1 = y_positions[idx] + offsets["benchmark"]
        ax.plot(
            [bracket_left, bracket_x, bracket_x, bracket_left],
            [y0, y0, y1, y1],
            color=BRACKET_COLOR,
            linewidth=1.2,
            zorder=4,
            clip_on=True,
        )
        sig_label = str(row["paired_sig_label"])
        text_color = (
            BENCHMARK_POSITIVE
            if float(row["delta_mean_repeat_correlation"]) >= 0.0 and sig_label != "n.s."
            else BENCHMARK_NEGATIVE
            if float(row["delta_mean_repeat_correlation"]) < 0.0 and sig_label != "n.s."
            else BRACKET_COLOR
        )
        ax.text(
            bracket_x + 0.008,
            (y0 + y1) / 2.0,
            sig_label,
            ha="left",
            va="center",
            fontsize=11.2,
            fontstyle="italic" if sig_label == "n.s." else "normal",
            fontweight="semibold" if sig_label != "n.s." else "normal",
            color=text_color,
            zorder=6,
            clip_on=True,
            bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"},
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Mean correlation with true treatment outcome across 5 repeats")
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
        bbox_to_anchor=(0.0, -0.2),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.99,
        0.045,
        "* repeat-paired 95% CI excludes 0   ** 99% CI excludes 0   *** 99.9% CI excludes 0   n.s. otherwise",
        ha="right",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.text(
        0.01,
        0.02,
        "Error bars are t-based 95% CIs across the five repeat-level correlations.",
        ha="left",
        va="bottom",
        fontsize=9.0,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.30, right=0.95)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{output_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE2_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    claude_repeat_rows = load_claude_repeat_rows()
    claude_plot_rows, claude_comparison_rows = build_claude_condition_summary(claude_repeat_rows)

    claude_repeat_rows.to_csv(RESULTS_DIR / "claude_literature_baseline_benchmark_repeat_rows.csv", index=False)
    claude_plot_rows.to_csv(RESULTS_DIR / "claude_literature_baseline_benchmark_plot_rows.csv", index=False)
    claude_comparison_rows.to_csv(
        RESULTS_DIR / "claude_literature_baseline_benchmark_comparison_vs_avg_prediction.csv",
        index=False,
    )

    existing_repeat_rows = pd.read_csv(EXISTING_REPEAT_ROWS_CSV)
    existing_comparison_rows = pd.read_csv(EXISTING_COMPARISON_CSV)
    gemini_repeat_rows = pd.read_csv(GEMINI_REPEAT_ROWS_CSV)
    gemini_comparison_rows = pd.read_csv(GEMINI_COMPARISON_CSV)

    all_repeat_rows = pd.concat(
        [existing_repeat_rows, gemini_repeat_rows, claude_repeat_rows],
        ignore_index=True,
    )
    all_comparison_rows = pd.concat(
        [existing_comparison_rows, gemini_comparison_rows, claude_comparison_rows],
        ignore_index=True,
    )

    plot_df, delta_df, comparison_df, pairwise_df, global_df, repeat_detail = build_figure2_tables(
        all_repeat_rows,
        all_comparison_rows,
    )

    plot_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows_with_gemini_claude.csv",
        index=False,
    )
    delta_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary_with_gemini_claude.csv",
        index=False,
    )
    comparison_df.to_csv(
        FIGURE2_RESULTS_DIR
        / "figure2_benchmark_report_vs_baseline_correlation_comparison_vs_avg_prediction_with_gemini_claude.csv",
        index=False,
    )
    pairwise_df.to_csv(
        FIGURE2_RESULTS_DIR
        / "figure2_benchmark_report_vs_baseline_correlation_pairwise_model_differences_with_gemini_claude.csv",
        index=False,
    )
    global_df.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_global_model_tests_with_gemini_claude.csv",
        index=False,
    )
    repeat_detail.to_csv(
        FIGURE2_RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_repeat_rows_with_gemini_claude.csv",
        index=False,
    )

    plot_figure2_extended(
        plot_df,
        delta_df,
        repeat_detail,
        ceiling=_noise_ceiling(),
        output_stem="figure2_benchmark_report_vs_baseline_correlation_with_gemini_claude",
    )


if __name__ == "__main__":
    main()
