from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[1]
VAL_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"
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
N_BOOT = 500
SEED = 20260331


def load_truth() -> np.ndarray:
    return (
        pd.read_csv(VAL_CSV)
        .sort_values("CONFIG_configId")["treatment_itt_efficiency"]
        .to_numpy(dtype=np.float32)
        * 100.0
    )


def load_paper_scores(model: str, truth: np.ndarray) -> tuple[pd.Index, np.ndarray]:
    df = pd.read_csv(PAPER_AVG_CSV)
    df = df.loc[df["model"] == model, ["source_id", *Q_COLS]].copy()
    df = df.sort_values("source_id").reset_index(drop=True)
    preds = df[Q_COLS].to_numpy(dtype=np.float32)
    return pd.Index(df["source_id"]), rowwise_corr(preds, truth)


def load_collection_scores(model: str, truth: np.ndarray) -> tuple[pd.Index, np.ndarray]:
    df = pd.read_csv(COLLECTION_AVG_CSV)
    df = df.loc[
        (df["model"] == model)
        & (df["variant_group"] == "metadata_filter"),
        ["variant_id", *Q_COLS],
    ].copy()
    df = df.sort_values("variant_id").reset_index(drop=True)
    preds = df[Q_COLS].to_numpy(dtype=np.float32)
    return pd.Index(df["variant_id"]), rowwise_corr(preds, truth)


def rowwise_corr(preds: np.ndarray, truth: np.ndarray) -> np.ndarray:
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


def bootstrap_score_matrix(preds: np.ndarray, truth: np.ndarray, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    n_items, n_q = preds.shape
    scores_a = np.empty((N_BOOT, n_items), dtype=np.float32)
    scores_b = np.empty((N_BOOT, n_items), dtype=np.float32)
    for b in range(N_BOOT):
        idx_a = rng.integers(0, n_q, size=n_q)
        idx_b = rng.integers(0, n_q, size=n_q)
        scores_a[b] = rowwise_corr(preds[:, idx_a], truth[idx_a])
        scores_b[b] = rowwise_corr(preds[:, idx_b], truth[idx_b])
    return scores_a, scores_b


def estimate_rank_reliability(preds: np.ndarray, truth: np.ndarray, seed: int) -> dict[str, float]:
    scores_a, scores_b = bootstrap_score_matrix(preds, truth, seed)
    rhos = np.empty(N_BOOT, dtype=np.float32)
    for b in range(N_BOOT):
        rhos[b] = float(spearmanr(scores_a[b], scores_b[b]).statistic)
    return {
        "rank_reliability_mean": float(np.nanmean(rhos)),
        "rank_reliability_sd": float(np.nanstd(rhos, ddof=1)),
    }


def align_frames(frames: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    common_ids: set[str] | None = None
    for df in frames.values():
        ids = set(df.index.tolist())
        common_ids = ids if common_ids is None else (common_ids & ids)
    assert common_ids is not None
    common_index = pd.Index(sorted(common_ids))
    return {model: df.reindex(common_index) for model, df in frames.items()}


def prepare_kind(kind: str, truth: np.ndarray) -> tuple[pd.Index, dict[str, np.ndarray], dict[str, np.ndarray]]:
    raw_preds: dict[str, np.ndarray] = {}
    score_frames: dict[str, pd.DataFrame] = {}
    if kind == "papers":
        path = PAPER_AVG_CSV
        id_col = "source_id"
        filter_mask = None
    else:
        path = COLLECTION_AVG_CSV
        id_col = "variant_id"
        filter_mask = "variant_group == 'metadata_filter'"

    df = pd.read_csv(path)
    if filter_mask:
        df = df.query(filter_mask)

    for model in MODELS:
        part = df.loc[df["model"] == model, [id_col, *Q_COLS]].copy().sort_values(id_col)
        ids = pd.Index(part[id_col])
        preds = part[Q_COLS].to_numpy(dtype=np.float32)
        raw_preds[model] = preds
        score_frames[model] = pd.DataFrame({"score": rowwise_corr(preds, truth)}, index=ids)

    aligned = align_frames(score_frames)
    common_ids = next(iter(aligned.values())).index
    aligned_scores = {model: df["score"].to_numpy(dtype=np.float32) for model, df in aligned.items()}
    aligned_preds = {}
    for model in MODELS:
        part = df.loc[df["model"] == model, [id_col, *Q_COLS]].copy().sort_values(id_col).set_index(id_col)
        aligned_preds[model] = part.reindex(common_ids)[Q_COLS].to_numpy(dtype=np.float32)
    return common_ids, aligned_scores, aligned_preds


def analyze_kind(kind: str, truth: np.ndarray) -> tuple[pd.DataFrame, pd.DataFrame]:
    ids, scores, preds = prepare_kind(kind, truth)

    reliability_rows = []
    reliability = {}
    for idx, model in enumerate(MODELS):
        rel = estimate_rank_reliability(preds[model], truth, seed=SEED + idx + (0 if kind == "papers" else 1000))
        reliability[model] = rel["rank_reliability_mean"]
        reliability_rows.append(
            {
                "kind": kind,
                "model": model,
                "n_items": len(ids),
                **rel,
            }
        )

    pairwise_rows = []
    for model_a, model_b in combinations(MODELS, 2):
        obs = float(spearmanr(scores[model_a], scores[model_b]).statistic)
        ceiling = float(np.sqrt(reliability[model_a] * reliability[model_b]))
        pairwise_rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": len(ids),
                "observed_spearman": obs,
                "rank_ceiling": ceiling,
                "ceiling_fraction": float(obs / ceiling) if ceiling > 0 else np.nan,
            }
        )

    return pd.DataFrame(reliability_rows), pd.DataFrame(pairwise_rows)


