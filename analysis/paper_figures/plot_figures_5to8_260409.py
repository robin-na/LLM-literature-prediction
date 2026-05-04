from __future__ import annotations

import hashlib
import os
import re
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
from scipy import stats

from analyze_literature_metadata_supervised_benchmarks import (
    COLLECTION_FEATURES as BENCH_COLLECTION_FEATURES,
    COLLECTION_NUMERIC,
    PAPER_FEATURES as BENCH_PAPER_FEATURES,
    PAPER_NUMERIC,
    evaluate_models,
    summarize_best,
)
import plot_figure7_metadata_effect_robustness as fig7_module
from plot_cross_model_repeat_rank_ceiling import (
    Q_COLS,
    load_collection_repeat_predictions as load_gpt_collection_repeat_predictions,
    load_paper_repeat_predictions as load_gpt_paper_repeat_predictions,
    load_truth,
    rowwise_corr,
)
from plot_figure8_collection_feature_importance_gpt41 import (
    FEATURE_KEYS as FIG8_FEATURE_KEYS,
    NONLINEAR_MODELS,
    compute_permutation_importance,
    compute_shap_tables,
    draw_figure as draw_feature_importance_figure,
    load_collection_feature_frame as load_current_figure8_collection_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
CLAUDE_WIDE_CSV = ROOT / "claude_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_wide.csv"
GEMINI_WIDE_CSV = ROOT / "gemini_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_wide.csv"
CLAUDE_BASELINE_REPEAT_CSV = (
    ROOT / "results" / "validation" / "claude_literature_baseline_benchmark_repeat5" / "claude_literature_baseline_benchmark_repeat_rows.csv"
)
PAPER_FEATURE_DATA_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "paper_feature_analysis_dataset_repeat5.csv"
)
PAPER_SIGNIFICANCE_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
CURRENT_COLLECTION_REL_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_relationship_dataset.csv"
)
COLLECTION_REPORT_INDEX_CSV = ROOT / "literature" / "output" / "collection_analysis_reports" / "metadata_filters" / "report_index.csv"

CLAUDE_MODEL = "Claude Sonnet 4.6"
GEMINI_MODEL = "Gemini 2.5 Pro"
CLAUDE_SOURCE_FILE_SUBSTRINGS = (
    "prediction_literature_papers2011_",
    "prediction_literature_collections717_",
)

FIGURE5_MODEL_ORDER = ["GPT-5.1", "GPT-4.1 Mini", "GPT-4.1", "GPT-5 Nano", "GPT-5 Mini", CLAUDE_MODEL, GEMINI_MODEL]
FIGURE67_MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano", CLAUDE_MODEL, GEMINI_MODEL]
FIGURE5_EPSILON = 0.06

MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
    CLAUDE_MODEL: "#9c755f",
    GEMINI_MODEL: "#a6761d",
}
FIGURE6_DATASET_LABELS = {
    "individual_papers": "Individual papers",
    "metadata_filter_collections": "Collections",
}
FIGURE6_DATASET_COLORS = {
    "individual_papers": "#73808f",
    "metadata_filter_collections": "#e59a3a",
}


