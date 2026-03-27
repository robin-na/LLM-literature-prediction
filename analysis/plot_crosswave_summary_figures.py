from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO_ROOT / "results"
from plot_paths import CROSSWAVE_PLOTS as PLOTS_DIR, ensure_plot_dir
DATA_DIR = REPO_ROOT / "science-data_and_code" / "data" / "processed_data"

VAL_METRICS_PATH = RESULTS_DIR / "prediction_positive_case_variations_41_metrics.csv"
LEARN_METRICS_PATH = RESULTS_DIR / "prediction_crosswave_variations_41_learning_with_baselines_metrics.csv"
ROBUST_VAL_METRICS_PATH = RESULTS_DIR / "prediction_crosswave_variations_41_validation_metrics.csv"
ROBUST_LEARN_METRICS_PATH = RESULTS_DIR / "prediction_crosswave_variations_41_learning_metrics.csv"
ROBUST_SUMMARY_PATH = RESULTS_DIR / "prediction_crosswave_variations_41_crosswave_variant_summary.csv"

VAL_GT_PATH = DATA_DIR / "df_paired_val.csv"
LEARN_GT_PATH = DATA_DIR / "df_paired_learn.csv"

MODE_ORDER = ["single", "reasoning", "joint", "joint_reasoning"]
MODE_LABELS = {
    "single": "single",
    "reasoning": "reasoning",
    "joint": "joint",
    "joint_reasoning": "joint+reasoning",
}
INPUT_ORDER = ["baseline", "both", "paper_only", "data_only"]
INPUT_LABELS = {
    "baseline": "baseline",
    "both": "both",
    "paper_only": "paper only",
    "data_only": "data only",
}
INPUT_COLORS = {
    "baseline": "#111827",
    "both": "#0f766e",
    "paper_only": "#b45309",
    "data_only": "#b91c1c",
}
MODE_MARKERS = {
    "single": "o",
    "reasoning": "^",
    "joint": "s",
    "joint_reasoning": "D",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot crosswave performance summary figures."
    )
    parser.add_argument(
        "--validation-metrics",
        type=Path,
        default=VAL_METRICS_PATH,
        help="Validation metrics CSV containing baselines and augmented variants.",
    )
    parser.add_argument(
        "--learning-with-baselines-metrics",
        type=Path,
        default=LEARN_METRICS_PATH,
        help="Learning metrics CSV that already includes the baseline family.",
    )
    parser.add_argument(
        "--robust-validation-metrics",
        type=Path,
        default=ROBUST_VAL_METRICS_PATH,
        help="Validation metrics CSV used for cross-wave robustness.",
    )
    parser.add_argument(
        "--robust-learning-metrics",
        type=Path,
        default=ROBUST_LEARN_METRICS_PATH,
        help="Learning metrics CSV used for cross-wave robustness.",
    )
    parser.add_argument(
        "--robust-summary",
        type=Path,
        default=ROBUST_SUMMARY_PATH,
        help="Cross-wave variant summary CSV.",
    )
    parser.add_argument(
        "--output-prefix",
        default="crosswave",
        help="Prefix for result tables and plots.",
    )
    return parser.parse_args()


def output_paths(prefix: str) -> dict[str, Path]:
    return {
        "performance_table": RESULTS_DIR / f"{prefix}_summary_plot_performance_table.csv",
        "augment_table": RESULTS_DIR / f"{prefix}_summary_plot_augmentation_table.csv",
        "robustness_table": RESULTS_DIR / f"{prefix}_summary_plot_robustness_table.csv",
        "elicitation_png": PLOTS_DIR / f"{prefix}_elicitation_performance.png",
        "elicitation_pdf": PLOTS_DIR / f"{prefix}_elicitation_performance.pdf",
        "augment_png": PLOTS_DIR / f"{prefix}_augmentation_performance_heatmap.png",
        "augment_pdf": PLOTS_DIR / f"{prefix}_augmentation_performance_heatmap.pdf",
        "robustness_png": PLOTS_DIR / f"{prefix}_robustness_scatter.png",
        "robustness_pdf": PLOTS_DIR / f"{prefix}_robustness_scatter.pdf",
    }


