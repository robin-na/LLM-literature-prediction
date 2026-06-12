from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

# Avoid matplotlib cache warnings when this script imports helper modules.
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

from plot_cross_model_repeat_rank_ceiling import (  # noqa: E402
    MODELS,
    common_ids,
    compute_repeat_scores,
    load_collection_repeat_predictions,
    load_paper_repeat_predictions,
    load_truth,
)


PAPER_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_sources_repeat5"
    / "validation_literature_analysis_report_source_significance.csv"
)
COLLECTION_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_metadata_filters"
    / "validation_literature_collection_analysis_report_metadata_filters_rows.csv"
)
RESULTS_DIR = ROOT / "results" / "paper" / "robustness"
PLOTS_DIR = ROOT / "plots" / "paper" / "exploratory"

Z_975 = 1.959963984540054


def simple_variance_decomposition(y: np.ndarray, se: np.ndarray) -> dict[str, float]:
    obs_var = float(np.var(y, ddof=1))
    noise_var = float(np.mean(se**2))
    hetero_var = float(max(0.0, obs_var - noise_var))
    obs_sd = float(np.sqrt(obs_var))
    noise_sd = float(np.sqrt(noise_var))
    hetero_sd = float(np.sqrt(hetero_var))
    return {
        "observed_sd": obs_sd,
        "noise_sd": noise_sd,
        "tau_simple": hetero_sd,
        "heterogeneity_share_simple": float(hetero_var / obs_var) if obs_var > 0 else np.nan,
        "observed_to_noise_sd_ratio": float(obs_sd / noise_sd) if noise_sd > 0 else np.nan,
    }


def dersimonian_laird(y: np.ndarray, se: np.ndarray) -> dict[str, float]:
    v = se**2
    w = 1.0 / v
    mu_fe = float(np.sum(w * y) / np.sum(w))
    q = float(np.sum(w * (y - mu_fe) ** 2))
    df_q = int(len(y) - 1)
    c = float(np.sum(w) - np.sum(w**2) / np.sum(w))
    tau2 = float(max(0.0, (q - df_q) / c))
    i2 = float(max(0.0, (q - df_q) / q)) if q > 0 else 0.0
    return {
        "tau_dl": float(np.sqrt(tau2)),
        "tau2_dl": tau2,
        "i2_dl": i2,
        "Q_dl": q,
        "Q_df_dl": df_q,
        "Q_p_dl": float(chi2.sf(q, df_q)),
    }


