from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot_paths import (  # noqa: E402
    VALIDATION_AUGMENTATION_CONVERGENCE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (  # noqa: E402
    VALIDATION_AUGMENTATION_DELTA_MODEL_RESULTS as DELTA_RESULTS,
    VALIDATION_AUGMENTATION_CONVERGENCE_RESULTS as RESULTS,
)


ROOT = Path(__file__).resolve().parents[1]

INPUT_TABLE = DELTA_RESULTS / "validation_augmentation_delta_by_model_table.csv"
SUMMARY_TABLE = RESULTS / "validation_augmentation_convergence_summary.csv"
SPREAD_TABLE = RESULTS / "validation_augmentation_convergence_spread.csv"

METRICS = ["rmse", "correlation", "r2", "directional_accuracy"]
METRIC_LABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$",
    "directional_accuracy": "Directional Accuracy",
}
MODE_LABELS = {
    "single": "single w/o explanation",
    "reasoning": "single with explanation",
}
MODEL_COLORS = {
    "GPT-3.5 Turbo": "#6c757d",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-4.1 Mini": "#1f77b4",
    "GPT-4o": "#2ca02c",
    "o3": "#d62728",
    "o4-mini": "#9467bd",
    "GPT-4.1": "#ff7f0e",
    "GPT-5.1": "#17becf",
}


def _improvement(metric: str, delta: pd.Series) -> pd.Series:
    if metric == "rmse":
        return -delta
    return delta


def _weakness(metric: str, baseline: pd.Series) -> pd.Series:
    if metric == "rmse":
        return baseline
    return -baseline


def load_model_level_summary() -> pd.DataFrame:
    df = pd.read_csv(INPUT_TABLE)
    rows: list[dict[str, object]] = []
    for metric in METRICS:
        base_col = f"baseline_{metric}"
        delta_col = f"delta_{metric}"
        metric_rows = (
            df.groupby(["model", "mode"], as_index=False)
            .agg(
                baseline=(base_col, "first"),
                augmented=(metric, "mean"),
                delta=(delta_col, "mean"),
                n_conditions=(metric, "size"),
            )
            .assign(metric=metric)
        )
        metric_rows["improvement"] = _improvement(metric, metric_rows["delta"])
        metric_rows["weakness"] = _weakness(metric, metric_rows["baseline"])
        rows.extend(metric_rows.to_dict("records"))
    out = pd.DataFrame(rows)
    return out


