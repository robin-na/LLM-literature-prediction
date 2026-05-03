from __future__ import annotations

import os
from itertools import combinations
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

PAPER_METRICS_CSV = RESULTS_DIR / "paper_repeat_correlation_metrics.csv"
COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"

FIGURE5_MODEL_ORDER = ["GPT-5.1", "GPT-4.1 Mini", "GPT-4.1", "GPT-5 Nano", "GPT-5 Mini", "Claude Sonnet 4.6", "Gemini 2.5 Pro"]


def assign_rank_deciles(scores: np.ndarray) -> np.ndarray:
    order = pd.Series(scores).rank(method="first", ascending=True).to_numpy(dtype=float)
    deciles = np.ceil(order * 10.0 / len(scores)).astype(int)
    return np.clip(deciles, 1, 10)


def jaccard(mask_a: np.ndarray, mask_b: np.ndarray) -> float:
    union = np.logical_or(mask_a, mask_b).sum()
    if union == 0:
        return float("nan")
    inter = np.logical_and(mask_a, mask_b).sum()
    return float(inter / union)


def build_pairwise_rows(metric_df: pd.DataFrame, *, kind: str, item_id_col: str) -> pd.DataFrame:
    wide = (
        metric_df.pivot(index=item_id_col, columns="model", values="correlation")
        .dropna()
        .reindex(columns=FIGURE5_MODEL_ORDER)
    )

    rows: list[dict[str, float | str | int]] = []
    for model_a, model_b in combinations(FIGURE5_MODEL_ORDER, 2):
        scores_a = wide[model_a].to_numpy(dtype=float)
        scores_b = wide[model_b].to_numpy(dtype=float)
        deciles_a = assign_rank_deciles(scores_a)
        deciles_b = assign_rank_deciles(scores_b)

        top_overlap = jaccard(deciles_a == 10, deciles_b == 10)
        bottom_overlap = jaccard(deciles_a == 1, deciles_b == 1)
        mean_abs_gap = float(np.mean(np.abs(deciles_a - deciles_b)))
        tau_b = float(stats.kendalltau(deciles_a, deciles_b, variant="b").statistic)

        rows.append(
            {
                "kind": kind,
                "model_a": model_a,
                "model_b": model_b,
                "n_items": int(len(wide)),
                "spearman_rho": float(stats.spearmanr(scores_a, scores_b).statistic),
                "kendall_tau_b_deciles": tau_b,
                "exact_decile_agreement": float(np.mean(deciles_a == deciles_b)),
                "within_one_decile_agreement": float(np.mean(np.abs(deciles_a - deciles_b) <= 1)),
                "mean_abs_decile_gap": mean_abs_gap,
                "scaled_decile_proximity": float(1.0 - mean_abs_gap / 9.0),
                "top_decile_jaccard": top_overlap,
                "bottom_decile_jaccard": bottom_overlap,
                "extreme_decile_jaccard_mean": float(np.nanmean([top_overlap, bottom_overlap])),
            }
        )

    return pd.DataFrame(rows)


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
        annot_kws={"fontsize": 8.5},
    )
    ax.set_title(title, fontsize=11, pad=7)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.tick_params(axis="y", rotation=0, labelsize=9)


def main() -> None:
    sns.set_theme(style="white", context="talk")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    paper_pairwise = build_pairwise_rows(pd.read_csv(PAPER_METRICS_CSV), kind="papers", item_id_col="source_id")
    collection_pairwise = build_pairwise_rows(
        pd.read_csv(COLLECTION_METRICS_CSV),
        kind="collections",
        item_id_col="variant_id",
    )
    pairwise = pd.concat([paper_pairwise, collection_pairwise], ignore_index=True)

    summary = (
        pairwise.groupby("kind", as_index=False)[
            [
                "spearman_rho",
                "kendall_tau_b_deciles",
                "exact_decile_agreement",
                "within_one_decile_agreement",
                "scaled_decile_proximity",
                "top_decile_jaccard",
                "bottom_decile_jaccard",
                "extreme_decile_jaccard_mean",
            ]
        ]
        .mean()
        .rename(
            columns={
                "spearman_rho": "mean_spearman_rho",
                "kendall_tau_b_deciles": "mean_kendall_tau_b_deciles",
            }
        )
    )

    pairwise.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_deciles_pairwise.csv", index=False)
    summary.to_csv(RESULTS_DIR / "figure5_cross_model_rank_robustness_deciles_summary.csv", index=False)

    fig, axes = plt.subplots(2, 5, figsize=(20.0, 7.8))
    specs = [
        ("papers", "kendall_tau_b_deciles", "Kendall tau-b\n(deciles)", "Individual papers"),
        ("papers", "exact_decile_agreement", "Exact decile\nmatch", "Individual papers"),
        ("papers", "within_one_decile_agreement", "Within 1 decile", ""),
        ("papers", "top_decile_jaccard", "Top-decile\noverlap", ""),
        ("papers", "bottom_decile_jaccard", "Bottom-decile\noverlap", ""),
        ("collections", "kendall_tau_b_deciles", "Kendall tau-b\n(deciles)", "Collections"),
        ("collections", "exact_decile_agreement", "Exact decile\nmatch", "Collections"),
        ("collections", "within_one_decile_agreement", "Within 1 decile", ""),
        ("collections", "top_decile_jaccard", "Top-decile\noverlap", ""),
        ("collections", "bottom_decile_jaccard", "Bottom-decile\noverlap", ""),
    ]
    for ax, (kind, value_col, title, ylabel) in zip(axes.flatten(), specs):
        sub = pairwise.loc[pairwise["kind"] == kind]
        matrix = build_matrix(sub, value_col)
        if value_col == "kendall_tau_b_deciles":
            sns.heatmap(
                matrix,
                ax=ax,
                cmap="RdBu_r",
                vmin=-1.0,
                vmax=1.0,
                annot=True,
                fmt=".2f",
                cbar=False,
                square=True,
                linewidths=0.6,
                linecolor="white",
                annot_kws={"fontsize": 8.5},
            )
            ax.set_title(title, fontsize=11, pad=7)
            ax.set_xlabel("")
            ax.set_ylabel(ylabel, fontsize=12 if ylabel else 10)
            ax.tick_params(axis="x", rotation=45, labelsize=9)
            ax.tick_params(axis="y", rotation=0, labelsize=9)
        else:
            draw_heatmap(ax, matrix, title, ylabel)

    fig.text(
        0.5,
        0.02,
        "Deciles are equal-count rank bins computed separately within each model over pairwise shared items. "
        "Overlap uses Jaccard similarity of decile-10 or decile-1 item sets.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"figure5_cross_model_rank_robustness_deciles.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
