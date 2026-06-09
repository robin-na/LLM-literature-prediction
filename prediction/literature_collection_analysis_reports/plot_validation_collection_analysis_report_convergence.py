from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import FancyArrowPatch


ROOT = Path(__file__).resolve().parents[2]
VAL_PROCESSED_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
AVG_PREDICTIONS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5"
    / "validation_literature_collection_analysis_report_repeat5_avg_predictions.csv"
)
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_collection_analysis_reports_repeat5"

TRUSTED_MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]

BASELINE_SPECS = {
    "GPT-4.1": {
        "initial_path": ROOT / "openAI_batch_output" / "prediction_positive_case_variations_41.jsonl",
        "initial_ids": ["baseline_joint_reasoning"],
        "repeat_path": ROOT / "openAI_batch_output" / "prediction_positive_case_reasoning_repeats_41.jsonl",
        "repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
    },
    "GPT-4.1 Mini": {
        "initial_path": ROOT / "openAI_batch_output" / "prediction_crosswave_variations_41mini.jsonl",
        "initial_ids": ["baseline_joint_reasoning", "validation/baseline_joint_reasoning"],
        "repeat_path": ROOT / "openAI_batch_output" / "prediction_positive_case_reasoning_repeats_41mini.jsonl",
        "repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
    },
    "GPT-5.1": {
        "initial_path": None,
        "initial_ids": [],
        "repeat_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
        "repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
    "GPT-5 Mini": {
        "initial_path": None,
        "initial_ids": [],
        "repeat_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
        "repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
    "GPT-5 Nano": {
        "initial_path": None,
        "initial_ids": [],
        "repeat_path": ROOT / "openAI_batch_output" / "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
        "repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
}

SHORT_LABELS = {
    "broad_all_2011": "All",
    "leaf_a0_b0_c0": "A0B0C0",
    "leaf_a0_b0_c1": "A0B0C1",
    "leaf_a0_b1_c0": "A0B1C0",
    "leaf_a0_b1_c1": "A0B1C1",
    "leaf_a1_b0_c0": "A1B0C0",
    "leaf_a1_b0_c1": "A1B0C1",
    "leaf_a1_b1_c0": "A1B1C0",
    "leaf_a1_b1_c1": "A1B1C1",
}


def parse_prediction_vector(content: object) -> np.ndarray:
    text = "".join(part.get("text", "") for part in content if isinstance(part, dict)) if isinstance(content, list) else str(content)
    payload = json.loads(text.strip())
    values: list[tuple[int, float]] = []
    for key, item in payload.items():
        if not str(key).startswith("Q"):
            continue
        try:
            idx = int(str(key)[1:])
        except ValueError:
            continue
        pred = item["prediction"] if isinstance(item, dict) else item
        values.append((idx, float(pred)))
    values.sort()
    return np.array([pred for _, pred in values], dtype=float)


def load_prediction_by_ids(path: Path, custom_ids: list[str]) -> np.ndarray:
    for line in path.open():
        obj = json.loads(line)
        custom_id = obj.get("custom_id")
        if custom_id not in custom_ids:
            continue
        vec = parse_prediction_vector(obj["response"]["body"]["choices"][0]["message"]["content"])
        if len(vec) != 20:
            raise ValueError(f"Expected 20 predictions for {custom_id} in {path}, found {len(vec)}")
        return vec
    raise KeyError(f"{custom_ids} not found in {path}")


def load_baseline_average(model: str) -> np.ndarray:
    spec = BASELINE_SPECS[model]
    runs: list[np.ndarray] = []
    if spec["initial_path"] is not None:
        runs.append(load_prediction_by_ids(spec["initial_path"], spec["initial_ids"]))
    repeat_path = spec["repeat_path"]
    for custom_id in spec["repeat_ids"]:
        runs.append(load_prediction_by_ids(repeat_path, [custom_id, f"validation/{custom_id}"]))
    return np.mean(np.vstack(runs), axis=0)


def mean_pairwise_correlation(arrays: list[np.ndarray]) -> float:
    vals: list[float] = []
    for a, b in combinations(arrays, 2):
        if np.std(a) == 0 or np.std(b) == 0:
            vals.append(np.nan)
        else:
            vals.append(float(np.corrcoef(a, b)[0, 1]))
    return float(np.nanmean(np.asarray(vals, dtype=float)))


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


def build_outputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, str]:
    val_df = pd.read_csv(VAL_PROCESSED_CSV).sort_values("CONFIG_configId")
    truth = val_df["treatment_itt_efficiency"].to_numpy(dtype=float) * 100.0

    avg_df = pd.read_csv(AVG_PREDICTIONS_CSV)
    avg_df = avg_df.loc[
        avg_df["model"].isin(TRUSTED_MODELS)
        & avg_df["variant_kind"].isin(["collection_direct", "subset_summary"])
    ].copy()

    q_cols = [f"Q{i}" for i in range(1, 21)]
    baseline_vectors = {model: load_baseline_average(model) for model in TRUSTED_MODELS}
    baseline_mean_pairwise_corr = mean_pairwise_correlation([baseline_vectors[m] for m in TRUSTED_MODELS])
    baseline_mean_corr_to_truth = float(np.mean([np.corrcoef(baseline_vectors[m], truth)[0, 1] for m in TRUSTED_MODELS]))

    variant_ids = sorted(set(avg_df["variant_id"]))
    rows: list[dict[str, object]] = []
    for variant_id in variant_ids:
        part = avg_df.loc[avg_df["variant_id"] == variant_id].copy()
        if set(part["model"]) != set(TRUSTED_MODELS):
            continue
        vectors = {row["model"]: row[q_cols].to_numpy(dtype=float) for _, row in part.iterrows()}
        mean_pairwise_corr = mean_pairwise_correlation([vectors[m] for m in TRUSTED_MODELS])
        mean_corr_to_truth = float(np.mean([np.corrcoef(vectors[m], truth)[0, 1] for m in TRUSTED_MODELS]))
        rows.append(
            {
                "variant_id": variant_id,
                "short_label": SHORT_LABELS.get(variant_id, variant_id),
                "variant_kind": part["variant_kind"].iloc[0],
                "description": part["description"].iloc[0],
                "mean_pairwise_corr_raw": mean_pairwise_corr,
                "delta_mean_pairwise_corr_raw_vs_baseline": mean_pairwise_corr - baseline_mean_pairwise_corr,
                "mean_corr_to_truth_raw": mean_corr_to_truth,
                "delta_mean_corr_to_truth_raw_vs_baseline": mean_corr_to_truth - baseline_mean_corr_to_truth,
            }
        )

    convergence_df = pd.DataFrame(rows).sort_values("variant_id").reset_index(drop=True)
    best_variant = str(
        convergence_df.sort_values("delta_mean_pairwise_corr_raw_vs_baseline", ascending=False)["variant_id"].iloc[0]
    )

    summary_df = pd.DataFrame(
        [
            {
                "models": ",".join(TRUSTED_MODELS),
                "n_variants": int(len(convergence_df)),
                "baseline_mean_pairwise_corr_raw": baseline_mean_pairwise_corr,
                "baseline_mean_corr_to_truth_raw": baseline_mean_corr_to_truth,
                "share_variants_higher_pairwise_corr_raw": float(
                    (convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"] > 0).mean()
                ),
                "mean_delta_pairwise_corr_raw": float(convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].mean()),
                "median_delta_pairwise_corr_raw": float(convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].median()),
                "mean_delta_corr_to_truth_raw": float(convergence_df["delta_mean_corr_to_truth_raw_vs_baseline"].mean()),
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
                "best_variant_id": best_variant,
            }
        ]
    )

    baseline_matrix = pairwise_correlation_matrix(baseline_vectors, TRUSTED_MODELS)
    best_part = avg_df.loc[avg_df["variant_id"] == best_variant].copy()
    best_vectors = {row["model"]: row[q_cols].to_numpy(dtype=float) for _, row in best_part.iterrows()}
    best_matrix = pairwise_correlation_matrix(best_vectors, TRUSTED_MODELS)
    return convergence_df, summary_df, baseline_matrix, best_matrix, best_variant


def plot_figure(
    convergence_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    baseline_matrix: pd.DataFrame,
    best_matrix: pd.DataFrame,
    best_variant: str,
) -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"

    sorted_df = convergence_df.sort_values("delta_mean_pairwise_corr_raw_vs_baseline", ascending=True).reset_index(drop=True)

    fig, axes = plt.subplots(2, 2, figsize=(13.4, 10.2))
    ax_bar, ax_scatter, ax_base, ax_best = axes.flat

    bar_colors = ["#2ca25f" if val > 0 else "#d62728" for val in sorted_df["delta_mean_pairwise_corr_raw_vs_baseline"]]
    ax_bar.axvline(0.0, color="black", linestyle="-", linewidth=1.3)
    ax_bar.hlines(
        y=np.arange(len(sorted_df)),
        xmin=0,
        xmax=sorted_df["delta_mean_pairwise_corr_raw_vs_baseline"],
        color=bar_colors,
        linewidth=2.0,
        alpha=0.8,
    )
    ax_bar.scatter(
        sorted_df["delta_mean_pairwise_corr_raw_vs_baseline"],
        np.arange(len(sorted_df)),
        s=46,
        color=bar_colors,
        edgecolor="white",
        linewidth=0.6,
        zorder=3,
    )
    ax_bar.set_yticks(np.arange(len(sorted_df)))
    ax_bar.set_yticklabels(sorted_df["short_label"])
    ax_bar.set_xlabel("Change in mean pairwise model correlation\non predicted outcome")
    ax_bar.set_ylabel("Collection report variant")
    ax_bar.set_title("Most collection reports increase cross-model agreement")
    share_pos = float(summary_df["share_variants_higher_pairwise_corr_raw"].iloc[0])
    ax_bar.text(
        0.98,
        0.98,
        f"Variants with Δ > 0: {share_pos:.1%}\nMean Δ: {summary_df['mean_delta_pairwise_corr_raw'].iloc[0]:+.3f}\nMedian Δ: {summary_df['median_delta_pairwise_corr_raw'].iloc[0]:+.3f}",
        transform=ax_bar.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d1d5db", "boxstyle": "round,pad=0.3"},
    )

    x = convergence_df["delta_mean_pairwise_corr_raw_vs_baseline"].to_numpy(dtype=float)
    y = convergence_df["delta_mean_corr_to_truth_raw_vs_baseline"].to_numpy(dtype=float)
    ax_scatter.scatter(x, y, s=54, color="#2b8cbe", alpha=0.85, edgecolor="white", linewidth=0.6)
    for _, row in convergence_df.iterrows():
        ax_scatter.annotate(
            row["short_label"],
            xy=(row["delta_mean_pairwise_corr_raw_vs_baseline"], row["delta_mean_corr_to_truth_raw_vs_baseline"]),
            xytext=(5, 4),
            textcoords="offset points",
            fontsize=9,
            color="#1f2937",
        )
    ax_scatter.axvline(0.0, color="black", linestyle="--", linewidth=1.1)
    ax_scatter.axhline(0.0, color="black", linestyle=":", linewidth=1.0)
    rho = float(summary_df["spearman_delta_corr_raw_vs_delta_truth_corr_raw"].iloc[0])
    pearson = float(summary_df["pearson_delta_corr_raw_vs_delta_truth_corr_raw"].iloc[0])
    ax_scatter.set_xlabel("Change in mean pairwise model correlation\non predicted outcome")
    ax_scatter.set_ylabel("Change in mean model correlation to truth\non predicted outcome")
    ax_scatter.set_title("Convergence is suggestive, but only 9 collection variants")
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

    combined_heatmap_vals = np.concatenate(
        [baseline_matrix.to_numpy(dtype=float).ravel(), best_matrix.to_numpy(dtype=float).ravel()]
    )
    combined_heatmap_vals = combined_heatmap_vals[np.isfinite(combined_heatmap_vals)]
    heatmap_vmin = max(0.0, float(combined_heatmap_vals.min()) - 0.03)
    heatmap_kwargs = dict(
        vmin=heatmap_vmin,
        vmax=1.0,
        cmap="magma",
        annot=True,
        fmt=".2f",
        square=True,
        cbar=False,
    )
    sns.heatmap(baseline_matrix, ax=ax_base, **heatmap_kwargs)
    ax_base.set_title("Baseline pairwise correlations\n(predicted outcome)")
    ax_base.tick_params(axis="x", rotation=35)
    ax_base.tick_params(axis="y", rotation=0)

    sns.heatmap(best_matrix, ax=ax_best, **heatmap_kwargs)
    ax_best.set_title(
        f"Most-convergent collection report\n{SHORT_LABELS.get(best_variant, best_variant)} (predicted outcome)"
    )
    ax_best.tick_params(axis="x", rotation=35)
    ax_best.tick_params(axis="y", rotation=0)

    fig.suptitle(
        "Collection-report augmentation also tends to make trusted models agree more on the predicted outcome\n"
        "A = exact/close PGG+punishment relevance, B = payoff-like outcomes, C = empirical only",
        fontsize=15,
        y=0.98,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    base_pos = ax_base.get_position()
    best_pos = ax_best.get_position()
    y_arrow = max(base_pos.y1, best_pos.y1) + 0.01
    x_start = base_pos.x1 + 0.015
    x_end = best_pos.x0 - 0.015
    arrow = FancyArrowPatch(
        (x_start, y_arrow),
        (x_end, y_arrow),
        transform=fig.transFigure,
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.5,
        color="#4b5563",
    )
    fig.add_artist(arrow)
    fig.text(
        (x_start + x_end) / 2,
        y_arrow + 0.012,
        f"augment {SHORT_LABELS.get(best_variant, best_variant)} collection report",
        ha="center",
        va="bottom",
        fontsize=10,
        color="#374151",
    )

    fig.savefig(
        PLOTS_DIR / "validation_literature_collection_analysis_report_convergence.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    convergence_df, summary_df, baseline_matrix, best_matrix, best_variant = build_outputs()
    convergence_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_convergence_dataset.csv",
        index=False,
    )
    summary_df.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_convergence_summary.csv",
        index=False,
    )
    baseline_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_convergence_baseline_pairwise_corr.csv",
        index=True,
    )
    best_matrix.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_convergence_best_pairwise_corr.csv",
        index=True,
    )
    plot_figure(convergence_df, summary_df, baseline_matrix, best_matrix, best_variant)


if __name__ == "__main__":
    main()