def build_matrix(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    matrix = pd.DataFrame(np.eye(len(MODELS)), index=MODELS, columns=MODELS)
    for row in df.itertuples(index=False):
        val = getattr(row, value_col)
        matrix.loc[row.model_a, row.model_b] = val
        matrix.loc[row.model_b, row.model_a] = val
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


def plot(pairwise_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8))
    specs = [
        ("papers", "observed_spearman", "Observed exact-rank\n(Spearman ρ)", "Individual papers"),
        ("papers", "rank_ceiling", "Within-model rank\nceiling", ""),
        ("collections", "observed_spearman", "Observed exact-rank\n(Spearman ρ)", "Collections"),
        ("collections", "rank_ceiling", "Within-model rank\nceiling", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = pairwise_df.loc[pairwise_df["kind"] == kind]
        draw_heatmap(ax, build_matrix(sub, value_col), title, ylabel)
    fig.text(
        0.5,
        0.02,
        "Rank ceiling is estimated from within-model bootstrap reproducibility of usefulness rankings across the 20 validation questions.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(PLOTS_DIR / "cross_model_rank_ceiling.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "cross_model_rank_ceiling.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    truth = load_truth()
    paper_rel, paper_pair = analyze_kind("papers", truth)
    col_rel, col_pair = analyze_kind("collections", truth)
    reliability_df = pd.concat([paper_rel, col_rel], ignore_index=True)
    pairwise_df = pd.concat([paper_pair, col_pair], ignore_index=True)
    summary_df = (
        pairwise_df.groupby("kind", as_index=False)[["observed_spearman", "rank_ceiling", "ceiling_fraction"]]
        .mean()
    )
    reliability_df.to_csv(RESULTS_DIR / "cross_model_rank_ceiling_reliability.csv", index=False)
    pairwise_df.to_csv(RESULTS_DIR / "cross_model_rank_ceiling_pairwise.csv", index=False)
    summary_df.to_csv(RESULTS_DIR / "cross_model_rank_ceiling_summary.csv", index=False)
    plot(pairwise_df)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
