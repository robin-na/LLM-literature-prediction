from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot_paths import (
    VALIDATION_AUGMENTATION_CONVERGENCE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (
    VALIDATION_AUGMENTATION_CONVERGENCE_RESULTS as RESULTS,
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS as MODEL_SUITE_RESULTS,
    VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_RESULTS as NO_AUG_RESULTS,
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS as REPEAT_RESULTS,
    ensure_results_dir,
)


RUN_METRICS = REPEAT_RESULTS / "validation_reasoning_repeat5_run_metrics.csv"
CONDITION_METRICS = REPEAT_RESULTS / "validation_reasoning_repeat5_condition_comparison.csv"
MODEL_SUITE_ROWS = MODEL_SUITE_RESULTS / "validation_model_suite_augmentation_rows.csv"
NO_AUG_BENCHMARKS = (
    NO_AUG_RESULTS / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

OUTPUT_MODEL_TABLE = RESULTS / "validation_augmentation_convergence_sampling_robustness_models.csv"
OUTPUT_CORR_TABLE = RESULTS / "validation_augmentation_convergence_sampling_robustness_correlations.csv"

METRICS = ["rmse", "correlation", "r2", "directional_accuracy"]
METRIC_LABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$",
    "directional_accuracy": "Directional Accuracy",
}
MODES = ["reasoning", "joint_reasoning"]
MODE_LABELS = {
    "reasoning": "with explanation",
    "joint_reasoning": "joint with explanation",
}
ESTIMATOR_LABELS = {
    "first_run": "First run",
    "mean_run_metric": "Mean of 5 run metrics",
    "mean_prediction_metric": "Average across 5 runs",
    "temp0_metric": "Temperature 0",
}
ESTIMATOR_ORDER = [
    "first_run",
    "mean_run_metric",
    "mean_prediction_metric",
    "temp0_metric",
]
MODEL_COLORS = {
    "GPT-3.5 Turbo": "#6c757d",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-4.1 Mini": "#1f77b4",
    "GPT-4o Mini": "#17a2b8",
    "GPT-4o": "#2ca02c",
    "o3": "#d62728",
    "o4-mini": "#9467bd",
    "GPT-4.1": "#ff7f0e",
    "GPT-5.1": "#00a6a6",
}
BENCHMARK_LINE_COLORS = {"E-Net": "#111111", "Noise ceiling": "#31a354"}


def _fit_line(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    if len(x) < 2:
        return None
    slope, intercept = np.polyfit(x, y, 1)
    xs = np.linspace(float(np.min(x)), float(np.max(x)), 100)
    ys = slope * xs + intercept
    return xs, ys


def build_model_table() -> pd.DataFrame:
    runs = pd.read_csv(RUN_METRICS)
    cond = pd.read_csv(CONDITION_METRICS)

    rows: list[dict[str, object]] = []

    for mode in MODES:
        run_mode = runs.loc[runs["mode"] == mode].copy()
        cond_mode = cond.loc[cond["mode"] == mode].copy()

        for metric in METRICS:
            base_first = (
                run_mode.loc[
                    (run_mode["variant"] == "baseline") & (run_mode["run_label"] == "initial"),
                    ["model", metric],
                ]
                .rename(columns={metric: "baseline"})
                .copy()
            )
            aug_first = (
                run_mode.loc[
                    (run_mode["variant"] != "baseline") & (run_mode["run_label"] == "initial"),
                    ["model", metric],
                ]
                .groupby("model", as_index=False)[metric]
                .mean()
                .rename(columns={metric: "augmented"})
            )
            merged_first = base_first.merge(aug_first, on="model", how="inner")
            for _, row in merged_first.iterrows():
                rows.append(
                    {
                        "mode": mode,
                        "metric": metric,
                        "estimator": "first_run",
                        "model": row["model"],
                        "baseline": float(row["baseline"]),
                        "augmented": float(row["augmented"]),
                        "delta": float(row["augmented"] - row["baseline"]),
                    }
                )

            for estimator in ["mean_run_metric", "mean_prediction_metric", "temp0_metric"]:
                col = f"{estimator}_{metric}"
                base = (
                    cond_mode.loc[cond_mode["variant"] == "baseline", ["model", col]]
                    .rename(columns={col: "baseline"})
                    .copy()
                )
                aug = (
                    cond_mode.loc[cond_mode["variant"] != "baseline", ["model", col]]
                    .groupby("model", as_index=False)[col]
                    .mean()
                    .rename(columns={col: "augmented"})
                )
                merged = base.merge(aug, on="model", how="inner").dropna()
                for _, row in merged.iterrows():
                    rows.append(
                        {
                            "mode": mode,
                            "metric": metric,
                            "estimator": estimator,
                            "model": row["model"],
                            "baseline": float(row["baseline"]),
                            "augmented": float(row["augmented"]),
                            "delta": float(row["augmented"] - row["baseline"]),
                        }
                    )

    return pd.DataFrame(rows)


def build_corr_table(model_table: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (mode, metric, estimator), part in model_table.groupby(
        ["mode", "metric", "estimator"], observed=True
    ):
        baseline = part["baseline"].to_numpy(dtype=float)
        delta = part["delta"].to_numpy(dtype=float)
        corr = float(np.corrcoef(baseline, delta)[0, 1]) if len(part) >= 2 else float("nan")
        rows.append(
            {
                "mode": mode,
                "metric": metric,
                "estimator": estimator,
                "n_models": int(len(part)),
                "r_baseline_vs_delta": corr,
                "baseline_mean": float(np.nanmean(baseline)),
                "delta_mean": float(np.nanmean(delta)),
            }
        )
    out = pd.DataFrame(rows)
    out["mode"] = pd.Categorical(out["mode"], categories=MODES, ordered=True)
    out["metric"] = pd.Categorical(out["metric"], categories=METRICS, ordered=True)
    out["estimator"] = pd.Categorical(
        out["estimator"], categories=ESTIMATOR_ORDER, ordered=True
    )
    return out.sort_values(["mode", "metric", "estimator"]).reset_index(drop=True)


def build_mixed_mode_avg5_table(variant_prefix: str | None = None) -> pd.DataFrame:
    oneoff = pd.read_csv(MODEL_SUITE_ROWS)
    repeat = pd.read_csv(CONDITION_METRICS)

    rows: list[dict[str, object]] = []

    for mode in ["single", "joint"]:
        part_all = oneoff.loc[oneoff["mode"] == mode].copy()
        part_aug = part_all.copy()
        if variant_prefix is not None:
            part_aug = part_aug.loc[part_aug["variant_name"].astype(str).str.startswith(variant_prefix)].copy()
        for metric in METRICS:
            base_col = f"baseline_{metric}"
            delta_col = f"delta_{metric}"
            if part_aug.empty:
                continue
            grouped = (
                part_aug.groupby("model", as_index=False)
                .agg(
                    baseline=(base_col, "first"),
                    augmented=(metric, "mean"),
                    delta=(delta_col, "mean"),
                )
                .assign(mode=mode, metric=metric, estimator="first_run")
            )
            rows.extend(grouped.to_dict("records"))

    for mode in ["reasoning", "joint_reasoning"]:
        part_all = repeat.loc[repeat["mode"] == mode].copy()
        part_aug = part_all.loc[part_all["variant"] != "baseline"].copy()
        if variant_prefix is not None:
            part_aug = part_aug.loc[part_aug["variant"].astype(str).str.startswith(variant_prefix)].copy()
        for metric in METRICS:
            col = f"mean_prediction_metric_{metric}"
            base = (
                part_all.loc[part_all["variant"] == "baseline", ["model", col]]
                .rename(columns={col: "baseline"})
                .copy()
            )
            aug = (
                part_aug.loc[:, ["model", col]]
                .groupby("model", as_index=False)[col]
                .mean()
                .rename(columns={col: "augmented"})
            )
            merged = base.merge(aug, on="model", how="inner")
            merged["delta"] = merged["augmented"] - merged["baseline"]
            merged["mode"] = mode
            merged["metric"] = metric
            merged["estimator"] = "mean_prediction_metric"
            rows.extend(merged.to_dict("records"))

    return pd.DataFrame(rows)


def load_benchmarks() -> pd.DataFrame:
    return pd.read_csv(NO_AUG_BENCHMARKS)


def plot_scatter_grid(
    model_table: pd.DataFrame,
    corr_table: pd.DataFrame,
    mode: str,
    estimators: list[str] | None = None,
    output_suffix: str | None = None,
) -> None:
    if estimators is None:
        estimators = (
            ["first_run", "mean_prediction_metric"]
            if mode == "reasoning"
            else ESTIMATOR_ORDER
        )
    ncols = len(estimators)
    fig, axes = plt.subplots(
        len(METRICS),
        ncols,
        figsize=(9.4 if ncols == 2 else 17.5, 3.2 * len(METRICS)),
        constrained_layout=False,
    )
    if ncols == 1:
        axes = np.asarray(axes).reshape(len(METRICS), 1)

    for row_idx, metric in enumerate(METRICS):
        for col_idx, estimator in enumerate(estimators):
            ax = axes[row_idx, col_idx]
            part = model_table.loc[
                (model_table["mode"] == mode)
                & (model_table["metric"] == metric)
                & (model_table["estimator"] == estimator)
            ].copy()
            ax.axhline(0.0, color="0.7", linewidth=1.0, linestyle="--", zorder=0)

            if len(part) >= 2:
                fit = _fit_line(
                    part["baseline"].to_numpy(dtype=float),
                    part["delta"].to_numpy(dtype=float),
                )
                if fit is not None:
                    xs, ys = fit
                    ax.plot(xs, ys, color="0.25", linewidth=1.3, zorder=1)

            for _, row in part.iterrows():
                ax.scatter(
                    row["baseline"],
                    row["delta"],
                    s=72,
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
                    fontsize=8,
                    color="0.25",
                )

            corr_row = corr_table.loc[
                (corr_table["mode"] == mode)
                & (corr_table["metric"] == metric)
                & (corr_table["estimator"] == estimator)
            ].iloc[0]
            ax.text(
                0.03,
                0.96,
                f"r = {corr_row['r_baseline_vs_delta']:.2f}\nn = {int(corr_row['n_models'])}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9.3,
                bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none", "pad": 1.5},
            )

            if row_idx == 0:
                ax.set_title(ESTIMATOR_LABELS[estimator], fontsize=11)
            if col_idx == 0:
                ax.set_ylabel(f"Δ{METRIC_LABELS[metric]}")
            ax.set_xlabel(f"Baseline {METRIC_LABELS[metric]}")
            ax.grid(alpha=0.18, zorder=0)

    fig.suptitle(
        f"Validation Augmentation Convergence Robustness: {MODE_LABELS[mode]}",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "Each panel correlates baseline no-augmentation performance with mean augmentation delta across report variants under a different sampling estimator.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(
        PLOTS
        / (
            f"validation_augmentation_convergence_sampling_robustness_{mode}"
            + (f"_{output_suffix}" if output_suffix else "")
            + ".png"
        ),
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_corr_heatmap(corr_table: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14.2, 6.4), constrained_layout=False)
    vmin, vmax = -1.0, 1.0

    for ax, mode in zip(axes, MODES, strict=False):
        part = corr_table.loc[corr_table["mode"] == mode].copy()
        pivot = part.pivot(index="estimator", columns="metric", values="r_baseline_vs_delta")
        pivot = pivot.reindex(index=ESTIMATOR_ORDER, columns=METRICS)
        n_pivot = part.pivot(index="estimator", columns="metric", values="n_models").reindex(
            index=ESTIMATOR_ORDER, columns=METRICS
        )

        im = ax.imshow(pivot.to_numpy(dtype=float), cmap="RdBu_r", vmin=vmin, vmax=vmax, aspect="auto")
        ax.set_title(MODE_LABELS[mode], fontsize=12)
        ax.set_xticks(np.arange(len(METRICS)))
        ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS])
        ax.set_yticks(np.arange(len(ESTIMATOR_ORDER)))
        ax.set_yticklabels([ESTIMATOR_LABELS[e] for e in ESTIMATOR_ORDER])

        for i, estimator in enumerate(ESTIMATOR_ORDER):
            for j, metric in enumerate(METRICS):
                val = pivot.loc[estimator, metric]
                n = int(n_pivot.loc[estimator, metric])
                color = "white" if np.isfinite(val) and abs(val) > 0.45 else "black"
                ax.text(
                    j,
                    i,
                    f"{val:.2f}\n(n={n})",
                    ha="center",
                    va="center",
                    fontsize=9,
                    color=color,
                )

    cbar = fig.colorbar(im, ax=axes, fraction=0.03, pad=0.04)
    cbar.set_label("Correlation of baseline performance with augmentation delta")
    fig.suptitle(
        "Validation Augmentation Convergence Robustness Across Sampling Estimators",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.02,
        "More negative values imply stronger convergence: weaker baselines tend to gain more.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.subplots_adjust(top=0.84, bottom=0.12, left=0.07, right=0.92, wspace=0.28)
    fig.savefig(
        PLOTS / "validation_augmentation_convergence_sampling_robustness_heatmap.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_mixed_mode_avg5_convergence(
    model_table: pd.DataFrame,
    title_suffix: str = "Best-Available Estimator by Mode",
    output_stem: str = "validation_augmentation_convergence_best_available_modes",
) -> None:
    mode_order = ["single", "reasoning", "joint", "joint_reasoning"]
    mode_titles = {
        "single": "single w/o explanation",
        "reasoning": "single with explanation",
        "joint": "joint w/o explanation",
        "joint_reasoning": "joint with explanation",
    }
    fig, axes = plt.subplots(
        len(METRICS),
        len(mode_order),
        figsize=(4.0 * len(mode_order), 3.5 * len(METRICS)),
        constrained_layout=False,
    )
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(1, len(mode_order))

    for row_idx, metric in enumerate(METRICS):
        for col_idx, mode in enumerate(mode_order):
            ax = axes[row_idx, col_idx]
            part = model_table.loc[
                (model_table["metric"] == metric) & (model_table["mode"] == mode)
            ].copy()
            ax.axhline(0.0, color="0.7", linewidth=1.0, linestyle="--", zorder=0)

            if len(part) >= 2:
                fit = _fit_line(
                    part["baseline"].to_numpy(dtype=float),
                    part["delta"].to_numpy(dtype=float),
                )
                if fit is not None:
                    xs, ys = fit
                    ax.plot(xs, ys, color="0.25", linewidth=1.3, zorder=1)
                corr = float(
                    np.corrcoef(
                        part["baseline"].to_numpy(dtype=float),
                        part["delta"].to_numpy(dtype=float),
                    )[0, 1]
                )
            else:
                corr = float("nan")

            for _, row in part.iterrows():
                ax.scatter(
                    row["baseline"],
                    row["delta"],
                    s=72,
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
                    fontsize=8,
                    color="0.25",
                )

            ax.text(
                0.03,
                0.96,
                f"r = {corr:.2f}\nn = {len(part)}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9.3,
                bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none", "pad": 1.5},
            )

            if row_idx == 0:
                ax.set_title(mode_titles[mode], fontsize=11)
            if col_idx == 0:
                direction = "lower is better" if metric == "rmse" else "higher is better"
                ax.set_ylabel(f"Δ{METRIC_LABELS[metric]}\n({direction})")
            ax.set_xlabel(f"Baseline {METRIC_LABELS[metric]}")
            ax.grid(alpha=0.18, zorder=0)

    fig.suptitle(
        f"Validation Augmentation Convergence: {title_suffix}",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "Direct modes use the one-off run. Explanation modes use the metric of the predictor formed by averaging 5 temperature-1 runs.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(
        PLOTS / f"{output_stem}.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_mixed_mode_avg5_dumbbells(
    model_table: pd.DataFrame,
    benchmarks: pd.DataFrame,
    title_suffix: str = "Best-Available Estimator by Mode",
    output_stem: str = "validation_augmentation_levels_best_available_modes",
) -> None:
    mode_order = ["single", "reasoning", "joint", "joint_reasoning"]
    mode_titles = {
        "single": "single w/o explanation",
        "reasoning": "single with explanation",
        "joint": "joint w/o explanation",
        "joint_reasoning": "joint with explanation",
    }
    point_colors = {"baseline": "#6c757d", "augmented": "#2b8cbe"}
    arrow_colors = {"better": "#d7301f", "worse": "#3182bd"}
    best_line_color = "#222222"

    fig, axes = plt.subplots(
        len(METRICS),
        len(mode_order),
        figsize=(4.1 * len(mode_order), 3.5 * len(METRICS)),
        constrained_layout=False,
    )
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(1, len(mode_order))

    for row_idx, metric in enumerate(METRICS):
        higher_is_better = metric != "rmse"
        for col_idx, mode in enumerate(mode_order):
            ax = axes[row_idx, col_idx]
            part = model_table.loc[
                (model_table["metric"] == metric) & (model_table["mode"] == mode)
            ].copy()
            if part.empty:
                ax.set_visible(False)
                continue

            part = part.sort_values(
                "baseline",
                ascending=not higher_is_better,
                kind="mergesort",
            ).reset_index(drop=True)
            x = np.arange(len(part))
            baseline = part["baseline"].to_numpy(dtype=float)
            augmented = part["augmented"].to_numpy(dtype=float)
            best_baseline = np.nanmin(baseline) if metric == "rmse" else np.nanmax(baseline)

            ax.axhline(
                best_baseline,
                color=best_line_color,
                linestyle="--",
                linewidth=1.1,
                alpha=0.9,
                zorder=0,
            )
            for bench_name in ["E-Net", "Noise ceiling"]:
                bench_value = float(
                    benchmarks.loc[benchmarks["benchmark"] == bench_name, metric].iloc[0]
                )
                if not np.isfinite(bench_value):
                    continue
                ax.axhline(
                    bench_value,
                    color=BENCHMARK_LINE_COLORS[bench_name],
                    linestyle="--",
                    linewidth=1.1,
                    alpha=0.9,
                    zorder=0,
                )

            for i in range(len(part)):
                improved = augmented[i] < baseline[i] if metric == "rmse" else augmented[i] > baseline[i]
                ax.annotate(
                    "",
                    xy=(x[i], augmented[i]),
                    xytext=(x[i], baseline[i]),
                    arrowprops={
                        "arrowstyle": "-|>",
                        "color": arrow_colors["better" if improved else "worse"],
                        "lw": 1.5,
                        "shrinkA": 4,
                        "shrinkB": 4,
                        "mutation_scale": 10,
                    },
                    zorder=1,
                )

            ax.scatter(
                x,
                baseline,
                s=52,
                color=point_colors["baseline"],
                edgecolors="white",
                linewidths=0.8,
                zorder=3,
                label="No augmentation",
            )
            ax.scatter(
                x,
                augmented,
                s=56,
                color=point_colors["augmented"],
                edgecolors="white",
                linewidths=0.8,
                zorder=4,
                label="Augmented",
            )

            ax.set_xticks(x)
            ax.set_xticklabels(part["model"], rotation=45, ha="right", fontsize=8.6)
            ax.grid(axis="y", alpha=0.18, zorder=0)
            ax.set_axisbelow(True)
            if row_idx == 0:
                ax.set_title(mode_titles[mode], fontsize=11)
            if col_idx == 0:
                direction = "lower is better" if metric == "rmse" else "higher is better"
                ax.set_ylabel(f"{METRIC_LABELS[metric]}\n({direction})")
            ax.set_xlabel("")

    handles = [
        plt.Line2D(
            [], [], color=point_colors["baseline"], marker="o", linestyle="None",
            markersize=7, label="No augmentation"
        ),
        plt.Line2D(
            [], [], color=point_colors["augmented"], marker="o", linestyle="None",
            markersize=7, label="Augmented"
        ),
        plt.Line2D([], [], color=arrow_colors["better"], linewidth=2, label="Improved"),
        plt.Line2D([], [], color=arrow_colors["worse"], linewidth=2, label="Worsened"),
        plt.Line2D([], [], color=best_line_color, linestyle="--", linewidth=1.5, label="Best no-augmentation"),
        plt.Line2D([], [], color=BENCHMARK_LINE_COLORS["E-Net"], linestyle="--", linewidth=1.5, label="E-Net"),
        plt.Line2D([], [], color=BENCHMARK_LINE_COLORS["Noise ceiling"], linestyle="--", linewidth=1.5, label="Noise ceiling"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=7, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        f"Validation Augmentation Levels by Model: {title_suffix}",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Models are ordered within each panel by no-augmentation performance. Arrows point from the matched no-augmentation value to the mean augmented value for each model.",
        ha="center",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(
        PLOTS / f"{output_stem}.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    ensure_results_dir(RESULTS)
    ensure_plot_dir(PLOTS)

    model_table = build_model_table()
    corr_table = build_corr_table(model_table)
    mixed_mode_table = build_mixed_mode_avg5_table()
    mixed_mode_table_paper_only = build_mixed_mode_avg5_table(variant_prefix="paper_only_")
    benchmarks = load_benchmarks()

    model_table.to_csv(OUTPUT_MODEL_TABLE, index=False)
    corr_table.to_csv(OUTPUT_CORR_TABLE, index=False)

    plot_corr_heatmap(corr_table)
    for mode in MODES:
        plot_scatter_grid(model_table, corr_table, mode)
    plot_scatter_grid(
        model_table,
        corr_table,
        "joint_reasoning",
        estimators=["first_run", "mean_prediction_metric"],
        output_suffix="compact",
    )
    plot_mixed_mode_avg5_convergence(mixed_mode_table)
    plot_mixed_mode_avg5_dumbbells(mixed_mode_table, benchmarks)
    plot_mixed_mode_avg5_convergence(
        mixed_mode_table_paper_only,
        title_suffix="Paper-Only Augmentation",
        output_stem="validation_augmentation_convergence_best_available_modes_paper_only",
    )
    plot_mixed_mode_avg5_dumbbells(
        mixed_mode_table_paper_only,
        benchmarks,
        title_suffix="Paper-Only Augmentation",
        output_stem="validation_augmentation_levels_best_available_modes_paper_only",
    )

    print(OUTPUT_MODEL_TABLE)
    print(OUTPUT_CORR_TABLE)
    print(PLOTS / "validation_augmentation_convergence_sampling_robustness_heatmap.png")
    for mode in MODES:
        print(PLOTS / f"validation_augmentation_convergence_sampling_robustness_{mode}.png")
    print(
        PLOTS
        / "validation_augmentation_convergence_sampling_robustness_joint_reasoning_compact.png"
    )
    print(PLOTS / "validation_augmentation_convergence_best_available_modes.png")
    print(PLOTS / "validation_augmentation_levels_best_available_modes.png")
    print(PLOTS / "validation_augmentation_convergence_best_available_modes_paper_only.png")
    print(PLOTS / "validation_augmentation_levels_best_available_modes_paper_only.png")


if __name__ == "__main__":
    main()
