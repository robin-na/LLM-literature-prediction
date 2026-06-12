from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from jsonl_parser import jsonl_to_dataframe
from noise_ceiling import compute_metrics as compute_noise_metrics
from noise_ceiling import load_pairs
from plot_paths import (
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (
    VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS as RESULTS,
)
from prediction_metrics import _directional_accuracy_np


ROOT = Path(__file__).resolve().parents[1]
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
DATA = ROOT / "science_data" / "data" / "processed_data"
Q_COLS = [f"Q{i}" for i in range(1, 21)]
MODES = ["single", "reasoning", "joint", "joint_reasoning"]
MODE_LABELS = {
    "single": "w/o explanation",
    "reasoning": "with explanation",
    "joint": "joint w/o explanation",
    "joint_reasoning": "joint with explanation",
}
MODEL_COLORS = {
    "GPT-3.5 Turbo": "#6c757d",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-4.1 Mini": "#1f77b4",
    "GPT-4o Mini": "#17becf",
    "GPT-4o": "#2ca02c",
    "o3": "#d62728",
    "o4-mini": "#9467bd",
    "GPT-4.1": "#ff7f0e",
    "GPT-5.1": "#bcbd22",
}
RAW_MODEL_SPECS = [
    {
        "model": "GPT-3.5 Turbo",
        "paths": {
            "single": ["prediction_positive_case_variants_single_35turbo.jsonl"],
            "reasoning": ["prediction_positive_case_variants_single_35turbo.jsonl"],
            "joint": ["prediction_positive_case_variants_joint_35turbo.jsonl"],
            "joint_reasoning": ["prediction_positive_case_variants_joint_35turbo.jsonl"],
        },
    },
    {
        "model": "GPT-4.1 Nano",
        "paths": {
            "single": ["prediction_crosswave_variations_41nano.jsonl"],
            "reasoning": ["prediction_crosswave_variations_41nano.jsonl"],
            "joint": ["prediction_crosswave_variations_41nano.jsonl"],
            "joint_reasoning": ["prediction_crosswave_variations_41nano.jsonl"],
        },
    },
    {
        "model": "GPT-4.1 Mini",
        "paths": {
            "single": ["prediction_crosswave_variations_41mini.jsonl"],
            "reasoning": ["prediction_crosswave_variations_41mini.jsonl"],
            "joint": ["prediction_crosswave_variations_41mini.jsonl"],
            "joint_reasoning": ["prediction_crosswave_variations_41mini.jsonl"],
        },
    },
    {
        "model": "GPT-4o Mini",
        "paths": {
            "single": ["prediction_positive_case_variants_single_4omini.jsonl"],
            "reasoning": ["prediction_positive_case_variants_single_4omini.jsonl"],
            "joint": ["prediction_positive_case_variants_joint_4omini.jsonl"],
            "joint_reasoning": ["prediction_positive_case_variants_joint_4omini.jsonl"],
        },
    },
    {
        "model": "GPT-4o",
        "paths": {
            "single": ["prediction_positive_case_variants_single_4o.jsonl"],
            "reasoning": ["prediction_positive_case_variants_single_4o.jsonl"],
            "joint": ["prediction_positive_case_variants_joint_4o.jsonl"],
            "joint_reasoning": ["prediction_positive_case_variants_joint_4o.jsonl"],
        },
    },
    {
        "model": "o3",
        "paths": {
            "single": [],
            "reasoning": ["prediction_positive_case_variants_single_o3.jsonl"],
            "joint": [],
            "joint_reasoning": ["prediction_positive_case_variants_joint_o3.jsonl"],
        },
    },
    {
        "model": "o4-mini",
        "paths": {
            "single": [],
            "reasoning": ["prediction_positive_case_variants_single_o4mini.jsonl"],
            "joint": [],
            "joint_reasoning": ["prediction_positive_case_variants_joint_o4mini.jsonl"],
        },
    },
    {
        "model": "GPT-4.1",
        "paths": {
            "single": ["prediction_positive_case_variations_41.jsonl", "prediction_baseline_41.jsonl"],
            "reasoning": ["prediction_positive_case_variations_41.jsonl"],
            "joint": ["prediction_positive_case_variations_41.jsonl"],
            "joint_reasoning": ["prediction_positive_case_variations_41.jsonl"],
        },
    },
    {
        "model": "GPT-5.1",
        "paths": {
            "single": ["prediction_positive_case_variants_single_gpt51.jsonl"],
            "reasoning": ["prediction_positive_case_variants_single_gpt51.jsonl"],
            "joint": ["prediction_positive_case_variants_joint_gpt51.jsonl"],
            "joint_reasoning": ["prediction_positive_case_variants_joint_gpt51.jsonl"],
        },
    },
]
BASELINE_ROWS = {
    "single": "baseline",
    "reasoning": "baseline_reasoning",
    "joint": "baseline_joint",
    "joint_reasoning": "baseline_joint_reasoning",
}
METRIC_SPECS = [
    {
        "metric": "rmse",
        "label": "RMSE",
        "baseline_stem": "validation_model_suite_baseline_rmse",
        "delta_stem": "validation_model_suite_mean_delta_rmse",
        "cbar": "Mean ΔRMSE vs matched baseline (lower is better)",
        "bench_col": "rmse",
    },
    {
        "metric": "correlation",
        "label": "Correlation",
        "baseline_stem": "validation_model_suite_baseline_correlation",
        "delta_stem": "validation_model_suite_mean_delta_correlation",
        "cbar": "Mean ΔCorrelation vs matched baseline (higher is better)",
        "bench_col": "correlation",
    },
    {
        "metric": "r2",
        "label": r"$R^2$ vs learning-wave mean",
        "baseline_stem": "validation_model_suite_baseline_r2",
        "delta_stem": "validation_model_suite_mean_delta_r2",
        "cbar": "Mean ΔR² vs matched baseline (higher is better)",
        "bench_col": "r2",
    },
    {
        "metric": "directional_accuracy",
        "label": "Directional Accuracy",
        "baseline_stem": "validation_model_suite_baseline_directional_accuracy",
        "delta_stem": "validation_model_suite_mean_delta_directional_accuracy",
        "cbar": "Mean ΔDirectional Accuracy vs matched baseline (higher is better)",
        "bench_col": "directional_accuracy",
    },
]


def _resolve_first_existing(candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = OPENAI_BATCH_OUTPUT / candidate
        if path.exists():
            return path
    return None


def _resolve_model_specs() -> list[dict[str, object]]:
    resolved: list[dict[str, object]] = []
    for spec in RAW_MODEL_SPECS:
        paths = {
            mode: _resolve_first_existing(candidates)
            for mode, candidates in spec["paths"].items()
        }
        resolved.append({"model": spec["model"], "paths": paths})
    return resolved


MODEL_SPECS = _resolve_model_specs()


def _parse_variation(variation: str) -> tuple[str, str]:
    if variation in BASELINE_ROWS.values():
        return "baseline", variation
    if variation.endswith("_joint_reasoning"):
        return variation[: -len("_joint_reasoning")], "joint_reasoning"
    if variation.endswith("_joint"):
        return variation[: -len("_joint")], "joint"
    if variation.endswith("_reasoning"):
        return variation[: -len("_reasoning")], "reasoning"
    return variation, "single"


def _rmse(pred: np.ndarray, truth: np.ndarray) -> float:
    return float(np.sqrt(np.mean((pred - truth) ** 2)))


def _corr(pred: np.ndarray, truth: np.ndarray) -> float:
    if np.std(pred) == 0 or np.std(truth) == 0:
        return float("nan")
    return float(np.corrcoef(pred, truth)[0, 1])


def _r2(pred: np.ndarray, truth: np.ndarray, train_mean: float) -> float:
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - train_mean) ** 2))
    return float(1.0 - mse / null_mse)


