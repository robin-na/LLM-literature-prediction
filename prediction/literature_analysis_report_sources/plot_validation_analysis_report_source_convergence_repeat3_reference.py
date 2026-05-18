from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import FancyArrowPatch

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

ROOT = Path(__file__).resolve().parents[2]
VAL_PROCESSED_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_overview"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_analysis_report_sources_overview"
SINGLE_REPEAT5_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_avg_predictions.csv"
)

TRUSTED_MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
Q_COLS = [f"Q{i}" for i in range(1, 21)]

RUN_SPECS = {
    "GPT-4.1": {
        "baseline_initial_path": ROOT / "openAI_batch_output" / "prediction_positive_case_variations_41.jsonl",
        "baseline_repeat_path": ROOT / "openAI_batch_output" / "prediction_positive_case_reasoning_repeats_41.jsonl",
        "baseline_ids": [
            "baseline_joint_reasoning",
            "baseline_joint_reasoning_rep1",
            "baseline_joint_reasoning_rep2",
            "baseline_joint_reasoning_rep3",
            "baseline_joint_reasoning_rep4",
        ],
        "benchmark_initial_path": ROOT / "openAI_batch_output" / "prediction_literature_analysis_report_strict243_joint_41.jsonl",
        "benchmark_repeat_path": ROOT / "openAI_batch_output" / "prediction_literature_collection_plus_pggms_joint_reps2to5_41.jsonl",
        "benchmark_ids": [
            "paper_analysis_report_joint/PGG_MS_202502",
            "paper_analysis_report_joint_rep2/PGG_MS_202502",
            "paper_analysis_report_joint_rep3/PGG_MS_202502",
            "paper_analysis_report_joint_rep4/PGG_MS_202502",
            "paper_analysis_report_joint_rep5/PGG_MS_202502",
        ],
    },
    "GPT-4.1 Mini": {
        "baseline_initial_path": ROOT / "openAI_batch_output" / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_repeat_path": ROOT / "openAI_batch_output" / "prediction_positive_case_reasoning_repeats_41mini.jsonl",
        "baseline_ids": [
            "baseline_joint_reasoning",
            "baseline_joint_reasoning_rep1",
            "baseline_joint_reasoning_rep2",
            "baseline_joint_reasoning_rep3",
            "baseline_joint_reasoning_rep4",
        ],
        "benchmark_initial_path": ROOT / "openAI_batch_output" / "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
        "benchmark_repeat_path": ROOT / "openAI_batch_output" / "prediction_literature_collection_plus_pggms_joint_reps2to5_41mini.jsonl",
        "benchmark_ids": [
            "paper_analysis_report_joint/PGG_MS_202502",
            "paper_analysis_report_joint_rep2/PGG_MS_202502",
            "paper_analysis_report_joint_rep3/PGG_MS_202502",
            "paper_analysis_report_joint_rep4/PGG_MS_202502",
            "paper_analysis_report_joint_rep5/PGG_MS_202502",
        ],
    },
    "GPT-5.1": {
        "suite_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    "GPT-5 Mini": {
        "suite_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
    "GPT-5 Nano": {
        "suite_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
        "benchmark_ids": [f"paper_analysis_report_joint_rep{i}/PGG_MS_202502" for i in range(1, 6)],
    },
}


def _row_to_vec(row: pd.Series) -> np.ndarray:
    return row[Q_COLS].to_numpy(dtype=float)


def _mean_rows(df: pd.DataFrame, row_ids: list[str]) -> np.ndarray:
    rows = [pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS) for row_id in row_ids if row_id in df.index]
    mat = pd.concat(rows, axis=1)
    return mat.mean(axis=1, skipna=True).to_numpy(dtype=float)


