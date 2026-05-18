from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from prediction_metrics import _corr_np, _paired_delta_ci, _rmse_np
from prediction_metrics import _directional_accuracy_np as _da_np


ROOT = ANALYSIS_ROOT.parent
RESULTS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_rows.csv"
)
BASELINE_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_baseline_avg_predictions.csv"
)
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
LEARN_DF = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_learn.csv"
VAL_DF = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_repeat5"

MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-4.1 Nano": "#8c564b",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
}
MODEL_LAYOUT = [
    ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano"],
    ["GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"],
]
METRICS = ["correlation", "r2", "rmse"]
METRIC_LABELS = {
    "correlation": "Raw correlation",
    "r2": r"Raw $R^2$ vs learning-wave mean",
    "rmse": "Raw RMSE",
}
BETTER_HIGHER = {"correlation": True, "r2": True, "rmse": False}
FILE_STEMS = {
    "correlation": "validation_literature_collection_analysis_report_repeat5_correlation_by_model.png",
    "r2": "validation_literature_collection_analysis_report_repeat5_r2_by_model.png",
    "rmse": "validation_literature_collection_analysis_report_repeat5_rmse_by_model.png",
}
Q_COLS = [f"Q{i}" for i in range(1, 21)]


def _r2_np(pred: np.ndarray, truth: np.ndarray, learning_mean: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - learning_mean) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def load_truth_arrays() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    val = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    learn = pd.read_csv(LEARN_DF)
    truth = val["efficiency_p"].to_numpy(dtype=float) * 100.0
    control = val["efficiency_np"].to_numpy(dtype=float) * 100.0
    learning_mean = np.full_like(truth, float(learn["treatment_itt_efficiency"].mean() * 100.0))
    return truth, control, learning_mean


def load_enet_predictions() -> np.ndarray:
    df = pd.read_csv(VAL_DF).sort_values("CONFIG_configId")
    return df["elastic_prereg_pred"].to_numpy(dtype=float) * 100.0


def compute_enet_rows(
    baseline_avg: pd.DataFrame,
    truth: np.ndarray,
    control: np.ndarray,
    learning_mean: np.ndarray,
    *,
    n_boot: int = 5000,
    seed: int = 42,
) -> pd.DataFrame:
    enet_pred = load_enet_predictions()
    rows: list[dict[str, object]] = []
    rng = np.random.default_rng(seed)

    for _, base in baseline_avg.iterrows():
        model = str(base["model"])
        baseline_pred = pd.to_numeric(base[Q_COLS], errors="coerce").to_numpy(dtype=float)
        mask = ~np.isnan(enet_pred) & ~np.isnan(baseline_pred) & ~np.isnan(truth)

        baseline_rmse = _rmse_np(baseline_pred[mask], truth[mask])
        baseline_corr = _corr_np(baseline_pred[mask], truth[mask])
        baseline_r2 = _r2_np(baseline_pred[mask], truth[mask], learning_mean[mask])
        baseline_da = _da_np(baseline_pred[mask], truth[mask], control[mask])

        rmse = _rmse_np(enet_pred[mask], truth[mask])
        corr = _corr_np(enet_pred[mask], truth[mask])
        r2 = _r2_np(enet_pred[mask], truth[mask], learning_mean[mask])
        da = _da_np(enet_pred[mask], truth[mask], control[mask])

        metric_specs = {
            "rmse": (_rmse_np, truth, None, rmse),
            "correlation": (_corr_np, truth, None, corr),
            "r2": (_r2_np, truth, learning_mean, r2),
            "directional_accuracy": (_da_np, truth, control, da),
        }

        row: dict[str, object] = {
            "model": model,
            "variant_id": "benchmark_enet",
            "variant_kind": "benchmark_enet",
            "count": np.nan,
            "description": "Elastic net benchmark on the validation wave.",
            "report_path": "",
            "n_runs": np.nan,
            "baseline_variation": "baseline_joint_reasoning_avg5",
            "baseline_n": int(mask.sum()),
            "n": int(mask.sum()),
            "rmse": rmse,
            "correlation": corr,
            "r2": r2,
            "directional_accuracy": float(da),
        }

        for metric, (metric_fn, truth_arr, aux_arr, raw_value) in metric_specs.items():
            if metric == "rmse":
                base_value = float(baseline_rmse)
            elif metric == "correlation":
                base_value = float(baseline_corr)
            elif metric == "r2":
                base_value = float(baseline_r2)
            else:
                base_value = float(baseline_da)
            delta, lo, hi = _paired_delta_ci(
                metric_fn,
                enet_pred,
                baseline_pred,
                truth_arr,
                aux_arr,
                mask,
                rng,
                n_boot,
            )
            row[f"baseline_{metric}"] = base_value
            row[f"delta_{metric}"] = delta
            row[f"delta_{metric}_ci_low"] = lo
            row[f"delta_{metric}_ci_high"] = hi
            if BETTER_HIGHER.get(metric, True):
                row[f"improved_{metric}"] = float(raw_value) > base_value
                row[f"sig_improved_{metric}"] = float(lo) > 0.0
            else:
                row[f"improved_{metric}"] = float(raw_value) < base_value
                row[f"sig_improved_{metric}"] = float(hi) < 0.0
        rows.append(row)

    return pd.DataFrame(rows)