def _directional_accuracy(pred: np.ndarray, truth: np.ndarray, control: np.ndarray) -> float:
    return float(_directional_accuracy_np(pred, truth, control))


def _metrics(
    pred: np.ndarray,
    truth: np.ndarray,
    control: np.ndarray,
    train_mean: float,
) -> dict[str, float]:
    return {
        "rmse": _rmse(pred, truth),
        "correlation": _corr(pred, truth),
        "r2": _r2(pred, truth, train_mean),
        "directional_accuracy": _directional_accuracy(pred, truth, control),
    }


def _load_dataframe(path: Path, cache: dict[Path, pd.DataFrame]) -> pd.DataFrame:
    if path not in cache:
        cache[path] = jsonl_to_dataframe(path).reindex(columns=Q_COLS)
    return cache[path]


def load_truth_and_benchmarks() -> tuple[np.ndarray, np.ndarray, float, pd.DataFrame]:
    truth_df = pd.read_csv(ROOT / "input" / "pgg_CONFIGmerged_validation.csv").sort_values(
        "CONFIG_configId"
    )
    truth = truth_df["efficiency_p"].to_numpy(dtype=float) * 100.0
    control = truth_df["efficiency_np"].to_numpy(dtype=float) * 100.0

    learn = pd.read_csv(DATA / "df_paired_learn.csv")
    train_mean = float(learn["treatment_itt_efficiency"].mean() * 100.0)

    df_val = pd.read_csv(DATA / "df_paired_val.csv").sort_values("CONFIG_configId")
    enet_pred = df_val["elastic_prereg_pred"].to_numpy(dtype=float) * 100.0
    enet = _metrics(enet_pred, truth, control, train_mean)

    noise = compute_noise_metrics(load_pairs(str(DATA / "df_analysis_val.csv")))
    rmse_noise = float(noise["rmse_min_y"] * 100.0)
    corr_noise = float(noise["r_max_y"])
    null_mse = float(np.mean((truth - train_mean) ** 2))

    benchmarks = pd.DataFrame(
        [
            {
                "benchmark": "E-Net",
                "rmse": enet["rmse"],
                "correlation": enet["correlation"],
                "r2": enet["r2"],
                "directional_accuracy": enet["directional_accuracy"],
            },
            {
                "benchmark": "Noise ceiling",
                "rmse": rmse_noise,
                "correlation": corr_noise,
                "r2": float(1.0 - (rmse_noise**2) / null_mse),
                "directional_accuracy": np.nan,
            },
            {
                "benchmark": "Train mean baseline",
                "rmse": float(np.sqrt(null_mse)),
                "correlation": 0.0,
                "r2": 0.0,
                "directional_accuracy": _directional_accuracy(
                    np.full_like(truth, train_mean, dtype=float),
                    truth,
                    control,
                ),
            },
        ]
    )
    return truth, control, train_mean, benchmarks


