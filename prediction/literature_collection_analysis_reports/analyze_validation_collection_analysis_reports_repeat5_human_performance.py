from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_human_performance"
LLM_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science_data" / "data" / "processed_data" / "prediction_survey.csv"
Q_COLS = [f"Q{i}" for i in range(1, 21)]
SOURCE_ORDER = ["sspp", "prolific"]
SOURCE_LABELS = {
    "sspp": "Experts",
    "prolific": "Laypeople",
}
MODEL_ORDER = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini"]
N_BOOTSTRAP = 4000
N_SUBCROWD = 5000
SUBCROWD_SIZE = 5


def summarize(values: np.ndarray) -> dict[str, float]:
    series = pd.Series(values, dtype=float)
    return {
        "n": int(series.size),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std": float(series.std(ddof=0)),
        "q10": float(series.quantile(0.10)),
        "q90": float(series.quantile(0.90)),
        "min": float(series.min()),
        "max": float(series.max()),
    }


def corr_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    centered_mat = mat - mat.mean(axis=1, keepdims=True)
    centered_truth = truth - truth.mean()
    denom = np.sqrt((centered_mat**2).sum(axis=1) * (centered_truth**2).sum())
    return (centered_mat @ centered_truth) / denom


def load_llm_baseline() -> tuple[pd.DataFrame, np.ndarray]:
    rows = pd.read_csv(LLM_REPEAT_ROWS_CSV)
    baseline = rows.loc[rows["condition"] == "baseline"].copy()
    mat = baseline[Q_COLS].to_numpy(dtype=float)
    return baseline, mat


def load_human_predictions() -> tuple[pd.DataFrame, np.ndarray]:
    rows = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    rows = rows.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth = (
        rows.loc[:, ["CONFIG_configId", "treatment_efficiency"]]
        .drop_duplicates()
        .sort_values("CONFIG_configId")
    )
    truth_vec = truth["treatment_efficiency"].to_numpy(dtype=float) * 100.0
    return rows, truth_vec


def build_human_matrix(rows: pd.DataFrame, source: str) -> pd.DataFrame:
    wide = (
        rows.loc[rows["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
        .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
        .sort_index()
    )
    return wide.loc[:, wide.notna().all(axis=0)]


def sample_subcrowd_corrs(mat: np.ndarray, truth: np.ndarray, *, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    players = np.arange(mat.shape[0])
    values: list[float] = []
    for _ in range(N_SUBCROWD):
        idx = rng.choice(players, size=SUBCROWD_SIZE, replace=False)
        values.append(float(np.corrcoef(mat[idx].mean(axis=0), truth)[0, 1]))
    return np.asarray(values, dtype=float)


def build_group_summary(llm_baseline: pd.DataFrame, llm_mat: np.ndarray, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []

    llm_corr = llm_baseline["correlation"].to_numpy(dtype=float)
    summary_rows.append(
        {
            "group": "LLM baseline repeats (pooled)",
            "kind": "llm_repeat",
            **summarize(llm_corr),
        }
    )
    for model, part in llm_baseline.groupby("model", observed=True):
        summary_rows.append(
            {
                "group": f"LLM baseline repeats ({model})",
                "kind": "llm_repeat",
                "model": model,
                **summarize(part["correlation"].to_numpy(dtype=float)),
            }
        )

    for seed, source in enumerate(SOURCE_ORDER):
        label = SOURCE_LABELS[source]
        wide = build_human_matrix(human_rows, source)
        mat = wide.to_numpy(dtype=float).T * 100.0
        participant_corr = corr_rows(mat, truth_vec)
        crowd_corr = float(np.corrcoef(mat.mean(axis=0), truth_vec)[0, 1])
        subcrowd_corr = sample_subcrowd_corrs(mat, truth_vec, seed=seed)

        summary_rows.append(
            {
                "group": f"{label} individuals",
                "kind": "human_individual",
                "source": source,
                **summarize(participant_corr),
            }
        )
        summary_rows.append(
            {
                "group": f"{label} 5-person subcrowds",
                "kind": "human_subcrowd_5",
                "source": source,
                **summarize(subcrowd_corr),
            }
        )
        summary_rows.append(
            {
                "group": f"{label} full crowd",
                "kind": "human_full_crowd",
                "source": source,
                "n": int(mat.shape[0]),
                "mean": crowd_corr,
                "median": crowd_corr,
                "std": 0.0,
                "q10": crowd_corr,
                "q90": crowd_corr,
                "min": crowd_corr,
                "max": crowd_corr,
            }
        )

    return pd.DataFrame(summary_rows)


def build_bootstrap_summary(llm_mat: np.ndarray, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    out_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        human_mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        diffs = np.empty(N_BOOTSTRAP, dtype=float)
        for idx in range(N_BOOTSTRAP):
            boot_idx = rng.integers(0, truth_vec.size, size=truth_vec.size)
            truth_boot = truth_vec[boot_idx]
            llm_corr = corr_rows(llm_mat[:, boot_idx], truth_boot).mean()
            human_corr = corr_rows(human_mat[:, boot_idx], truth_boot).mean()
            diffs[idx] = llm_corr - human_corr
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline mean corr minus {label.lower()} individual mean corr",
                "mean_diff": float(diffs.mean()),
                "ci_low_95": float(np.quantile(diffs, 0.025)),
                "ci_high_95": float(np.quantile(diffs, 0.975)),
                "prob_diff_gt_zero": float(np.mean(diffs > 0.0)),
            }
        )

    return pd.DataFrame(out_rows)


def build_rank_test_summary(llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        human_mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        human_corr = corr_rows(human_mat, truth_vec)

        pooled_llm = llm_baseline["correlation"].to_numpy(dtype=float)
        pooled_mw = stats.mannwhitneyu(pooled_llm, human_corr, alternative="greater")
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline repeats > {label.lower()} individuals",
                "model": "pooled",
                "mannwhitney_u": float(pooled_mw.statistic),
                "p_value_one_sided": float(pooled_mw.pvalue),
                "llm_mean_corr": float(pooled_llm.mean()),
                "human_mean_corr": float(human_corr.mean()),
                "share_humans_below_llm_mean": float(np.mean(human_corr < pooled_llm.mean())),
            }
        )

        for model, part in llm_baseline.groupby("model", observed=True):
            llm_corr = part["correlation"].to_numpy(dtype=float)
            mw = stats.mannwhitneyu(llm_corr, human_corr, alternative="greater")
            out_rows.append(
                {
                    "comparison": f"{model} baseline repeats > {label.lower()} individuals",
                    "model": model,
                    "mannwhitney_u": float(mw.statistic),
                    "p_value_one_sided": float(mw.pvalue),
                    "llm_mean_corr": float(llm_corr.mean()),
                    "human_mean_corr": float(human_corr.mean()),
                    "share_humans_below_llm_mean": float(np.mean(human_corr < llm_corr.mean())),
                }
            )

    return pd.DataFrame(out_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    llm_baseline, llm_mat = load_llm_baseline()
    human_rows, truth_vec = load_human_predictions()

    group_summary = build_group_summary(llm_baseline, llm_mat, human_rows, truth_vec)
    bootstrap_summary = build_bootstrap_summary(llm_mat, human_rows, truth_vec)
    rank_test_summary = build_rank_test_summary(llm_baseline, human_rows, truth_vec)

    group_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_performance_group_summary.csv",
        index=False,
    )
    bootstrap_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_performance_bootstrap_summary.csv",
        index=False,
    )
    rank_test_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_performance_rank_test_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