def load_spread_summary(model_summary: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for include_nano in [True, False]:
        subset = model_summary.copy()
        inclusion_label = "All models" if include_nano else "Excluding GPT-4.1 Nano"
        if not include_nano:
            subset = subset.loc[subset["model"] != "GPT-4.1 Nano"].copy()

        for metric in METRICS:
            for mode, part in subset.loc[subset["metric"] == metric].groupby("mode"):
                baseline = part["baseline"].to_numpy(dtype=float)
                augmented = part["augmented"].to_numpy(dtype=float)
                baseline = baseline[np.isfinite(baseline)]
                augmented = augmented[np.isfinite(augmented)]
                rows.append(
                    {
                        "inclusion": inclusion_label,
                        "metric": metric,
                        "mode": mode,
                        "n_models": len(part),
                        "baseline_std": float(np.std(baseline, ddof=0)),
                        "augmented_std": float(np.std(augmented, ddof=0)),
                        "delta_std": float(np.std(augmented, ddof=0) - np.std(baseline, ddof=0)),
                        "baseline_range": float(np.max(baseline) - np.min(baseline)),
                        "augmented_range": float(np.max(augmented) - np.min(augmented)),
                        "delta_range": float(
                            (np.max(augmented) - np.min(augmented))
                            - (np.max(baseline) - np.min(baseline))
                        ),
                    }
                )
    return pd.DataFrame(rows)


def _fit_line(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    if len(x) < 2:
        return None
    slope, intercept = np.polyfit(x, y, 1)
    xs = np.linspace(float(np.min(x)), float(np.max(x)), 100)
    ys = slope * xs + intercept
    return xs, ys


def plot_gain_vs_baseline(model_summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(len(METRICS), 2, figsize=(12.8, 3.55 * len(METRICS)), constrained_layout=False)
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(1, 2)

    for row_idx, metric in enumerate(METRICS):
        for col_idx, mode in enumerate(["single", "reasoning"]):
            ax = axes[row_idx, col_idx]
            part = model_summary.loc[
                (model_summary["metric"] == metric) & (model_summary["mode"] == mode)
            ].copy()

            ax.axhline(0.0, color="0.65", linewidth=1.0, linestyle="--", zorder=0)

            x = part["baseline"].to_numpy(dtype=float)
            y = part["delta"].to_numpy(dtype=float)
            if len(part) >= 2:
                corr = float(np.corrcoef(x, y)[0, 1])
                fit = _fit_line(x, y)
                if fit is not None:
                    xs, ys = fit
                    ax.plot(xs, ys, color="0.25", linewidth=1.4, zorder=1)
            else:
                corr = float("nan")

            for _, row in part.iterrows():
                ax.scatter(
                    row["baseline"],
                    row["delta"],
                    s=70,
                    color=MODEL_COLORS.get(str(row["model"]), "#444444"),
                    edgecolors="white",
                    linewidths=0.8,
                    zorder=3,
                )
                ax.annotate(
                    str(row["model"]),
                    (row["baseline"], row["delta"]),
                    xytext=(4, 4),
                    textcoords="offset points",
                    fontsize=8.3,
                    color="0.2",
                )

            ax.grid(alpha=0.18, zorder=0)
            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode])
            if col_idx == 0:
                direction = "lower is better" if metric == "rmse" else "higher is better"
                metric_text = METRIC_LABELS[metric]
                ax.set_ylabel(f"Δ{metric_text}\n({direction})")
            ax.set_xlabel(f"Baseline {METRIC_LABELS[metric]}")
            ax.text(
                0.03,
                0.95,
                f"$r = {corr:.2f}$",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=10,
                bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none", "pad": 1.5},
            )

    fig.suptitle(
        "Validation Augmentation Convergence: Baseline Performance vs Average Delta",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "Y-axis is the mean augmentation delta relative to matched no-augmentation within mode.",
        ha="center",
        va="bottom",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(PLOTS / "validation_augmentation_convergence_gain_vs_baseline.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_augmentation_convergence_gain_vs_baseline.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_spread_before_after(spread_summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, len(METRICS), figsize=(4.3 * len(METRICS), 7.8), constrained_layout=False)
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(2, 1)
    mode_positions = {"single": 1, "reasoning": 0}
    mode_colors = {"single": "#6c757d", "reasoning": "#2b8cbe"}

    for row_idx, inclusion in enumerate(["All models", "Excluding GPT-4.1 Nano"]):
        for col_idx, metric in enumerate(METRICS):
            ax = axes[row_idx, col_idx]
            part = spread_summary.loc[
                (spread_summary["inclusion"] == inclusion) & (spread_summary["metric"] == metric)
            ].copy()
            for _, row in part.iterrows():
                y = mode_positions[str(row["mode"])]
                x0 = float(row["baseline_std"])
                x1 = float(row["augmented_std"])
                ax.plot([x0, x1], [y, y], color="0.55", linewidth=2.0, zorder=1)
                ax.scatter(x0, y, s=70, color="white", edgecolors="0.35", linewidths=1.4, zorder=2)
                ax.scatter(
                    x1,
                    y,
                    s=80,
                    color=mode_colors[str(row["mode"])],
                    edgecolors="white",
                    linewidths=0.8,
                    zorder=3,
                )
                ax.text(x0, y + 0.12, f"{x0:.2f}", ha="center", va="bottom", fontsize=8, color="0.35")
                ax.text(x1, y - 0.16, f"{x1:.2f}", ha="center", va="top", fontsize=8, color="0.2")

            if row_idx == 0:
                ax.set_title(METRIC_LABELS[metric])
            if col_idx == 0:
                ax.set_ylabel(inclusion)
            ax.set_yticks([0, 1])
            ax.set_yticklabels([MODE_LABELS["reasoning"], MODE_LABELS["single"]])
            ax.grid(axis="x", alpha=0.2, zorder=0)
            ax.set_xlabel("Cross-model SD")

    fig.suptitle(
        "Validation Augmentation Convergence: Cross-Model Spread Before vs After",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "White markers: no-augmentation baseline. Colored markers: mean augmented performance across report variants. Smaller SD implies stronger convergence.",
        ha="center",
        va="bottom",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(PLOTS / "validation_augmentation_convergence_spread_before_after.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_augmentation_convergence_spread_before_after.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_metric_focus(
    metric: str,
    model_summary: pd.DataFrame,
    spread_summary: pd.DataFrame,
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11.8, 8.6), constrained_layout=False)

    for col_idx, mode in enumerate(["single", "reasoning"]):
        ax = axes[0, col_idx]
        part = model_summary.loc[
            (model_summary["metric"] == metric) & (model_summary["mode"] == mode)
        ].copy()
        ax.axhline(0.0, color="0.65", linewidth=1.0, linestyle="--", zorder=0)

        x = part["weakness"].to_numpy(dtype=float)
        y = part["improvement"].to_numpy(dtype=float)
        corr = float(np.corrcoef(x, y)[0, 1]) if len(part) >= 2 else float("nan")
        fit = _fit_line(x, y) if len(part) >= 2 else None
        if fit is not None:
            xs, ys = fit
            ax.plot(xs, ys, color="0.25", linewidth=1.4, zorder=1)

        for _, row in part.iterrows():
            ax.scatter(
                row["weakness"],
                row["improvement"],
                s=75,
                color=MODEL_COLORS.get(str(row["model"]), "#444444"),
                edgecolors="white",
                linewidths=0.8,
                zorder=3,
            )
            ax.annotate(
                str(row["model"]),
                (row["weakness"], row["improvement"]),
                xytext=(4, 4),
                textcoords="offset points",
                fontsize=8.3,
                color="0.2",
            )

        ax.set_title(MODE_LABELS[mode])
        ax.set_xlabel("Baseline weakness (higher = worse)")
        ax.set_ylabel(f"{METRIC_LABELS[metric]} gain\n(higher is better)")
        ax.grid(alpha=0.18, zorder=0)
        ax.text(
            0.03,
            0.95,
            f"$r = {corr:.2f}$",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=10,
            bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none", "pad": 1.5},
        )

    mode_positions = {"single": 1, "reasoning": 0}
    mode_colors = {"single": "#6c757d", "reasoning": "#2b8cbe"}
    for col_idx, inclusion in enumerate(["All models", "Excluding GPT-4.1 Nano"]):
        ax = axes[1, col_idx]
        part = spread_summary.loc[
            (spread_summary["inclusion"] == inclusion) & (spread_summary["metric"] == metric)
        ].copy()
        for _, row in part.iterrows():
            y = mode_positions[str(row["mode"])]
            x0 = float(row["baseline_std"])
            x1 = float(row["augmented_std"])
            ax.plot([x0, x1], [y, y], color="0.55", linewidth=2.0, zorder=1)
            ax.scatter(x0, y, s=70, color="white", edgecolors="0.35", linewidths=1.4, zorder=2)
            ax.scatter(
                x1,
                y,
                s=80,
                color=mode_colors[str(row["mode"])],
                edgecolors="white",
                linewidths=0.8,
                zorder=3,
            )
            ax.text(x0, y + 0.12, f"{x0:.2f}", ha="center", va="bottom", fontsize=8, color="0.35")
            ax.text(x1, y - 0.16, f"{x1:.2f}", ha="center", va="top", fontsize=8, color="0.2")
        ax.set_title(inclusion)
        ax.set_yticks([0, 1])
        ax.set_yticklabels([MODE_LABELS["reasoning"], MODE_LABELS["single"]])
        ax.set_xlabel("Cross-model SD")
        ax.set_ylabel("Mode")
        ax.grid(axis="x", alpha=0.2, zorder=0)

    fig.suptitle(
        f"Validation Augmentation Convergence: {METRIC_LABELS[metric]}",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "Top: weaker baseline vs average gain. Bottom: white = no-augmentation baseline SD, colored = mean augmented SD.",
        ha="center",
        va="bottom",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    stem = f"validation_augmentation_convergence_{metric}"
    fig.savefig(PLOTS / f"{stem}.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    model_summary = load_model_level_summary()
    spread_summary = load_spread_summary(model_summary)
    model_summary.to_csv(SUMMARY_TABLE, index=False)
    spread_summary.to_csv(SPREAD_TABLE, index=False)
    plot_gain_vs_baseline(model_summary)
    plot_spread_before_after(spread_summary)
    for metric in METRICS:
        plot_metric_focus(metric, model_summary, spread_summary)
    print(SUMMARY_TABLE)
    print(SPREAD_TABLE)
    print(PLOTS / "validation_augmentation_convergence_gain_vs_baseline.png")
    print(PLOTS / "validation_augmentation_convergence_spread_before_after.png")


if __name__ == "__main__":
    main()
