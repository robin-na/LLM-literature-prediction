from __future__ import annotations

import os
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"
REPEAT_ROWS_CSV = RESULTS_DIR / "incremental_pgg_science_repeat_rows.csv"
ENSEMBLE30_CSV = RESULTS_DIR / "incremental_pgg_science_ensemble_correlation_summary.csv"

VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
Q_COLS = [f"Q{i}" for i in range(1, 21)]
CONDITION_ORDER = ["baseline", "science_gpt41", "science_gpt51"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "PGG Science report (GPT-4.1)",
    "science_gpt51": "PGG Science report (GPT-5.1)",
}

MODEL_ORDER = [
    "Claude Sonnet 4.6",
    "GPT-5.1",
    "Gemini 2.5 Flash",
    "GPT-4.1 Mini",
    "GPT-4.1",
    "Claude Haiku 4.5",
    "Claude Opus 4.6",
    "GPT-5 Nano",
    "GPT-5 Mini",
    "GPT-4.1 Nano",
    "Gemini 2.5 Pro",
]

SUBSET_K = 5
BOOTSTRAP_DRAWS = 50000
CHUNK_SIZE = 5000


def _truth_vector() -> np.ndarray:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    return validation["efficiency_p"].to_numpy(dtype=float) * 100.0


def corr_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    mat = np.asarray(mat, dtype=float)
    truth = np.asarray(truth, dtype=float)
    centered_mat = mat - mat.mean(axis=1, keepdims=True)
    centered_truth = truth - truth.mean()
    denom = np.sqrt((centered_mat**2).sum(axis=1) * (centered_truth**2).sum())
    out = np.full(mat.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (centered_mat[valid] @ centered_truth) / denom[valid]
    return out


def summarize_distribution(values: np.ndarray) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return {
            "count": 0,
            "mean": float("nan"),
            "sd": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
            "p01": float("nan"),
            "p05": float("nan"),
            "p10": float("nan"),
            "p25": float("nan"),
            "p50": float("nan"),
            "p75": float("nan"),
            "p90": float("nan"),
            "p95": float("nan"),
            "p99": float("nan"),
        }
    return {
        "count": int(arr.size),
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=0)),
        "min": float(arr.min()),
        "max": float(arr.max()),
        "p01": float(np.quantile(arr, 0.01)),
        "p05": float(np.quantile(arr, 0.05)),
        "p10": float(np.quantile(arr, 0.10)),
        "p25": float(np.quantile(arr, 0.25)),
        "p50": float(np.quantile(arr, 0.50)),
        "p75": float(np.quantile(arr, 0.75)),
        "p90": float(np.quantile(arr, 0.90)),
        "p95": float(np.quantile(arr, 0.95)),
        "p99": float(np.quantile(arr, 0.99)),
    }


def build_exact_subset_index(n_runs: int, subset_k: int) -> np.ndarray:
    combos = np.array(list(combinations(range(n_runs), subset_k)), dtype=np.int16)
    return combos


def exact_subensemble_correlations(
    prediction_matrix: np.ndarray,
    truth: np.ndarray,
    *,
    combos: np.ndarray,
    chunk_size: int = CHUNK_SIZE,
) -> np.ndarray:
    corrs: list[np.ndarray] = []
    for start in range(0, combos.shape[0], chunk_size):
        stop = min(start + chunk_size, combos.shape[0])
        chunk = combos[start:stop]
        mean_preds = prediction_matrix[chunk].mean(axis=1)
        corrs.append(corr_rows(mean_preds, truth))
    return np.concatenate(corrs, axis=0)