def sanitize_with_hash(custom_id: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", custom_id)
    if len(safe) <= 64:
        return safe
    digest = hashlib.sha1(custom_id.encode("utf-8")).hexdigest()[:8]
    suffix = f"___h{digest}"
    max_head_len = 64 - len(suffix)
    return f"{safe[:max_head_len]}{suffix}"


def summarize_repeat_vector(values: np.ndarray) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    mean = float(np.mean(arr)) if n else float("nan")
    if n <= 1:
        return {"n": n, "mean": mean, "sd": float("nan"), "se": float("nan")}
    sd = float(np.std(arr, ddof=1))
    return {"n": n, "mean": mean, "sd": sd, "se": float(sd / np.sqrt(n))}


def internal_repeat_ids(repeat_map: dict[str, pd.DataFrame]) -> pd.Index:
    shared: set[str] | None = None
    for df in repeat_map.values():
        ids = set(df.index.astype(str).tolist())
        shared = ids if shared is None else (shared & ids)
    assert shared is not None
    return pd.Index(sorted(shared))


def load_baseline_repeat_data(
    model_order: list[str],
    truth: np.ndarray,
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], dict[str, int]]:
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    claude_rows = pd.read_csv(CLAUDE_BASELINE_REPEAT_CSV)
    gemini_usecols = ["source_file", "model_label", "condition_stem", "prompt_elicitation", "repeat_index", *Q_COLS]
    gemini_rows = pd.read_csv(GEMINI_WIDE_CSV, usecols=lambda c: c in gemini_usecols)
    gemini_rows = gemini_rows.loc[
        gemini_rows["source_file"].astype(str).str.contains("prediction_literature_baseline-benchmark_joint_reps1to5_gemini25pro\\.jsonl")
        & gemini_rows["model_label"].eq(GEMINI_MODEL)
        & gemini_rows["condition_stem"].eq("baseline")
        & gemini_rows["prompt_elicitation"].eq("joint_reasoning")
        & gemini_rows["repeat_index"].between(1, 5)
    ].copy()
    gemini_rows["model"] = GEMINI_MODEL
    gemini_rows["condition"] = "baseline"
    gemini_rows["repeat"] = gemini_rows["repeat_index"].astype(int)
    gemini_pred = gemini_rows.loc[:, Q_COLS].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=np.float32)
    gemini_rows["correlation"] = rowwise_corr(gemini_pred, truth).astype(float)
    gemini_rows = gemini_rows.loc[:, ["model", "condition", "repeat", "correlation", *Q_COLS]]

    all_rows = pd.concat([repeat_rows, claude_rows, gemini_rows], ignore_index=True, sort=False)
    all_rows = all_rows.loc[all_rows["condition"] == "baseline"].copy()

    baseline_avg_vectors: dict[str, np.ndarray] = {}
    baseline_repeat_scores: dict[str, np.ndarray] = {}
    baseline_n_runs: dict[str, int] = {}

    for model in model_order:
        part = all_rows.loc[all_rows["model"] == model].sort_values("repeat").copy()
        if part.empty:
            raise KeyError(f"Missing baseline repeat rows for {model}.")
        baseline_repeat_scores[model] = part["correlation"].to_numpy(dtype=float)
        baseline_avg_vectors[model] = (
            part.loc[:, Q_COLS].apply(pd.to_numeric, errors="coerce").mean(axis=0).to_numpy(dtype=np.float32)
        )
        baseline_n_runs[model] = int(len(part))

    return baseline_avg_vectors, baseline_repeat_scores, baseline_n_runs


def load_claude_augmented_wide() -> pd.DataFrame:
    wide = pd.read_csv(CLAUDE_WIDE_CSV)
    mask = wide["model_label"].eq(CLAUDE_MODEL)
    mask &= wide["source_file"].astype(str).str.contains("|".join(map(re.escape, CLAUDE_SOURCE_FILE_SUBSTRINGS)))
    return wide.loc[mask].copy()


def build_claude_full_id_map(kind: str) -> dict[str, tuple[int, str]]:
    if kind == "paper":
        paper_ids = sorted(pd.read_csv(PAPER_SIGNIFICANCE_CSV)["source_id"].astype(str).unique().tolist())
        full_ids = [
            (rep, source_id, f"paper_analysis_report_joint_rep{rep}/{source_id}")
            for rep in range(1, 6)
            for source_id in paper_ids
        ]
    elif kind == "collection":
        variant_ids = sorted(pd.read_csv(COLLECTION_REPORT_INDEX_CSV)["variant_id"].astype(str).unique().tolist())
        full_ids = [
            (rep, variant_id, f"collection_analysis_report_joint_rep{rep}/{variant_id}")
            for rep in range(1, 6)
            for variant_id in variant_ids
        ]
    else:
        raise ValueError(kind)

    mapping: dict[str, tuple[int, str]] = {}
    for rep, item_id, full_id in full_ids:
        mapping[sanitize_with_hash(full_id)] = (rep, item_id)
    return mapping


