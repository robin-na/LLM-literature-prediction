from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_validation_reasoning_repeat5 import (
    evaluate_predictions,
    load_prediction_cube,
    load_targets,
)
from plot_paths import (
    VALIDATION_AUGMENTATION_CONVERGENCE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (
    VALIDATION_AUGMENTATION_CONVERGENCE_RESULTS as RESULTS,
    ensure_results_dir,
)


MODES = ["reasoning", "joint_reasoning"]
MODE_LABELS = {
    "reasoning": "with explanation",
    "joint_reasoning": "joint with explanation",
}
METRICS = ["rmse", "correlation", "r2"]
METRIC_LABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$",
}
BETTER_HIGHER = {"rmse": False, "correlation": True, "r2": True}
FAMILY_COLORS = {
    "both": "#4c78a8",
    "paper_only": "#f58518",
    "data_only": "#54a24b",
}

OUTPUT_CASES = RESULTS / "validation_augmentation_superior_anchor_cases.csv"
OUTPUT_SUMMARY = RESULTS / "validation_augmentation_superior_anchor_summary.csv"
OUTPUT_ANCHORS = RESULTS / "validation_augmentation_superior_anchor_models.csv"


def _family(variant: str) -> str:
    if variant.startswith("paper_only_"):
        return "paper_only"
    if variant.startswith("data_only_"):
        return "data_only"
    if variant.startswith("both_"):
        return "both"
    return "other"


def _prediction_distance(a: pd.Series, b: pd.Series) -> float:
    valid = a.notna() & b.notna()
    if not valid.any():
        return float("nan")
    diff = a.loc[valid].to_numpy(dtype=float) - b.loc[valid].to_numpy(dtype=float)
    return math.sqrt(float(np.mean(diff**2)))


def build_avg_prediction_table() -> tuple[dict[tuple[str, str, str], pd.Series], pd.DataFrame, pd.Series]:
    target = load_targets()
    cube = load_prediction_cube(target)

    avg_preds: dict[tuple[str, str, str], pd.Series] = {}
    rows: list[dict[str, object]] = []

    keys = {(model, mode, variant) for model, mode, variant, _ in cube.keys()}
    for model, mode, variant in sorted(keys):
        temp1_labels = [
            label
            for label in ["initial", "rep1", "rep2", "rep3", "rep4"]
            if (model, mode, variant, label) in cube
        ]
        if not temp1_labels:
            continue
        preds = pd.concat([cube[(model, mode, variant, label)] for label in temp1_labels], axis=1)
        avg_pred = preds.mean(axis=1, skipna=True)
        metrics = evaluate_predictions(avg_pred, target)
        avg_preds[(model, mode, variant)] = avg_pred
        rows.append({"model": model, "mode": mode, "variant": variant, **metrics})

    metrics_df = pd.DataFrame(rows)
    return avg_preds, metrics_df, target


