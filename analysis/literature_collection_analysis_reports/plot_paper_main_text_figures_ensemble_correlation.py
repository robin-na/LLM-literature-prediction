from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

from plot_paper_main_text_figures import (
    BENCHMARK_NEGATIVE,
    BENCHMARK_POSITIVE,
    NO_AUG_BENCHMARKS_CSV,
    VALIDATION_CSV,
    corr_with_question_bootstrap_ci,
    paired_corr_delta_bootstrap,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text"

EXISTING_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
EXISTING_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
)
EXISTING_BASELINE_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
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

Q_COLS = [f"Q{i}" for i in range(1, 21)]
CONDITION_COLORS = {"baseline": "#c9ced6", "benchmark": "#f2a65a"}
CONDITION_LABELS = {"baseline": "No augmentation", "benchmark": "Benchmark paper augmented"}


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def load_existing_avg_predictions() -> pd.DataFrame:
    baseline = pd.read_csv(EXISTING_BASELINE_AVG_PRED_CSV).loc[:, ["model", *Q_COLS]].copy()
    baseline["condition"] = "baseline"

    benchmark = pd.read_csv(EXISTING_AVG_PRED_CSV)
    benchmark = benchmark.loc[benchmark["variant_id"] == "benchmark_pgg_ms", ["model", *Q_COLS]].copy()
    benchmark["condition"] = "benchmark"

    out = pd.concat([baseline, benchmark], ignore_index=True)
    out["source"] = "openai"
    return out.loc[:, ["model", "condition", "source", *Q_COLS]]


def load_repeat_avg_predictions(path: Path, *, source: str) -> pd.DataFrame:
    rows = pd.read_csv(path)
    avg = (
        rows.groupby(["model", "condition"], as_index=False)[Q_COLS]
        .mean()
        .sort_values(["model", "condition"])
        .reset_index(drop=True)
    )
    avg["source"] = source
    return avg.loc[:, ["model", "condition", "source", *Q_COLS]]


def load_all_avg_predictions() -> pd.DataFrame:
    return pd.concat(
        [
            load_existing_avg_predictions(),
            load_repeat_avg_predictions(GEMINI_REPEAT_ROWS_CSV, source="gemini"),
            load_repeat_avg_predictions(CLAUDE_REPEAT_ROWS_CSV, source="claude"),
        ],
        ignore_index=True,
    )