def question_bootstrap_rows(kind: str, df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model in MODELS:
        sub = df.loc[df["model"] == model].copy()
        y = sub["delta_correlation"].to_numpy(dtype=float)
        se = (
            (sub["delta_correlation_ci_high"] - sub["delta_correlation_ci_low"])
            / (2 * Z_975)
        ).to_numpy(dtype=float)
        mask = np.isfinite(y) & np.isfinite(se) & (se > 0)
        y = y[mask]
        se = se[mask]
        rows.append(
            {
                "kind": kind,
                "uncertainty_basis": "question_bootstrap",
                "model": model,
                "k": int(len(y)),
                "mean_delta_correlation": float(np.mean(y)),
                "mean_se": float(np.mean(se)),
                "median_se": float(np.median(se)),
                **simple_variance_decomposition(y, se),
                **dersimonian_laird(y, se),
            }
        )
    return pd.DataFrame(rows)


def repeat_rows(kind: str, repeat_predictions: dict[str, dict[str, pd.DataFrame]], baseline_map: dict[str, float]) -> pd.DataFrame:
    truth = load_truth()
    ids = common_ids(repeat_predictions)
    repeat_scores = compute_repeat_scores(repeat_predictions, truth, ids)
    rows = []
    for model in MODELS:
        mat = np.stack([repeat_scores[model][f"rep{i}"] for i in range(1, 6)], axis=1)
        y = mat.mean(axis=1) - baseline_map[model]
        se = mat.std(axis=1, ddof=1) / np.sqrt(mat.shape[1])
        mask = np.isfinite(y) & np.isfinite(se) & (se > 0)
        y = y[mask]
        se = se[mask]
        rows.append(
            {
                "kind": kind,
                "uncertainty_basis": "repeat_noise",
                "model": model,
                "k": int(len(y)),
                "mean_delta_correlation": float(np.mean(y)),
                "mean_se": float(np.mean(se)),
                "median_se": float(np.median(se)),
                **simple_variance_decomposition(y, se),
                **dersimonian_laird(y, se),
            }
        )
    return pd.DataFrame(rows)


def plot(summary_df: pd.DataFrame) -> None:
    plot_df = summary_df.copy()
    plot_df["row"] = plot_df["kind"].map({"papers": "Individual papers", "collections": "Collections"}) + "  |  " + plot_df["model"]
    plot_df["basis"] = plot_df["uncertainty_basis"].map(
        {
            "question_bootstrap": "Question bootstrap",
            "repeat_noise": "Repeat noise",
        }
    )

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 6.5))
    for ax, value_col, title in [
        (axes[0], "heterogeneity_share_simple", "Variance Share Beyond Noise"),
        (axes[1], "i2_dl", "Meta-analytic I²"),
    ]:
        heat = (
            plot_df.pivot(index="row", columns="basis", values=value_col)
            .reindex(
                [
                    f"Individual papers  |  {m}" for m in MODELS
                ]
                + [
                    f"Collections  |  {m}" for m in MODELS
                ]
            )
        )
        sns.heatmap(
            heat,
            ax=ax,
            cmap="YlGnBu",
            vmin=0,
            vmax=1,
            annot=True,
            fmt=".2f",
            cbar=False,
            linewidths=0.6,
            linecolor="white",
            annot_kws={"fontsize": 9},
        )
        ax.set_title(title, fontsize=13, pad=8)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.tick_params(axis="x", rotation=0, labelsize=10)
        ax.tick_params(axis="y", rotation=0, labelsize=9)

    fig.text(
        0.5,
        0.02,
        "Question-bootstrap uncertainty uses the paired 20-question CI already saved per item. Repeat-noise uncertainty uses within-item variation across the 5 augmentation repeats.",
        ha="center",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(PLOTS_DIR / "cross_model_meta_heterogeneity_correlation.png", dpi=300, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "cross_model_meta_heterogeneity_correlation.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

    papers = pd.read_csv(PAPER_CSV)
    collections = pd.read_csv(COLLECTION_CSV)
    collections = collections.loc[collections["variant_group"] == "metadata_filter"].copy()

    summary_df = pd.concat(
        [
            question_bootstrap_rows("papers", papers),
            question_bootstrap_rows("collections", collections),
            repeat_rows(
                "papers",
                load_paper_repeat_predictions(),
                papers.groupby("model")["baseline_correlation"].first().to_dict(),
            ),
            repeat_rows(
                "collections",
                load_collection_repeat_predictions(),
                collections.groupby("model")["baseline_correlation"].first().to_dict(),
            ),
        ],
        ignore_index=True,
    )

    overall_df = (
        summary_df.groupby(["kind", "uncertainty_basis"], as_index=False)[
            [
                "k",
                "observed_sd",
                "noise_sd",
                "tau_simple",
                "heterogeneity_share_simple",
                "observed_to_noise_sd_ratio",
                "tau_dl",
                "i2_dl",
            ]
        ]
        .mean()
    )

    summary_df.to_csv(RESULTS_DIR / "cross_model_meta_heterogeneity_correlation_summary.csv", index=False)
    overall_df.to_csv(RESULTS_DIR / "cross_model_meta_heterogeneity_correlation_overall.csv", index=False)
    plot(summary_df)


if __name__ == "__main__":
    sns.set_theme(style="white", context="talk")
    main()