def load_claude_repeat_predictions(kind: str) -> dict[str, pd.DataFrame]:
    wide = load_claude_augmented_wide()
    if kind == "paper":
        subset = wide.loc[wide["source_file"].astype(str).str.contains("prediction_literature_papers2011_")].copy()
    elif kind == "collection":
        subset = wide.loc[wide["source_file"].astype(str).str.contains("prediction_literature_collections717_")].copy()
    else:
        raise ValueError(kind)

    full_id_map = build_claude_full_id_map(kind)
    resolved = subset["raw_row_id"].astype(str).map(full_id_map)
    subset = subset.loc[resolved.notna()].copy()
    resolved = resolved.loc[resolved.notna()]
    subset["repeat"] = [value[0] for value in resolved]
    subset["item_id"] = [value[1] for value in resolved]
    subset = subset.drop_duplicates(["repeat", "item_id"], keep="last").reset_index(drop=True)

    repeat_map: dict[str, pd.DataFrame] = {}
    for rep in range(1, 6):
        part = subset.loc[subset["repeat"] == rep, ["item_id", *Q_COLS]].copy()
        repeat_map[f"rep{rep}"] = part.set_index("item_id").sort_index()
    return repeat_map


def load_gemini_repeat_predictions(kind: str) -> dict[str, pd.DataFrame]:
    usecols = ["source_file", "model_label", "condition_stem", "prompt_elicitation", "augmented_input_id", "repeat_index", *Q_COLS]
    wide = pd.read_csv(GEMINI_WIDE_CSV, usecols=lambda c: c in usecols)
    wide = wide.loc[
        wide["model_label"].eq(GEMINI_MODEL)
        & wide["prompt_elicitation"].astype(str).isin(["joint", "joint_reasoning"])
        & wide["repeat_index"].between(1, 5)
    ].copy()

    if kind == "paper":
        valid_ids = set(pd.read_csv(PAPER_SIGNIFICANCE_CSV)["source_id"].astype(str).unique().tolist())
        subset = wide.loc[
            wide["condition_stem"].eq("paper_analysis_report")
            & wide["source_file"].astype(str).str.contains("prediction_literature_analysis_report_extended2011_")
        ].copy()
    elif kind == "collection":
        valid_ids = set(pd.read_csv(COLLECTION_REPORT_INDEX_CSV)["variant_id"].astype(str).unique().tolist())
        subset = wide.loc[
            wide["condition_stem"].eq("collection_analysis_report")
            & wide["source_file"].astype(str).str.contains("prediction_literature_collection_analysis_report_metadata_filters_")
        ].copy()
    else:
        raise ValueError(kind)

    subset["item_id"] = subset["augmented_input_id"].astype(str)
    subset = subset.loc[subset["item_id"].isin(valid_ids)].copy()
    subset["repeat"] = subset["repeat_index"].astype(int)
    subset = subset.drop_duplicates(["repeat", "item_id"], keep="last").reset_index(drop=True)

    repeat_map: dict[str, pd.DataFrame] = {}
    for rep in range(1, 6):
        part = subset.loc[subset["repeat"] == rep, ["item_id", *Q_COLS]].copy()
        repeat_map[f"rep{rep}"] = part.set_index("item_id").sort_index()
    return repeat_map


def load_paper_repeat_predictions() -> dict[str, dict[str, pd.DataFrame]]:
    out = load_gpt_paper_repeat_predictions()
    out[CLAUDE_MODEL] = load_claude_repeat_predictions("paper")
    out[GEMINI_MODEL] = load_gemini_repeat_predictions("paper")
    return out


def load_collection_repeat_predictions() -> dict[str, dict[str, pd.DataFrame]]:
    out = load_gpt_collection_repeat_predictions()
    out[CLAUDE_MODEL] = load_claude_repeat_predictions("collection")
    out[GEMINI_MODEL] = load_gemini_repeat_predictions("collection")
    return out


