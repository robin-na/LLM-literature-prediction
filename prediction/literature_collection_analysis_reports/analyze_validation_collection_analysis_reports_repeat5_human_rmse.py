from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_human_rmse"
LLM_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
Q_COLS = [f"Q{i}" for i in range(1, 21)]
SOURCE_ORDER = ["sspp", "prolific"]
SOURCE_LABELS = {
    "sspp": "Experts",
    "prolific": "Laypeople",
}
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


def rmse_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    return np.sqrt(np.mean((mat - truth[None, :]) ** 2, axis=1))


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


def sample_subcrowd_rmse(mat: np.ndarray, truth: np.ndarray, *, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    players = np.arange(mat.shape[0])
    values: list[float] = []
    for _ in range(N_SUBCROWD):
        idx = rng.choice(players, size=SUBCROWD_SIZE, replace=False)
        values.append(float(np.sqrt(np.mean((mat[idx].mean(axis=0) - truth) ** 2))))
    return np.asarray(values, dtype=float)


def build_group_summary(llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []
    summary_rows.append(
        {
            "group": "LLM baseline repeats (pooled)",
            "kind": "llm_repeat",
            **summarize(llm_baseline["rmse"].to_numpy(dtype=float)),
        }
    )
    for model, part in llm_baseline.groupby("model", observed=True):
        summary_rows.append(
            {
                "group": f"LLM baseline repeats ({model})",
                "kind": "llm_repeat",
                "model": model,
                **summarize(part["rmse"].to_numpy(dtype=float)),
            }
        )

    for seed, source in enumerate(SOURCE_ORDER):
        label = SOURCE_LABELS[source]
        wide = build_human_matrix(human_rows, source)
        mat = wide.to_numpy(dtype=float).T * 100.0
        participant_rmse = rmse_rows(mat, truth_vec)
        crowd_rmse = float(np.sqrt(np.mean((mat.mean(axis=0) - truth_vec) ** 2)))
        subcrowd_rmse = sample_subcrowd_rmse(mat, truth_vec, seed=seed)

        summary_rows.append(
            {
                "group": f"{label} individuals",
                "kind": "human_individual",
                "source": source,
                **summarize(participant_rmse),
            }
        )
        summary_rows.append(
            {
                "group": f"{label} 5-person subcrowds",
                "kind": "human_subcrowd_5",
                "source": source,
                **summarize(subcrowd_rmse),
            }
        )
        summary_rows.append(
            {
                "group": f"{label} full crowd",
                "kind": "human_full_crowd",
                "source": source,
                "n": int(mat.shape[0]),
                "mean": crowd_rmse,
                "median": crowd_rmse,
                "std": 0.0,
                "q10": crowd_rmse,
                "q90": crowd_rmse,
                "min": crowd_rmse,
                "max": crowd_rmse,
            }
        )

    return pd.DataFrame(summary_rows)


def build_crowd_summary(llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    rows.append(
        {
            "group": "LLM baseline average of all 20 runs",
            "rmse": float(np.sqrt(np.mean((llm_baseline[Q_COLS].mean(axis=0).to_numpy(dtype=float) - truth_vec) ** 2))),
        }
    )
    for model, part in llm_baseline.groupby("model", observed=True):
        rows.append(
            {
                "group": f"{model} baseline average of 5 repeats",
                "rmse": float(np.sqrt(np.mean((part[Q_COLS].mean(axis=0).to_numpy(dtype=float) - truth_vec) ** 2))),
            }
        )
    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        rows.append(
            {
                "group": f"{label} full crowd",
                "rmse": float(np.sqrt(np.mean((mat.mean(axis=0) - truth_vec) ** 2))),
            }
        )
    return pd.DataFrame(rows)


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
            llm_rmse = rmse_rows(llm_mat[:, boot_idx], truth_boot).mean()
            human_rmse = rmse_rows(human_mat[:, boot_idx], truth_boot).mean()
            diffs[idx] = llm_rmse - human_rmse
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline mean RMSE minus {label.lower()} individual mean RMSE",
                "mean_diff": float(diffs.mean()),
                "ci_low_95": float(np.quantile(diffs, 0.025)),
                "ci_high_95": float(np.quantile(diffs, 0.975)),
                "prob_diff_lt_zero": float(np.mean(diffs < 0.0)),
            }
        )
    return pd.DataFrame(out_rows)


def build_rank_test_summary(llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, truth_vec: np.ndarray) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    pooled_llm = llm_baseline["rmse"].to_numpy(dtype=float)
    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        human_mat = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        human_rmse = rmse_rows(human_mat, truth_vec)
        pooled_mw = stats.mannwhitneyu(pooled_llm, human_rmse, alternative="less")
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline repeats < {label.lower()} individuals",
                "model": "pooled",
                "mannwhitney_u": float(pooled_mw.statistic),
                "p_value_one_sided": float(pooled_mw.pvalue),
                "llm_mean_rmse": float(pooled_llm.mean()),
                "human_mean_rmse": float(human_rmse.mean()),
                "share_humans_above_llm_mean": float(np.mean(human_rmse > pooled_llm.mean())),
            }
        )
        for model, part in llm_baseline.groupby("model", observed=True):
            llm_rmse = part["rmse"].to_numpy(dtype=float)
            mw = stats.mannwhitneyu(llm_rmse, human_rmse, alternative="less")
            out_rows.append(
                {
                    "comparison": f"{model} baseline repeats < {label.lower()} individuals",
                    "model": model,
                    "mannwhitney_u": float(mw.statistic),
                    "p_value_one_sided": float(mw.pvalue),
                    "llm_mean_rmse": float(llm_rmse.mean()),
                    "human_mean_rmse": float(human_rmse.mean()),
                    "share_humans_above_llm_mean": float(np.mean(human_rmse > llm_rmse.mean())),
                }
            )
    return pd.DataFrame(out_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    llm_baseline, llm_mat = load_llm_baseline()
    human_rows, truth_vec = load_human_predictions()

    group_summary = build_group_summary(llm_baseline, human_rows, truth_vec)
    crowd_summary = build_crowd_summary(llm_baseline, human_rows, truth_vec)
    bootstrap_summary = build_bootstrap_summary(llm_mat, human_rows, truth_vec)
    rank_test_summary = build_rank_test_summary(llm_baseline, human_rows, truth_vec)

    group_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_rmse_group_summary.csv",
        index=False,
    )
    crowd_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_rmse_crowd_summary.csv",
        index=False,
    )
    bootstrap_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_rmse_bootstrap_summary.csv",
        index=False,
    )
    rank_test_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_rmse_rank_test_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