def parse_variation_name(name: str) -> tuple[str, str]:
    if name.endswith("_joint_reasoning"):
        return name[: -len("_joint_reasoning")], "joint_reasoning"
    if name.endswith("_joint"):
        return name[: -len("_joint")], "joint"
    if name.endswith("_reasoning"):
        return name[: -len("_reasoning")], "reasoning"
    return name, "single"


def input_group_from_family(family: str) -> str:
    if family.startswith("both_"):
        return "both"
    if family.startswith("paper_only_"):
        return "paper_only"
    if family.startswith("data_only_"):
        return "data_only"
    return "baseline"


def matched_baseline_name(mode: str) -> str:
    mapping = {
        "single": "baseline",
        "reasoning": "baseline_reasoning",
        "joint": "baseline_joint",
        "joint_reasoning": "baseline_joint_reasoning",
    }
    return mapping[mode]


def load_null_mse(path: Path) -> float:
    df = pd.read_csv(path)
    return float(np.mean(((df["treatment_itt_efficiency"] - df["control_itt_efficiency"]) * 100.0) ** 2))


def with_metadata(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    parsed = out["variation"].map(parse_variation_name)
    out["family"] = parsed.map(lambda item: item[0])
    out["mode"] = parsed.map(lambda item: item[1])
    out["input_group"] = out["family"].map(input_group_from_family)
    return out


def add_r2(df: pd.DataFrame, null_mse: float) -> pd.DataFrame:
    out = df.copy()
    out["mse"] = out["rmse"] ** 2
    out["r2"] = 1.0 - (out["mse"] / null_mse)
    return out


def load_performance_table(validation_metrics_path: Path, learning_metrics_path: Path) -> pd.DataFrame:
    val_metrics = pd.read_csv(validation_metrics_path)
    val_metrics = with_metadata(val_metrics)
    val_metrics = add_r2(val_metrics, load_null_mse(VAL_GT_PATH))
    val_metrics["wave"] = "validation"
    val_metrics["source"] = "validation_batch"

    learn_metrics = pd.read_csv(learning_metrics_path)
    if "family" not in learn_metrics.columns:
        learn_metrics = with_metadata(learn_metrics)
    learn_metrics = add_r2(learn_metrics, load_null_mse(LEARN_GT_PATH))
    learn_metrics["wave"] = "learning"
    learn_metrics["source"] = learn_metrics.get("source", "learning_batch")

    keep_cols = [
        "wave",
        "source",
        "variation",
        "family",
        "mode",
        "input_group",
        "rmse",
        "correlation",
        "directional_accuracy",
        "r2",
        "n",
    ]
    combined = pd.concat([val_metrics[keep_cols], learn_metrics[keep_cols]], ignore_index=True)
    return combined


def build_augmentation_table(perf_df: pd.DataFrame) -> pd.DataFrame:
    base = perf_df[perf_df["input_group"] == "baseline"][
        ["wave", "variation", "mode", "rmse", "r2", "correlation", "directional_accuracy"]
    ].rename(
        columns={
            "variation": "baseline_variation",
            "rmse": "baseline_rmse",
            "r2": "baseline_r2",
            "correlation": "baseline_correlation",
            "directional_accuracy": "baseline_directional_accuracy",
        }
    )
    augmented = perf_df[perf_df["input_group"] != "baseline"].copy()
    augmented["baseline_variation"] = augmented["mode"].map(matched_baseline_name)
    merged = augmented.merge(
        base,
        on=["wave", "mode", "baseline_variation"],
        how="left",
    )
    for metric in ["rmse", "r2", "correlation", "directional_accuracy"]:
        merged[f"delta_{metric}"] = merged[metric] - merged[f"baseline_{metric}"]

    grouped = (
        merged.groupby(["wave", "input_group", "mode"], dropna=False)
        .agg(
            n_variants=("variation", "size"),
            median_delta_rmse=("delta_rmse", "median"),
            median_delta_r2=("delta_r2", "median"),
            median_delta_correlation=("delta_correlation", "median"),
            median_delta_directional_accuracy=("delta_directional_accuracy", "median"),
            mean_delta_rmse=("delta_rmse", "mean"),
            mean_delta_r2=("delta_r2", "mean"),
            mean_delta_correlation=("delta_correlation", "mean"),
            mean_delta_directional_accuracy=("delta_directional_accuracy", "mean"),
        )
        .reset_index()
    )
    return grouped


def percentile_rank(series: pd.Series, higher_is_better: bool) -> pd.Series:
    n = len(series)
    if n <= 1:
        return pd.Series(np.repeat(100.0, n), index=series.index)
    rank = series.rank(method="min", ascending=not higher_is_better)
    return 100.0 * (n - rank) / (n - 1)


def build_robustness_table(
    robust_validation_metrics_path: Path,
    robust_learning_metrics_path: Path,
    robust_summary_path: Path,
) -> pd.DataFrame:
    val = with_metadata(pd.read_csv(robust_validation_metrics_path))
    learn = with_metadata(pd.read_csv(robust_learning_metrics_path))
    val = add_r2(val, load_null_mse(VAL_GT_PATH))
    learn = add_r2(learn, load_null_mse(LEARN_GT_PATH))

    shared = sorted(set(val["variation"]).intersection(learn["variation"]))
    val = val[val["variation"].isin(shared)].copy()
    learn = learn[learn["variation"].isin(shared)].copy()

    val["validation_rmse_percentile"] = percentile_rank(val["rmse"], higher_is_better=False)
    learn["learning_rmse_percentile"] = percentile_rank(learn["rmse"], higher_is_better=False)
    val["validation_r2_percentile"] = percentile_rank(val["r2"], higher_is_better=True)
    learn["learning_r2_percentile"] = percentile_rank(learn["r2"], higher_is_better=True)
    val["validation_correlation_percentile"] = percentile_rank(val["correlation"], higher_is_better=True)
    learn["learning_correlation_percentile"] = percentile_rank(learn["correlation"], higher_is_better=True)
    val["validation_directional_accuracy_percentile"] = percentile_rank(
        val["directional_accuracy"], higher_is_better=True
    )
    learn["learning_directional_accuracy_percentile"] = percentile_rank(
        learn["directional_accuracy"], higher_is_better=True
    )

    merged = val[
        [
            "variation",
            "family",
            "mode",
            "input_group",
            "rmse",
            "r2",
            "correlation",
            "directional_accuracy",
            "validation_rmse_percentile",
            "validation_r2_percentile",
            "validation_correlation_percentile",
            "validation_directional_accuracy_percentile",
        ]
    ].merge(
        learn[
            [
                "variation",
                "rmse",
                "r2",
                "correlation",
                "directional_accuracy",
                "learning_rmse_percentile",
                "learning_r2_percentile",
                "learning_correlation_percentile",
                "learning_directional_accuracy_percentile",
            ]
        ],
        on="variation",
        how="inner",
        suffixes=("_validation", "_learning"),
    )

    robust_summary = pd.read_csv(robust_summary_path)[["variation", "mean_crosswave_rank"]]
    merged = merged.merge(robust_summary, on="variation", how="left")
    return merged.sort_values("mean_crosswave_rank")


def plot_elicitation(perf_df: pd.DataFrame, output_png: Path, output_pdf: Path) -> None:
    metrics = [
        ("rmse", "RMSE"),
        ("r2", "R^2"),
        ("correlation", "Correlation"),
        ("directional_accuracy", "Directional accuracy"),
    ]
    wave_order = ["validation", "learning"]

    sns.set_theme(style="whitegrid", font_scale=1.0)
    fig, axes = plt.subplots(len(wave_order), len(metrics), figsize=(18, 9), constrained_layout=True)

    x_positions = np.arange(len(MODE_ORDER))
    for row_idx, wave in enumerate(wave_order):
        wave_df = perf_df[perf_df["wave"] == wave].copy()
        for col_idx, (metric, title) in enumerate(metrics):
            ax = axes[row_idx, col_idx]
            for input_group in INPUT_ORDER:
                group_df = wave_df[wave_df["input_group"] == input_group]
                families = sorted(group_df["family"].unique())
                for family in families:
                    family_df = group_df[group_df["family"] == family].copy()
                    family_df["mode"] = pd.Categorical(family_df["mode"], MODE_ORDER, ordered=True)
                    family_df = family_df.sort_values("mode")
                    if family_df.empty:
                        continue
                    xs = [MODE_ORDER.index(mode) for mode in family_df["mode"]]
                    ax.plot(
                        xs,
                        family_df[metric],
                        color=INPUT_COLORS[input_group],
                        alpha=0.22 if input_group != "baseline" else 0.8,
                        linewidth=1.2 if input_group != "baseline" else 2.2,
                        marker="o",
                        markersize=3,
                    )
                median_df = (
                    group_df.groupby("mode", as_index=False)[metric]
                    .median()
                    .assign(mode=lambda frame: pd.Categorical(frame["mode"], MODE_ORDER, ordered=True))
                    .sort_values("mode")
                )
                if not median_df.empty:
                    ax.plot(
                        [MODE_ORDER.index(mode) for mode in median_df["mode"]],
                        median_df[metric],
                        color=INPUT_COLORS[input_group],
                        linewidth=3.0,
                        marker="o",
                        markersize=6,
                        label=INPUT_LABELS[input_group] if row_idx == 0 and col_idx == 0 else None,
                    )

            ax.set_xticks(x_positions)
            ax.set_xticklabels([MODE_LABELS[m] for m in MODE_ORDER], rotation=20, ha="right")
            ax.set_title(f"{wave}: {title}")
            if col_idx == 0:
                ax.set_ylabel("Value")
            if metric == "directional_accuracy":
                ax.set_ylim(0.3, 0.75)
            if metric == "correlation":
                ax.set_ylim(0.25, 0.82)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)

    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4, frameon=False)
    fig.suptitle("Sensitivity To Elicitation Strategy Across Waves", y=1.02, fontsize=18)
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    fig.savefig(output_pdf, bbox_inches="tight")
    plt.close(fig)


