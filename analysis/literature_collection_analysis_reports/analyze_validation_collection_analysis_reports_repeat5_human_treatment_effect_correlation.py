from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "validation" / "literature_collection_analysis_reports_repeat5_human_treatment_effect_correlation"
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
    series = pd.Series(values, dtype=float).dropna()
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
    truth_ss = float(np.sum(centered_truth**2))
    if truth_ss <= 0:
        return np.full(mat.shape[0], np.nan, dtype=float)
    row_ss = np.sum(centered_mat**2, axis=1)
    denom = np.sqrt(row_ss * truth_ss)
    out = np.full(mat.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (centered_mat[valid] @ centered_truth) / denom[valid]
    return out


def load_llm_baseline() -> tuple[pd.DataFrame, np.ndarray]:
    rows = pd.read_csv(LLM_REPEAT_ROWS_CSV)
    baseline = rows.loc[rows["condition"] == "baseline"].copy()
    mat = baseline[Q_COLS].to_numpy(dtype=float)
    return baseline, mat


def load_human_predictions() -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    rows = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    rows = rows.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth = (
        rows.loc[:, ["CONFIG_configId", "treatment_efficiency", "control_efficiency"]]
        .drop_duplicates()
        .sort_values("CONFIG_configId")
    )
    treatment = truth["treatment_efficiency"].to_numpy(dtype=float) * 100.0
    control = truth["control_efficiency"].to_numpy(dtype=float) * 100.0
    return rows, treatment, control


def build_human_matrix(rows: pd.DataFrame, source: str) -> pd.DataFrame:
    wide = (
        rows.loc[rows["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
        .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
        .sort_index()
    )
    return wide.loc[:, wide.notna().all(axis=0)]


def sample_subcrowd_corrs(effect_mat: np.ndarray, true_effect: np.ndarray, *, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    players = np.arange(effect_mat.shape[0])
    values: list[float] = []
    while len(values) < N_SUBCROWD:
        idx = rng.choice(players, size=SUBCROWD_SIZE, replace=False)
        corr = corr_rows(effect_mat[idx].mean(axis=0, keepdims=True), true_effect)[0]
        if np.isfinite(corr):
            values.append(float(corr))
    return np.asarray(values, dtype=float)


def build_group_summary(llm_baseline: pd.DataFrame, llm_pred: np.ndarray, human_rows: pd.DataFrame, control: np.ndarray, true_effect: np.ndarray) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []
    llm_corr = corr_rows(llm_pred - control[None, :], true_effect)
    summary_rows.append(
        {
            "group": "LLM baseline repeats (pooled)",
            "kind": "llm_repeat",
            **summarize(llm_corr),
        }
    )
    for model, part in llm_baseline.groupby("model", observed=True):
        pred = part[Q_COLS].to_numpy(dtype=float)
        corr = corr_rows(pred - control[None, :], true_effect)
        summary_rows.append(
            {
                "group": f"LLM baseline repeats ({model})",
                "kind": "llm_repeat",
                "model": model,
                **summarize(corr),
            }
        )

    for seed, source in enumerate(SOURCE_ORDER):
        label = SOURCE_LABELS[source]
        wide = build_human_matrix(human_rows, source)
        pred = wide.to_numpy(dtype=float).T * 100.0
        effect = pred - control[None, :]
        participant_corr = corr_rows(effect, true_effect)
        crowd_corr = corr_rows(effect.mean(axis=0, keepdims=True), true_effect)[0]
        subcrowd_corr = sample_subcrowd_corrs(effect, true_effect, seed=seed)

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
                "n": int(effect.shape[0]),
                "mean": float(crowd_corr),
                "median": float(crowd_corr),
                "std": 0.0,
                "q10": float(crowd_corr),
                "q90": float(crowd_corr),
                "min": float(crowd_corr),
                "max": float(crowd_corr),
            }
        )

    return pd.DataFrame(summary_rows)


def build_crowd_summary(llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, control: np.ndarray, true_effect: np.ndarray) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    all_llm_pred = llm_baseline[Q_COLS].mean(axis=0).to_numpy(dtype=float)
    rows.append(
        {
            "group": "LLM baseline average of all 20 runs",
            "treatment_effect_correlation": float(corr_rows((all_llm_pred - control)[None, :], true_effect)[0]),
        }
    )
    for model, part in llm_baseline.groupby("model", observed=True):
        pred = part[Q_COLS].mean(axis=0).to_numpy(dtype=float)
        rows.append(
            {
                "group": f"{model} baseline average of 5 repeats",
                "treatment_effect_correlation": float(corr_rows((pred - control)[None, :], true_effect)[0]),
            }
        )
    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        pred = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        effect = pred - control[None, :]
        rows.append(
            {
                "group": f"{label} full crowd",
                "treatment_effect_correlation": float(corr_rows(effect.mean(axis=0, keepdims=True), true_effect)[0]),
            }
        )
    return pd.DataFrame(rows)


def build_bootstrap_summary(llm_pred: np.ndarray, human_rows: pd.DataFrame, control: np.ndarray, true_effect: np.ndarray) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    llm_effect = llm_pred - control[None, :]
    out_rows: list[dict[str, object]] = []

    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        human_pred = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        human_effect = human_pred - control[None, :]
        diffs: list[float] = []
        while len(diffs) < N_BOOTSTRAP:
            idx = rng.integers(0, true_effect.size, size=true_effect.size)
            truth_boot = true_effect[idx]
            llm_corr = corr_rows(llm_effect[:, idx], truth_boot)
            human_corr = corr_rows(human_effect[:, idx], truth_boot)
            llm_mean = np.nanmean(llm_corr)
            human_mean = np.nanmean(human_corr)
            if np.isfinite(llm_mean) and np.isfinite(human_mean):
                diffs.append(float(llm_mean - human_mean))
        diff_arr = np.asarray(diffs, dtype=float)
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline mean treatment-effect corr minus {label.lower()} individual mean treatment-effect corr",
                "mean_diff": float(diff_arr.mean()),
                "ci_low_95": float(np.quantile(diff_arr, 0.025)),
                "ci_high_95": float(np.quantile(diff_arr, 0.975)),
                "prob_diff_gt_zero": float(np.mean(diff_arr > 0.0)),
            }
        )

    return pd.DataFrame(out_rows)


