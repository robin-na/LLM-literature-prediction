from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"
REPEAT_ROWS_CSV = RESULTS_DIR / "incremental_pgg_science_repeat_rows.csv"
ENSEMBLE30_CSV = RESULTS_DIR / "incremental_pgg_science_ensemble_correlation_summary.csv"

VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
Q_COLS = [f"Q{i}" for i in range(1, 21)]
CONDITION_ORDER = ["baseline", "science_gpt41", "science_gpt51"]
MODEL_ORDER = [
    "Claude Sonnet 4.6",
    "GPT-5.1",
    "GPT-4.1",
    "Claude Haiku 4.5",
    "Claude Opus 4.6",
    "GPT-5 Nano",
    "GPT-5 Mini",
    "GPT-4.1 Nano",
    "Gemini 2.5 Pro",
]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "PGG Science report (GPT-4.1)",
    "science_gpt51": "PGG Science report (GPT-5.1)",
}

N_MONTE_CARLO = 20000
CHUNK_SIZE = 2000
TOLERANCES = [0.01, 0.02, 0.05]


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


def _truth_vector() -> np.ndarray:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    return validation["efficiency_p"].to_numpy(dtype=float) * 100.0


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


def sample_without_replacement_indices(
    rng: np.random.Generator,
    *,
    n_runs: int,
    sample_size: int,
    n_samples: int,
) -> np.ndarray:
    random_keys = rng.random((n_samples, n_runs))
    order = np.argpartition(random_keys, kth=sample_size - 1, axis=1)[:, :sample_size]
    return order.astype(np.int16, copy=False)


def simulate_k_distribution(
    prediction_matrix: np.ndarray,
    truth: np.ndarray,
    *,
    sample_size: int,
    n_samples: int,
    seed: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n_runs = prediction_matrix.shape[0]
    corrs: list[np.ndarray] = []
    remaining = n_samples
    while remaining > 0:
        batch = min(CHUNK_SIZE, remaining)
        subset_idx = sample_without_replacement_indices(
            rng,
            n_runs=n_runs,
            sample_size=sample_size,
            n_samples=batch,
        )
        mean_preds = prediction_matrix[subset_idx].mean(axis=1)
        corrs.append(corr_rows(mean_preds, truth))
        remaining -= batch
    return np.concatenate(corrs, axis=0)


def summarize(values: np.ndarray) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    return {
        "count": int(arr.size),
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=0)),
        "p05": float(np.quantile(arr, 0.05)),
        "p10": float(np.quantile(arr, 0.10)),
        "p25": float(np.quantile(arr, 0.25)),
        "p50": float(np.quantile(arr, 0.50)),
        "p75": float(np.quantile(arr, 0.75)),
        "p90": float(np.quantile(arr, 0.90)),
        "p95": float(np.quantile(arr, 0.95)),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def build_size_curve_tables() -> tuple[pd.DataFrame, pd.DataFrame]:
    repeat_rows = load_repeat_rows()
    ensemble30 = load_ensemble30().set_index(["model", "condition"])
    truth = _truth_vector()

    curve_rows: list[dict[str, object]] = []
    threshold_rows: list[dict[str, object]] = []

    for model_idx, model in enumerate(MODEL_ORDER):
        for condition_idx, condition in enumerate(CONDITION_ORDER):
            sub = repeat_rows.loc[
                (repeat_rows["model"] == model) & (repeat_rows["condition"] == condition),
                ["repeat", "correlation", *Q_COLS],
            ].sort_values("repeat")
            if sub.empty:
                continue
            pred_mat = sub.loc[:, Q_COLS].to_numpy(dtype=float)
            single_run_corr_mean = float(sub["correlation"].mean())
            ensemble30_corr = float(ensemble30.loc[(model, condition), "correlation"])
            if pred_mat.shape != (30, 20):
                raise ValueError(f"Expected 30x20 matrix for {model} / {condition}, got {pred_mat.shape}")

            model_curve_rows: list[dict[str, object]] = []
            for k in range(1, 31):
                if k == 30:
                    dist = np.full(1, ensemble30_corr, dtype=float)
                else:
                    dist = simulate_k_distribution(
                        pred_mat,
                        truth,
                        sample_size=k,
                        n_samples=N_MONTE_CARLO,
                        seed=100_000 + 1000 * model_idx + 100 * condition_idx + k,
                    )
                summary = summarize(dist)
                abs_gap = np.abs(dist - ensemble30_corr)
                model_curve_rows.append(
                    {
                        "model": model,
                        "condition": condition,
                        "k_runs": k,
                        "single_run_corr_mean": single_run_corr_mean,
                        "ensemble30_correlation": ensemble30_corr,
                        **summary,
                        "mean_gap_to_ensemble30": float(ensemble30_corr - summary["mean"]),
                        "mean_abs_gap_to_ensemble30": float(abs_gap.mean()),
                        "p50_abs_gap_to_ensemble30": float(np.quantile(abs_gap, 0.50)),
                        "p80_abs_gap_to_ensemble30": float(np.quantile(abs_gap, 0.80)),
                        "p90_abs_gap_to_ensemble30": float(np.quantile(abs_gap, 0.90)),
                        "p95_abs_gap_to_ensemble30": float(np.quantile(abs_gap, 0.95)),
                    }
                )

            curve_rows.extend(model_curve_rows)
            model_curve = pd.DataFrame(model_curve_rows)
            for tol in TOLERANCES:
                mean_gap_hits = model_curve.loc[model_curve["mean_abs_gap_to_ensemble30"] <= tol, "k_runs"]
                p90_hits = model_curve.loc[model_curve["p90_abs_gap_to_ensemble30"] <= tol, "k_runs"]
                p95_hits = model_curve.loc[model_curve["p95_abs_gap_to_ensemble30"] <= tol, "k_runs"]
                threshold_rows.append(
                    {
                        "model": model,
                        "condition": condition,
                        "tolerance": tol,
                        "min_k_mean_abs_gap": int(mean_gap_hits.iloc[0]) if not mean_gap_hits.empty else pd.NA,
                        "min_k_p90_abs_gap": int(p90_hits.iloc[0]) if not p90_hits.empty else pd.NA,
                        "min_k_p95_abs_gap": int(p95_hits.iloc[0]) if not p95_hits.empty else pd.NA,
                    }
                )

    curve_df = pd.DataFrame(curve_rows)
    curve_df["model"] = pd.Categorical(curve_df["model"], categories=MODEL_ORDER, ordered=True)
    curve_df["condition"] = pd.Categorical(curve_df["condition"], categories=CONDITION_ORDER, ordered=True)
    curve_df = curve_df.sort_values(["condition", "model", "k_runs"]).reset_index(drop=True)

    threshold_df = pd.DataFrame(threshold_rows)
    threshold_df["model"] = pd.Categorical(threshold_df["model"], categories=MODEL_ORDER, ordered=True)
    threshold_df["condition"] = pd.Categorical(threshold_df["condition"], categories=CONDITION_ORDER, ordered=True)
    threshold_df = threshold_df.sort_values(["condition", "tolerance", "model"]).reset_index(drop=True)
    return curve_df, threshold_df