def build_tables() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    truth, control, train_mean, benchmarks = load_truth_and_benchmarks()
    cache: dict[Path, pd.DataFrame] = {}
    baseline_rows: list[dict[str, object]] = []
    aug_rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        model = str(spec["model"])
        paths: dict[str, Path | None] = spec["paths"]  # type: ignore[assignment]
        baseline_metrics: dict[str, dict[str, float]] = {}

        for mode in MODES:
            path = paths.get(mode)
            if path is None:
                continue
            df = _load_dataframe(path, cache)
            row_name = BASELINE_ROWS[mode]
            if row_name not in df.index:
                continue
            pred = df.loc[row_name, Q_COLS].to_numpy(dtype=float)
            metrics = _metrics(pred, truth, control, train_mean)
            baseline_metrics[mode] = metrics
            baseline_rows.append(
                {
                    "model": model,
                    "mode": mode,
                    "path": str(path),
                    **metrics,
                }
            )

        for mode in MODES:
            path = paths.get(mode)
            if path is None or mode not in baseline_metrics:
                continue
            df = _load_dataframe(path, cache)
            for variation in df.index:
                variant_name, parsed_mode = _parse_variation(str(variation))
                if variant_name == "baseline" or parsed_mode != mode:
                    continue
                pred = df.loc[variation, Q_COLS].to_numpy(dtype=float)
                metrics = _metrics(pred, truth, control, train_mean)
                base = baseline_metrics[mode]
                aug_rows.append(
                    {
                        "model": model,
                        "mode": mode,
                        "variation": str(variation),
                        "variant_name": variant_name,
                        "path": str(path),
                        **metrics,
                        "baseline_rmse": base["rmse"],
                        "baseline_correlation": base["correlation"],
                        "baseline_r2": base["r2"],
                        "baseline_directional_accuracy": base["directional_accuracy"],
                        "delta_rmse": metrics["rmse"] - base["rmse"],
                        "delta_correlation": metrics["correlation"] - base["correlation"],
                        "delta_r2": metrics["r2"] - base["r2"],
                        "delta_directional_accuracy": metrics["directional_accuracy"] - base["directional_accuracy"],
                    }
                )

    baseline_df = pd.DataFrame(baseline_rows)
    aug_df = pd.DataFrame(aug_rows)

    summary_rows: list[dict[str, object]] = []
    for (model, mode), part in aug_df.groupby(["model", "mode"]):
        row: dict[str, object] = {
            "model": model,
            "mode": mode,
            "n_variants": int(len(part)),
            "baseline_rmse": float(part["baseline_rmse"].iloc[0]),
            "baseline_correlation": float(part["baseline_correlation"].iloc[0]),
            "baseline_r2": float(part["baseline_r2"].iloc[0]),
            "baseline_directional_accuracy": float(part["baseline_directional_accuracy"].iloc[0]),
            "mean_rmse": float(part["rmse"].mean()),
            "mean_correlation": float(part["correlation"].mean()),
            "mean_r2": float(part["r2"].mean()),
            "mean_directional_accuracy": float(part["directional_accuracy"].mean()),
            "mean_delta_rmse": float(part["delta_rmse"].mean()),
            "mean_delta_correlation": float(part["delta_correlation"].mean()),
            "mean_delta_r2": float(part["delta_r2"].mean()),
            "mean_delta_directional_accuracy": float(part["delta_directional_accuracy"].mean()),
            "share_better_rmse": float((part["delta_rmse"] < 0).mean()),
            "share_better_correlation": float((part["delta_correlation"] > 0).mean()),
            "share_better_r2": float((part["delta_r2"] > 0).mean()),
            "share_better_directional_accuracy": float((part["delta_directional_accuracy"] > 0).mean()),
        }
        best_rmse = part.loc[part["delta_rmse"].idxmin()]
        best_corr = part.loc[part["delta_correlation"].idxmax()]
        best_r2 = part.loc[part["delta_r2"].idxmax()]
        best_dir = part.loc[part["delta_directional_accuracy"].idxmax()]
        row.update(
            {
                "best_rmse_variant": best_rmse["variation"],
                "best_rmse": float(best_rmse["rmse"]),
                "best_delta_rmse": float(best_rmse["delta_rmse"]),
                "best_corr_variant": best_corr["variation"],
                "best_correlation": float(best_corr["correlation"]),
                "best_delta_correlation": float(best_corr["delta_correlation"]),
                "best_r2_variant": best_r2["variation"],
                "best_r2": float(best_r2["r2"]),
                "best_delta_r2": float(best_r2["delta_r2"]),
                "best_directional_accuracy_variant": best_dir["variation"],
                "best_directional_accuracy": float(best_dir["directional_accuracy"]),
                "best_delta_directional_accuracy": float(best_dir["delta_directional_accuracy"]),
            }
        )
        summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows)
    return baseline_df, aug_df, summary_df, benchmarks