def load_all_repeat_rows() -> pd.DataFrame:
    return pd.concat(
        [
            pd.read_csv(EXISTING_REPEAT_ROWS_CSV),
            pd.read_csv(GEMINI_REPEAT_ROWS_CSV),
            pd.read_csv(CLAUDE_REPEAT_ROWS_CSV),
        ],
        ignore_index=True,
    ).sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def build_figure2_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, float]:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth = validation["efficiency_p"].to_numpy(dtype=float) * 100.0
    avg_pred = load_all_avg_predictions()
    all_repeat_rows = load_all_repeat_rows()

    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []

    model_list = sorted(avg_pred["model"].unique().tolist())
    for seed_idx, model in enumerate(model_list):
        baseline_row = avg_pred.loc[(avg_pred["model"] == model) & (avg_pred["condition"] == "baseline")]
        benchmark_row = avg_pred.loc[(avg_pred["model"] == model) & (avg_pred["condition"] == "benchmark")]
        if baseline_row.empty or benchmark_row.empty:
            continue

        baseline_vec = baseline_row.iloc[0][Q_COLS].to_numpy(dtype=float)
        benchmark_vec = benchmark_row.iloc[0][Q_COLS].to_numpy(dtype=float)
        baseline_corr, baseline_lo, baseline_hi = corr_with_question_bootstrap_ci(
            baseline_vec,
            truth,
            seed=100 + seed_idx,
        )
        benchmark_corr, benchmark_lo, benchmark_hi = corr_with_question_bootstrap_ci(
            benchmark_vec,
            truth,
            seed=200 + seed_idx,
        )
        delta_corr, delta_ci, sig_label = paired_corr_delta_bootstrap(
            baseline_vec,
            benchmark_vec,
            truth,
            seed=300 + seed_idx,
        )

        plot_rows.extend(
            [
                {
                    "model": model,
                    "condition": "baseline",
                    "correlation": baseline_corr,
                    "ci_low": baseline_lo,
                    "ci_high": baseline_hi,
                    "delta_correlation": delta_corr,
                    "paired_sig_label": sig_label,
                },
                {
                    "model": model,
                    "condition": "benchmark",
                    "correlation": benchmark_corr,
                    "ci_low": benchmark_lo,
                    "ci_high": benchmark_hi,
                    "delta_correlation": delta_corr,
                    "paired_sig_label": sig_label,
                },
            ]
        )
        delta_rows.append(
            {
                "model": model,
                "baseline_correlation": baseline_corr,
                "correlation": benchmark_corr,
                "delta_correlation": delta_corr,
                "delta_correlation_ci_low": delta_ci["ci95_low"],
                "delta_correlation_ci_high": delta_ci["ci95_high"],
                "delta_correlation_ci99_low": delta_ci["ci99_low"],
                "delta_correlation_ci99_high": delta_ci["ci99_high"],
                "delta_correlation_ci999_low": delta_ci["ci999_low"],
                "delta_correlation_ci999_high": delta_ci["ci999_high"],
                "paired_sig_label": sig_label,
            }
        )

    plot_df = pd.DataFrame(plot_rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)["model"]
        .tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    delta_df = pd.DataFrame(delta_rows)
    delta_df["model"] = pd.Categorical(delta_df["model"], categories=baseline_order, ordered=True)
    delta_df = delta_df.sort_values("model").reset_index(drop=True)

    repeat_detail = all_repeat_rows.loc[:, ["model", "condition", "repeat", "correlation"]].copy()
    repeat_detail["model"] = pd.Categorical(repeat_detail["model"], categories=baseline_order, ordered=True)
    repeat_detail = repeat_detail.sort_values(["model", "condition", "repeat"]).reset_index(drop=True)
    return plot_df, delta_df, repeat_detail, load_noise_ceiling()


def plot_figure2(plot_df: pd.DataFrame, delta_df: pd.DataFrame, ceiling: float, *, output_stem: str) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(11.0, 7.0))

    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.18, "benchmark": 0.18}
    delta_lookup = delta_df.set_index("model")
    bracket_color = "#6b7280"

    ax.axvline(ceiling, color="#0f766e", linestyle="--", linewidth=1.4, zorder=1)

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
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.28),
            elinewidth=0.9,
            capsize=2.5,
            zorder=3,
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
            color=bracket_color,
            linewidth=1.2,
            zorder=4,
            clip_on=True,
        )
        sig_label = str(row["paired_sig_label"])
        text_color = (
            BENCHMARK_POSITIVE
            if float(row["delta_correlation"]) >= 0.0 and sig_label != "n.s."
            else BENCHMARK_NEGATIVE
            if float(row["delta_correlation"]) < 0.0 and sig_label != "n.s."
            else bracket_color
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
            zorder=5,
            clip_on=True,
            bbox={"boxstyle": "round,pad=0.08", "facecolor": "white", "edgecolor": "none"},
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["benchmark"], linewidth=8, label=CONDITION_LABELS["benchmark"]),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.16),
        ncol=3,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.99,
        0.02,
        "* paired 95% CI excludes 0   ** paired 99% CI excludes 0   *** paired 99.9% CI excludes 0   n.s. otherwise",
        ha="right",
        va="bottom",
        fontsize=9.2,
        color="#4b5563",
    )
    fig.subplots_adjust(bottom=0.24, right=0.95)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{output_stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    plot_df, delta_df, repeat_detail, ceiling = build_figure2_data()

    plot_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_plot_rows_with_gemini_claude.csv",
        index=False,
    )
    delta_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_summary_with_gemini_claude.csv",
        index=False,
    )
    delta_df.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_deltas_with_gemini_claude.csv",
        index=False,
    )
    repeat_detail.to_csv(
        RESULTS_DIR / "figure2_benchmark_report_vs_baseline_correlation_repeat_rows_with_gemini_claude.csv",
        index=False,
    )

    plot_figure2(
        plot_df,
        delta_df,
        ceiling,
        output_stem="figure2_benchmark_report_vs_baseline_correlation_with_gemini_claude",
    )


if __name__ == "__main__":
    main()