def build_anchor_cases(
    avg_preds: dict[tuple[str, str, str], pd.Series],
    metrics_df: pd.DataFrame,
    target: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    case_rows: list[dict[str, object]] = []
    anchor_rows: list[dict[str, object]] = []

    for mode in MODES:
        base_part = metrics_df.loc[
            (metrics_df["mode"] == mode) & (metrics_df["variant"] == "baseline")
        ].copy()
        aug_part = metrics_df.loc[
            (metrics_df["mode"] == mode) & (metrics_df["variant"] != "baseline")
        ].copy()

        for metric in METRICS:
            ascending = not BETTER_HIGHER[metric]
            top_models = (
                base_part.sort_values(metric, ascending=ascending)
                .head(3)["model"]
                .tolist()
            )
            anchor_pred = pd.concat(
                [avg_preds[(model, mode, "baseline")] for model in top_models], axis=1
            ).mean(axis=1, skipna=True)
            anchor_metric = evaluate_predictions(anchor_pred, target)[metric]
            anchor_rows.append(
                {
                    "mode": mode,
                    "metric": metric,
                    "anchor_models": " | ".join(top_models),
                    "anchor_metric_value": anchor_metric,
                }
            )

            for _, row in aug_part.iterrows():
                model = str(row["model"])
                variant = str(row["variant"])
                baseline_row = base_part.loc[base_part["model"] == model].iloc[0]
                baseline_pred = avg_preds[(model, mode, "baseline")]
                aug_pred = avg_preds[(model, mode, variant)]

                base_metric = float(baseline_row[metric])
                aug_metric = float(row[metric])
                improvement = aug_metric - base_metric if BETTER_HIGHER[metric] else base_metric - aug_metric

                base_dist = _prediction_distance(baseline_pred, anchor_pred)
                aug_dist = _prediction_distance(aug_pred, anchor_pred)
                closeness_gain = base_dist - aug_dist
                gap_closed_frac = closeness_gain / base_dist if np.isfinite(base_dist) and base_dist > 0 else float("nan")

                case_rows.append(
                    {
                        "mode": mode,
                        "metric": metric,
                        "model": model,
                        "variant": variant,
                        "family": _family(variant),
                        "anchor_models": " | ".join(top_models),
                        "baseline_metric": base_metric,
                        "augmented_metric": aug_metric,
                        "improvement": improvement,
                        "baseline_dist_to_anchor": base_dist,
                        "augmented_dist_to_anchor": aug_dist,
                        "closeness_gain": closeness_gain,
                        "gap_closed_frac": gap_closed_frac,
                        "improved": bool(improvement > 0),
                        "moved_closer": bool(closeness_gain > 0),
                    }
                )

    return pd.DataFrame(case_rows), pd.DataFrame(anchor_rows)


def build_summary(cases: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    levels = ["overall", "both", "paper_only", "data_only"]
    for mode in MODES:
        for metric in METRICS:
            for level in levels:
                part = cases.loc[(cases["mode"] == mode) & (cases["metric"] == metric)].copy()
                if level != "overall":
                    part = part.loc[part["family"] == level].copy()
                improved = part.loc[part["improved"]].copy()
                rows.append(
                    {
                        "mode": mode,
                        "metric": metric,
                        "level": level,
                        "n_cases": int(len(part)),
                        "n_improved": int(len(improved)),
                        "share_cases_improved": float(part["improved"].mean()) if len(part) else float("nan"),
                        "share_improved_moved_closer": float(improved["moved_closer"].mean()) if len(improved) else float("nan"),
                        "mean_gap_closed_frac_improved": float(improved["gap_closed_frac"].mean()) if len(improved) else float("nan"),
                        "median_gap_closed_frac_improved": float(improved["gap_closed_frac"].median()) if len(improved) else float("nan"),
                        "mean_closeness_gain_improved": float(improved["closeness_gain"].mean()) if len(improved) else float("nan"),
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


def plot_scatter(cases: pd.DataFrame, summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(15.4, 9.4), constrained_layout=False)

    for row_idx, mode in enumerate(MODES):
        for col_idx, metric in enumerate(METRICS):
            ax = axes[row_idx, col_idx]
            part = cases.loc[(cases["mode"] == mode) & (cases["metric"] == metric)].copy()

            ax.axhline(0.0, color="0.7", linewidth=1.0, linestyle="--", zorder=0)
            ax.axvline(0.0, color="0.7", linewidth=1.0, linestyle="--", zorder=0)

            if len(part) >= 2:
                fit = _fit_line(
                    part["closeness_gain"].to_numpy(dtype=float),
                    part["improvement"].to_numpy(dtype=float),
                )
                if fit is not None:
                    xs, ys = fit
                    ax.plot(xs, ys, color="0.25", linewidth=1.3, zorder=1)
                corr = float(
                    np.corrcoef(
                        part["closeness_gain"].to_numpy(dtype=float),
                        part["improvement"].to_numpy(dtype=float),
                    )[0, 1]
                )
            else:
                corr = float("nan")

            for family, fam_part in part.groupby("family"):
                ax.scatter(
                    fam_part["closeness_gain"],
                    fam_part["improvement"],
                    s=46,
                    alpha=0.7,
                    color=FAMILY_COLORS.get(family, "#777777"),
                    edgecolors="white",
                    linewidths=0.5,
                    label=family,
                    zorder=3,
                )

            srow = summary.loc[
                (summary["mode"] == mode)
                & (summary["metric"] == metric)
                & (summary["level"] == "overall")
            ].iloc[0]
            ax.text(
                0.03,
                0.97,
                f"r = {corr:.2f}\ncloser among improved = {srow['share_improved_moved_closer']:.2f}\nmean gap closed = {srow['mean_gap_closed_frac_improved']:.2f}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9.2,
                bbox={"facecolor": "white", "alpha": 0.82, "edgecolor": "none", "pad": 1.5},
            )

            if row_idx == 0:
                ax.set_title(METRIC_LABELS[metric], fontsize=12)
            if col_idx == 0:
                ax.set_ylabel(f"{MODE_LABELS[mode]}\nPerformance improvement")
            ax.set_xlabel("Change in closeness to superior baseline predictions")
            ax.grid(alpha=0.18, zorder=0)

    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle(
        "Validation Augmentation: Do Improvements Move Toward Superior Baseline Predictions?",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.02,
        "X > 0 means the augmented prediction moved closer to the top-3 baseline-model ensemble for that mode/metric. Y > 0 means augmentation improved performance.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.06, 1, 0.95])
    fig.savefig(PLOTS / "validation_augmentation_superior_anchor_scatter.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_summary_heatmap(summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14.0, 6.6), constrained_layout=False)
    levels = ["overall", "both", "paper_only", "data_only"]
    level_labels = {
        "overall": "Overall",
        "both": "Both",
        "paper_only": "Paper only",
        "data_only": "Data only",
    }

    for ax, mode in zip(axes, MODES, strict=False):
        part = summary.loc[summary["mode"] == mode].copy()
        pivot = part.pivot(index="level", columns="metric", values="share_improved_moved_closer").reindex(
            index=levels, columns=METRICS
        )
        gap = part.pivot(index="level", columns="metric", values="mean_gap_closed_frac_improved").reindex(
            index=levels, columns=METRICS
        )

        im = ax.imshow(pivot.to_numpy(dtype=float), cmap="YlGnBu", vmin=0.0, vmax=1.0, aspect="auto")
        ax.set_title(MODE_LABELS[mode], fontsize=12)
        ax.set_xticks(np.arange(len(METRICS)))
        ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS])
        ax.set_yticks(np.arange(len(levels)))
        ax.set_yticklabels([level_labels[level] for level in levels])

        for i, level in enumerate(levels):
            for j, metric in enumerate(METRICS):
                share = pivot.loc[level, metric]
                gap_val = gap.loc[level, metric]
                color = "white" if np.isfinite(share) and share > 0.55 else "black"
                ax.text(
                    j,
                    i,
                    f"{share:.2f}\n({gap_val:.2f})",
                    ha="center",
                    va="center",
                    fontsize=9,
                    color=color,
                )

    cbar = fig.colorbar(im, ax=axes, fraction=0.03, pad=0.04)
    cbar.set_label("Share of improved cases that moved closer")
    fig.suptitle(
        "Validation Augmentation: How Often Improved Cases Move Toward Superior Baselines",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.02,
        "Cells show share of improved cases that moved closer; parentheses show mean fraction of the original gap-to-anchor closed among improved cases.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.05, 1, 0.95])
    fig.savefig(PLOTS / "validation_augmentation_superior_anchor_summary_heatmap.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_results_dir(RESULTS)
    ensure_plot_dir(PLOTS)

    avg_preds, metrics_df, target = build_avg_prediction_table()
    cases, anchors = build_anchor_cases(avg_preds, metrics_df, target)
    summary = build_summary(cases)

    cases.to_csv(OUTPUT_CASES, index=False)
    anchors.to_csv(OUTPUT_ANCHORS, index=False)
    summary.to_csv(OUTPUT_SUMMARY, index=False)

    plot_scatter(cases, summary)
    plot_summary_heatmap(summary)

    print(OUTPUT_CASES)
    print(OUTPUT_ANCHORS)
    print(OUTPUT_SUMMARY)
    print(PLOTS / "validation_augmentation_superior_anchor_scatter.png")
    print(PLOTS / "validation_augmentation_superior_anchor_summary_heatmap.png")


if __name__ == "__main__":
    main()