def variant_label(variant_id: str) -> str:
    if variant_id == "benchmark_enet":
        return "E-Net"
    if variant_id == "benchmark_pgg_ms":
        return "Benchmark (report)"
    if variant_id == "benchmark_pgg_ms_full":
        return "Benchmark (full)"
    if variant_id == "broad_all_2011":
        return "All"
    return variant_id.replace("leaf_", "")


def sort_variants(part: pd.DataFrame, metric: str) -> list[str]:
    ascending = not BETTER_HIGHER[metric]
    pinned = ["benchmark_enet", "benchmark_pgg_ms", "benchmark_pgg_ms_full"]
    present_pinned = [variant for variant in pinned if variant in set(part["variant_id"])]
    rest = part[~part["variant_id"].isin(present_pinned)].sort_values(metric, ascending=ascending)
    return [*present_pinned, *rest["variant_id"].tolist()]


def add_raw_ci_columns(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    out = df.copy()
    out[f"{metric}_ci_low_raw"] = out[f"baseline_{metric}"] + out[f"delta_{metric}_ci_low"]
    out[f"{metric}_ci_high_raw"] = out[f"baseline_{metric}"] + out[f"delta_{metric}_ci_high"]
    return out


def plot_metric(rows: pd.DataFrame, metric: str) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(18, 10.8), sharey=True)
    axes_flat = axes.flatten()

    y_candidates = np.concatenate(
        [
            rows[metric].to_numpy(dtype=float),
            rows[f"{metric}_ci_low_raw"].to_numpy(dtype=float),
            rows[f"{metric}_ci_high_raw"].to_numpy(dtype=float),
            rows[f"baseline_{metric}"].to_numpy(dtype=float),
        ]
    )
    y_candidates = y_candidates[np.isfinite(y_candidates)]
    pad = 0.03 if metric in {"correlation", "r2"} else 0.4
    y_min = float(y_candidates.min()) - pad
    y_max = float(y_candidates.max()) + pad

    for ax, model in zip(axes_flat, [m for row in MODEL_LAYOUT for m in row]):
        color = MODEL_COLORS[model]
        part = rows[rows["model"] == model].copy()
        ax.set_title(model, loc="left")
        ax.set_ylim(y_min, y_max)
        ax.grid(axis="y", alpha=0.18)
        ax.set_axisbelow(True)

        if part.empty:
            ax.set_xticks([])
            ax.text(0.5, 0.5, "Pending", transform=ax.transAxes, ha="center", va="center", color="0.45", fontsize=12)
            continue

        order = sort_variants(part, metric)
        part["variant_id"] = pd.Categorical(part["variant_id"], categories=order, ordered=True)
        part = part.sort_values("variant_id").reset_index(drop=True)

        finite_baselines = part[f"baseline_{metric}"].dropna().to_numpy(dtype=float)
        baseline = float(finite_baselines[0])
        ax.axhline(
            baseline,
            color="black",
            linestyle="--",
            linewidth=1.8,
            alpha=0.95,
            zorder=3,
        )

        for i, row in part.iterrows():
            variant_id = str(row["variant_id"])
            improved = bool(row[f"improved_{metric}"])
            significant = bool(row[f"sig_improved_{metric}"])
            low = float(row[f"{metric}_ci_low_raw"])
            high = float(row[f"{metric}_ci_high_raw"])
            raw = float(row[metric])

            if variant_id == "benchmark_enet":
                point_color = "#111111"
                marker = "s"
            elif variant_id == "benchmark_pgg_ms":
                point_color = "#ff8c42"
                marker = "D"
            elif variant_id == "benchmark_pgg_ms_full":
                point_color = "#7a3db8"
                marker = "^"
            else:
                point_color = color if improved else "#b0b0b0"
                marker = "o"

            yerr = np.array([[raw - low], [high - raw]], dtype=float)
            ax.errorbar(
                i,
                raw,
                yerr=yerr,
                fmt=marker,
                markersize=8.2 if variant_id in {"benchmark_enet", "benchmark_pgg_ms"} else 7.4,
                color=point_color,
                markerfacecolor=point_color,
                markeredgecolor="black" if significant else "white",
                markeredgewidth=1.2 if significant else 0.8,
                ecolor="0.35",
                elinewidth=1.4,
                capsize=4,
                capthick=1.2,
                zorder=4,
            )

        ax.set_xticks(np.arange(len(order)))
        ax.set_xticklabels([variant_label(v) for v in order], rotation=45, ha="right")
        ax.set_xlabel("Augmentation variant\n(E-Net pinned left; others sorted best to worst)")

    for row_axes in axes:
        row_axes[0].set_ylabel(METRIC_LABELS[metric])

    handles = [
        Line2D([], [], color="#111111", marker="s", linestyle="None", markersize=7, label="E-Net"),
        Line2D([], [], color="#ff8c42", marker="D", linestyle="None", markersize=7, label="Benchmark paper (report)"),
        Line2D([], [], color="#7a3db8", marker="^", linestyle="None", markersize=7, label="Benchmark paper (full)"),
        Line2D([], [], color="#2b8cbe", marker="o", linestyle="None", markersize=7, label="Improves baseline"),
        Line2D([], [], color="#b0b0b0", marker="o", linestyle="None", markersize=7, label="Does not improve baseline"),
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="white", markersize=7, label="Not significant"),
        Line2D([], [], color="black", marker="o", linestyle="None", markerfacecolor="black", markersize=7, label="Paired-bootstrap CI excludes 0"),
        Line2D([], [], color="0.35", linewidth=1.2, label="95% paired-bootstrap CI"),
        Line2D([], [], color="black", linestyle="--", linewidth=1.1, label="No-augmentation baseline"),
    ]

    title_label = {
        "correlation": "correlation",
        "r2": r"$R^2$",
        "rmse": "RMSE",
    }[metric]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 0.02))
    fig.suptitle(
        f"Repeat-5 collection-level augmentation on validation {title_label}\n"
        "Leaf labels encode A/B/C switches: A = exact/close on PGG and punishment relevance; "
        "B = payoff-like outcomes; C = empirical only",
        fontsize=14,
        y=0.98,
    )
    fig.text(
        0.5,
        0.06,
        "Points are raw metric values after averaging five runs. Error bars are paired-bootstrap 95% CIs for "
        "augmentation-minus-baseline, translated onto the raw metric scale. The dashed line is the matched five-run baseline.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.12, 1, 0.93])
    fig.savefig(PLOTS_DIR / FILE_STEMS[metric], dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = pd.read_csv(RESULTS_CSV)
    baseline_avg = pd.read_csv(BASELINE_AVG_CSV)
    truth, control, learning_mean = load_truth_arrays()

    enet_rows = compute_enet_rows(baseline_avg, truth, control, learning_mean)
    rows = pd.concat([rows, enet_rows], ignore_index=True, sort=False)

    for metric in METRICS:
        rows = add_raw_ci_columns(rows, metric)

    for metric in METRICS:
        plot_metric(rows, metric)


if __name__ == "__main__":
    main()