def _load_refs() -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
    from jsonl_parser import jsonl_to_dataframe

    baselines: dict[str, np.ndarray] = {}
    benchmarks: dict[str, np.ndarray] = {}
    for model, spec in RUN_SPECS.items():
        if "suite_path" in spec:
            df = jsonl_to_dataframe(spec["suite_path"]).reindex(columns=Q_COLS)
            baselines[model] = _mean_rows(df, list(spec["baseline_ids"]))
            benchmarks[model] = _mean_rows(df, list(spec["benchmark_ids"]))
            continue

        baseline_df = pd.concat(
            [
                jsonl_to_dataframe(spec["baseline_initial_path"]).reindex(columns=Q_COLS),
                jsonl_to_dataframe(spec["baseline_repeat_path"]).reindex(columns=Q_COLS),
            ],
            axis=0,
        )
        benchmark_df = pd.concat(
            [
                jsonl_to_dataframe(spec["benchmark_initial_path"]).reindex(columns=Q_COLS),
                jsonl_to_dataframe(spec["benchmark_repeat_path"]).reindex(columns=Q_COLS),
            ],
            axis=0,
        )
        baselines[model] = _mean_rows(baseline_df, list(spec["baseline_ids"]))
        benchmarks[model] = _mean_rows(benchmark_df, list(spec["benchmark_ids"]))
    return baselines, benchmarks


def mean_pairwise_correlation(arrays: list[np.ndarray]) -> float:
    vals: list[float] = []
    for a, b in combinations(arrays, 2):
        if np.std(a) == 0 or np.std(b) == 0:
            vals.append(np.nan)
        else:
            vals.append(float(np.corrcoef(a, b)[0, 1]))
    vals_arr = np.asarray(vals, dtype=float)
    return float(np.nanmean(vals_arr))


def mean_pairwise_rmse(arrays: list[np.ndarray]) -> float:
    vals = [float(np.sqrt(np.mean((a - b) ** 2))) for a, b in combinations(arrays, 2)]
    return float(np.mean(vals))


def mean_question_sd(arrays: list[np.ndarray]) -> float:
    return float(np.mean(np.std(np.vstack(arrays), axis=0, ddof=0)))


def pairwise_correlation_matrix(model_to_vec: dict[str, np.ndarray], model_order: list[str]) -> pd.DataFrame:
    data = np.full((len(model_order), len(model_order)), np.nan, dtype=float)
    for i, left in enumerate(model_order):
        for j, right in enumerate(model_order):
            a = model_to_vec[left]
            b = model_to_vec[right]
            if i == j:
                data[i, j] = 1.0
            elif np.std(a) == 0 or np.std(b) == 0:
                data[i, j] = np.nan
            else:
                data[i, j] = float(np.corrcoef(a, b)[0, 1])
    return pd.DataFrame(data, index=model_order, columns=model_order)


def spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    xr = pd.Series(x).rank(method="average").to_numpy(dtype=float)
    yr = pd.Series(y).rank(method="average").to_numpy(dtype=float)
    return float(np.corrcoef(xr, yr)[0, 1])


