from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "science_data" / "data" / "processed_data"
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"

sys.path.append(str(ROOT / "analysis"))
from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from noise_ceiling import compute_metrics as compute_noise_metrics  # noqa: E402
from noise_ceiling import load_pairs  # noqa: E402
from plot_paths import (  # noqa: E402
    VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_PLOTS as PLOTS,
)
from prediction_metrics import _directional_accuracy_np  # noqa: E402
from result_paths import (  # noqa: E402
    VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_RESULTS as RESULTS,
)


RAW_MODEL_SPECS = [
    {
        "model": "GPT-3.5 Turbo",
        "direct_candidates": ["prediction_positive_case_variants_single_35turbo.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_positive_case_variants_single_35turbo.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "direct_candidates": ["prediction_crosswave_variations_41nano.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_crosswave_variations_41nano.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "direct_candidates": ["prediction_crosswave_variations_41mini.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_crosswave_variations_41mini.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "GPT-4o",
        "direct_candidates": ["prediction_positive_case_variants_single_4o.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_positive_case_variants_single_4o.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "o4-mini",
        "direct_candidates": [],
        "direct_row": None,
        "reasoning_candidates": ["prediction_positive_case_variants_single_o4mini.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "o3",
        "direct_candidates": [],
        "direct_row": None,
        "reasoning_candidates": [
            "prediction_positive_case_variants_single_o3.jsonl",
            "prediction_positive_case_variants_single_reasoning_o3.jsonl",
        ],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1",
        "direct_candidates": ["prediction_baseline_41.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_positive_case_variations_41.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
    {
        "model": "GPT-5.1",
        "direct_candidates": ["prediction_positive_case_variants_single_gpt51.jsonl"],
        "direct_row": "baseline",
        "reasoning_candidates": ["prediction_positive_case_variants_single_gpt51.jsonl"],
        "reasoning_row": "baseline_reasoning",
    },
]


def _resolve_first_existing(candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = OPENAI_BATCH_OUTPUT / candidate
        if path.exists():
            return path
    return None


def _resolve_model_specs() -> tuple[list[dict[str, object]], list[str]]:
    resolved: list[dict[str, object]] = []
    skipped: list[str] = []
    for spec in RAW_MODEL_SPECS:
        direct_file = _resolve_first_existing(spec["direct_candidates"])
        reasoning_file = _resolve_first_existing(spec["reasoning_candidates"])
        if reasoning_file is None:
            skipped.append(str(spec["model"]))
            continue
        resolved.append(
            {
                "model": spec["model"],
                "direct_file": direct_file,
                "direct_row": spec["direct_row"],
                "reasoning_file": reasoning_file,
                "reasoning_row": spec["reasoning_row"],
            }
        )
    return resolved, skipped


MODEL_SPECS, SKIPPED_MODELS = _resolve_model_specs()

Q_COLS = [f"Q{i}" for i in range(1, 21)]
BAR_COLORS = {"direct": "#6c757d", "reasoning": "#2b8cbe"}
MODE_DISPLAY = {"direct": "w/o explanation", "reasoning": "with explanation"}
HUMAN_COLORS = {"Laypeople": "#fdae61", "Experts": "#1b9e77"}
LINE_COLORS = {
    "E-Net": "#111111",
    "Noise ceiling": "#31a354",
    "Train mean baseline": "#756bb1",
}
YLIMS = {
    "rmse": (0.0, 16.0),
    "correlation": (-0.75, 0.85),
    "r2": (-2.5, 0.75),
    "directional_accuracy": (0.0, 1.05),
}
YLABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$ vs learning-wave mean",
    "directional_accuracy": "Directional Accuracy",
}
OUTPUT_STEMS = {
    "rmse": "validation_no_augmentation_model_comparison_rmse",
    "correlation": "validation_no_augmentation_model_comparison_correlation",
    "r2": "validation_no_augmentation_model_comparison_r2",
    "directional_accuracy": "validation_no_augmentation_model_comparison_directional_accuracy",
}
SCATTER_STEM = "validation_no_augmentation_model_comparison_scatter"
BOOTSTRAP_SAMPLES = 5000
BOOTSTRAP_SEED = 42


def load_validation_truth() -> tuple[np.ndarray, np.ndarray]:
    df = pd.read_csv(ROOT / "input" / "pgg_CONFIGmerged_validation.csv").sort_values(
        "CONFIG_configId"
    )
    truth = df["efficiency_p"].to_numpy(dtype=float) * 100.0
    control = df["efficiency_np"].to_numpy(dtype=float) * 100.0
    return truth, control


def load_train_mean() -> float:
    df = pd.read_csv(DATA / "df_paired_learn.csv")
    return float(df["treatment_itt_efficiency"].mean() * 100.0)


def load_prediction_row(path: Path, row_name: str) -> np.ndarray:
    df = jsonl_to_dataframe(path)
    if row_name not in df.index:
        raise KeyError(f"Row '{row_name}' not found in {path}")
    return df.loc[row_name, Q_COLS].to_numpy(dtype=float)


def metric_values(
    pred: np.ndarray,
    truth: np.ndarray,
    control: np.ndarray,
    null_mse: float,
) -> dict[str, float]:
    mse = float(np.mean((pred - truth) ** 2))
    rmse = float(np.sqrt(mse))
    if np.std(pred) == 0 or np.std(truth) == 0:
        corr = float("nan")
    else:
        corr = float(np.corrcoef(pred, truth)[0, 1])
    r2 = float(1.0 - mse / null_mse)
    dir_acc = float(_directional_accuracy_np(pred, truth, control))
    return {
        "rmse": rmse,
        "correlation": corr,
        "r2": r2,
        "directional_accuracy": dir_acc,
    }


def bootstrap_metric_intervals(
    pred: np.ndarray,
    truth: np.ndarray,
    control: np.ndarray,
    train_mean: float,
    n_boot: int,
    seed: int,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    n = len(truth)
    idx = rng.integers(0, n, size=(n_boot, n))

    pred_s = pred[idx]
    truth_s = truth[idx]
    control_s = control[idx]

    mse = np.mean((pred_s - truth_s) ** 2, axis=1)
    rmse = np.sqrt(mse)

    pred_centered = pred_s - pred_s.mean(axis=1, keepdims=True)
    truth_centered = truth_s - truth_s.mean(axis=1, keepdims=True)
    cov = np.mean(pred_centered * truth_centered, axis=1)
    pred_std = pred_centered.std(axis=1)
    truth_std = truth_centered.std(axis=1)
    denom = pred_std * truth_std
    corr = np.divide(cov, denom, out=np.full_like(cov, np.nan), where=denom > 0)

    null_mse = np.mean((truth_s - train_mean) ** 2, axis=1)
    r2 = np.divide(
        mse,
        null_mse,
        out=np.full_like(mse, np.nan),
        where=null_mse > 0,
    )
    r2 = 1.0 - r2

    true_dir = np.sign(truth_s - control_s)
    pred_dir = np.sign(pred_s - control_s)
    dir_acc = np.mean(true_dir == pred_dir, axis=1)

    return {
        "rmse_lo": float(np.nanquantile(rmse, 0.025)),
        "rmse_hi": float(np.nanquantile(rmse, 0.975)),
        "correlation_lo": float(np.nanquantile(corr, 0.025)),
        "correlation_hi": float(np.nanquantile(corr, 0.975)),
        "r2_lo": float(np.nanquantile(r2, 0.025)),
        "r2_hi": float(np.nanquantile(r2, 0.975)),
        "directional_accuracy_lo": float(np.nanquantile(dir_acc, 0.025)),
        "directional_accuracy_hi": float(np.nanquantile(dir_acc, 0.975)),
    }


def build_model_metrics(
    truth: np.ndarray,
    control: np.ndarray,
    null_mse: float,
    train_mean: float,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    for spec in MODEL_SPECS:
        for mode, file_key, row_key in [
            ("direct", "direct_file", "direct_row"),
            ("reasoning", "reasoning_file", "reasoning_row"),
        ]:
            if spec[file_key] is None or spec[row_key] is None:
                metrics = {
                    "rmse": np.nan,
                    "correlation": np.nan,
                    "r2": np.nan,
                    "rmse_lo": np.nan,
                    "rmse_hi": np.nan,
                    "correlation_lo": np.nan,
                    "correlation_hi": np.nan,
                    "r2_lo": np.nan,
                    "r2_hi": np.nan,
                    "directional_accuracy": np.nan,
                    "directional_accuracy_lo": np.nan,
                    "directional_accuracy_hi": np.nan,
                }
            else:
                pred = load_prediction_row(spec[file_key], spec[row_key])
                metrics = metric_values(pred, truth, control, null_mse)
                metrics.update(
                    bootstrap_metric_intervals(
                        pred=pred,
                        truth=truth,
                        control=control,
                        train_mean=train_mean,
                        n_boot=BOOTSTRAP_SAMPLES,
                        seed=int(rng.integers(0, 2**32 - 1)),
                    )
                )
            rows.append({"model": spec["model"], "mode": mode, **metrics})
    return pd.DataFrame(rows)


def build_model_predictions() -> dict[tuple[str, str], np.ndarray]:
    preds: dict[tuple[str, str], np.ndarray | None] = {}
    for spec in MODEL_SPECS:
        if spec["direct_file"] is None or spec["direct_row"] is None:
            preds[(spec["model"], "direct")] = None
        else:
            preds[(spec["model"], "direct")] = load_prediction_row(
                spec["direct_file"], spec["direct_row"]
            )
        preds[(spec["model"], "reasoning")] = load_prediction_row(
            spec["reasoning_file"], spec["reasoning_row"]
        )
    return preds


def build_benchmarks(
    truth: np.ndarray,
    control: np.ndarray,
    null_mse: float,
    train_mean: float,
) -> pd.DataFrame:
    df_val = pd.read_csv(DATA / "df_paired_val.csv").sort_values("CONFIG_configId")
    enet_pred = df_val["elastic_prereg_pred"].to_numpy(dtype=float) * 100.0
    enet_metrics = metric_values(enet_pred, truth, control, null_mse)

    noise = compute_noise_metrics(load_pairs(str(DATA / "df_analysis_val.csv")))
    rmse_noise = float(noise["rmse_min_y"] * 100.0)
    corr_noise = float(noise["r_max_y"])
    r2_noise = float(1.0 - (rmse_noise**2) / null_mse)

    rmse_train = float(np.sqrt(null_mse))
    train_mean_pred = np.full_like(truth, train_mean, dtype=float)
    train_mean_da = float(_directional_accuracy_np(train_mean_pred, truth, control))

    return pd.DataFrame(
        [
            {
                "benchmark": "E-Net",
                "rmse": enet_metrics["rmse"],
                "correlation": enet_metrics["correlation"],
                "r2": enet_metrics["r2"],
                "directional_accuracy": enet_metrics["directional_accuracy"],
                "note": "Integrative experiments benchmark",
            },
            {
                "benchmark": "Noise ceiling",
                "rmse": rmse_noise,
                "correlation": corr_noise,
                "r2": r2_noise,
                "directional_accuracy": np.nan,
                "note": "RMSE noise floor / target-only correlation ceiling",
            },
            {
                "benchmark": "Train mean baseline",
                "rmse": rmse_train,
                "correlation": 0.0,
                "r2": 0.0,
                "directional_accuracy": train_mean_da,
                "note": f"Constant predictor at {train_mean:.2f}; correlation shown as 0 by convention",
            },
        ]
    )


def build_human_metrics(
    truth: np.ndarray,
    control: np.ndarray,
    null_mse: float,
) -> pd.DataFrame:
    df = pd.read_csv(DATA / "prediction_survey.csv").query(
        "prediction.between(-0.2, 1.2) and n_predictions_made == 20"
    )

    rows: list[dict[str, object]] = []
    for group_name, query in [
        ("Laypeople", "source == 'prolific'"),
        ("Experts", "source == 'sspp'"),
    ]:
        subset = df.query(query)
        for player_id, part in subset.groupby("playerID"):
            pred = (
                part.set_index("CONFIG_configId")
                .reindex(range(20))["prediction"]
                .to_numpy(dtype=float)
                * 100.0
            )
            if np.isnan(pred).any():
                continue
            metrics = metric_values(pred, truth, control, null_mse)
            rows.append({"group": group_name, "playerID": player_id, **metrics})
    return pd.DataFrame(rows)


def _add_human_scatter(
    ax: plt.Axes,
    human_metrics: pd.DataFrame,
    metric: str,
    n_models: int,
    y_limits: tuple[float, float],
) -> list:
    rng = np.random.default_rng(42)
    handles = []
    clipped_notes: list[str] = []

    for group_name in ["Laypeople", "Experts"]:
        part = human_metrics.loc[human_metrics["group"] == group_name].copy()
        x = rng.uniform(-0.35, n_models - 0.65, size=len(part))
        y = part[metric].to_numpy(dtype=float)
        clipped_low = int((y < y_limits[0]).sum())
        clipped_high = int((y > y_limits[1]).sum())
        y_plot = np.clip(y, y_limits[0], y_limits[1])

        alpha = 0.28 if group_name == "Laypeople" else 0.50
        size = 22 if group_name == "Laypeople" else 30
        handle = ax.scatter(
            x,
            y_plot,
            s=size,
            color=HUMAN_COLORS[group_name],
            alpha=alpha,
            edgecolors="none",
            zorder=1,
            label=group_name,
        )
        handles.append(handle)

        total_clipped = clipped_low + clipped_high
        if total_clipped:
            clipped_notes.append(f"{group_name}: {total_clipped} clipped")

    if clipped_notes:
        ax.text(
            0.01,
            0.01,
            "; ".join(clipped_notes),
            transform=ax.transAxes,
            fontsize=8,
            color="0.45",
            ha="left",
            va="bottom",
        )
    return handles


def _add_error_bars(
    ax: plt.Axes,
    bars,
    values: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray,
) -> None:
    for bar, value, lo, hi in zip(bars, values, lower, upper):
        if not (np.isfinite(value) and np.isfinite(lo) and np.isfinite(hi)):
            continue
        x = bar.get_x() + bar.get_width() / 2
        yerr = np.array([[max(0.0, value - lo)], [max(0.0, hi - value)]])
        ax.errorbar(
            x,
            value,
            yerr=yerr,
            fmt="none",
            ecolor="0.15",
            elinewidth=1.2,
            capsize=3,
            capthick=1.2,
            zorder=4,
        )


def _add_bar_labels(
    ax: plt.Axes,
    bars,
    values: np.ndarray,
    metric: str,
    upper: np.ndarray | None = None,
) -> None:
    y_min, y_max = YLIMS[metric]
    y_span = y_max - y_min
    if upper is None:
        upper = np.zeros_like(values, dtype=float)
    for bar, value, hi in zip(bars, values, upper):
        if not np.isfinite(value):
            continue
        x = bar.get_x() + bar.get_width() / 2
        offset = 0.02 * y_span
        top = max(value, value + (hi - value if np.isfinite(hi) else 0.0))
        y = min(top + offset, y_max - 0.03 * y_span)
        ax.text(
            x,
            y,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=8.5,
            color="0.15",
            zorder=5,
        )


def plot_scatter_grid(
    truth: np.ndarray,
    train_mean: float,
    model_metrics: pd.DataFrame,
    model_predictions: dict[tuple[str, str], np.ndarray | None],
) -> None:
    x_min = min(60.0, float(np.floor(min(truth.min(), train_mean) / 5) * 5))
    x_max = max(100.0, float(np.ceil(max(truth.max(), train_mean) / 5) * 5))
    x_grid = np.linspace(x_min, x_max, 400)

    fig, axes = plt.subplots(
        2,
        len(MODEL_SPECS),
        figsize=(max(19.5, 2.35 * len(MODEL_SPECS)), 7),
        sharex=True,
        sharey=True,
    )
    fig.supxlabel("True Efficiency")
    fig.supylabel("Predicted Efficiency")

    for col_idx, spec in enumerate(MODEL_SPECS):
        for row_idx, mode in enumerate(["direct", "reasoning"]):
            ax = axes[row_idx, col_idx]
            pred = model_predictions[(spec["model"], mode)]
            metrics_row = model_metrics.loc[
                (model_metrics["model"] == spec["model"])
                & (model_metrics["mode"] == mode)
            ].iloc[0]

            if pred is None:
                ax.set_xlim(x_min, x_max)
                ax.set_ylim(x_min, x_max)
                ax.grid(alpha=0.18, zorder=0)
                if row_idx == 0:
                    ax.set_title(spec["model"])
                ax.text(
                    0.05,
                    0.93,
                    MODE_DISPLAY["direct"],
                    transform=ax.transAxes,
                    fontsize=10,
                    fontweight="bold",
                    ha="left",
                    va="top",
                )
                ax.text(
                    0.5,
                    0.5,
                    "Not run",
                    transform=ax.transAxes,
                    fontsize=14,
                    color="0.45",
                    ha="center",
                    va="center",
                )
                continue

            ax.scatter(
                truth,
                pred,
                s=72,
                color=BAR_COLORS[mode],
                alpha=0.78,
                edgecolors="white",
                linewidths=0.8,
                zorder=3,
            )
            ax.plot(x_grid, x_grid, color="black", linewidth=1.8, zorder=2)
            ax.axhline(
                train_mean,
                color="0.45",
                linestyle="--",
                linewidth=1.4,
                zorder=1,
            )
            ax.fill_between(
                x_grid,
                x_grid,
                train_mean,
                color="#9bd35a",
                alpha=0.22,
                zorder=0,
            )

            ax.set_xlim(x_min, x_max)
            ax.set_ylim(x_min, x_max)
            ax.grid(alpha=0.18, zorder=0)

            if row_idx == 0:
                ax.set_title(spec["model"])
            ax.text(
                0.05,
                0.93,
                MODE_DISPLAY[mode],
                transform=ax.transAxes,
                fontsize=10,
                fontweight="bold",
                ha="left",
                va="top",
            )
            ax.text(
                0.56,
                0.10,
                (
                    f"$R^2 = {metrics_row['r2']:.2f}$\n"
                    f"$RMSE = {metrics_row['rmse']:.2f}$\n"
                    f"$r = {metrics_row['correlation']:.2f}$\n"
                    f"$DA = {metrics_row['directional_accuracy']:.2f}$"
                ),
                transform=ax.transAxes,
                fontsize=10,
                ha="left",
                va="bottom",
                bbox={"facecolor": "white", "alpha": 0.65, "edgecolor": "none", "pad": 1.5},
            )

    fig.suptitle("Validation No-Augmentation: Predicted vs True Efficiency", y=0.98)
    fig.tight_layout(rect=[0.03, 0.03, 1, 0.95])
    fig.savefig(PLOTS / f"{SCATTER_STEM}.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / f"{SCATTER_STEM}.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_metric(
    metric: str,
    model_metrics: pd.DataFrame,
    benchmarks: pd.DataFrame,
    human_metrics: pd.DataFrame,
) -> None:
    fig, ax = plt.subplots(figsize=(max(12.0, 1.45 * len(MODEL_SPECS) + 2.5), 5.8))
    y_limits = YLIMS[metric]
    n_models = len(MODEL_SPECS)

    human_handles = _add_human_scatter(
        ax=ax,
        human_metrics=human_metrics,
        metric=metric,
        n_models=n_models,
        y_limits=y_limits,
    )

    x = np.arange(n_models)
    width = 0.34

    base_order = [spec["model"] for spec in MODEL_SPECS]
    reasoning_order = (
        model_metrics.query("mode == 'reasoning'")
        .set_index("model")
        .loc[base_order, metric]
    )
    ordered_models = (
        reasoning_order.sort_values(
            ascending=(metric == "rmse"),
            kind="mergesort",
            na_position="last",
        )
        .index.tolist()
    )
    direct = (
        model_metrics.query("mode == 'direct'")
        .set_index("model")
        .loc[ordered_models, metric]
        .to_numpy(dtype=float)
    )
    reasoning = (
        model_metrics.query("mode == 'reasoning'")
        .set_index("model")
        .loc[ordered_models, metric]
        .to_numpy(dtype=float)
    )
    direct_lo = (
        model_metrics.query("mode == 'direct'")
        .set_index("model")
        .loc[ordered_models, f"{metric}_lo"]
        .to_numpy(dtype=float)
    )
    direct_hi = (
        model_metrics.query("mode == 'direct'")
        .set_index("model")
        .loc[ordered_models, f"{metric}_hi"]
        .to_numpy(dtype=float)
    )
    reasoning_lo = (
        model_metrics.query("mode == 'reasoning'")
        .set_index("model")
        .loc[ordered_models, f"{metric}_lo"]
        .to_numpy(dtype=float)
    )
    reasoning_hi = (
        model_metrics.query("mode == 'reasoning'")
        .set_index("model")
        .loc[ordered_models, f"{metric}_hi"]
        .to_numpy(dtype=float)
    )

    direct_bars = ax.bar(
        x - width / 2,
        direct,
        width=width,
        color=BAR_COLORS["direct"],
        alpha=0.95,
        label=MODE_DISPLAY["direct"],
        zorder=3,
    )
    reasoning_bars = ax.bar(
        x + width / 2,
        reasoning,
        width=width,
        color=BAR_COLORS["reasoning"],
        alpha=0.95,
        label=MODE_DISPLAY["reasoning"],
        zorder=3,
    )

    line_handles = []
    line_labels = []
    for benchmark_name in ["E-Net", "Noise ceiling", "Train mean baseline"]:
        value = float(
            benchmarks.loc[benchmarks["benchmark"] == benchmark_name, metric].iloc[0]
        )
        if not np.isfinite(value):
            continue
        linestyle = {
            "E-Net": "-",
            "Noise ceiling": "--",
            "Train mean baseline": ":",
        }[benchmark_name]
        handle = ax.axhline(
            value,
            color=LINE_COLORS[benchmark_name],
            linestyle=linestyle,
            linewidth=1.8,
            alpha=0.95,
            zorder=2,
            label=benchmark_name,
        )
        line_handles.append(handle)
        line_labels.append(f"{benchmark_name}: {value:.2f}")

    _add_error_bars(ax, direct_bars, direct, direct_lo, direct_hi)
    _add_error_bars(ax, reasoning_bars, reasoning, reasoning_lo, reasoning_hi)

    _add_bar_labels(ax, direct_bars, direct, metric, upper=direct_hi)
    _add_bar_labels(ax, reasoning_bars, reasoning, metric, upper=reasoning_hi)

    ax.set_xticks(x)
    ax.set_xticklabels(ordered_models)
    ax.set_ylabel(YLABELS[metric])
    ax.set_title(f"Validation No-Augmentation Comparison: {YLABELS[metric]}")
    ax.set_ylim(*y_limits)
    ax.set_xlim(-0.6, n_models - 0.25)
    ax.grid(axis="y", alpha=0.25, zorder=0)

    legend_handles = [direct_bars[0], reasoning_bars[0], *line_handles, *human_handles]
    legend_labels = [
        MODE_DISPLAY["direct"],
        MODE_DISPLAY["reasoning"],
        *line_labels,
        "Laypeople",
        "Experts",
    ]
    if metric in {"correlation", "r2"}:
        ax.legend(
            legend_handles,
            legend_labels,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.12),
            frameon=False,
            ncol=3,
        )
        fig.tight_layout(rect=[0, 0.08, 1, 1])
    else:
        ax.legend(
            legend_handles,
            legend_labels,
            loc="upper left",
            frameon=False,
            ncol=2,
        )
        fig.tight_layout()

    stem = OUTPUT_STEMS[metric]
    fig.savefig(PLOTS / f"{stem}.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    PLOTS.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)

    truth, control = load_validation_truth()
    train_mean = load_train_mean()
    null_mse = float(np.mean((truth - train_mean) ** 2))

    model_metrics = build_model_metrics(truth, control, null_mse, train_mean)
    model_predictions = build_model_predictions()
    benchmarks = build_benchmarks(truth, control, null_mse, train_mean)
    human_metrics = build_human_metrics(truth, control, null_mse)

    model_metrics.to_csv(
        RESULTS / "validation_no_augmentation_model_comparison_metrics.csv",
        index=False,
    )
    benchmarks.to_csv(
        RESULTS / "validation_no_augmentation_model_comparison_benchmarks.csv",
        index=False,
    )
    human_metrics.to_csv(
        RESULTS / "validation_no_augmentation_model_comparison_humans.csv",
        index=False,
    )

    for metric in ["rmse", "correlation", "r2", "directional_accuracy"]:
        plot_metric(metric, model_metrics, benchmarks, human_metrics)
    plot_scatter_grid(truth, train_mean, model_metrics, model_predictions)
    if SKIPPED_MODELS:
        print("Skipped models with no matching output file:", ", ".join(SKIPPED_MODELS))


if __name__ == "__main__":
    main()
