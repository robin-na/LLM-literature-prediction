from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot_paths import (
    VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (
    VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_RESULTS as RESULTS,
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS,
    ensure_results_dir,
)


MODEL_ORDER = [
    "GPT-3.5 Turbo",
    "GPT-4.1 Nano",
    "GPT-4.1 Mini",
    "GPT-4o Mini",
    "GPT-4o",
    "o3",
    "o4-mini",
    "GPT-4.1",
    "GPT-5.1",
]

MODE_LABELS = {
    "reasoning": "with explanation",
    "joint_reasoning": "joint with explanation",
}

RUN_LABEL_ORDER = ["initial", "rep1", "rep2", "rep3", "rep4"]
RUN_DISPLAY = {
    "initial": "Run 1",
    "rep1": "Run 2",
    "rep2": "Run 3",
    "rep3": "Run 4",
    "rep4": "Run 5",
}

RUN_COLORS = {
    "initial": "#d9d9d9",
    "rep1": "#cbcbcb",
    "rep2": "#bdbdbd",
    "rep3": "#afafaf",
    "rep4": "#a1a1a1",
}
AVG_COLOR = "#2b8cbe"

LINE_COLORS = {
    "E-Net": "#111111",
    "Noise ceiling": "#31a354",
    "Train mean baseline": "#756bb1",
}

METRIC_SPECS = {
    "rmse": {
        "avg_col": "avg5_prediction_rmse",
        "run_col_prefix": "run_",
        "benchmark_col": "rmse",
        "ylabel": "RMSE",
        "ascending": True,
        "stem": "validation_no_augmentation_repeat5_runs_reasoning_rmse",
    },
    "correlation": {
        "avg_col": "avg5_prediction_correlation",
        "run_col_prefix": "run_",
        "benchmark_col": "correlation",
        "ylabel": "Correlation",
        "ascending": False,
        "stem": "validation_no_augmentation_repeat5_runs_reasoning_correlation",
    },
    "r2": {
        "avg_col": "avg5_prediction_r2",
        "run_col_prefix": "run_",
        "benchmark_col": "r2",
        "ylabel": r"$R^2$ vs learning-wave mean",
        "ascending": False,
        "stem": "validation_no_augmentation_repeat5_runs_reasoning_r2",
    },
    "directional_accuracy": {
        "avg_col": "avg5_prediction_directional_accuracy",
        "run_col_prefix": "run_",
        "benchmark_col": "directional_accuracy",
        "ylabel": "Directional Accuracy",
        "ascending": False,
        "stem": "validation_no_augmentation_repeat5_runs_reasoning_directional_accuracy",
    },
}

INPUT_CONDITIONS = (
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS
    / "validation_reasoning_repeat5_condition_comparison.csv"
)
INPUT_RUNS = (
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS
    / "validation_reasoning_repeat5_run_metrics.csv"
)
INPUT_BENCHMARKS = (
    RESULTS / "validation_no_augmentation_model_comparison_benchmarks.csv"
)
OUTPUT_TABLE = RESULTS / "validation_no_augmentation_repeat5_runs.csv"


def load_table() -> pd.DataFrame:
    cond = pd.read_csv(INPUT_CONDITIONS)
    runs = pd.read_csv(INPUT_RUNS)

    cond = cond[
        (cond["variant"] == "baseline") & (cond["mode"].isin(MODE_LABELS))
    ][
        [
            "model",
            "mode",
            "n_temp1_runs",
            "mean_prediction_metric_rmse",
            "mean_prediction_metric_correlation",
            "mean_prediction_metric_r2",
            "mean_prediction_metric_directional_accuracy",
        ]
    ].rename(
        columns={
            "mean_prediction_metric_rmse": "avg5_prediction_rmse",
            "mean_prediction_metric_correlation": "avg5_prediction_correlation",
            "mean_prediction_metric_r2": "avg5_prediction_r2",
            "mean_prediction_metric_directional_accuracy": "avg5_prediction_directional_accuracy",
        }
    )

    runs = runs[
        (runs["variant"] == "baseline")
        & (runs["mode"].isin(MODE_LABELS))
        & (runs["run_label"].isin(RUN_LABEL_ORDER))
    ][["model", "mode", "run_label", "rmse", "correlation", "r2", "directional_accuracy"]]

    rows: list[dict[str, object]] = []
    for (model, mode), part in runs.groupby(["model", "mode"], observed=True):
        rec: dict[str, object] = {"model": model, "mode": mode}
        for run_label in RUN_LABEL_ORDER:
            run_part = part.loc[part["run_label"] == run_label]
            if run_part.empty:
                rec[f"run_{run_label}_rmse"] = np.nan
                rec[f"run_{run_label}_correlation"] = np.nan
                rec[f"run_{run_label}_r2"] = np.nan
                rec[f"run_{run_label}_directional_accuracy"] = np.nan
            else:
                row = run_part.iloc[0]
                rec[f"run_{run_label}_rmse"] = float(row["rmse"])
                rec[f"run_{run_label}_correlation"] = float(row["correlation"])
                rec[f"run_{run_label}_r2"] = float(row["r2"])
                rec[f"run_{run_label}_directional_accuracy"] = float(row["directional_accuracy"])
        rows.append(rec)

    run_wide = pd.DataFrame(rows)
    df = cond.merge(run_wide, on=["model", "mode"], how="inner")
    df["model"] = pd.Categorical(df["model"], categories=MODEL_ORDER, ordered=True)
    return df.sort_values(["mode", "model"]).reset_index(drop=True)


def load_benchmarks() -> pd.DataFrame:
    return pd.read_csv(INPUT_BENCHMARKS)


def metric_ylim(df: pd.DataFrame, benchmark_df: pd.DataFrame, metric: str, avg_col: str, benchmark_col: str) -> tuple[float, float]:
    arrs = [df[avg_col].to_numpy(dtype=float)]
    for run_label in RUN_LABEL_ORDER:
        arrs.append(df[f"run_{run_label}_{metric}"].to_numpy(dtype=float))
    arrs.append(benchmark_df[benchmark_col].to_numpy(dtype=float))
    values = np.concatenate(arrs)
    values = values[np.isfinite(values)]
    lo = float(values.min())
    hi = float(values.max())
    lo = min(lo, 0.0)
    pad = 0.12 * (hi - lo if hi > lo else 1.0)
    return lo - pad, hi + pad


def add_labels(ax: plt.Axes, bars, values: np.ndarray, fontsize: int = 6) -> None:
    ymin, ymax = ax.get_ylim()
    span = ymax - ymin
    for bar, value in zip(bars, values, strict=False):
        if not np.isfinite(value):
            continue
        y = value + 0.012 * span if value >= 0 else value - 0.012 * span
        va = "bottom" if value >= 0 else "top"
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{value:.2f}",
            ha="center",
            va=va,
            fontsize=fontsize,
            rotation=90,
        )