def _ordered_models(df: pd.DataFrame) -> list[str]:
    available = set(df["model"])
    return [spec["model"] for spec in MODEL_SPECS if spec["model"] in available]


def _baseline_footer(benchmarks: pd.DataFrame, metric: str) -> str:
    order = ["E-Net", "Noise ceiling", "Train mean baseline"]
    parts = []
    for bench in order:
        value = float(benchmarks.loc[benchmarks["benchmark"] == bench, metric].iloc[0])
        if not np.isfinite(value):
            continue
        parts.append(f"{bench}: {value:.2f}")
    return " | ".join(parts)


def plot_baseline_heatmaps(baseline_df: pd.DataFrame, benchmarks: pd.DataFrame) -> None:
    models = _ordered_models(baseline_df)
    for spec in METRIC_SPECS:
        metric = spec["metric"]
        pivot = (
            baseline_df.pivot(index="model", columns="mode", values=metric)
            .reindex(index=models, columns=MODES)
        )
        labels = pivot.apply(lambda col: col.map(lambda x: "" if pd.isna(x) else f"{x:.2f}"))
        cmap = sns.color_palette("YlGnBu", as_cmap=True)
        cmap.set_bad("#f3f3f3")

        fig, ax = plt.subplots(figsize=(8.4, 5.6))
        sns.heatmap(
            pivot,
            ax=ax,
            cmap=cmap,
            annot=labels,
            fmt="",
            linewidths=0.5,
            cbar_kws={"label": spec["label"]},
            mask=pivot.isna(),
        )
        ax.set_xticklabels([MODE_LABELS[m] for m in MODES], rotation=0)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_title(f"Validation No-Augmentation Performance: {spec['label']}")
        fig.text(
            0.5,
            0.02,
            _baseline_footer(benchmarks, metric),
            ha="center",
            va="bottom",
            fontsize=9.5,
            color="0.3",
        )
        fig.tight_layout(rect=[0, 0.05, 1, 1])
        fig.savefig(PLOTS / f"{spec['baseline_stem']}.png", dpi=220, bbox_inches="tight")
        fig.savefig(PLOTS / f"{spec['baseline_stem']}.pdf", bbox_inches="tight")
        plt.close(fig)