def plot_size_curve(curve_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(3, 3, figsize=(15.5, 11.5), sharex=True, sharey=False)
    axes = axes.flatten()

    for ax, model in zip(axes, MODEL_ORDER):
        part = curve_df.loc[curve_df["model"] == model].copy()
        if part.empty:
            ax.axis("off")
            continue
        for condition, color in [
            ("baseline", "#9ca3af"),
            ("science_gpt41", "#2563eb"),
            ("science_gpt51", "#f28e2b"),
        ]:
            sub = part.loc[part["condition"] == condition].copy()
            ax.plot(sub["k_runs"], sub["mean"], color=color, linewidth=2.0, label=CONDITION_LABELS[condition])
            ax.fill_between(
                sub["k_runs"],
                sub["p10"],
                sub["p90"],
                color=color,
                alpha=0.16,
                linewidth=0,
            )
            ax.scatter(
                [30],
                [float(sub.loc[sub["k_runs"] == 30, "ensemble30_correlation"].iloc[0])],
                color=color,
                s=18,
                zorder=3,
            )
        ax.set_title(model, fontsize=11)
        ax.set_xlim(1, 30)
        ax.set_xticks([1, 3, 5, 10, 15, 20, 25, 30])
        ax.grid(False)

    for ax in axes[6:]:
        ax.set_xlabel("Number of runs averaged")
    for ax in axes[::3]:
        ax.set_ylabel("Correlation")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.01))
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ensemble_size_curve.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_ensemble_size_curve.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    curve_df, threshold_df = build_size_curve_tables()
    curve_df.to_csv(RESULTS_DIR / "incremental_pgg_science_ensemble_size_curve.csv", index=False)
    threshold_df.to_csv(RESULTS_DIR / "incremental_pgg_science_ensemble_size_thresholds.csv", index=False)
    plot_size_curve(curve_df)


if __name__ == "__main__":
    main()
