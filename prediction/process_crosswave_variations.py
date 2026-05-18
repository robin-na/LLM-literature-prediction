from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(REPO_ROOT / "analysis"))

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from prediction_metrics import (  # noqa: E402
    _corr_np,
    _directional_accuracy_np,
    _load_baseline,
    _paired_delta_ci,
    _rmse_np,
    compute_delta_metrics,
    compute_metrics,
    load_ground_truth,
)


RESULTS_DIR = REPO_ROOT / "results"
OPENAI_OUTPUT_DIR = REPO_ROOT / "openAI_batch_output"
VAL_GT = REPO_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"
LEARN_GT = REPO_ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_learn.csv"
VAL_REFERENCE_PRED = RESULTS_DIR / "prediction_positive_case_variations_41.csv"
VAL_REFERENCE_METRICS = RESULTS_DIR / "prediction_positive_case_variations_41_metrics.csv"
LEARN_BASELINE_PRED = RESULTS_DIR / "prediction_learning_wave_elicitation_41.csv"
LEARN_BASELINE_METRICS = RESULTS_DIR / "prediction_learning_wave_elicitation_41_metrics.csv"
N_BOOT = 1000
SEED = 42


def parse_variation_name(name: str) -> tuple[str, str]:
    if name.endswith("_joint_reasoning"):
        return name[: -len("_joint_reasoning")], "joint_reasoning"
    if name.endswith("_joint"):
        return name[: -len("_joint")], "joint"
    if name.endswith("_reasoning"):
        return name[: -len("_reasoning")], "reasoning"
    return name, "single"


def input_group_from_family(family: str) -> str:
    if family.startswith("both_"):
        return "both"
    if family.startswith("paper_only_"):
        return "paper_only"
    if family.startswith("data_only_"):
        return "data_only"
    if family.startswith("pgg_CONFIGmerged_"):
        return "experiment_catalog"
    return "baseline"


def ci_verdict(better_direction: str, ci_low: float, ci_high: float) -> str:
    if math.isnan(ci_low) or math.isnan(ci_high):
        return "missing"
    if better_direction == "lower":
        if ci_high < 0:
            return "better"
        if ci_low > 0:
            return "worse"
        return "uncertain"
    if ci_low > 0:
        return "better"
    if ci_high < 0:
        return "worse"
    return "uncertain"


def build_metadata(index: pd.Index) -> pd.DataFrame:
    meta = pd.DataFrame({"variation": list(index)})
    parsed = meta["variation"].map(parse_variation_name)
    meta["family"] = parsed.map(lambda item: item[0])
    meta["mode"] = parsed.map(lambda item: item[1])
    meta["input_group"] = meta["family"].map(input_group_from_family)
    return meta