def plot_mean_delta_heatmaps(summary_df: pd.DataFrame) -> None:
    models = _ordered_models(summary_df)
    cmap = sns.color_palette("RdBu_r", as_cmap=True)
    cmap.set_bad("#f3f3f3")

    for spec in METRIC_SPECS:
        metric = spec["metric"]
        delta_col = f"mean_delta_{metric}"
        share_col = (
            "share_better_rmse" if metric == "rmse" else f"share_better_{metric}"
        )
        pivot = (
            summary_df.pivot(index="model", columns="mode", values=delta_col)
            .reindex(index=models, columns=MODES)
        )
        share_pivot = (
            summary_df.pivot(index="model", columns="mode", values=share_col)
            .reindex(index=models, columns=MODES)
        )
        absmax = float(np.nanquantile(np.abs(pivot.to_numpy(dtype=float)), 0.95))
        absmax = 0.1 if absmax == 0 or np.isnan(absmax) else absmax
        labels = np.empty(pivot.shape, dtype=object)
        for i in range(pivot.shape[0]):
            for j in range(pivot.shape[1]):
                val = pivot.iloc[i, j]
                share = share_pivot.iloc[i, j]
                labels[i, j] = "" if pd.isna(val) else f"{val:.2f}\n({int(round(100*share))}%)"

        fig, ax = plt.subplots(figsize=(8.6, 5.8))
        sns.heatmap(
            pivot,
            ax=ax,
            cmap=cmap,
            center=0,
            vmin=-absmax,
            vmax=absmax,
            annot=labels,
            fmt="",
            annot_kws={"fontsize": 8, "linespacing": 0.9},
            linewidths=0.5,
            cbar_kws={"label": spec["cbar"]},
            mask=pivot.isna(),
        )
        ax.set_xticklabels([MODE_LABELS[m] for m in MODES], rotation=0)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_title(
            f"Validation Augmentation Summary: Mean Δ{spec['label']}\nCell labels show mean delta and share of variants improving."
        )
        fig.tight_layout()
        fig.savefig(PLOTS / f"{spec['delta_stem']}.png", dpi=220, bbox_inches="tight")
        fig.savefig(PLOTS / f"{spec['delta_stem']}.pdf", bbox_inches="tight")
        plt.close(fig)