def build_repeat_metrics(
    repeat_predictions: dict[str, dict[str, pd.DataFrame]],
    truth: np.ndarray,
    baseline_avg_vectors: dict[str, np.ndarray],
    baseline_repeat_scores: dict[str, np.ndarray],
    baseline_n_runs: dict[str, int],
    *,
    model_order: list[str],
    item_id_col: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    metric_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for model in model_order:
        repeat_map = repeat_predictions[model]
        ids = internal_repeat_ids(repeat_map)
        pred_mats = []
        score_list = []
        for rep in range(1, 6):
            preds = repeat_map[f"rep{rep}"].reindex(ids)[Q_COLS].to_numpy(dtype=np.float32)
            pred_mats.append(preds)
            score_list.append(rowwise_corr(preds, truth))
        pred_stack = np.stack(pred_mats, axis=0)
        avg_preds = np.mean(pred_stack, axis=0)
        avg_scores = rowwise_corr(avg_preds, truth)
        score_mat = np.stack(score_list, axis=1)

        baseline_avg_pred = baseline_avg_vectors[model]
        baseline_scores = baseline_repeat_scores[model]
        baseline_avg_corr = float(rowwise_corr(baseline_avg_pred[None, :], truth)[0])
        baseline_summary = summarize_repeat_vector(baseline_scores)
        delta_mat = score_mat - baseline_scores[None, :]

        for i, item_id in enumerate(ids):
            corr_summary = summarize_repeat_vector(score_mat[i])
            delta_summary = summarize_repeat_vector(delta_mat[i])
            metric_rows.append(
                {
                    "model": model,
                    item_id_col: str(item_id),
                    "n_aug_runs": int(pred_stack.shape[0]),
                    "n_baseline_runs": baseline_n_runs[model],
                    "correlation": float(avg_scores[i]),
                    "correlation_mean_repeat": corr_summary["mean"],
                    "correlation_repeat_sd": corr_summary["sd"],
                    "correlation_repeat_se": corr_summary["se"],
                    "baseline_correlation": baseline_avg_corr,
                    "baseline_correlation_mean_repeat": baseline_summary["mean"],
                    "baseline_repeat_sd": baseline_summary["sd"],
                    "baseline_repeat_se": baseline_summary["se"],
                    "delta_correlation": float(avg_scores[i] - baseline_avg_corr),
                    "delta_correlation_mean_repeat": delta_summary["mean"],
                    "delta_correlation_repeat_sd": delta_summary["sd"],
                    "delta_correlation_repeat_se": delta_summary["se"],
                }
            )

        summary_rows.append(
            {
                "model": model,
                "n_items": int(len(ids)),
                "baseline_correlation": baseline_avg_corr,
                "baseline_correlation_mean_repeat": baseline_summary["mean"],
                "baseline_repeat_sd": baseline_summary["sd"],
                "baseline_repeat_se": baseline_summary["se"],
                "mean_augmented_correlation": float(np.nanmean(avg_scores)),
                "mean_augmented_correlation_mean_repeat": float(np.nanmean(score_mat.mean(axis=1))),
            }
        )

    metric_df = pd.DataFrame(metric_rows).sort_values(["model", item_id_col]).reset_index(drop=True)
    summary_df = pd.DataFrame(summary_rows).sort_values("model").reset_index(drop=True)
    return metric_df, summary_df


def build_figure5_pairwise_rows(
    metric_df: pd.DataFrame,
    *,
    kind: str,
    item_id_col: str,
    epsilon: float,
) -> pd.DataFrame:
    wide = (
        metric_df.pivot(index=item_id_col, columns="model", values="correlation")
        .dropna()
        .reindex(columns=FIGURE5_MODEL_ORDER)
    )
    upper_idx = np.triu_indices(len(wide), k=1)
    values = {model: wide[model].to_numpy(dtype=np.float32) for model in FIGURE5_MODEL_ORDER}

    rows: list[dict[str, float | str | int]] = []
    for model_a, model_b in combinations(FIGURE5_MODEL_ORDER, 2):
        scores_a = values[model_a]
        scores_b = values[model_b]
        diff_a = scores_a[upper_idx[0]] - scores_a[upper_idx[1]]
        diff_b = scores_b[upper_idx[0]] - scores_b[upper_idx[1]]
        informative_mask = (np.abs(diff_a) > epsilon) & (np.abs(diff_b) > epsilon)
        agreement = float(np.mean(np.sign(diff_a[informative_mask]) == np.sign(diff_b[informative_mask])))
        rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": int(len(wide)),
                "epsilon": float(epsilon),
                "observed_spearman": float(stats.spearmanr(scores_a, scores_b).statistic),
                "order_agreement_excluding_near_ties": agreement,
                "informative_pair_coverage": float(informative_mask.mean()),
            }
        )
    return pd.DataFrame(rows)