def plot_mode(df: pd.DataFrame, benchmark_df: pd.DataFrame, mode: str) -> None:
    panel = df[df["mode"] == mode].copy()
    plot_dir = ensure_plot_dir(PLOTS)

    fig, axes = plt.subplots(1, len(METRIC_SPECS), figsize=(6.2 * len(METRIC_SPECS), 6.8))
    axes = np.atleast_1d(axes)
    line_handles = []
    line_labels = []

    for ax, (metric, spec) in zip(axes, METRIC_SPECS.items(), strict=False):
        avg_col = spec["avg_col"]
        panel_sorted = panel.sort_values(
            by=avg_col,
            ascending=bool(spec["ascending"]),
            kind="mergesort",
        ).reset_index(drop=True)

        x = np.arange(len(panel_sorted))
        width = 0.11
        offsets = np.array([-2.7, -1.6, -0.5, 0.6, 1.7, 3.1]) * width

        ylim = metric_ylim(
            panel_sorted,
            benchmark_df,
            metric=metric,
            avg_col=avg_col,
            benchmark_col=spec["benchmark_col"],
        )

        bar_handles = []
        for i, run_label in enumerate(RUN_LABEL_ORDER):
            vals = panel_sorted[f"run_{run_label}_{metric}"].to_numpy(dtype=float)
            bars = ax.bar(
                x + offsets[i],
                vals,
                width=width,
                color=RUN_COLORS[run_label],
                edgecolor="white",
                linewidth=0.5,
                zorder=3,
                label=RUN_DISPLAY[run_label],
            )
            add_labels(ax, bars, vals)
            if not bar_handles:
                bar_handles.append(bars[0])

        avg_vals = panel_sorted[avg_col].to_numpy(dtype=float)
        avg_bars = ax.bar(
            x + offsets[-1],
            avg_vals,
            width=width,
            color=AVG_COLOR,
            edgecolor="white",
            linewidth=0.6,
            zorder=3,
            label="Average of 5 Predictions",
        )
        add_labels(ax, avg_bars, avg_vals)

        if len(bar_handles) == 1:
            pass

        for _, row in benchmark_df.iterrows():
            value = float(row[spec["benchmark_col"]])
            if not np.isfinite(value):
                continue
            label = f"{row['benchmark']} ({row[spec['benchmark_col']]:.2f})"
            line = ax.axhline(
                value,
                color=LINE_COLORS[str(row["benchmark"])],
                linestyle="--",
                linewidth=1.3,
                zorder=2,
            )
            if label not in line_labels:
                line_handles.append(line)
                line_labels.append(label)

        ax.set_title(spec["ylabel"], fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(panel_sorted["model"], rotation=35, ha="right")
        ax.set_ylim(*ylim)
        ax.grid(axis="y", color="#e6e6e6", linewidth=0.8, zorder=1)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_visible(False)

    axes[0].set_ylabel("Performance")

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=RUN_COLORS[label]) for label in RUN_LABEL_ORDER
    ] + [
        plt.Rectangle((0, 0), 1, 1, color=AVG_COLOR)
    ] + line_handles
    legend_labels = [RUN_DISPLAY[label] for label in RUN_LABEL_ORDER] + [
        "Average of 5 Predictions"
    ] + line_labels

    fig.suptitle(
        f"Validation No-Augmentation: Five Runs and Averaged Predictor ({MODE_LABELS[mode]})",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.935,
        "Baseline only. Models are ordered by the blue bar within each metric.",
        ha="center",
        fontsize=10,
    )
    fig.legend(
        legend_handles,
        legend_labels,
        loc="lower center",
        ncol=5,
        frameon=False,
        bbox_to_anchor=(0.5, -0.045),
    )

    fig.subplots_adjust(top=0.80, bottom=0.28, wspace=0.18)
    fig.savefig(
        plot_dir / f"validation_no_augmentation_repeat5_runs_{mode}.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    ensure_results_dir(RESULTS)
    ensure_plot_dir(PLOTS)

    comparison = load_table()
    comparison.to_csv(OUTPUT_TABLE, index=False)

    benchmarks = load_benchmarks()
    for mode in MODE_LABELS:
        plot_mode(comparison, benchmarks, mode)

    print(OUTPUT_TABLE)
    for mode in MODE_LABELS:
        print(PLOTS / f"validation_no_augmentation_repeat5_runs_{mode}.png")


if __name__ == "__main__":
    main()
