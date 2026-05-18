from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe
from literature_analysis_report_sources.analyze_validation_analysis_report_sources import (
    LOWER_IS_BETTER,
    METRIC_LABELS,
    Q_COLS,
    compute_metrics,
    load_truth,
)


ROOT = ANALYSIS_ROOT.parent
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_extended2012"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_analysis_report_sources_extended2012"

PGG_MS_ID = "PGG_MS_202502"
BENCHMARK_LABEL = "Benchmark paper"
DEFAULT_METRIC = "correlation"
DEFAULT_N_BOOT = 2000

MODEL_SPECS = [
    {
        "model": "GPT-4.1",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "strict_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
        "remaining_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_broad_remaining1769_joint_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
]

METRIC_ORDER = ["correlation", "rmse", "directional_accuracy", "r2"]
NATURAL_BOUNDS = {
    "correlation": (-1.0, 1.0),
    "directional_accuracy": (0.0, 1.0),
    "r2": (-1.0, 1.0),
}


def merge_frames(strict_path: Path, remaining_path: Path) -> pd.DataFrame:
    strict = jsonl_to_dataframe(strict_path)
    remaining = jsonl_to_dataframe(remaining_path)
    merged = pd.concat([strict, remaining], axis=0)
    return merged[~merged.index.duplicated(keep="first")]


def extract_source_id(variation: str) -> str:
    if "/" in variation:
        return variation.split("/", 1)[1]
    return variation


def _corr_rows(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    a_center = a - a.mean(axis=1, keepdims=True)
    b_center = b - b.mean(axis=1, keepdims=True)
    denom = np.sqrt((a_center**2).sum(axis=1) * (b_center**2).sum(axis=1))
    out = np.full(a.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (a_center[valid] * b_center[valid]).sum(axis=1) / denom[valid]
    return out


def bootstrap_metric_ci(
    metric: str,
    pred: np.ndarray,
    truth: np.ndarray,
    control: np.ndarray,
    boot_idx: np.ndarray,
) -> tuple[float, float]:
    pred_boot = pred[boot_idx]
    truth_boot = truth[boot_idx]
    control_boot = control[boot_idx]

    if metric == "correlation":
        vals = _corr_rows(pred_boot, truth_boot)
    elif metric == "rmse":
        vals = np.sqrt(np.mean((pred_boot - truth_boot) ** 2, axis=1))
    elif metric == "r2":
        mse = np.mean((pred_boot - truth_boot) ** 2, axis=1)
        null_mse = np.mean((truth_boot - control_boot) ** 2, axis=1)
        vals = np.full(len(mse), np.nan, dtype=float)
        valid = null_mse > 0
        vals[valid] = 1.0 - mse[valid] / null_mse[valid]
    elif metric == "directional_accuracy":
        pred_dir = pred_boot - control_boot
        truth_dir = truth_boot - control_boot
        vals = np.mean(np.sign(pred_dir) == np.sign(truth_dir), axis=1)
    else:
        raise ValueError(f"Unsupported metric for bootstrap CI: {metric}")

    vals = vals[np.isfinite(vals)]
    if vals.size == 0:
        return float("nan"), float("nan")
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return float(lo), float(hi)


def build_model_rows(metric: str, n_boot: int = DEFAULT_N_BOOT, seed: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    treatment, control = load_truth()
    truth_arr = treatment.reindex(Q_COLS).to_numpy(dtype=float)
    control_arr = control.reindex(Q_COLS).to_numpy(dtype=float)
    rng = np.random.default_rng(seed)
    boot_idx = rng.integers(0, len(Q_COLS), size=(n_boot, len(Q_COLS)))
    model_rows: list[dict[str, object]] = []
    baseline_rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        base_df = jsonl_to_dataframe(spec["baseline_path"]).reindex(columns=Q_COLS)
        baseline_metrics = compute_metrics(base_df.loc[spec["baseline_variation"]], treatment, control)
        baseline_value = float(baseline_metrics[metric])
        baseline_pred = pd.to_numeric(base_df.loc[spec["baseline_variation"]], errors="coerce").reindex(Q_COLS).to_numpy(dtype=float)
        baseline_ci_low, baseline_ci_high = bootstrap_metric_ci(
            metric,
            baseline_pred,
            truth_arr,
            control_arr,
            boot_idx,
        )
        baseline_rows.append(
            {
                "model": spec["model"],
                "metric": metric,
                "baseline_value": baseline_value,
                "baseline_ci_low": baseline_ci_low,
                "baseline_ci_high": baseline_ci_high,
            }
        )

        if not spec["strict_path"].exists() or not spec["remaining_path"].exists():
            continue

        pred_df = merge_frames(spec["strict_path"], spec["remaining_path"]).reindex(columns=Q_COLS)
        for variation, pred_row in pred_df.iterrows():
            source_id = extract_source_id(str(variation))
            metrics = compute_metrics(pred_row, treatment, control)
            raw_value = float(metrics[metric])
            pred_arr = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS).to_numpy(dtype=float)
            ci_low, ci_high = bootstrap_metric_ci(
                metric,
                pred_arr,
                truth_arr,
                control_arr,
                boot_idx,
            )
            improved = raw_value < baseline_value if metric in LOWER_IS_BETTER else raw_value > baseline_value
            model_rows.append(
                {
                    "model": spec["model"],
                    "source_id": source_id,
                    "metric": metric,
                    "raw_value": raw_value,
                    "ci_low": ci_low,
                    "ci_high": ci_high,
                    "baseline_value": baseline_value,
                    "improved": improved,
                    "is_benchmark": source_id == PGG_MS_ID,
                }
            )

    rows = pd.DataFrame(model_rows)
    baselines = pd.DataFrame(baseline_rows)
    return rows, baselines


def add_ranks(rows: pd.DataFrame, metric: str) -> pd.DataFrame:
    if rows.empty:
        return rows
    ascending = metric in LOWER_IS_BETTER
    ranked_parts: list[pd.DataFrame] = []
    for model, part in rows.groupby("model", dropna=False):
        ranked = part.sort_values(["raw_value", "source_id"], ascending=[ascending, True]).reset_index(drop=True)
        ranked["rank"] = np.arange(1, len(ranked) + 1)
        ranked_parts.append(ranked)
    return pd.concat(ranked_parts, ignore_index=True)


def choose_ylim(rows: pd.DataFrame, baselines: pd.DataFrame, metric: str) -> tuple[float, float]:
    values: list[float] = []
    if not rows.empty:
        values.extend(rows["raw_value"].dropna().astype(float).tolist())
    if not baselines.empty:
        values.extend(baselines["baseline_value"].dropna().astype(float).tolist())

    if not values:
        return NATURAL_BOUNDS.get(metric, (0.0, 1.0))

    lo = min(values)
    hi = max(values)
    span = hi - lo
    pad = max(0.03, span * 0.08)
    lo -= pad
    hi += pad

    if metric in NATURAL_BOUNDS:
        nat_lo, nat_hi = NATURAL_BOUNDS[metric]
        lo = max(lo, nat_lo)
        hi = min(hi, nat_hi)
    return lo, hi


def plot_ranked_levels(metric: str = DEFAULT_METRIC) -> tuple[Path, Path, Path]:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    matplotlib.rcParams["font.family"] = "Arial"
    matplotlib.rcParams["font.size"] = 12

    rows, baselines = build_model_rows(metric)
    ranked = add_ranks(rows, metric)
    y_limits = choose_ylim(ranked, baselines, metric)
    max_rank = int(ranked["rank"].max()) if not ranked.empty else 2012

    figure_rows: list[dict[str, object]] = []
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), sharey=True, constrained_layout=False)

    for ax, spec in zip(axes, MODEL_SPECS):
        model = spec["model"]
        baseline_value = float(baselines.loc[baselines["model"] == model, "baseline_value"].iloc[0])
        part = ranked.loc[ranked["model"] == model].copy()

        if not part.empty:
            improved = part.loc[part["improved"]]
            not_improved = part.loc[~part["improved"]]

            ax.scatter(
                not_improved["rank"],
                not_improved["raw_value"],
                s=10,
                color="#bdbdbd",
                alpha=0.55,
                linewidths=0,
                zorder=2,
            )
            ax.scatter(
                improved["rank"],
                improved["raw_value"],
                s=10,
                color="#2ca25f",
                alpha=0.75,
                linewidths=0,
                zorder=3,
            )

            benchmark = part.loc[part["is_benchmark"]]
            if not benchmark.empty:
                bench_row = benchmark.iloc[0]
                ax.axvline(
                    float(bench_row["rank"]),
                    color="black",
                    linestyle="--",
                    linewidth=1.2,
                    alpha=0.9,
                    zorder=1,
                )
                bench_yerr = np.array(
                    [
                        [float(bench_row["raw_value"]) - float(bench_row["ci_low"])],
                        [float(bench_row["ci_high"]) - float(bench_row["raw_value"])],
                    ]
                )
                ax.errorbar(
                    [bench_row["rank"]],
                    [bench_row["raw_value"]],
                    yerr=bench_yerr,
                    fmt="none",
                    ecolor="#f28e2b",
                    elinewidth=1.2,
                    alpha=0.95,
                    capsize=0,
                    zorder=3.8,
                )
                ax.scatter(
                    [bench_row["rank"]],
                    [bench_row["raw_value"]],
                    s=58,
                    color="#f28e2b",
                    marker="D",
                    edgecolors="white",
                    linewidths=0.8,
                    zorder=4,
                )
                benchmark_rank = int(bench_row["rank"])
            else:
                benchmark_rank = None

            share_improved = float(part["improved"].mean())
            summary_text = [
                f"n = {len(part)}",
                f"{100 * share_improved:.0f}% above baseline",
            ]
            if benchmark_rank is not None:
                summary_text.append(f"Benchmark rank = {benchmark_rank}")
            ax.text(
                0.02,
                0.98,
                "\n".join(summary_text),
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9,
                color="0.25",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.75, "pad": 2.5},
            )

            for _, row in part.iterrows():
                figure_rows.append(
                    {
                        "model": model,
                        "source_id": row["source_id"],
                        "metric": metric,
                        "raw_value": row["raw_value"],
                        "baseline_value": row["baseline_value"],
                        "rank": int(row["rank"]),
                        "improved": bool(row["improved"]),
                        "is_benchmark": bool(row["is_benchmark"]),
                    }
                )

            ax.set_xticks([1, max_rank])
        else:
            ax.text(
                0.5,
                0.55,
                "Augmented outputs pending",
                transform=ax.transAxes,
                ha="center",
                va="center",
                fontsize=11,
                color="0.45",
            )
            ax.text(
                0.5,
                0.44,
                f"Baseline = {baseline_value:.3f}",
                transform=ax.transAxes,
                ha="center",
                va="center",
                fontsize=10,
                color="0.35",
            )
            ax.set_xticks([1, max_rank])

        baseline_row = baselines.loc[baselines["model"] == model].iloc[0]
        ax.axhspan(
            float(baseline_row["baseline_ci_low"]),
            float(baseline_row["baseline_ci_high"]),
            color="black",
            alpha=0.08,
            zorder=0.5,
        )
        ax.axhline(baseline_value, color="black", linewidth=1.3, zorder=1)
        ax.set_xlim(0.5, max_rank + 0.5)
        ax.set_ylim(*y_limits)
        ax.set_title(model)
        ax.set_xlabel("Augmented source rank\n(best to worst)")
        ax.grid(axis="y", alpha=0.18)
        ax.set_axisbelow(True)

    axes[0].set_ylabel(f"Raw {METRIC_LABELS[metric]}")

    handles = [
        Line2D([], [], color="#2ca25f", marker="o", linestyle="None", markersize=5, label="Above baseline"),
        Line2D([], [], color="#bdbdbd", marker="o", linestyle="None", markersize=5, label="At or below baseline"),
        Line2D([], [], color="black", linewidth=1.3, label="No augmentation baseline"),
        Line2D([], [], color="black", linewidth=6, alpha=0.08, label="Baseline 95% CI"),
        Line2D([], [], color="black", linestyle="--", linewidth=1.2, label=BENCHMARK_LABEL + " rank"),
        Line2D([], [], color="#f28e2b", marker="D", linestyle="None", markersize=6, label=BENCHMARK_LABEL),
        Line2D([], [], color="#f28e2b", linewidth=1.2, label=BENCHMARK_LABEL + " 95% CI"),
    ]
    fig.legend(handles=handles, loc="lower left", ncol=3, frameon=False, bbox_to_anchor=(0.02, 0.01))
    fig.suptitle(
        f"Ranked raw {METRIC_LABELS[metric]} across paper augmentations\nExtended 2012-paper pool, joint reasoning",
        fontsize=15,
        y=0.98,
    )
    fig.tight_layout(rect=[0.02, 0.13, 1, 0.90])

    stem = f"validation_literature_analysis_report_source_ranked_{metric}"
    png_path = PLOTS_DIR / f"{stem}.png"
    csv_path = RESULTS_DIR / f"{stem}.csv"
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    plt.close(fig)

    pd.DataFrame(figure_rows).sort_values(["model", "rank"]).to_csv(csv_path, index=False)
    return png_path, csv_path


def main() -> None:
    png_path, csv_path = plot_ranked_levels(metric=DEFAULT_METRIC)
    print(csv_path)
    print(png_path)


if __name__ == "__main__":
    main()
