from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[1]
VAL_CSV = ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
PAPER_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_avg_predictions.csv"
)
COLLECTION_AVG_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_avg_predictions.csv"
)

RESULTS_DIR = ROOT / "results" / "paper" / "robustness"
PLOTS_DIR = ROOT / "plots" / "paper" / "exploratory"

MODELS = ["GPT-5 Mini", "GPT-5 Nano", "GPT-4.1", "GPT-4.1 Mini", "GPT-5.1"]
Q_COLS = [f"Q{i}" for i in range(1, 21)]
N_BOOT = 1000
BOOT_SEED = 20260331
Z_95 = 1.959963984540054


def load_truth() -> np.ndarray:
    return (
        pd.read_csv(VAL_CSV)
        .sort_values("CONFIG_configId")["treatment_itt_efficiency"]
        .to_numpy(dtype=np.float32)
        * 100.0
    )


def load_paper_matrix(model: str) -> tuple[pd.Index, np.ndarray]:
    df = pd.read_csv(PAPER_AVG_CSV)
    df = df.loc[df["model"] == model, ["source_id", *Q_COLS]].copy()
    df = df.sort_values("source_id").reset_index(drop=True)
    return pd.Index(df["source_id"]), df[Q_COLS].to_numpy(dtype=np.float32)


def load_collection_matrix(model: str) -> tuple[pd.Index, np.ndarray]:
    df = pd.read_csv(COLLECTION_AVG_CSV)
    df = df.loc[
        (df["model"] == model) & (~df["variant_kind"].eq("benchmark_paper")) & (~df["variant_group"].eq("all_papers")),
        ["variant_id", "variant_group", *Q_COLS],
    ].copy()
    df = df.loc[df["variant_group"] == "metadata_filter"].sort_values("variant_id").reset_index(drop=True)
    return pd.Index(df["variant_id"]), df[Q_COLS].to_numpy(dtype=np.float32)


def rowwise_corr(preds: np.ndarray, truth: np.ndarray) -> np.ndarray:
    preds = preds.astype(np.float32, copy=False)
    truth = truth.astype(np.float32, copy=False)
    pred_center = preds - preds.mean(axis=1, keepdims=True)
    truth_center = truth - truth.mean()
    numer = np.sum(pred_center * truth_center[None, :], axis=1)
    denom = np.sqrt(np.sum(pred_center**2, axis=1) * np.sum(truth_center**2))
    return np.divide(
        numer,
        denom,
        out=np.full(preds.shape[0], np.nan, dtype=np.float32),
        where=denom > 0,
    )


def bootstrap_corrs(preds: np.ndarray, truth: np.ndarray, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n_items, n_questions = preds.shape
    out = np.empty((N_BOOT, n_items), dtype=np.float32)
    for b in range(N_BOOT):
        idx = rng.integers(0, n_questions, size=n_questions)
        out[b] = rowwise_corr(preds[:, idx], truth[idx])
    return out


def ci_order_matrices(preds: np.ndarray, truth: np.ndarray, seed: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    obs = rowwise_corr(preds, truth)
    boot = bootstrap_corrs(preds, truth, seed=seed)
    cov = np.cov(boot, rowvar=False, ddof=1).astype(np.float32)
    var = np.diag(cov).astype(np.float32)
    obs_diff = obs[:, None] - obs[None, :]
    se_diff = np.sqrt(np.maximum(var[:, None] + var[None, :] - 2.0 * cov, 0.0), dtype=np.float32)
    informative = np.abs(obs_diff) > (Z_95 * se_diff)
    np.fill_diagonal(informative, False)
    sign = np.zeros_like(obs_diff, dtype=np.int8)
    sign[obs_diff > 0] = 1
    sign[obs_diff < 0] = -1
    sign[~informative] = 0
    return obs.astype(np.float32), informative, sign


def pairwise_rows(
    *,
    kind: str,
    ids: pd.Index,
    corr_by_model: dict[str, np.ndarray],
    informative_by_model: dict[str, np.ndarray],
    sign_by_model: dict[str, np.ndarray],
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    iu = np.triu_indices(len(ids), k=1)
    top_k = max(1, round(len(ids) * 0.10))
    for model_a, model_b in combinations(MODELS, 2):
        corr_a = corr_by_model[model_a]
        corr_b = corr_by_model[model_b]
        inf_a = informative_by_model[model_a][iu]
        inf_b = informative_by_model[model_b][iu]
        sign_a = sign_by_model[model_a][iu]
        sign_b = sign_by_model[model_b][iu]
        common_inf = inf_a & inf_b

        top_a = set(ids[np.argsort(corr_a)[-top_k:]])
        top_b = set(ids[np.argsort(corr_b)[-top_k:]])

        rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": len(ids),
                "spearman_rank_corr": float(spearmanr(corr_a, corr_b).statistic),
                "pearson_value_corr": float(np.corrcoef(corr_a, corr_b)[0, 1]),
                "ci_aware_order_agreement": float((sign_a[common_inf] == sign_b[common_inf]).mean()),
                "ci_aware_pair_coverage": float(common_inf.mean()),
                "top_10_pct_jaccard": float(len(top_a & top_b) / len(top_a | top_b)),
            }
        )
    return pd.DataFrame(rows)


def summary_rows(pairwise_df: pd.DataFrame) -> pd.DataFrame:
    metric_cols = [
        "spearman_rank_corr",
        "pearson_value_corr",
        "ci_aware_order_agreement",
        "ci_aware_pair_coverage",
        "top_10_pct_jaccard",
    ]
    return pairwise_df.groupby("kind", as_index=False)[metric_cols].mean()


def build_matrix(pairwise_df: pd.DataFrame, metric: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODELS)), index=MODELS, columns=MODELS)
    for row in pairwise_df.itertuples(index=False):
        value = getattr(row, metric)
        matrix.loc[row.model_a, row.model_b] = value
        matrix.loc[row.model_b, row.model_a] = value
    return matrix