def build_outputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, float]]:
    val_df = pd.read_csv(VAL_PROCESSED_CSV).sort_values("CONFIG_configId")
    control = val_df["control_itt_efficiency"].to_numpy(dtype=float) * 100.0
    treatment = val_df["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0
    effect_truth = val_df["treatment_effect"].to_numpy(dtype=float) * 100.0

    avg_df = pd.read_csv(SINGLE_REPEAT5_AVG_CSV)
    baselines, benchmarks = _load_refs()
    paper_predictions: dict[str, dict[str, np.ndarray]] = {}
    for model in TRUSTED_MODELS:
        part = avg_df.loc[avg_df["model"] == model].copy()
        paper_predictions[model] = {
            str(row["source_id"]): _row_to_vec(row)
            for _, row in part.iterrows()
        }

    common_sources = sorted(set.intersection(*(set(paper_predictions[model]) for model in TRUSTED_MODELS)))
    baseline_raw = [baselines[model] for model in TRUSTED_MODELS]
    baseline_effect = [baselines[model] - control for model in TRUSTED_MODELS]
    baseline_stats = {
        "raw_pairwise_corr": mean_pairwise_correlation(baseline_raw),
        "effect_pairwise_corr": mean_pairwise_correlation(baseline_effect),
        "raw_pairwise_rmse": mean_pairwise_rmse(baseline_raw),
        "raw_question_sd": mean_question_sd(baseline_raw),
        "raw_mean_corr_to_truth": float(np.mean([np.corrcoef(vec, treatment)[0, 1] for vec in baseline_raw if np.std(vec) > 0])),
        "effect_mean_corr_to_truth": float(np.mean([np.corrcoef(vec, effect_truth)[0, 1] for vec in baseline_effect if np.std(vec) > 0])),
    }

    rows: list[dict[str, object]] = []
    for source_id in common_sources:
        raw = [paper_predictions[model][source_id] for model in TRUSTED_MODELS]
        effect = [paper_predictions[model][source_id] - control for model in TRUSTED_MODELS]
        raw_pairwise_corr = mean_pairwise_correlation(raw)
        effect_pairwise_corr = mean_pairwise_correlation(effect)
        raw_pairwise_rmse = mean_pairwise_rmse(raw)
        raw_question_sd = mean_question_sd(raw)
        mean_corr_to_truth_raw = float(np.mean([np.corrcoef(vec, treatment)[0, 1] for vec in raw if np.std(vec) > 0]))
        mean_corr_to_truth_effect = float(np.mean([np.corrcoef(vec, effect_truth)[0, 1] for vec in effect if np.std(vec) > 0]))
        rows.append(
            {
                "source_id": source_id,
                "mean_pairwise_corr_raw": raw_pairwise_corr,
                "delta_mean_pairwise_corr_raw_vs_baseline": raw_pairwise_corr - baseline_stats["raw_pairwise_corr"],
                "mean_pairwise_corr_effect": effect_pairwise_corr,
                "delta_mean_pairwise_corr_effect_vs_baseline": effect_pairwise_corr - baseline_stats["effect_pairwise_corr"],
                "mean_pairwise_rmse_raw": raw_pairwise_rmse,
                "delta_mean_pairwise_rmse_raw_vs_baseline": raw_pairwise_rmse - baseline_stats["raw_pairwise_rmse"],
                "mean_question_sd_raw": raw_question_sd,
                "delta_mean_question_sd_raw_vs_baseline": raw_question_sd - baseline_stats["raw_question_sd"],
                "mean_corr_to_truth_raw": mean_corr_to_truth_raw,
                "delta_mean_corr_to_truth_raw_vs_baseline": mean_corr_to_truth_raw - baseline_stats["raw_mean_corr_to_truth"],
                "mean_corr_to_truth_effect": mean_corr_to_truth_effect,
                "delta_mean_corr_to_truth_effect_vs_baseline": mean_corr_to_truth_effect - baseline_stats["effect_mean_corr_to_truth"],
            }
        )

    convergence_df = pd.DataFrame(rows).sort_values("source_id").reset_index(drop=True)

    benchmark_raw = [benchmarks[model] for model in TRUSTED_MODELS]
    benchmark_effect = [benchmarks[model] - control for model in TRUSTED_MODELS]
    benchmark_stats = {
        "raw_pairwise_corr": mean_pairwise_correlation(benchmark_raw),
        "effect_pairwise_corr": mean_pairwise_correlation(benchmark_effect),
        "mean_corr_to_truth_raw": float(np.mean([np.corrcoef(vec, treatment)[0, 1] for vec in benchmark_raw if np.std(vec) > 0])),
        "mean_corr_to_truth_effect": float(np.mean([np.corrcoef(vec, effect_truth)[0, 1] for vec in benchmark_effect if np.std(vec) > 0])),
    }

    summary = pd.DataFrame(
        [
            {
                "models": ",".join(TRUSTED_MODELS),
                "n_papers": int(len(convergence_df)),
                "baseline_mean_pairwise_corr_raw": baseline_stats["raw_pairwise_corr"],
                "baseline_mean_pairwise_corr_effect": baseline_stats["effect_pairwise_corr"],
                "share_papers_higher_pairwise_corr_raw": float((convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"] > 0).mean()),
                "share_papers_higher_pairwise_corr_effect": float((convergence_df["delta_mean_pairwise_corr_effect_vs_baseline"] > 0).mean()),
                "mean_delta_pairwise_corr_raw": float(convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].mean()),
                "mean_delta_pairwise_corr_effect": float(convergence_df["delta_mean_pairwise_corr_effect_vs_baseline"].mean()),
                "spearman_delta_corr_raw_vs_delta_truth_corr_raw": spearman_corr(
                    convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].to_numpy(dtype=float),
                    convergence_df["delta_mean_corr_to_truth_raw_vs_baseline"].to_numpy(dtype=float),
                ),
                "pearson_delta_corr_raw_vs_delta_truth_corr_raw": float(
                    np.corrcoef(
                        convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].to_numpy(dtype=float),
                        convergence_df["delta_mean_corr_to_truth_raw_vs_baseline"].to_numpy(dtype=float),
                    )[0, 1]
                ),
                "benchmark_delta_pairwise_corr_raw": benchmark_stats["raw_pairwise_corr"] - baseline_stats["raw_pairwise_corr"],
                "benchmark_delta_mean_corr_to_truth_raw": benchmark_stats["mean_corr_to_truth_raw"] - baseline_stats["raw_mean_corr_to_truth"],
            }
        ]
    )

    baseline_matrix = pairwise_correlation_matrix({model: baselines[model] for model in TRUSTED_MODELS}, TRUSTED_MODELS)
    benchmark_matrix = pairwise_correlation_matrix({model: benchmarks[model] for model in TRUSTED_MODELS}, TRUSTED_MODELS)
    return convergence_df, summary, baseline_matrix, benchmark_matrix, benchmark_stats