def plot_augmentation_heatmap(augment_df: pd.DataFrame, output_png: Path, output_pdf: Path) -> None:
    metrics = [
        ("median_delta_rmse", "Delta RMSE\n(negative is better)"),
        ("median_delta_r2", "Delta R^2"),
        ("median_delta_correlation", "Delta correlation"),
        ("median_delta_directional_accuracy", "Delta directional accuracy"),
    ]
    wave_order = ["validation", "learning"]
    row_labels = [INPUT_LABELS[g] for g in INPUT_ORDER if g != "baseline"]

    sns.set_theme(style="white", font_scale=1.0)
    fig, axes = plt.subplots(len(wave_order), len(metrics), figsize=(18, 8), constrained_layout=True)

    for col_idx, (metric, _) in enumerate(metrics):
        vmax = np.nanmax(np.abs(augment_df[metric].to_numpy(dtype=float)))
        vmax = float(vmax) if np.isfinite(vmax) and vmax > 0 else 1.0
        for row_idx, wave in enumerate(wave_order):
            ax = axes[row_idx, col_idx]
            subset = augment_df[
                (augment_df["wave"] == wave) & (augment_df["input_group"] != "baseline")
            ].copy()
            pivot = (
                subset.pivot(index="input_group", columns="mode", values=metric)
                .reindex(index=[g for g in INPUT_ORDER if g != "baseline"], columns=MODE_ORDER)
            )
            sns.heatmap(
                pivot,
                ax=ax,
                cmap="RdBu_r",
                center=0.0,
                vmin=-vmax,
                vmax=vmax,
                annot=True,
                fmt=".2f",
                cbar=col_idx == len(metrics) - 1,
                linewidths=0.5,
                linecolor="#e5e7eb",
                annot_kws={"fontsize": 9},
            )
            ax.set_title(f"{wave}: {metrics[col_idx][1]}")
            ax.set_xlabel("")
            ax.set_ylabel("" if col_idx else "augmentation group")
            ax.set_xticklabels([MODE_LABELS[m] for m in MODE_ORDER], rotation=20, ha="right")
            ax.set_yticklabels(row_labels, rotation=0)

    fig.suptitle("Augmentation Gain Vs Matched No-Input Baseline", y=1.02, fontsize=18)
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    fig.savefig(output_pdf, bbox_inches="tight")
    plt.close(fig)