def write_figure5_outputs(paper_metrics_df: pd.DataFrame, collection_metrics_df: pd.DataFrame) -> None:
    plot_pairwise = pd.concat(
        [
            build_figure5_pairwise_rows(
                paper_metrics_df,
                kind="papers",
                item_id_col="source_id",
                epsilon=FIGURE5_EPSILON,
            ),
            build_figure5_pairwise_rows(
                collection_metrics_df,
                kind="collections",
                item_id_col="variant_id",
                epsilon=FIGURE5_EPSILON,
            ),
        ],
        ignore_index=True,
    )

    summary = (
        plot_pairwise.groupby("kind", as_index=False)[["observed_spearman", "order_agreement_excluding_near_ties", "informative_pair_coverage"]]
        .mean()
        .rename(
            columns={
                "observed_spearman": "mean_spearman_rho",
                "order_agreement_excluding_near_ties": "mean_order_agreement_excluding_near_ties",
                "informative_pair_coverage": "mean_informative_pair_coverage",
            }
        )
    )
    coverage = plot_pairwise.loc[:, ["kind", "model_a", "model_b", "epsilon", "informative_pair_coverage"]].copy()

    plot_pairwise.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_pairwise.csv", index=False)
    summary.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_summary.csv", index=False)
    coverage.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_epsilon_coverage.csv", index=False)

    def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
        matrix = pd.DataFrame(np.eye(len(FIGURE5_MODEL_ORDER)), index=FIGURE5_MODEL_ORDER, columns=FIGURE5_MODEL_ORDER)
        for row in df.itertuples(index=False):
            value = float(getattr(row, value_col))
            matrix.loc[row.model_a, row.model_b] = value
            matrix.loc[row.model_b, row.model_a] = value
        return matrix

    def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str, ylabel: str = "") -> None:
        sns.heatmap(
            matrix,
            ax=ax,
            cmap="YlGnBu",
            vmin=0.0,
            vmax=1.0,
            annot=True,
            fmt=".2f",
            cbar=False,
            square=True,
            linewidths=0.6,
            linecolor="white",
            annot_kws={"fontsize": 9},
        )
        ax.set_title(title, fontsize=12, pad=8)
        ax.set_xlabel("")
        ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
        ax.tick_params(axis="x", rotation=45, labelsize=9)
        ax.tick_params(axis="y", rotation=0, labelsize=9)

    fig, axes = plt.subplots(2, 2, figsize=(12.4, 9.2))
    specs = [
        ("papers", "observed_spearman", "Spearman rho", "Individual papers"),
        ("papers", "order_agreement_excluding_near_ties", "Order agreement\n(excluding near-ties)", ""),
        ("collections", "observed_spearman", "Spearman rho", "Collections"),
        ("collections", "order_agreement_excluding_near_ties", "Order agreement\n(excluding near-ties)", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = plot_pairwise.loc[plot_pairwise["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, value_col), title, ylabel)

    fig.text(
        0.5,
        0.02,
        f"epsilon = {FIGURE5_EPSILON:.2f}. Order agreement excludes item pairs whose score gap is at most epsilon in either model.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure5_cross_model_rank_robustness.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def build_alt_benchmark_datasets(
    paper_metrics_df: pd.DataFrame,
    collection_metrics_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    perf_cols = [
        "correlation",
        "baseline_correlation",
        "delta_correlation",
        "rmse",
        "baseline_rmse",
        "delta_rmse",
        "rmse_improvement",
        "r2",
        "baseline_r2",
        "delta_r2",
        "directional_accuracy",
        "baseline_directional_accuracy",
        "delta_directional_accuracy",
    ]
    paper_feature_df = pd.read_csv(PAPER_FEATURE_DATA_CSV)
    base_paper = paper_feature_df.loc[paper_feature_df["model"] == "GPT-4.1"].copy()
    missing_paper_models = [model for model in FIGURE67_MODEL_ORDER if model not in set(paper_feature_df["model"].astype(str))]
    extra_paper_frames = []
    for model in missing_paper_models:
        extra = base_paper.copy()
        extra["model"] = model
        extra_paper_frames.append(extra)
    if extra_paper_frames:
        paper_feature_df = pd.concat([paper_feature_df, *extra_paper_frames], ignore_index=True)
    paper_feature_df = paper_feature_df.loc[paper_feature_df["model"].isin(FIGURE67_MODEL_ORDER)].copy()
    paper_metric_cols = paper_metrics_df.loc[:, ["model", "source_id", "correlation", "baseline_correlation", "delta_correlation"]]
    alt_paper_bench = (
        paper_feature_df.drop(
            columns=[
                col
                for col in perf_cols
                if col in paper_feature_df.columns
            ]
        )
        .merge(paper_metric_cols, on=["model", "source_id"], how="left", validate="many_to_one")
    )

    collection_rel_df = pd.read_csv(CURRENT_COLLECTION_REL_CSV)
    collection_rel_df = collection_rel_df.loc[collection_rel_df["variant_group"] == "metadata_filter"].copy()
    base_collection = collection_rel_df.loc[collection_rel_df["model"] == "GPT-4.1"].copy()
    missing_collection_models = [model for model in FIGURE67_MODEL_ORDER if model not in set(collection_rel_df["model"].astype(str))]
    extra_collection_frames = []
    for model in missing_collection_models:
        extra = base_collection.copy()
        extra["model"] = model
        extra_collection_frames.append(extra)
    if extra_collection_frames:
        collection_rel_df = pd.concat([collection_rel_df, *extra_collection_frames], ignore_index=True)
    collection_rel_df = collection_rel_df.loc[collection_rel_df["model"].isin(FIGURE67_MODEL_ORDER)].copy()
    metric_cols = ["correlation", "baseline_correlation", "delta_correlation"]
    alt_collection_bench = (
        collection_rel_df.drop(columns=[col for col in perf_cols if col in collection_rel_df.columns])
        .merge(
            collection_metrics_df.loc[:, ["model", "variant_id", *metric_cols]],
            on=["model", "variant_id"],
            how="left",
            validate="many_to_one",
        )
    )
    return alt_paper_bench, alt_collection_bench


def build_alt_benchmark_tables(
    alt_paper_bench: pd.DataFrame,
    alt_collection_bench: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    results = pd.concat(
        [
            evaluate_models(
                alt_paper_bench,
                dataset_name="individual_papers",
                features=BENCH_PAPER_FEATURES,
                numeric_cols=PAPER_NUMERIC,
                group_col="source_id",
                within_model=True,
            ),
            evaluate_models(
                alt_collection_bench,
                dataset_name="metadata_filter_collections",
                features=BENCH_COLLECTION_FEATURES,
                numeric_cols=COLLECTION_NUMERIC,
                group_col="variant_id",
                within_model=True,
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    best = summarize_best(results)
    return results, best


def write_figure6_outputs(best: pd.DataFrame) -> None:
    rows = best.loc[(best["target"] == "correlation") & (best["scope"] == "within_model")].copy()
    rows = rows.loc[rows["scope_name"].isin(FIGURE67_MODEL_ORDER)].copy()
    rows["dataset_label"] = rows["dataset"].map(FIGURE6_DATASET_LABELS)
    rows["model_label"] = rows["model_name"].astype(str).str.replace("_", " ", regex=False).str.title()
    rows["scope_order"] = rows["scope_name"].map({name: idx for idx, name in enumerate(FIGURE67_MODEL_ORDER)})
    rows = rows.sort_values(["scope_order", "dataset_label"]).reset_index(drop=True)
    rows["se_fold_r2"] = rows["sd_fold_r2"] / np.sqrt(5)
    rows["se_fold_spearman"] = rows["sd_fold_spearman"] / np.sqrt(5)
    rows.to_csv(RESULTS_DIR / "figure6_metadata_predictability_correlation_rows.csv", index=False)

    def draw_panel(ax: plt.Axes, df: pd.DataFrame, metric: str, err: str, xlabel: str, show_ylabels: bool) -> None:
        row_y = np.arange(len(FIGURE67_MODEL_ORDER))[::-1].astype(float)
        y_map = dict(zip(FIGURE67_MODEL_ORDER, row_y))
        offsets = {"individual_papers": 0.18, "metadata_filter_collections": -0.18}
        height = 0.33

        for dataset in ["individual_papers", "metadata_filter_collections"]:
            part = df.loc[df["dataset"] == dataset].copy()
            ys = [y_map[name] + offsets[dataset] for name in part["scope_name"]]
            xs = part[metric].to_numpy(dtype=float)
            xerr = part[err].to_numpy(dtype=float)

            ax.barh(
                ys,
                xs,
                height=height,
                color=FIGURE6_DATASET_COLORS[dataset],
                alpha=0.86,
                edgecolor="none",
                zorder=2,
            )
            ax.errorbar(
                xs,
                ys,
                xerr=xerr,
                fmt="none",
                ecolor="#46505d",
                elinewidth=1.0,
                alpha=0.45,
                capsize=2.3,
                zorder=3,
            )

        ax.axvline(0.0, color="#777777", lw=1.1, ls=(0, (4, 3)), zorder=1)
        ax.set_xlabel(xlabel)
        ax.set_yticks(row_y)
        if show_ylabels:
            ax.set_yticklabels(FIGURE67_MODEL_ORDER)
        else:
            ax.tick_params(axis="y", labelleft=False)
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", color="#e6e6e6", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cfcfcf")
        ax.spines["bottom"].set_color("#cfcfcf")

    def annotate_models(ax: plt.Axes, df: pd.DataFrame, x_pos: float) -> None:
        row_y = np.arange(len(FIGURE67_MODEL_ORDER))[::-1].astype(float)
        y_map = dict(zip(FIGURE67_MODEL_ORDER, row_y))
        offsets = {"individual_papers": 0.18, "metadata_filter_collections": -0.18}
        for dataset in ["individual_papers", "metadata_filter_collections"]:
            part = df.loc[df["dataset"] == dataset].copy()
            for row in part.itertuples(index=False):
                ax.text(
                    x_pos,
                    y_map[row.scope_name] + offsets[dataset],
                    str(row.model_label),
                    ha="left",
                    va="center",
                    fontsize=8.6,
                    color=FIGURE6_DATASET_COLORS[dataset],
                )

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.25), sharey=True)
    draw_panel(axes[0], rows, "mean_fold_r2", "se_fold_r2", "Grouped-CV R^2", show_ylabels=True)
    draw_panel(axes[1], rows, "mean_fold_spearman", "se_fold_spearman", "Grouped-CV Spearman", show_ylabels=False)

    axes[0].set_xlim(-0.18, max(0.26, rows["mean_fold_r2"].max() + rows["se_fold_r2"].max() + 0.02))
    axes[1].set_xlim(-0.03, max(0.56, rows["mean_fold_spearman"].max() + rows["se_fold_spearman"].max() + 0.03))
    annotate_models(axes[0], rows, x_pos=-0.173)

    handles = [
        Line2D([0], [0], color=FIGURE6_DATASET_COLORS[key], lw=10, solid_capstyle="round", label=label)
        for key, label in FIGURE6_DATASET_LABELS.items()
    ]
    handles.append(Line2D([0], [0], color="#777777", lw=1.1, ls=(0, (4, 3)), label="No signal"))
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.985),
        columnspacing=1.2,
        handlelength=2.0,
    )

    fig.subplots_adjust(top=0.78, left=0.31, right=0.985, bottom=0.19, wspace=0.16)
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure6_metadata_predictability_correlation.{ext}", dpi=300)
    plt.close(fig)


def write_figure7_outputs(paper_metrics_df: pd.DataFrame) -> None:
    current_df = fig7_module.load_paper_df().drop(columns=["delta_correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("source_id", keep="first")
    )
    alt_df = paper_metrics_df.loc[:, ["model", "source_id", "delta_correlation"]].merge(
        base_feature_df,
        on="source_id",
        how="left",
        validate="many_to_one",
    )

    fig7_module.MODELS = FIGURE67_MODEL_ORDER
    fig7_module.MODEL_COLORS = {name: MODEL_COLORS[name] for name in FIGURE67_MODEL_ORDER}
    rows = fig7_module.build_rows(alt_df, item_type="Individual papers", feature_cols=fig7_module.PAPER_FEATURES)
    rows.to_csv(RESULTS_DIR / "figure7_individual_metadata_effect_robustness_rows.csv", index=False)
    fig7_module.draw_figure(
        rows,
        None,
        PLOTS_DIR / "figure7_individual_metadata_effect_robustness.png",
        PLOTS_DIR / "figure7_individual_metadata_effect_robustness.pdf",
    )


def write_figure8_outputs(
    collection_metrics_df: pd.DataFrame,
    benchmark_results: pd.DataFrame,
) -> pd.DataFrame:
    current_df = load_current_figure8_collection_df().drop(columns=["delta_correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("variant_id", keep="first")
    )
    alt_df = collection_metrics_df.loc[:, ["model", "variant_id", "delta_correlation"]].merge(
        base_feature_df,
        on="variant_id",
        how="left",
        validate="many_to_one",
    )

    nonlinear = benchmark_results.loc[
        (benchmark_results["dataset"] == "metadata_filter_collections")
        & (benchmark_results["target"] == "delta_correlation")
        & (benchmark_results["scope"] == "within_model")
        & (benchmark_results["scope_name"].isin(FIGURE67_MODEL_ORDER))
        & (benchmark_results["model_name"].isin(NONLINEAR_MODELS))
    ].copy()
    best_nonlinear = (
        nonlinear.sort_values(["scope_name", "cv_r2", "cv_spearman"], ascending=[True, False, False])
        .groupby("scope_name", as_index=False)
        .head(1)
        .reset_index(drop=True)
    )
    best_nonlinear.to_csv(RESULTS_DIR / "figure8_collection_best_nonlinear_model_by_model.csv", index=False)

    estimator_name = str(best_nonlinear.loc[best_nonlinear["scope_name"] == CLAUDE_MODEL, "model_name"].iloc[0])
    df = alt_df.loc[alt_df["model"] == CLAUDE_MODEL].sort_values("variant_id").reset_index(drop=True)
    X = df[FIG8_FEATURE_KEYS].apply(pd.to_numeric, errors="coerce")
    X = X.fillna(X.median(numeric_only=True))
    y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
    groups = df["variant_id"].astype(str).to_numpy()

    perm_df = compute_permutation_importance(X, y, groups, estimator_name)
    shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)

    stem = "figure8_collection_feature_importance_claude_sonnet46"
    perm_df.to_csv(RESULTS_DIR / f"{stem}_permutation.csv", index=False)
    shap_points.to_csv(RESULTS_DIR / f"{stem}_shap_points.csv", index=False)
    shap_summary.to_csv(RESULTS_DIR / f"{stem}_shap_summary.csv", index=False)
    draw_feature_importance_figure(
        CLAUDE_MODEL,
        estimator_name,
        perm_df,
        shap_points,
        PLOTS_DIR / f"{stem}.png",
        PLOTS_DIR / f"{stem}.pdf",
    )
    return best_nonlinear


def main() -> None:
    sns.set_theme(style="white", context="talk")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    truth = load_truth()
    baseline_avg_vectors, baseline_repeat_scores, baseline_n_runs = load_baseline_repeat_data(FIGURE67_MODEL_ORDER, truth)

    paper_repeat_predictions = load_paper_repeat_predictions()
    collection_repeat_predictions = load_collection_repeat_predictions()

    paper_metrics_df, paper_summary_df = build_repeat_metrics(
        paper_repeat_predictions,
        truth,
        baseline_avg_vectors,
        baseline_repeat_scores,
        baseline_n_runs,
        model_order=FIGURE67_MODEL_ORDER,
        item_id_col="source_id",
    )
    collection_metrics_df, collection_summary_df = build_repeat_metrics(
        collection_repeat_predictions,
        truth,
        baseline_avg_vectors,
        baseline_repeat_scores,
        baseline_n_runs,
        model_order=FIGURE67_MODEL_ORDER,
        item_id_col="variant_id",
    )

    paper_metrics_df.to_csv(RESULTS_DIR / "paper_repeat_correlation_metrics.csv", index=False)
    paper_summary_df.to_csv(RESULTS_DIR / "paper_repeat_correlation_model_summary.csv", index=False)
    collection_metrics_df.to_csv(RESULTS_DIR / "collection_repeat_correlation_metrics.csv", index=False)
    collection_summary_df.to_csv(RESULTS_DIR / "collection_repeat_correlation_model_summary.csv", index=False)

    write_figure5_outputs(paper_metrics_df, collection_metrics_df)

    alt_paper_bench, alt_collection_bench = build_alt_benchmark_datasets(paper_metrics_df, collection_metrics_df)
    alt_paper_bench.to_csv(RESULTS_DIR / "figure6_paper_metadata_benchmark_dataset.csv", index=False)
    alt_collection_bench.to_csv(RESULTS_DIR / "figure6_collection_metadata_benchmark_dataset.csv", index=False)

    benchmark_results, benchmark_best = build_alt_benchmark_tables(alt_paper_bench, alt_collection_bench)
    benchmark_results.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_benchmark.csv", index=False)
    benchmark_best.to_csv(RESULTS_DIR / "literature_metadata_supervised_model_best.csv", index=False)
    write_figure6_outputs(benchmark_best)

    write_figure7_outputs(paper_metrics_df)
    write_figure8_outputs(collection_metrics_df, benchmark_results)


if __name__ == "__main__":
    main()