def draw_heatmap(ax: plt.Axes, matrix: pd.DataFrame, title: str, ylabel: str = "") -> None:
    sns.heatmap(
        matrix,
        ax=ax,
        cmap="YlGnBu",
        vmin=0,
        vmax=1,
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


def plot_heatmaps(pairwise_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8))
    specs = [
        ("papers", "spearman_rank_corr", "Exact rank\n(Spearman ρ)", "Individual papers"),
        ("papers", "ci_aware_order_agreement", "CI-aware order\n(95% interval)", ""),
        ("collections", "spearman_rank_corr", "Exact rank\n(Spearman ρ)", "Collections"),
        ("collections", "ci_aware_order_agreement", "CI-aware order\n(95% interval)", ""),
    ]
    for ax, (kind, metric, title, ylabel) in zip(axes.flatten(), specs):
        sub = pairwise_df.loc[pairwise_df["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, metric), title, ylabel)
    fig.text(
        0.5,
        0.02,
        "CI-aware order counts an item pair only when a bootstrap-SE-based 95% interval for the correlation difference excludes 0.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(PLOTS_DIR / "cross_model_ci_aware_robustness_correlation.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "cross_model_ci_aware_robustness_correlation.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


def analyze_kind(
    kind: str,
    loader,
    truth: np.ndarray,
    seed_offset: int,
) -> pd.DataFrame:
    loaded: dict[str, tuple[pd.Index, np.ndarray]] = {}
    common_ids: set[str] | None = None

    for model in MODELS:
        ids, preds = loader(model)
        loaded[model] = (ids, preds)
        ids_set = set(ids.tolist())
        common_ids = ids_set if common_ids is None else (common_ids & ids_set)

    assert common_ids is not None
    common_ids_index = pd.Index(sorted(common_ids))

    corr_by_model: dict[str, np.ndarray] = {}
    informative_by_model: dict[str, np.ndarray] = {}
    sign_by_model: dict[str, np.ndarray] = {}

    for idx, model in enumerate(MODELS):
        ids, preds = loaded[model]
        reindexer = ids.get_indexer(common_ids_index)
        preds = preds[reindexer]
        obs, informative, sign = ci_order_matrices(preds, truth, seed=BOOT_SEED + seed_offset + idx)
        corr_by_model[model] = obs
        informative_by_model[model] = informative
        sign_by_model[model] = sign

    return pairwise_rows(
        kind=kind,
        ids=common_ids_index,
        corr_by_model=corr_by_model,
        informative_by_model=informative_by_model,
        sign_by_model=sign_by_model,
    )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    truth = load_truth()
    paper_rows = analyze_kind("papers", load_paper_matrix, truth, seed_offset=0)
    collection_rows = analyze_kind("collections", load_collection_matrix, truth, seed_offset=1000)
    pairwise_df = pd.concat([paper_rows, collection_rows], ignore_index=True)
    summary_df = summary_rows(pairwise_df)
    pairwise_df.to_csv(RESULTS_DIR / "cross_model_ci_aware_robustness_pairwise_metrics.csv", index=False)
    summary_df.to_csv(RESULTS_DIR / "cross_model_ci_aware_robustness_summary.csv", index=False)
    plot_heatmaps(pairwise_df)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