def plot_robustness_scatter(robust_df: pd.DataFrame, output_png: Path, output_pdf: Path) -> None:
    plot_specs = [
        ("validation_rmse_percentile", "learning_rmse_percentile", "RMSE percentile"),
        ("r2_validation", "r2_learning", "R^2"),
        ("correlation_validation", "correlation_learning", "Correlation"),
        (
            "directional_accuracy_validation",
            "directional_accuracy_learning",
            "Directional accuracy",
        ),
    ]

    sns.set_theme(style="whitegrid", font_scale=1.0)
    fig, axes = plt.subplots(2, 2, figsize=(14, 12), constrained_layout=True)
    axes = axes.ravel()

    label_variants = robust_df.nsmallest(6, "mean_crosswave_rank")["variation"].tolist()
    for ax, (x_col, y_col, title) in zip(axes, plot_specs):
        if "percentile" in x_col:
            bounds = (0, 100)
        else:
            vals = pd.concat([robust_df[x_col], robust_df[y_col]], ignore_index=True)
            lo = float(vals.min())
            hi = float(vals.max())
            pad = 0.05 * (hi - lo if hi > lo else 1.0)
            bounds = (lo - pad, hi + pad)

        ax.plot(bounds, bounds, linestyle="--", linewidth=1.2, color="#6b7280")
        for input_group in ["both", "paper_only", "data_only"]:
            for mode in MODE_ORDER:
                subset = robust_df[
                    (robust_df["input_group"] == input_group) & (robust_df["mode"] == mode)
                ]
                if subset.empty:
                    continue
                ax.scatter(
                    subset[x_col],
                    subset[y_col],
                    color=INPUT_COLORS[input_group],
                    marker=MODE_MARKERS[mode],
                    s=70,
                    alpha=0.85,
                    edgecolor="white",
                    linewidth=0.6,
                    label=None,
                )

        if title == "R^2":
            for _, row in robust_df[robust_df["variation"].isin(label_variants)].iterrows():
                ax.annotate(
                    row["variation"],
                    (row[x_col], row[y_col]),
                    xytext=(4, 4),
                    textcoords="offset points",
                    fontsize=8,
                    color="#111827",
                )

        ax.set_title(f"Validation vs learning: {title}")
        ax.set_xlabel("validation")
        ax.set_ylabel("learning")
        ax.set_xlim(bounds)
        ax.set_ylim(bounds)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    legend_handles = []
    legend_labels = []
    for input_group in ["both", "paper_only", "data_only"]:
        handle = plt.Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label=INPUT_LABELS[input_group],
            markerfacecolor=INPUT_COLORS[input_group],
            markersize=8,
        )
        legend_handles.append(handle)
        legend_labels.append(INPUT_LABELS[input_group])
    for mode in MODE_ORDER:
        handle = plt.Line2D(
            [0],
            [0],
            marker=MODE_MARKERS[mode],
            color="#374151",
            label=MODE_LABELS[mode],
            linestyle="None",
            markersize=8,
        )
        legend_handles.append(handle)
        legend_labels.append(MODE_LABELS[mode])
    fig.legend(legend_handles, legend_labels, loc="lower center", ncol=4, frameon=False)
    fig.suptitle("Cross-Wave Robustness Of Augmented Variants", y=1.02, fontsize=18)
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    fig.savefig(output_pdf, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    ensure_plot_dir(PLOTS_DIR)
    paths = output_paths(args.output_prefix)

    perf_df = load_performance_table(args.validation_metrics, args.learning_with_baselines_metrics)
    perf_df.to_csv(paths["performance_table"], index=False)

    augment_df = build_augmentation_table(perf_df)
    augment_df.to_csv(paths["augment_table"], index=False)

    robust_df = build_robustness_table(
        args.robust_validation_metrics, args.robust_learning_metrics, args.robust_summary
    )
    robust_df.to_csv(paths["robustness_table"], index=False)

    plot_elicitation(perf_df, paths["elicitation_png"], paths["elicitation_pdf"])
    plot_augmentation_heatmap(augment_df, paths["augment_png"], paths["augment_pdf"])
    plot_robustness_scatter(robust_df, paths["robustness_png"], paths["robustness_pdf"])

    print(f"Wrote {paths['performance_table'].name}")
    print(f"Wrote {paths['augment_table'].name}")
    print(f"Wrote {paths['robustness_table'].name}")
    print(f"Wrote {paths['elicitation_png'].name}")
    print(f"Wrote {paths['augment_png'].name}")
    print(f"Wrote {paths['robustness_png'].name}")


if __name__ == "__main__":
    main()