def bootstrap_subensemble_correlations(
    prediction_matrix: np.ndarray,
    truth: np.ndarray,
    *,
    subset_k: int,
    n_boot: int,
    seed: int,
    chunk_size: int = CHUNK_SIZE,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n_runs = prediction_matrix.shape[0]
    corrs: list[np.ndarray] = []
    remaining = n_boot
    while remaining > 0:
        batch = min(chunk_size, remaining)
        indices = rng.integers(0, n_runs, size=(batch, subset_k), endpoint=False)
        mean_preds = prediction_matrix[indices].mean(axis=1)
        corrs.append(corr_rows(mean_preds, truth))
        remaining -= batch
    return np.concatenate(corrs, axis=0)


def load_repeat_rows() -> pd.DataFrame:
    rows = pd.read_csv(REPEAT_ROWS_CSV)
    rows["model"] = pd.Categorical(rows["model"], categories=MODEL_ORDER, ordered=True)
    rows["condition"] = pd.Categorical(rows["condition"], categories=CONDITION_ORDER, ordered=True)
    return rows.sort_values(["condition", "model", "repeat"]).reset_index(drop=True)


def load_ensemble30() -> pd.DataFrame:
    df = pd.read_csv(ENSEMBLE30_CSV)
    df["model"] = pd.Categorical(df["model"], categories=MODEL_ORDER, ordered=True)
    df["condition"] = pd.Categorical(df["condition"], categories=CONDITION_ORDER, ordered=True)
    return df.sort_values(["condition", "model"]).reset_index(drop=True)


def build_subensemble_tables() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    repeat_rows = load_repeat_rows()
    ensemble30 = load_ensemble30()
    truth = _truth_vector()
    combos = build_exact_subset_index(n_runs=30, subset_k=SUBSET_K)

    exact_summary_rows: list[dict[str, object]] = []
    bootstrap_summary_rows: list[dict[str, object]] = []

    for model_idx, model in enumerate(MODEL_ORDER):
        for condition_idx, condition in enumerate(CONDITION_ORDER):
            sub = repeat_rows.loc[
                (repeat_rows["model"] == model) & (repeat_rows["condition"] == condition),
                ["repeat", *Q_COLS, "correlation"],
            ].sort_values("repeat")
            if sub.empty:
                continue
            pred_mat = sub.loc[:, Q_COLS].to_numpy(dtype=float)
            single_run_corrs = sub["correlation"].to_numpy(dtype=float)
            if pred_mat.shape != (30, 20):
                raise ValueError(f"Expected 30x20 matrix for {model} / {condition}, got {pred_mat.shape}")

            exact_corrs = exact_subensemble_correlations(pred_mat, truth, combos=combos)
            bootstrap_corrs = bootstrap_subensemble_correlations(
                pred_mat,
                truth,
                subset_k=SUBSET_K,
                n_boot=BOOTSTRAP_DRAWS,
                seed=10_000 + 100 * model_idx + condition_idx,
            )

            exact_summary = summarize_distribution(exact_corrs)
            bootstrap_summary = summarize_distribution(bootstrap_corrs)

            exact_summary_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "subset_k": SUBSET_K,
                    "distribution": "exact_without_replacement",
                    "single_run_corr_mean": float(single_run_corrs.mean()),
                    "single_run_corr_sd": float(single_run_corrs.std(ddof=1)),
                    **exact_summary,
                }
            )
            bootstrap_summary_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "subset_k": SUBSET_K,
                    "distribution": "bootstrap_with_replacement",
                    "single_run_corr_mean": float(single_run_corrs.mean()),
                    "single_run_corr_sd": float(single_run_corrs.std(ddof=1)),
                    **bootstrap_summary,
                }
            )

    exact_df = pd.DataFrame(exact_summary_rows)
    bootstrap_df = pd.DataFrame(bootstrap_summary_rows)

    comparison = (
        exact_df.merge(
            bootstrap_df,
            on=["model", "condition", "subset_k", "single_run_corr_mean", "single_run_corr_sd"],
            suffixes=("_exact", "_bootstrap"),
        )
        .merge(
            ensemble30.loc[:, ["model", "condition", "correlation", "ci_low", "ci_high"]].rename(
                columns={
                    "correlation": "ensemble30_correlation",
                    "ci_low": "ensemble30_ci_low",
                    "ci_high": "ensemble30_ci_high",
                }
            ),
            on=["model", "condition"],
            how="left",
        )
    )
    comparison["gain_k5_exact_vs_single"] = comparison["mean_exact"] - comparison["single_run_corr_mean"]
    comparison["gain_k5_bootstrap_vs_single"] = comparison["mean_bootstrap"] - comparison["single_run_corr_mean"]
    comparison["gain_ensemble30_vs_k5_exact"] = comparison["ensemble30_correlation"] - comparison["mean_exact"]
    comparison["gain_ensemble30_vs_k5_bootstrap"] = comparison["ensemble30_correlation"] - comparison["mean_bootstrap"]
    comparison["sampling_uncertainty_width90_exact"] = comparison["p95_exact"] - comparison["p05_exact"]
    comparison["sampling_uncertainty_width90_bootstrap"] = comparison["p95_bootstrap"] - comparison["p05_bootstrap"]
    comparison["model"] = pd.Categorical(comparison["model"], categories=MODEL_ORDER, ordered=True)
    comparison["condition"] = pd.Categorical(comparison["condition"], categories=CONDITION_ORDER, ordered=True)
    comparison = comparison.sort_values(["condition", "model"]).reset_index(drop=True)

    return (
        exact_df.sort_values(["condition", "mean", "model"], ascending=[True, False, True]).reset_index(drop=True),
        bootstrap_df.sort_values(["condition", "mean", "model"], ascending=[True, False, True]).reset_index(drop=True),
        comparison,
    )