def split_prediction_table(pred_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    val_cols = [c for c in pred_df.columns if isinstance(c, str) and c.startswith("Q")]
    learn_cols = [c for c in pred_df.columns if isinstance(c, str) and c.startswith("L")]
    return pred_df[val_cols].copy(), pred_df[learn_cols].copy()


def missing_summary(pred_df: pd.DataFrame, expected_questions: list[str], dataset: str) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for variation, row in pred_df.iterrows():
        pred = pd.to_numeric(row, errors="coerce").reindex(expected_questions)
        missing = [q for q in expected_questions if pd.isna(pred[q])]
        records.append(
            {
                "dataset": dataset,
                "variation": variation,
                "n_expected": len(expected_questions),
                "n_present": int(pred.notna().sum()),
                "n_missing": len(missing),
                "missing_labels": ",".join(missing),
            }
        )
    return pd.DataFrame.from_records(records)


def paired_compare_external(
    pred_row: pd.Series,
    base_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
    seed: int,
    n_boot: int,
) -> dict[str, float | int]:
    questions = list(treatment.index)
    pred_arr = pd.to_numeric(pred_row, errors="coerce").reindex(questions).to_numpy(float)
    base_arr = pd.to_numeric(base_row, errors="coerce").reindex(questions).to_numpy(float)
    truth_arr = treatment.reindex(questions).to_numpy(float)
    ctrl_arr = control.reindex(questions).to_numpy(float)

    rmse_mask = ~np.isnan(pred_arr) & ~np.isnan(base_arr) & ~np.isnan(truth_arr)
    corr_mask = rmse_mask.copy()
    dir_mask = rmse_mask & ~np.isnan(ctrl_arr)

    rng = np.random.default_rng(seed)
    d_rmse = _paired_delta_ci(_rmse_np, pred_arr, base_arr, truth_arr, None, rmse_mask, rng, n_boot)
    rng = np.random.default_rng(seed)
    d_corr = _paired_delta_ci(_corr_np, pred_arr, base_arr, truth_arr, None, corr_mask, rng, n_boot)
    rng = np.random.default_rng(seed)
    d_dir = _paired_delta_ci(
        _directional_accuracy_np,
        pred_arr,
        base_arr,
        truth_arr,
        ctrl_arr,
        dir_mask,
        rng,
        n_boot,
    )
    return {
        "delta_rmse": d_rmse[0],
        "delta_rmse_ci_low": d_rmse[1],
        "delta_rmse_ci_high": d_rmse[2],
        "delta_correlation": d_corr[0],
        "delta_correlation_ci_low": d_corr[1],
        "delta_correlation_ci_high": d_corr[2],
        "delta_directional_accuracy": d_dir[0],
        "delta_directional_accuracy_ci_low": d_dir[1],
        "delta_directional_accuracy_ci_high": d_dir[2],
        "n": int(rmse_mask.sum()),
    }


def matched_baseline_name(mode: str) -> str:
    mapping = {
        "single": "baseline",
        "reasoning": "baseline_reasoning",
        "joint": "baseline_joint",
        "joint_reasoning": "baseline_joint_reasoning",
    }
    return mapping[mode]


def compute_learning_external_deltas(
    learn_pred_df: pd.DataFrame,
    learn_baseline_df: pd.DataFrame,
    treatment: pd.Series,
    control: pd.Series,
    baseline_selector,
    baseline_label: str,
) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for variation, row in learn_pred_df.iterrows():
        family, mode = parse_variation_name(variation)
        base_name = baseline_selector(mode)
        base_row = learn_baseline_df.loc[base_name]
        delta = paired_compare_external(row, base_row, treatment, control, SEED, N_BOOT)
        delta.update(
            {
                "variation": variation,
                "family": family,
                "mode": mode,
                "input_group": input_group_from_family(family),
                "baseline_variation": base_name,
                "baseline_label": baseline_label,
                "rmse_ci_verdict": ci_verdict(
                    "lower", delta["delta_rmse_ci_low"], delta["delta_rmse_ci_high"]
                ),
                "correlation_ci_verdict": ci_verdict(
                    "higher",
                    delta["delta_correlation_ci_low"],
                    delta["delta_correlation_ci_high"],
                ),
                "directional_accuracy_ci_verdict": ci_verdict(
                    "higher",
                    delta["delta_directional_accuracy_ci_low"],
                    delta["delta_directional_accuracy_ci_high"],
                ),
            }
        )
        records.append(delta)
    return pd.DataFrame.from_records(records).sort_values("variation")


def compare_validation_duplicates(
    new_pred_df: pd.DataFrame,
    new_metrics_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    old_pred_df = pd.read_csv(VAL_REFERENCE_PRED, index_col=0)
    old_metrics_df = pd.read_csv(VAL_REFERENCE_METRICS, index_col=0)

    questions = [c for c in new_pred_df.columns if c.startswith("Q")]
    shared = sorted(set(new_pred_df.index).intersection(old_pred_df.index))
    rows: list[dict[str, object]] = []
    for variation in shared:
        new_row = pd.to_numeric(new_pred_df.loc[variation], errors="coerce").reindex(questions)
        old_row = pd.to_numeric(old_pred_df.loc[variation], errors="coerce").reindex(questions)
        mask = new_row.notna() & old_row.notna()
        diff = (new_row[mask] - old_row[mask]).astype(float)
        rows.append(
            {
                "variation": variation,
                "n_overlap": int(mask.sum()),
                "n_exact_same": int((diff == 0).sum()),
                "n_different": int((diff != 0).sum()),
                "share_exact_same": float((diff == 0).mean()) if mask.sum() else float("nan"),
                "mean_abs_prediction_diff": float(diff.abs().mean()) if mask.sum() else float("nan"),
                "max_abs_prediction_diff": float(diff.abs().max()) if mask.sum() else float("nan"),
                "rmse_new": float(new_metrics_df.loc[variation, "rmse"]),
                "rmse_old": float(old_metrics_df.loc[variation, "rmse"]),
                "rmse_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "rmse"] - old_metrics_df.loc[variation, "rmse"]
                ),
                "correlation_new": float(new_metrics_df.loc[variation, "correlation"]),
                "correlation_old": float(old_metrics_df.loc[variation, "correlation"]),
                "correlation_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "correlation"]
                    - old_metrics_df.loc[variation, "correlation"]
                ),
                "directional_accuracy_new": float(
                    new_metrics_df.loc[variation, "directional_accuracy"]
                ),
                "directional_accuracy_old": float(
                    old_metrics_df.loc[variation, "directional_accuracy"]
                ),
                "directional_accuracy_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "directional_accuracy"]
                    - old_metrics_df.loc[variation, "directional_accuracy"]
                ),
            }
        )

    detail_df = pd.DataFrame.from_records(rows).sort_values(
        ["n_different", "mean_abs_prediction_diff", "variation"],
        ascending=[False, False, True],
    )
    summary_df = pd.DataFrame.from_records(
        [
            {
                "shared_variants": len(shared),
                "exact_match_variants": int((detail_df["n_different"] == 0).sum()),
                "changed_variants": int((detail_df["n_different"] > 0).sum()),
                "mean_share_exact_same": float(detail_df["share_exact_same"].mean()),
                "mean_abs_prediction_diff_across_variants": float(
                    detail_df["mean_abs_prediction_diff"].mean()
                ),
                "max_abs_prediction_diff_across_variants": float(
                    detail_df["max_abs_prediction_diff"].max()
                ),
                "mean_rmse_shift_new_minus_old": float(
                    detail_df["rmse_shift_new_minus_old"].mean()
                ),
                "mean_correlation_shift_new_minus_old": float(
                    detail_df["correlation_shift_new_minus_old"].mean()
                ),
                "mean_directional_accuracy_shift_new_minus_old": float(
                    detail_df["directional_accuracy_shift_new_minus_old"].mean()
                ),
            }
        ]
    )
    return detail_df, summary_df