def _scatter_limits(values: np.ndarray, extra_values: list[float]) -> tuple[float, float]:
    finite = values[np.isfinite(values)]
    lo = float(np.nanquantile(finite, 0.01))
    hi = float(np.nanquantile(finite, 0.99))
    for val in extra_values:
        if np.isfinite(val):
            lo = min(lo, float(val))
            hi = max(hi, float(val))
    pad = 0.08 * (hi - lo + 1e-9)
    return lo - pad, hi + pad


def plot_figure(
    convergence_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    baseline_matrix: pd.DataFrame,
    benchmark_matrix: pd.DataFrame,
    benchmark_stats: dict[str, float],
) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(2, 2, figsize=(13.2, 10.2))
    ax_hist, ax_scatter, ax_base, ax_bench = axes.flat

    delta_col = "delta_mean_pairwise_corr_raw_vs_baseline"
    truth_col = "delta_mean_corr_to_truth_raw_vs_baseline"
    delta_vals = convergence_df[delta_col].to_numpy(dtype=float)
    truth_vals = convergence_df[truth_col].to_numpy(dtype=float)
    benchmark_delta = float(summary_df["benchmark_delta_pairwise_corr_raw"].iloc[0])
    benchmark_truth = float(summary_df["benchmark_delta_mean_corr_to_truth_raw"].iloc[0])

    ax_hist.hist(delta_vals, bins=36, color="#9ca3af", edgecolor="white", linewidth=0.5)
    ax_hist.axvline(0.0, color="black", linestyle="-", linewidth=1.3, label="No change vs baseline")
    ax_hist.axvline(float(np.mean(delta_vals)), color="#2b8cbe", linestyle="-", linewidth=1.4, label="Mean paper")
    ax_hist.axvline(float(np.median(delta_vals)), color="#6b7280", linestyle=":", linewidth=1.4, label="Median paper")
    ax_hist.axvline(benchmark_delta, color="#f28e2b", linestyle="-.", linewidth=1.6, label="Benchmark report")
    ax_hist.set_xlabel("Change in mean pairwise model correlation\non predicted outcome")
    ax_hist.set_ylabel("Number of papers")
    ax_hist.set_title("Matched repeat-5 references")
    ax_hist.text(
        0.98,
        0.98,
        f"Papers with Δ > 0: {(delta_vals > 0).mean():.1%}\nMean Δ: {np.mean(delta_vals):+.3f}\nMedian Δ: {np.median(delta_vals):+.3f}",
        transform=ax_hist.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d1d5db", "boxstyle": "round,pad=0.3"},
    )
    ax_hist.legend(loc="upper left", frameon=False)

    ax_scatter.scatter(delta_vals, truth_vals, s=16, color="#9ca3af", alpha=0.35, linewidth=0)
    ax_scatter.scatter(
        benchmark_delta,
        benchmark_truth,
        marker="D",
        s=70,
        color="#f28e2b",
        edgecolor="black",
        linewidth=0.6,
        zorder=4,
    )
    ax_scatter.annotate("Benchmark", xy=(benchmark_delta, benchmark_truth), xytext=(7, 7), textcoords="offset points", fontsize=9, color="#7c2d12")
    ax_scatter.axvline(0.0, color="black", linestyle="--", linewidth=1.1)
    ax_scatter.axhline(0.0, color="black", linestyle=":", linewidth=1.0)
    ax_scatter.set_xlim(*_scatter_limits(delta_vals, [0.0, benchmark_delta]))
    ax_scatter.set_ylim(*_scatter_limits(truth_vals, [benchmark_truth]))
    ax_scatter.set_xlabel("Change in mean pairwise model correlation\non predicted outcome")
    ax_scatter.set_ylabel("Change in mean model correlation to truth\non predicted outcome")
    rho = float(summary_df["spearman_delta_corr_raw_vs_delta_truth_corr_raw"].iloc[0])
    pearson = float(summary_df["pearson_delta_corr_raw_vs_delta_truth_corr_raw"].iloc[0])
    ax_scatter.set_title("Matched repeat-5 references")
    ax_scatter.text(
        0.02,
        0.98,
        f"Spearman ρ = {rho:.2f}\nPearson r = {pearson:.2f}",
        transform=ax_scatter.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d1d5db", "boxstyle": "round,pad=0.3"},
    )

    combined_heatmap_vals = np.concatenate([baseline_matrix.to_numpy(dtype=float).ravel(), benchmark_matrix.to_numpy(dtype=float).ravel()])
    combined_heatmap_vals = combined_heatmap_vals[np.isfinite(combined_heatmap_vals)]
    heatmap_vmin = max(0.0, float(combined_heatmap_vals.min()) - 0.03)
    heatmap_kwargs = dict(vmin=heatmap_vmin, vmax=1.0, cmap="magma", annot=True, fmt=".2f", square=True, cbar=False)
    sns.heatmap(baseline_matrix, ax=ax_base, **heatmap_kwargs)
    ax_base.set_title("Baseline pairwise correlations\n(predicted outcome)")
    ax_base.tick_params(axis="x", rotation=35)
    ax_base.tick_params(axis="y", rotation=0)
    sns.heatmap(benchmark_matrix, ax=ax_bench, **heatmap_kwargs)
    ax_bench.set_title("Benchmark report pairwise correlations\n(predicted outcome)")
    ax_bench.tick_params(axis="x", rotation=35)
    ax_bench.tick_params(axis="y", rotation=0)

    fig.suptitle(
        "Same-paper augmentation with matched repeat-5 references\nTrusted models: GPT-4.1, GPT-4.1 Mini, GPT-5.1, GPT-5 Mini, GPT-5 Nano",
        fontsize=15,
        y=0.98,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    base_pos = ax_base.get_position()
    bench_pos = ax_bench.get_position()
    y_arrow = max(base_pos.y1, bench_pos.y1) + 0.01
    x_start = base_pos.x1 + 0.015
    x_end = bench_pos.x0 - 0.015
    arrow = FancyArrowPatch((x_start, y_arrow), (x_end, y_arrow), transform=fig.transFigure, arrowstyle="->", mutation_scale=14, linewidth=1.5, color="#4b5563")
    fig.add_artist(arrow)
    fig.text((x_start + x_end) / 2, y_arrow + 0.012, "augment benchmark paper report", ha="center", va="bottom", fontsize=10, color="#374151")

    fig.savefig(
        PLOTS_DIR / "validation_literature_analysis_report_source_convergence_repeat5_reference.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    convergence_df, summary_df, baseline_matrix, benchmark_matrix, benchmark_stats = build_outputs()
    convergence_df.to_csv(RESULTS_DIR / "single_paper_convergence_repeat5_reference_dataset.csv", index=False)
    summary_df.to_csv(RESULTS_DIR / "single_paper_convergence_repeat5_reference_summary.csv", index=False)
    baseline_matrix.to_csv(RESULTS_DIR / "single_paper_convergence_repeat5_reference_baseline_pairwise_corr.csv", index=True)
    benchmark_matrix.to_csv(RESULTS_DIR / "single_paper_convergence_repeat5_reference_benchmark_pairwise_corr.csv", index=True)
    plot_figure(convergence_df, summary_df, baseline_matrix, benchmark_matrix, benchmark_stats)
    print(RESULTS_DIR / "single_paper_convergence_repeat5_reference_dataset.csv")
    print(RESULTS_DIR / "single_paper_convergence_repeat5_reference_summary.csv")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_convergence_repeat5_reference.png")


if __name__ == "__main__":
    main()