def build_plot_rows(comparison: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, row in comparison.iterrows():
        rows.extend(
            [
                {
                    "model": row["model"],
                    "condition": row["condition"],
                    "series": "single_run_mean",
                    "value": row["single_run_corr_mean"],
                    "lo": np.nan,
                    "hi": np.nan,
                },
                {
                    "model": row["model"],
                    "condition": row["condition"],
                    "series": "k5_exact",
                    "value": row["mean_exact"],
                    "lo": row["p05_exact"],
                    "hi": row["p95_exact"],
                },
                {
                    "model": row["model"],
                    "condition": row["condition"],
                    "series": "ensemble30",
                    "value": row["ensemble30_correlation"],
                    "lo": row["ensemble30_ci_low"],
                    "hi": row["ensemble30_ci_high"],
                },
            ]
        )
    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "model", "series"]).reset_index(drop=True)


def plot_subensemble_summary(plot_rows: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 7.5), sharex=True, sharey=True)
    series_specs = {
        "single_run_mean": {"color": "#6b7280", "marker": "o", "label": "Mean single-run correlation"},
        "k5_exact": {"color": "#2563eb", "marker": "s", "label": "5-run ensemble mean (5th-95th pct)"},
        "ensemble30": {"color": "#f28e2b", "marker": "D", "label": "30-run ensemble correlation"},
    }

    for ax, condition in zip(axes, CONDITION_ORDER):
        part = plot_rows.loc[plot_rows["condition"] == condition].copy()
        model_order = list(reversed(MODEL_ORDER))
        y_positions = np.arange(len(model_order))
        y_map = {model: pos for pos, model in enumerate(model_order)}

        for series, x_offset in [("single_run_mean", -0.18), ("k5_exact", 0.0), ("ensemble30", 0.18)]:
            sub = part.loc[part["series"] == series].copy()
            y = np.array([y_map[str(model)] + x_offset for model in sub["model"]], dtype=float)
            spec = series_specs[series]
            if series == "k5_exact":
                ax.hlines(
                    y,
                    sub["lo"].to_numpy(dtype=float),
                    sub["hi"].to_numpy(dtype=float),
                    color=spec["color"],
                    linewidth=1.8,
                    alpha=0.9,
                    zorder=2,
                )
            elif series == "ensemble30":
                ax.hlines(
                    y,
                    sub["lo"].to_numpy(dtype=float),
                    sub["hi"].to_numpy(dtype=float),
                    color=spec["color"],
                    linewidth=1.3,
                    alpha=0.45,
                    zorder=1,
                )
            ax.scatter(
                sub["value"].to_numpy(dtype=float),
                y,
                s=42,
                color=spec["color"],
                marker=spec["marker"],
                edgecolor="white",
                linewidth=0.6,
                zorder=3,
            )

        ax.set_title(CONDITION_LABELS[condition], fontsize=12)
        ax.set_yticks(y_positions, model_order)
        ax.grid(False)
        ax.set_xlim(0.0, 1.0)
        ax.set_xticks(np.arange(0.0, 1.01, 0.1))
        ax.set_xlabel("Correlation")

    axes[0].set_ylabel("Model")

    legend_items = [
        Line2D([0], [0], marker=series_specs["single_run_mean"]["marker"], color="none", markerfacecolor=series_specs["single_run_mean"]["color"], markeredgecolor="white", markersize=7, label=series_specs["single_run_mean"]["label"]),
        Line2D([0], [0], marker=series_specs["k5_exact"]["marker"], color=series_specs["k5_exact"]["color"], markerfacecolor=series_specs["k5_exact"]["color"], markeredgecolor="white", markersize=7, linewidth=1.8, label=series_specs["k5_exact"]["label"]),
        Line2D([0], [0], marker=series_specs["ensemble30"]["marker"], color=series_specs["ensemble30"]["color"], markerfacecolor=series_specs["ensemble30"]["color"], markeredgecolor="white", markersize=7, linewidth=1.3, label=series_specs["ensemble30"]["label"]),
    ]
    fig.legend(handles=legend_items, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_k5_sampling_uncertainty.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_k5_sampling_uncertainty.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    exact_df, bootstrap_df, comparison = build_subensemble_tables()
    plot_rows = build_plot_rows(comparison)

    exact_df.to_csv(RESULTS_DIR / "incremental_pgg_science_k5_exact_summary.csv", index=False)
    bootstrap_df.to_csv(RESULTS_DIR / "incremental_pgg_science_k5_bootstrap_summary.csv", index=False)
    comparison.to_csv(RESULTS_DIR / "incremental_pgg_science_k5_vs_single_vs_ensemble30.csv", index=False)
    plot_rows.to_csv(RESULTS_DIR / "incremental_pgg_science_k5_plot_rows.csv", index=False)

    plot_subensemble_summary(plot_rows)


if __name__ == "__main__":
    main()