def compare_against_reference(
    new_pred_df: pd.DataFrame,
    new_metrics_df: pd.DataFrame,
    reference_pred_path: Path,
    reference_metrics_path: Path,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    old_pred_df = pd.read_csv(reference_pred_path, index_col=0)
    old_metrics_df = pd.read_csv(reference_metrics_path, index_col=0)

    questions = [c for c in new_pred_df.columns if c.startswith("Q")]
    shared = sorted(set(new_pred_df.index).intersection(old_pred_df.index))
    rows: list[dict[str, object]] = []
    for variation in shared:
        new_row = pd.to_numeric(new_pred_df.loc[variation], errors="coerce").reindex(questions)
        old_row = pd.to_numeric(old_pred_df.loc[variation], errors="coerce").reindex(questions)
        mask = new_row.notna() & old_row.notna()
        diff = (new_row[mask] - old_row[mask]).astype(float)
        rows.append(
            {
                "variation": variation,
                "n_overlap": int(mask.sum()),
                "n_exact_same": int((diff == 0).sum()),
                "n_different": int((diff != 0).sum()),
                "share_exact_same": float((diff == 0).mean()) if mask.sum() else float("nan"),
                "mean_abs_prediction_diff": float(diff.abs().mean()) if mask.sum() else float("nan"),
                "max_abs_prediction_diff": float(diff.abs().max()) if mask.sum() else float("nan"),
                "rmse_new": float(new_metrics_df.loc[variation, "rmse"]),
                "rmse_old": float(old_metrics_df.loc[variation, "rmse"]),
                "rmse_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "rmse"] - old_metrics_df.loc[variation, "rmse"]
                ),
                "correlation_new": float(new_metrics_df.loc[variation, "correlation"]),
                "correlation_old": float(old_metrics_df.loc[variation, "correlation"]),
                "correlation_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "correlation"]
                    - old_metrics_df.loc[variation, "correlation"]
                ),
                "directional_accuracy_new": float(
                    new_metrics_df.loc[variation, "directional_accuracy"]
                ),
                "directional_accuracy_old": float(
                    old_metrics_df.loc[variation, "directional_accuracy"]
                ),
                "directional_accuracy_shift_new_minus_old": float(
                    new_metrics_df.loc[variation, "directional_accuracy"]
                    - old_metrics_df.loc[variation, "directional_accuracy"]
                ),
            }
        )

    detail_df = pd.DataFrame.from_records(rows).sort_values(
        ["n_different", "mean_abs_prediction_diff", "variation"],
        ascending=[False, False, True],
    )
    summary_df = pd.DataFrame.from_records(
        [
            {
                "shared_variants": len(shared),
                "exact_match_variants": int((detail_df["n_different"] == 0).sum()),
                "changed_variants": int((detail_df["n_different"] > 0).sum()),
                "mean_share_exact_same": float(detail_df["share_exact_same"].mean()),
                "mean_abs_prediction_diff_across_variants": float(
                    detail_df["mean_abs_prediction_diff"].mean()
                ),
                "max_abs_prediction_diff_across_variants": float(
                    detail_df["max_abs_prediction_diff"].max()
                ),
                "mean_rmse_shift_new_minus_old": float(
                    detail_df["rmse_shift_new_minus_old"].mean()
                ),
                "mean_correlation_shift_new_minus_old": float(
                    detail_df["correlation_shift_new_minus_old"].mean()
                ),
                "mean_directional_accuracy_shift_new_minus_old": float(
                    detail_df["directional_accuracy_shift_new_minus_old"].mean()
                ),
            }
        ]
    )
    return detail_df, summary_df


