from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe


ROOT = ANALYSIS_ROOT.parent
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
BACKFILL_OUTPUT_DIR = OPENAI_BATCH_OUTPUT / "backfill_repeat5_missing"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_repeat5"
METADATA_CSV = ROOT / "paper_collection" / "WoS_251031_fileInfo.csv"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
LEARN_DF = ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
FEATURE_DATASET_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_analysis_report_source_features"
    / "paper_feature_analysis_dataset.csv"
)

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRICS = ["correlation", "rmse", "r2", "directional_accuracy"]
EXPECTED_AUG_RUNS = 5

RUN_SPECS = [
    {
        "model": "GPT-4.1",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_41.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_41.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
    },
    {
        "model": "GPT-4.1 Mini",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41mini.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41mini.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_41mini.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_41mini.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41mini.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
    },
    {
        "model": "GPT-4.1 Nano",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_41nano.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41nano.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_41nano.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_41nano.jsonl",
        "baseline_initial_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_repeat_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41nano.jsonl",
        "baseline_initial_id": "baseline_joint_reasoning",
        "baseline_repeat_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 5)],
    },
    {
        "model": "GPT-5.1",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt51.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt51.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt51.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt51.jsonl",
        "baseline_suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
    {
        "model": "GPT-5 Mini",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt5mini.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt5mini.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5mini.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5mini.jsonl",
        "baseline_suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
    {
        "model": "GPT-5 Nano",
        "backfill_path": BACKFILL_OUTPUT_DIR / "prediction_repeat5_backfill_missing_gpt5nano.jsonl",
        "aug_initial_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt5nano.jsonl",
        "aug_repeat23_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps2to3_gpt5nano.jsonl",
        "aug_repeat45_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_reps4to5_gpt5nano.jsonl",
        "baseline_suite_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
        "baseline_ids": [f"baseline_joint_reasoning_rep{i}" for i in range(1, 6)],
    },
]


def load_validation() -> tuple[np.ndarray, np.ndarray]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth = (df["efficiency_p"].to_numpy(dtype=float) * 100.0).astype(np.float32)
    control = (df["efficiency_np"].to_numpy(dtype=float) * 100.0).astype(np.float32)
    return truth, control


def load_learning_treatment_mean() -> float:
    df = pd.read_csv(LEARN_DF)
    return float(df["treatment_itt_efficiency"].mean() * 100.0)


def load_metadata() -> dict[str, dict[str, object]]:
    df = pd.read_csv(METADATA_CSV)
    df = df.loc[df["custom_id"].notna()].copy()
    df["source_id"] = df["custom_id"].astype(str).map(lambda value: Path(value).stem)
    df = df.drop_duplicates("source_id", keep="first")
    meta = df.set_index("source_id")[
        ["Article Title", "Source Title", "Publication Year"]
    ].to_dict("index")
    meta["PGG_MS_202502"] = {
        "Article Title": "Integrative Experiments Identify How Punishment Impacts Welfare in Public Goods Games",
        "Source Title": "",
        "Publication Year": 2025,
    }
    return meta


def _corr_rowwise(pred: np.ndarray, truth: np.ndarray) -> np.ndarray:
    pred_mean = pred.mean(axis=1, keepdims=True)
    pred_center = pred - pred_mean
    truth_center = truth - truth.mean()
    num = np.sum(pred_center * truth_center[None, :], axis=1)
    denom = np.sqrt(np.sum(pred_center**2, axis=1) * np.sum(truth_center**2))
    return np.divide(
        num,
        denom,
        out=np.full(pred.shape[0], np.nan, dtype=np.float32),
        where=denom > 0,
    )


def _summarize_significance(rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for model, part in rows.groupby("model", dropna=False):
        for metric in METRICS:
            improve = part.loc[part[f"sig_improve_{metric}"]].copy()
            worsen = part.loc[part[f"sig_worsen_{metric}"]].copy()

            if metric == "rmse":
                improve = improve.sort_values(f"delta_{metric}", ascending=True)
                worsen = worsen.sort_values(f"delta_{metric}", ascending=False)
            else:
                improve = improve.sort_values(f"delta_{metric}", ascending=False)
                worsen = worsen.sort_values(f"delta_{metric}", ascending=True)

            best_improve = improve.iloc[0] if not improve.empty else None
            worst_worsen = worsen.iloc[0] if not worsen.empty else None

            out_rows.append(
                {
                    "model": model,
                    "metric": metric,
                    "n_sig_improve": int(len(improve)),
                    "n_sig_worsen": int(len(worsen)),
                    "mean_n_aug_runs": float(part["n_aug_runs"].mean()),
                    "n_baseline_runs": int(part["n_baseline_runs"].iloc[0]),
                    "best_sig_improve_source_id": best_improve["source_id"] if best_improve is not None else "",
                    "best_sig_improve_delta": float(best_improve[f"delta_{metric}"]) if best_improve is not None else np.nan,
                    "worst_sig_worsen_source_id": worst_worsen["source_id"] if worst_worsen is not None else "",
                    "worst_sig_worsen_delta": float(worst_worsen[f"delta_{metric}"]) if worst_worsen is not None else np.nan,
                }
            )
    return pd.DataFrame(out_rows).sort_values(["model", "metric"]).reset_index(drop=True)


def _load_aug_tables(spec: dict[str, object]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    initial_df = jsonl_to_dataframe(spec["aug_initial_path"]).reindex(columns=Q_COLS)
    repeat23_df = jsonl_to_dataframe(spec["aug_repeat23_path"]).reindex(columns=Q_COLS)
    repeat45_df = jsonl_to_dataframe(spec["aug_repeat45_path"]).reindex(columns=Q_COLS)
    backfill_path = spec.get("backfill_path")
    if backfill_path and Path(backfill_path).exists():
        backfill_df = jsonl_to_dataframe(Path(backfill_path)).reindex(columns=Q_COLS)
        if not backfill_df.empty:
            initial_mask = backfill_df.index.to_series().astype(str).str.startswith("paper_analysis_report_joint/")
            repeat23_mask = backfill_df.index.to_series().astype(str).str.startswith(
                ("paper_analysis_report_joint_rep2/", "paper_analysis_report_joint_rep3/")
            )
            repeat45_mask = backfill_df.index.to_series().astype(str).str.startswith(
                ("paper_analysis_report_joint_rep4/", "paper_analysis_report_joint_rep5/")
            )
            if initial_mask.any():
                initial_df = pd.concat([initial_df, backfill_df.loc[initial_mask]], axis=0)
                initial_df = initial_df[~initial_df.index.duplicated(keep="last")]
            if repeat23_mask.any():
                repeat23_df = pd.concat([repeat23_df, backfill_df.loc[repeat23_mask]], axis=0)
                repeat23_df = repeat23_df[~repeat23_df.index.duplicated(keep="last")]
            if repeat45_mask.any():
                repeat45_df = pd.concat([repeat45_df, backfill_df.loc[repeat45_mask]], axis=0)
                repeat45_df = repeat45_df[~repeat45_df.index.duplicated(keep="last")]
    return initial_df, repeat23_df, repeat45_df


def _load_baseline_table(spec: dict[str, object]) -> pd.DataFrame:
    if "baseline_suite_path" in spec:
        return jsonl_to_dataframe(spec["baseline_suite_path"]).reindex(columns=Q_COLS)

    initial_df = jsonl_to_dataframe(spec["baseline_initial_path"]).reindex(columns=Q_COLS)
    repeat_df = jsonl_to_dataframe(spec["baseline_repeat_path"]).reindex(columns=Q_COLS)
    return pd.concat([initial_df, repeat_df], axis=0)


def _available_row(df: pd.DataFrame, row_id: str) -> pd.Series | None:
    if row_id not in df.index:
        return None
    return pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS)


def _mean_rows(rows: list[pd.Series]) -> pd.Series:
    mat = pd.concat(rows, axis=1)
    mat.columns = [f"run{i+1}" for i in range(len(rows))]
    return mat.mean(axis=1, skipna=True)


def _extract_source_ids(initial_df: pd.DataFrame, repeat_dfs: list[pd.DataFrame]) -> list[str]:
    source_ids: set[str] = set()
    for idx in initial_df.index:
        if str(idx).startswith("paper_analysis_report_joint/"):
            source_ids.add(str(idx).split("/", 1)[1])
    for repeat_df in repeat_dfs:
        for idx in repeat_df.index:
            parts = str(idx).split("/", 1)
            if len(parts) == 2 and parts[0].startswith("paper_analysis_report_joint_rep"):
                source_ids.add(parts[1])
    return sorted(source_ids)


def build_average_tables() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    avg_rows: list[dict[str, object]] = []
    baseline_rows: list[dict[str, object]] = []
    coverage_rows: list[dict[str, object]] = []
    registry_rows: list[dict[str, object]] = []
    manifest_rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        aug_paths = [
            ("augmentation", "rep1", spec["aug_initial_path"]),
            ("augmentation", "rep2to3", spec["aug_repeat23_path"]),
            ("augmentation", "rep4to5", spec["aug_repeat45_path"]),
        ]
        if "baseline_suite_path" in spec:
            manifest_paths = [
                *aug_paths,
                ("baseline", "reps1to5", spec["baseline_suite_path"]),
            ]
        else:
            manifest_paths = [
                *aug_paths,
                ("baseline", "rep1", spec["baseline_initial_path"]),
                ("baseline", "reps2to5", spec["baseline_repeat_path"]),
            ]

        for input_role, input_group, path in manifest_paths:
            manifest_rows.append(
                {
                    "model": spec["model"],
                    "input_role": input_role,
                    "input_group": input_group,
                    "path": str(path),
                    "exists": bool(path.exists()),
                }
            )

        if not spec["aug_initial_path"].exists():
            continue
        if not spec["aug_repeat23_path"].exists():
            continue
        if not spec["aug_repeat45_path"].exists():
            continue

        initial_df, repeat23_df, repeat45_df = _load_aug_tables(spec)
        baseline_df = _load_baseline_table(spec)
        source_ids = _extract_source_ids(initial_df, [repeat23_df, repeat45_df])

        if "baseline_suite_path" in spec:
            baseline_ids = list(spec["baseline_ids"])
        else:
            baseline_ids = [spec["baseline_initial_id"], *list(spec["baseline_repeat_ids"])]

        baseline_series = [
            series
            for row_id in baseline_ids
            if (series := _available_row(baseline_df, str(row_id))) is not None
        ]
        if not baseline_series:
            continue

        baseline_mean = _mean_rows(baseline_series)
        baseline_row = {"model": spec["model"], "n_baseline_runs": len(baseline_series)}
        baseline_row.update({q: float(baseline_mean[q]) for q in Q_COLS})
        baseline_rows.append(baseline_row)

        if "baseline_suite_path" in spec:
            baseline_registry_specs = [
                (
                    f"rep{rep}",
                    spec["baseline_suite_path"],
                    f"baseline_joint_reasoning_rep{rep}",
                )
                for rep in range(1, 6)
            ]
        else:
            baseline_registry_specs = [
                ("rep1", spec["baseline_initial_path"], spec["baseline_initial_id"]),
                *[
                    (
                        f"rep{rep + 1}",
                        spec["baseline_repeat_path"],
                        row_id,
                    )
                    for rep, row_id in enumerate(spec["baseline_repeat_ids"])
                ],
            ]

        for run_label, path, row_id in baseline_registry_specs:
            registry_rows.append(
                {
                    "model": spec["model"],
                    "role": "baseline",
                    "source_id": "",
                    "run_label": run_label,
                    "row_id": row_id,
                    "path": str(path),
                    "available": bool(row_id in baseline_df.index),
                }
            )

        n_full_aug_runs = 0
        min_aug_runs = EXPECTED_AUG_RUNS
        max_aug_runs = 0
        for source_id in source_ids:
            aug_series = []
            aug_run_specs = [
                ("rep1", initial_df, f"paper_analysis_report_joint/{source_id}", spec["aug_initial_path"]),
                ("rep2", repeat23_df, f"paper_analysis_report_joint_rep2/{source_id}", spec["aug_repeat23_path"]),
                ("rep3", repeat23_df, f"paper_analysis_report_joint_rep3/{source_id}", spec["aug_repeat23_path"]),
                ("rep4", repeat45_df, f"paper_analysis_report_joint_rep4/{source_id}", spec["aug_repeat45_path"]),
                ("rep5", repeat45_df, f"paper_analysis_report_joint_rep5/{source_id}", spec["aug_repeat45_path"]),
            ]
            for run_label, df, row_id, path in aug_run_specs:
                available = row_id in df.index
                registry_rows.append(
                    {
                        "model": spec["model"],
                        "role": "augmentation",
                        "source_id": source_id,
                        "run_label": run_label,
                        "row_id": row_id,
                        "path": str(path),
                        "available": bool(available),
                    }
                )
                if (series := _available_row(df, row_id)) is not None:
                    aug_series.append(series)

            if not aug_series:
                continue

            min_aug_runs = min(min_aug_runs, len(aug_series))
            max_aug_runs = max(max_aug_runs, len(aug_series))
            if len(aug_series) == EXPECTED_AUG_RUNS:
                n_full_aug_runs += 1

            mean_series = _mean_rows(aug_series)
            row = {
                "model": spec["model"],
                "mode": "joint_reasoning",
                "source_id": source_id,
                "n_aug_runs": len(aug_series),
                "n_baseline_runs": len(baseline_series),
            }
            row.update({q: float(mean_series[q]) for q in Q_COLS})
            avg_rows.append(row)

        coverage_rows.append(
            {
                "model": spec["model"],
                "n_sources_initial_or_repeat": len(source_ids),
                "n_sources_averaged": int(sum(1 for row in avg_rows if row["model"] == spec["model"])),
                "expected_aug_runs": EXPECTED_AUG_RUNS,
                "n_sources_with_all_5_aug_runs": n_full_aug_runs,
                "n_sources_missing_any_aug_runs": int(len(source_ids) - n_full_aug_runs),
                "min_aug_runs_observed": int(min_aug_runs if source_ids else 0),
                "max_aug_runs_observed": int(max_aug_runs),
                "n_baseline_runs_used": len(baseline_series),
            }
        )

    avg_df = pd.DataFrame(avg_rows).sort_values(["model", "source_id"]).reset_index(drop=True)
    baseline_avg_df = pd.DataFrame(baseline_rows).sort_values("model").reset_index(drop=True)
    coverage_df = pd.DataFrame(coverage_rows).sort_values("model").reset_index(drop=True)
    registry_df = pd.DataFrame(registry_rows).sort_values(
        ["model", "role", "source_id", "run_label"]
    ).reset_index(drop=True)
    manifest_df = pd.DataFrame(manifest_rows).sort_values(
        ["model", "input_role", "input_group"]
    ).reset_index(drop=True)
    return avg_df, baseline_avg_df, coverage_df, registry_df, manifest_df


def analyze_significance(
    avg_df: pd.DataFrame,
    baseline_avg_df: pd.DataFrame,
    *,
    n_boot: int = 5000,
    seed: int = 42,
    chunk_size: int = 64,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    truth, control = load_validation()
    learning_mean = np.float32(load_learning_treatment_mean())
    meta = load_metadata()

    true_dir = np.sign(truth - control).astype(np.float32)
    null_mse_full = float(np.mean((truth - learning_mean) ** 2))

    rng = np.random.default_rng(seed)
    boot_idx = rng.integers(0, len(truth), size=(n_boot, len(truth)), dtype=np.int16)
    truth_bs = truth[boot_idx].astype(np.float32)
    control_bs = control[boot_idx].astype(np.float32)
    true_dir_bs = np.sign(truth_bs - control_bs).astype(np.float32)
    null_mse_bs = np.mean((truth_bs - learning_mean) ** 2, axis=1).astype(np.float32)
    truth_mean_bs = truth_bs.mean(axis=1, keepdims=True)
    truth_center_bs = truth_bs - truth_mean_bs
    truth_ss_bs = np.sum(truth_center_bs**2, axis=1).astype(np.float32)

    rows: list[dict[str, object]] = []

    for model in sorted(avg_df["model"].unique()):
        pred_df = avg_df.loc[avg_df["model"] == model].copy()
        base_df = baseline_avg_df.loc[baseline_avg_df["model"] == model].copy()
        if pred_df.empty or base_df.empty:
            continue

        source_ids = pred_df["source_id"].tolist()
        preds = pred_df[Q_COLS].to_numpy(dtype=np.float32)
        base = base_df.iloc[0][Q_COLS].to_numpy(dtype=np.float32)
        base_bs = base[boot_idx].astype(np.float32)

        base_mse_full = float(np.mean((base - truth) ** 2))
        base_rmse = float(np.sqrt(base_mse_full))
        base_corr = float(np.corrcoef(base, truth)[0, 1])
        base_r2 = float(1.0 - base_mse_full / null_mse_full)
        base_da = float(np.mean(np.sign(base - control) == true_dir))

        base_mse_bs = np.mean((base_bs - truth_bs) ** 2, axis=1).astype(np.float32)
        base_rmse_bs = np.sqrt(base_mse_bs).astype(np.float32)
        base_r2_bs = (1.0 - base_mse_bs / null_mse_bs).astype(np.float32)
        base_da_bs = np.mean(
            np.sign(base_bs - control_bs) == true_dir_bs, axis=1
        ).astype(np.float32)
        base_mean_bs = base_bs.mean(axis=1, keepdims=True)
        base_center_bs = base_bs - base_mean_bs
        base_num_bs = np.sum(base_center_bs * truth_center_bs, axis=1)
        base_den_bs = np.sqrt(np.sum(base_center_bs**2, axis=1) * truth_ss_bs)
        base_corr_bs = np.divide(
            base_num_bs,
            base_den_bs,
            out=np.full(n_boot, np.nan, dtype=np.float32),
            where=base_den_bs > 0,
        )

        mse_full = np.mean((preds - truth[None, :]) ** 2, axis=1)
        rmse_full = np.sqrt(mse_full)
        corr_full = _corr_rowwise(preds, truth)
        r2_full = 1.0 - mse_full / null_mse_full
        da_full = np.mean(
            np.sign(preds - control[None, :]) == true_dir[None, :],
            axis=1,
        )

        for start in range(0, preds.shape[0], chunk_size):
            end = min(start + chunk_size, preds.shape[0])
            pred_chunk = preds[start:end]
            id_chunk = source_ids[start:end]
            meta_chunk = pred_df.iloc[start:end]

            pred_bs = pred_chunk[:, boot_idx]
            mse_bs = np.mean((pred_bs - truth_bs[None, :, :]) ** 2, axis=2)
            rmse_bs = np.sqrt(mse_bs)
            r2_bs = 1.0 - mse_bs / null_mse_bs[None, :]
            da_bs = np.mean(
                np.sign(pred_bs - control_bs[None, :, :]) == true_dir_bs[None, :, :],
                axis=2,
            )

            pred_mean_bs = pred_bs.mean(axis=2)
            pred_center_bs = pred_bs - pred_mean_bs[:, :, None]
            pred_num_bs = np.sum(pred_center_bs * truth_center_bs[None, :, :], axis=2)
            pred_den_bs = np.sqrt(
                np.sum(pred_center_bs**2, axis=2) * truth_ss_bs[None, :]
            )
            corr_bs = np.divide(
                pred_num_bs,
                pred_den_bs,
                out=np.full((end - start, n_boot), np.nan, dtype=np.float32),
                where=pred_den_bs > 0,
            )

            delta_arrays = {
                "rmse": rmse_bs - base_rmse_bs[None, :],
                "correlation": corr_bs - base_corr_bs[None, :],
                "r2": r2_bs - base_r2_bs[None, :],
                "directional_accuracy": da_bs - base_da_bs[None, :],
            }

            for j, source_id in enumerate(id_chunk):
                info = meta.get(source_id, {})
                row: dict[str, object] = {
                    "model": model,
                    "mode": "joint_reasoning",
                    "source_id": source_id,
                    "title": info.get("Article Title", ""),
                    "journal": info.get("Source Title", ""),
                    "year": info.get("Publication Year", ""),
                    "n_aug_runs": int(meta_chunk["n_aug_runs"].iloc[j]),
                    "n_baseline_runs": int(base_df["n_baseline_runs"].iloc[0]),
                    "rmse": float(rmse_full[start + j]),
                    "baseline_rmse": base_rmse,
                    "correlation": float(corr_full[start + j]),
                    "baseline_correlation": base_corr,
                    "r2": float(r2_full[start + j]),
                    "baseline_r2": base_r2,
                    "directional_accuracy": float(da_full[start + j]),
                    "baseline_directional_accuracy": base_da,
                }

                delta_full = {
                    "rmse": float(rmse_full[start + j] - base_rmse),
                    "correlation": float(corr_full[start + j] - base_corr),
                    "r2": float(r2_full[start + j] - base_r2),
                    "directional_accuracy": float(da_full[start + j] - base_da),
                }

                for metric in METRICS:
                    delta_boot = delta_arrays[metric][j]
                    finite = delta_boot[np.isfinite(delta_boot)]
                    ci_low, ci_high = (
                        np.nanpercentile(finite, [2.5, 97.5]) if finite.size else (np.nan, np.nan)
                    )
                    row[f"delta_{metric}"] = delta_full[metric]
                    row[f"delta_{metric}_ci_low"] = float(ci_low)
                    row[f"delta_{metric}_ci_high"] = float(ci_high)
                    if metric == "rmse":
                        row[f"sig_improve_{metric}"] = bool(ci_high < 0)
                        row[f"sig_worsen_{metric}"] = bool(ci_low > 0)
                    else:
                        row[f"sig_improve_{metric}"] = bool(ci_low > 0)
                        row[f"sig_worsen_{metric}"] = bool(ci_high < 0)

                rows.append(row)

    detail = pd.DataFrame(rows).sort_values(["model", "source_id"]).reset_index(drop=True)
    summary = _summarize_significance(detail)
    return detail, summary


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    avg_df, baseline_avg_df, coverage_df, registry_df, manifest_df = build_average_tables()
    if avg_df.empty:
        raise FileNotFoundError("No repeat-5 averaged individual-paper predictions could be built.")

    detail, summary = analyze_significance(avg_df, baseline_avg_df)

    detail_path = RESULTS_DIR / "validation_literature_analysis_report_source_significance.csv"
    summary_path = RESULTS_DIR / "validation_literature_analysis_report_source_significance_summary.csv"
    avg_path = RESULTS_DIR / "validation_literature_analysis_report_source_avg_predictions.csv"
    baseline_avg_path = RESULTS_DIR / "validation_literature_analysis_report_source_baseline_avg_predictions.csv"
    coverage_path = RESULTS_DIR / "validation_literature_analysis_report_source_run_coverage.csv"
    registry_path = RESULTS_DIR / "validation_literature_analysis_report_source_run_registry.csv"
    manifest_path = RESULTS_DIR / "validation_literature_analysis_report_source_input_manifest.csv"
    repeat5_feature_dataset_path = RESULTS_DIR / "paper_feature_analysis_dataset_repeat5.csv"

    detail.to_csv(detail_path, index=False)
    summary.to_csv(summary_path, index=False)
    avg_df.to_csv(avg_path, index=False)
    baseline_avg_df.to_csv(baseline_avg_path, index=False)
    coverage_df.to_csv(coverage_path, index=False)
    registry_df.to_csv(registry_path, index=False)
    manifest_df.to_csv(manifest_path, index=False)

    if FEATURE_DATASET_CSV.exists():
        feature_df = pd.read_csv(FEATURE_DATASET_CSV)
        metric_cols = [
            "model",
            "mode",
            "source_id",
            "title",
            "journal",
            "year",
            "delta_correlation",
            "delta_rmse",
            "delta_r2",
            "delta_directional_accuracy",
        ]
        detail_subset = detail[metric_cols].copy()
        feature_key_cols = [col for col in ["model", "mode", "source_id"] if col in feature_df.columns]
        feature_only_cols = [col for col in feature_df.columns if col not in detail_subset.columns]
        repeat5_feature_df = detail_subset.merge(
            feature_df[feature_key_cols + feature_only_cols],
            on=feature_key_cols,
            how="left",
        )
        repeat5_feature_df.to_csv(repeat5_feature_dataset_path, index=False)

    print(detail_path)
    print(summary_path)
    print(avg_path)
    print(baseline_avg_path)
    print(coverage_path)
    print(registry_path)
    print(manifest_path)
    if FEATURE_DATASET_CSV.exists():
        print(repeat5_feature_dataset_path)


if __name__ == "__main__":
    main()