def build_rank_test_summary(llm_pred: np.ndarray, llm_baseline: pd.DataFrame, human_rows: pd.DataFrame, control: np.ndarray, true_effect: np.ndarray) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    pooled_llm = corr_rows(llm_pred - control[None, :], true_effect)

    for source in SOURCE_ORDER:
        label = SOURCE_LABELS[source]
        human_pred = build_human_matrix(human_rows, source).to_numpy(dtype=float).T * 100.0
        human_corr = corr_rows(human_pred - control[None, :], true_effect)

        pooled_mw = stats.mannwhitneyu(pooled_llm, human_corr, alternative="greater")
        out_rows.append(
            {
                "comparison": f"LLM pooled baseline repeats > {label.lower()} individuals",
                "model": "pooled",
                "mannwhitney_u": float(pooled_mw.statistic),
                "p_value_one_sided": float(pooled_mw.pvalue),
                "llm_mean_treatment_effect_corr": float(np.nanmean(pooled_llm)),
                "human_mean_treatment_effect_corr": float(np.nanmean(human_corr)),
                "share_humans_below_llm_mean": float(np.mean(human_corr < np.nanmean(pooled_llm))),
            }
        )

        for model, part in llm_baseline.groupby("model", observed=True):
            pred = part[Q_COLS].to_numpy(dtype=float)
            llm_corr = corr_rows(pred - control[None, :], true_effect)
            mw = stats.mannwhitneyu(llm_corr, human_corr, alternative="greater")
            out_rows.append(
                {
                    "comparison": f"{model} baseline repeats > {label.lower()} individuals",
                    "model": model,
                    "mannwhitney_u": float(mw.statistic),
                    "p_value_one_sided": float(mw.pvalue),
                    "llm_mean_treatment_effect_corr": float(np.nanmean(llm_corr)),
                    "human_mean_treatment_effect_corr": float(np.nanmean(human_corr)),
                    "share_humans_below_llm_mean": float(np.mean(human_corr < np.nanmean(llm_corr))),
                }
            )

    return pd.DataFrame(out_rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    llm_baseline, llm_pred = load_llm_baseline()
    human_rows, treatment, control = load_human_predictions()
    true_effect = treatment - control

    group_summary = build_group_summary(llm_baseline, llm_pred, human_rows, control, true_effect)
    crowd_summary = build_crowd_summary(llm_baseline, human_rows, control, true_effect)
    bootstrap_summary = build_bootstrap_summary(llm_pred, human_rows, control, true_effect)
    rank_test_summary = build_rank_test_summary(llm_pred, llm_baseline, human_rows, control, true_effect)

    group_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_treatment_effect_correlation_group_summary.csv",
        index=False,
    )
    crowd_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_treatment_effect_correlation_crowd_summary.csv",
        index=False,
    )
    bootstrap_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_treatment_effect_correlation_bootstrap_summary.csv",
        index=False,
    )
    rank_test_summary.to_csv(
        RESULTS_DIR / "validation_literature_collection_analysis_report_repeat5_human_treatment_effect_correlation_rank_test_summary.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