def add_rank_columns(metrics_df: pd.DataFrame) -> pd.DataFrame:
    ranked = metrics_df.copy()
    ranked["rmse_rank"] = ranked["rmse"].rank(method="min", ascending=True)
    ranked["correlation_rank"] = ranked["correlation"].rank(method="min", ascending=False)
    ranked["directional_accuracy_rank"] = ranked["directional_accuracy"].rank(
        method="min", ascending=False
    )
    ranked["overall_rank_mean"] = ranked[
        ["rmse_rank", "correlation_rank", "directional_accuracy_rank"]
    ].mean(axis=1)
    ranked["overall_rank"] = ranked["overall_rank_mean"].rank(method="min")
    return ranked


def wave_group_summary(
    metrics_df: pd.DataFrame,
    metadata_df: pd.DataFrame,
    wave: str,
) -> pd.DataFrame:
    merged = metadata_df.merge(metrics_df.reset_index(), left_on="variation", right_on="variation")
    ranked = add_rank_columns(merged.set_index("variation")).reset_index()
    grouped = (
        ranked.groupby(["input_group", "mode"], dropna=False)
        .agg(
            n_variants=("variation", "size"),
            mean_rmse=("rmse", "mean"),
            mean_correlation=("correlation", "mean"),
            mean_directional_accuracy=("directional_accuracy", "mean"),
            median_rmse=("rmse", "median"),
            median_correlation=("correlation", "median"),
            median_directional_accuracy=("directional_accuracy", "median"),
            mean_overall_rank=("overall_rank", "mean"),
            median_overall_rank=("overall_rank", "median"),
        )
        .reset_index()
    )
    grouped.insert(0, "wave", wave)
    return grouped.sort_values(["mean_overall_rank", "input_group", "mode"])


def learning_with_baselines_metrics(
    learn_metrics_df: pd.DataFrame,
    learn_baseline_metrics_df: pd.DataFrame,
) -> pd.DataFrame:
    baseline_subset = learn_baseline_metrics_df.loc[
        [
            "baseline",
            "baseline_reasoning",
            "baseline_joint",
            "baseline_joint_reasoning",
        ]
    ].copy()
    baseline_subset["source"] = "no_input_baseline"
    augmented = learn_metrics_df.copy()
    augmented = augmented.loc[[idx for idx in augmented.index if not str(idx).startswith("baseline")]]
    augmented["source"] = "augmented"
    combined = pd.concat([baseline_subset, augmented], axis=0)
    combined = combined.reset_index().rename(columns={"index": "variation"})
    meta = build_metadata(pd.Index(combined["variation"]))
    combined = meta.merge(combined, on="variation", how="left")
    return combined