def _fit_line(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    if len(x) < 2:
        return None
    slope, intercept = np.polyfit(x, y, 1)
    xs = np.linspace(float(np.min(x)), float(np.max(x)), 100)
    ys = slope * xs + intercept
    return xs, ys


def plot_convergence(summary_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(len(METRIC_SPECS), len(MODES), figsize=(16.6, 3.2 * len(METRIC_SPECS)), constrained_layout=False)
    if len(METRIC_SPECS) == 1:
        axes = np.asarray(axes).reshape(1, len(MODES))
    for row_idx, spec in enumerate(METRIC_SPECS):
        metric = spec["metric"]
        for col_idx, mode in enumerate(MODES):
            ax = axes[row_idx, col_idx]
            part = summary_df.loc[summary_df["mode"] == mode].copy()
            x = part[f"baseline_{metric}"].to_numpy(dtype=float)
            y = part[f"mean_delta_{metric}"].to_numpy(dtype=float)

            ax.axhline(0.0, color="0.65", linewidth=1.0, linestyle="--", zorder=0)
            if len(part) >= 2:
                corr = float(np.corrcoef(x, y)[0, 1])
                fit = _fit_line(x, y)
                if fit is not None:
                    xs, ys = fit
                    ax.plot(xs, ys, color="0.25", linewidth=1.3, zorder=1)
            else:
                corr = float("nan")

            for _, row in part.iterrows():
                ax.scatter(
                    row[f"baseline_{metric}"],
                    row[f"mean_delta_{metric}"],
                    s=70,
                    color=MODEL_COLORS.get(str(row["model"]), "#444444"),
                    edgecolors="white",
                    linewidths=0.8,
                    zorder=3,
                )
                ax.annotate(
                    str(row["model"]),
                    (row[f"baseline_{metric}"], row[f"mean_delta_{metric}"]),
                    xytext=(4, 4),
                    textcoords="offset points",
                    fontsize=7.8,
                    color="0.2",
                )

            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode])
            if col_idx == 0:
                direction = "lower is better" if metric == "rmse" else "higher is better"
                metric_name = spec["label"]
                ax.set_ylabel(f"Mean Δ{metric_name}\n({direction})")
            ax.set_xlabel(f"Baseline {spec['label']}")
            ax.grid(alpha=0.18, zorder=0)
            ax.text(
                0.03,
                0.95,
                f"$r = {corr:.2f}$",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9.5,
                bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none", "pad": 1.5},
            )

    fig.suptitle(
        "Validation Augmentation Convergence: Baseline Performance vs Mean Delta",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "Each point is one model. Deltas are relative to the matched no-augmentation baseline within the same elicitation mode.",
        ha="center",
        va="bottom",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(PLOTS / "validation_model_suite_convergence.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_model_suite_convergence.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_spread(summary_df: pd.DataFrame) -> None:
    rows: list[dict[str, object]] = []
    for inclusion, subset in [
        ("All models", summary_df.copy()),
        ("Excluding GPT-4.1 Nano", summary_df.loc[summary_df["model"] != "GPT-4.1 Nano"].copy()),
    ]:
        for metric in [spec["metric"] for spec in METRIC_SPECS]:
            for mode, part in subset.groupby("mode"):
                base = part[f"baseline_{metric}"].to_numpy(dtype=float)
                aug = part[f"mean_{metric}"].to_numpy(dtype=float)
                rows.append(
                    {
                        "inclusion": inclusion,
                        "metric": metric,
                        "mode": mode,
                        "baseline_std": float(np.std(base, ddof=0)),
                        "augmented_std": float(np.std(aug, ddof=0)),
                    }
                )
    spread = pd.DataFrame(rows)
    spread.to_csv(RESULTS / "validation_model_suite_spread_summary.csv", index=False)

    fig, axes = plt.subplots(2, len(METRIC_SPECS), figsize=(4.4 * len(METRIC_SPECS), 8.2), constrained_layout=False)
    if len(METRIC_SPECS) == 1:
        axes = np.asarray(axes).reshape(2, 1)
    mode_positions = {mode: 3 - i for i, mode in enumerate(MODES)}
    mode_colors = {
        "single": "#6c757d",
        "reasoning": "#2b8cbe",
        "joint": "#e6550d",
        "joint_reasoning": "#31a354",
    }
    for row_idx, inclusion in enumerate(["All models", "Excluding GPT-4.1 Nano"]):
        for col_idx, metric in enumerate([spec["metric"] for spec in METRIC_SPECS]):
            ax = axes[row_idx, col_idx]
            part = spread.loc[
                (spread["inclusion"] == inclusion) & (spread["metric"] == metric)
            ].copy()
            for _, row in part.iterrows():
                y = mode_positions[str(row["mode"])]
                x0 = float(row["baseline_std"])
                x1 = float(row["augmented_std"])
                ax.plot([x0, x1], [y, y], color="0.55", linewidth=2.0, zorder=1)
                ax.scatter(x0, y, s=68, color="white", edgecolors="0.35", linewidths=1.4, zorder=2)
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
                label = next(spec["label"] for spec in METRIC_SPECS if spec["metric"] == metric)
                ax.set_title(label)
            if col_idx == 0:
                ax.set_ylabel(inclusion)
            ax.set_yticks(list(mode_positions.values()))
            ax.set_yticklabels([MODE_LABELS[m] for m in MODES])
            ax.set_xlabel("Cross-model SD")
            ax.grid(axis="x", alpha=0.2, zorder=0)

    fig.suptitle(
        "Validation Model Suite: Cross-Model Spread Before vs After Augmentation",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.015,
        "White markers: no-augmentation baseline. Colored markers: mean augmented performance across report variants.",
        ha="center",
        va="bottom",
        fontsize=9.2,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.04, 1, 0.95])
    fig.savefig(PLOTS / "validation_model_suite_spread_before_after.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_model_suite_spread_before_after.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    baseline_df, aug_df, summary_df, benchmarks = build_tables()
    baseline_df.to_csv(RESULTS / "validation_model_suite_baselines.csv", index=False)
    aug_df.to_csv(RESULTS / "validation_model_suite_augmentation_rows.csv", index=False)
    summary_df.to_csv(RESULTS / "validation_model_suite_augmentation_summary.csv", index=False)
    benchmarks.to_csv(RESULTS / "validation_model_suite_benchmarks.csv", index=False)

    plot_baseline_heatmaps(baseline_df, benchmarks)
    plot_mean_delta_heatmaps(summary_df)
    plot_convergence(summary_df)
    plot_spread(summary_df)

    print(RESULTS / "validation_model_suite_baselines.csv")
    print(RESULTS / "validation_model_suite_augmentation_summary.csv")
    print(PLOTS / "validation_model_suite_convergence.png")


if __name__ == "__main__":
    main()