def crosswave_variant_summary(
    val_metrics_df: pd.DataFrame,
    val_delta_df: pd.DataFrame,
    learn_metrics_df: pd.DataFrame,
    learn_matched_delta_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    val_ranked = add_rank_columns(val_metrics_df)
    learn_ranked = add_rank_columns(learn_metrics_df)
    meta = build_metadata(val_metrics_df.index)

    summary = (
        meta.merge(
            val_ranked.reset_index().rename(columns={"index": "variation"}),
            on="variation",
            how="left",
            suffixes=("", "_validation"),
        )
        .merge(
            val_delta_df.reset_index().rename(columns={"index": "variation"}),
            on="variation",
            how="left",
            suffixes=("", "_validation_delta"),
        )
        .merge(
            learn_ranked.reset_index().rename(columns={"index": "variation"}),
            on="variation",
            how="left",
            suffixes=("_validation", "_learning"),
        )
        .merge(
            learn_matched_delta_df,
            on=["variation", "family", "mode", "input_group"],
            how="left",
            suffixes=("", "_learning_delta"),
        )
    )

    summary = summary.rename(
        columns={
            "rmse_validation": "validation_rmse",
            "correlation_validation": "validation_correlation",
            "directional_accuracy_validation": "validation_directional_accuracy",
            "rmse_rank_validation": "validation_rmse_rank",
            "correlation_rank_validation": "validation_correlation_rank",
            "directional_accuracy_rank_validation": "validation_directional_accuracy_rank",
            "overall_rank_mean_validation": "validation_overall_rank_mean",
            "overall_rank_validation": "validation_overall_rank",
            "rmse_learning": "learning_rmse",
            "correlation_learning": "learning_correlation",
            "directional_accuracy_learning": "learning_directional_accuracy",
            "rmse_rank_learning": "learning_rmse_rank",
            "correlation_rank_learning": "learning_correlation_rank",
            "directional_accuracy_rank_learning": "learning_directional_accuracy_rank",
            "overall_rank_mean_learning": "learning_overall_rank_mean",
            "overall_rank_learning": "learning_overall_rank",
            "delta_rmse": "validation_delta_rmse",
            "delta_correlation": "validation_delta_correlation",
            "delta_directional_accuracy": "validation_delta_directional_accuracy",
            "delta_rmse_ci_low": "validation_delta_rmse_ci_low",
            "delta_rmse_ci_high": "validation_delta_rmse_ci_high",
            "delta_correlation_ci_low": "validation_delta_correlation_ci_low",
            "delta_correlation_ci_high": "validation_delta_correlation_ci_high",
            "delta_directional_accuracy_ci_low": "validation_delta_directional_accuracy_ci_low",
            "delta_directional_accuracy_ci_high": "validation_delta_directional_accuracy_ci_high",
            "rmse_ci_verdict": "learning_matched_rmse_ci_verdict",
            "correlation_ci_verdict": "learning_matched_correlation_ci_verdict",
            "directional_accuracy_ci_verdict": "learning_matched_directional_accuracy_ci_verdict",
        }
    )
    summary["mean_crosswave_rank"] = (
        summary["validation_overall_rank"] + summary["learning_overall_rank"]
    ) / 2.0
    summary["rank_gap_learning_minus_validation"] = (
        summary["learning_overall_rank"] - summary["validation_overall_rank"]
    )
    summary = summary.sort_values(
        ["mean_crosswave_rank", "validation_overall_rank", "learning_overall_rank"]
    )

    corr_df = pd.DataFrame.from_records(
        [
            {
                "metric": "overall_rank",
                "spearman_correlation": float(
                    summary["validation_overall_rank"].corr(
                        summary["learning_overall_rank"], method="spearman"
                    )
                ),
            },
            {
                "metric": "rmse_rank",
                "spearman_correlation": float(
                    summary["validation_rmse_rank"].corr(
                        summary["learning_rmse_rank"], method="spearman"
                    )
                ),
            },
            {
                "metric": "correlation_rank",
                "spearman_correlation": float(
                    summary["validation_correlation_rank"].corr(
                        summary["learning_correlation_rank"], method="spearman"
                    )
                ),
            },
            {
                "metric": "directional_accuracy_rank",
                "spearman_correlation": float(
                    summary["validation_directional_accuracy_rank"].corr(
                        summary["learning_directional_accuracy_rank"], method="spearman"
                    )
                ),
            },
        ]
    )
    return summary, corr_df


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Process a crosswave prediction JSONL into split outputs and summaries."
    )
    parser.add_argument(
        "--jsonl",
        type=Path,
        default=OPENAI_OUTPUT_DIR / "prediction_crosswave_variations_41.jsonl",
        help="Path to the crosswave prediction JSONL.",
    )
    parser.add_argument(
        "--reference-validation-pred",
        type=Path,
        default=VAL_REFERENCE_PRED,
        help="Reference validation prediction CSV for overlap comparisons.",
    )
    parser.add_argument(
        "--reference-validation-metrics",
        type=Path,
        default=VAL_REFERENCE_METRICS,
        help="Reference validation metrics CSV for overlap comparisons.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    jsonl_path = args.jsonl
    combined_pred_df = jsonl_to_dataframe(jsonl_path, platform="openai")
    combined_csv = RESULTS_DIR / f"{jsonl_path.stem}.csv"
    combined_pred_df.to_csv(combined_csv)

    val_pred_df, learn_pred_df = split_prediction_table(combined_pred_df)

    val_treatment, val_control = load_ground_truth(VAL_GT, question_prefix="Q")
    learn_treatment, learn_control = load_ground_truth(
        LEARN_GT, question_prefix="L", label_mode="ordinal"
    )

    val_pred_df = val_pred_df.reindex(columns=list(val_treatment.index))
    learn_pred_df = learn_pred_df.reindex(columns=list(learn_treatment.index))

    val_pred_csv = RESULTS_DIR / f"{jsonl_path.stem}_validation.csv"
    learn_pred_csv = RESULTS_DIR / f"{jsonl_path.stem}_learning.csv"
    val_pred_df.to_csv(val_pred_csv)
    learn_pred_df.to_csv(learn_pred_csv)

    val_metrics_df = compute_metrics(
        val_pred_df, val_treatment, val_control, np.random.default_rng(SEED), N_BOOT
    )
    val_metrics_csv = RESULTS_DIR / f"{jsonl_path.stem}_validation_metrics.csv"
    val_metrics_df.to_csv(val_metrics_csv)

    canonical_baseline = _load_baseline(OPENAI_OUTPUT_DIR, RESULTS_DIR, None, "openai")
    val_delta_df = compute_delta_metrics(
        val_pred_df,
        canonical_baseline,
        val_treatment,
        val_control,
        np.random.default_rng(SEED),
        N_BOOT,
    )
    val_delta_csv = RESULTS_DIR / f"{jsonl_path.stem}_validation_metrics_delta.csv"
    val_delta_df.to_csv(val_delta_csv)

    learn_metrics_df = compute_metrics(
        learn_pred_df, learn_treatment, learn_control, np.random.default_rng(SEED), N_BOOT
    )
    learn_metrics_csv = RESULTS_DIR / f"{jsonl_path.stem}_learning_metrics.csv"
    learn_metrics_df.to_csv(learn_metrics_csv)

    val_missing_df = missing_summary(val_pred_df, list(val_treatment.index), "validation")
    learn_missing_df = missing_summary(learn_pred_df, list(learn_treatment.index), "learning")
    missing_df = pd.concat([val_missing_df, learn_missing_df], ignore_index=True)
    missing_csv = RESULTS_DIR / f"{jsonl_path.stem}_missing_summary.csv"
    missing_df.to_csv(missing_csv, index=False)

    duplicate_detail_df, duplicate_summary_df = compare_against_reference(
        val_pred_df,
        val_metrics_df,
        args.reference_validation_pred,
        args.reference_validation_metrics,
    )
    duplicate_detail_csv = RESULTS_DIR / f"{jsonl_path.stem}_validation_duplicate_comparison.csv"
    duplicate_summary_csv = RESULTS_DIR / f"{jsonl_path.stem}_validation_duplicate_summary.csv"
    duplicate_detail_df.to_csv(duplicate_detail_csv, index=False)
    duplicate_summary_df.to_csv(duplicate_summary_csv, index=False)

    learn_baseline_pred_df = pd.read_csv(LEARN_BASELINE_PRED, index_col=0)
    learn_baseline_metrics_df = pd.read_csv(LEARN_BASELINE_METRICS, index_col=0)

    matched_delta_df = compute_learning_external_deltas(
        learn_pred_df,
        learn_baseline_pred_df,
        learn_treatment,
        learn_control,
        matched_baseline_name,
        baseline_label="matched_elicitation_baseline",
    )
    matched_delta_csv = (
        RESULTS_DIR / f"{jsonl_path.stem}_learning_metrics_delta_vs_matched_baseline.csv"
    )
    matched_delta_df.to_csv(matched_delta_csv, index=False)

    baseline_reasoning_delta_df = compute_learning_external_deltas(
        learn_pred_df,
        learn_baseline_pred_df,
        learn_treatment,
        learn_control,
        lambda mode: "baseline_reasoning",
        baseline_label="baseline_reasoning",
    )
    baseline_reasoning_delta_csv = (
        RESULTS_DIR / f"{jsonl_path.stem}_learning_metrics_delta_vs_baseline_reasoning.csv"
    )
    baseline_reasoning_delta_df.to_csv(baseline_reasoning_delta_csv, index=False)

    learn_with_baselines_df = learning_with_baselines_metrics(
        learn_metrics_df, learn_baseline_metrics_df
    )
    learn_with_baselines_csv = RESULTS_DIR / f"{jsonl_path.stem}_learning_with_baselines_metrics.csv"
    learn_with_baselines_df.to_csv(learn_with_baselines_csv, index=False)

    metadata_df = build_metadata(val_metrics_df.index)
    val_group_df = wave_group_summary(val_metrics_df, metadata_df, "validation")
    learn_group_df = wave_group_summary(learn_metrics_df, metadata_df, "learning")
    group_summary_df = pd.concat([val_group_df, learn_group_df], ignore_index=True)
    group_summary_csv = RESULTS_DIR / f"{jsonl_path.stem}_wave_input_mode_summary.csv"
    group_summary_df.to_csv(group_summary_csv, index=False)

    crosswave_summary_df, rank_corr_df = crosswave_variant_summary(
        val_metrics_df, val_delta_df, learn_metrics_df, matched_delta_df
    )
    crosswave_summary_csv = RESULTS_DIR / f"{jsonl_path.stem}_crosswave_variant_summary.csv"
    rank_corr_csv = RESULTS_DIR / f"{jsonl_path.stem}_crosswave_rank_correlation.csv"
    crosswave_summary_df.to_csv(crosswave_summary_csv, index=False)
    rank_corr_df.to_csv(rank_corr_csv, index=False)

    print(f"Wrote {combined_csv.name}")
    print(f"Wrote {val_pred_csv.name}")
    print(f"Wrote {val_metrics_csv.name}")
    print(f"Wrote {val_delta_csv.name}")
    print(f"Wrote {learn_pred_csv.name}")
    print(f"Wrote {learn_metrics_csv.name}")
    print(f"Wrote {missing_csv.name}")
    print(f"Wrote {duplicate_detail_csv.name}")
    print(f"Wrote {duplicate_summary_csv.name}")
    print(f"Wrote {matched_delta_csv.name}")
    print(f"Wrote {baseline_reasoning_delta_csv.name}")
    print(f"Wrote {learn_with_baselines_csv.name}")
    print(f"Wrote {group_summary_csv.name}")
    print(f"Wrote {crosswave_summary_csv.name}")
    print(f"Wrote {rank_corr_csv.name}")


if __name__ == "__main__":
    main()
