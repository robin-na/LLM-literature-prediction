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
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources_extended2011"
METADATA_CSV = ROOT / "paper_collection" / "WoS_251031_fileInfo.csv"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRICS = ["correlation", "rmse", "r2", "directional_accuracy"]

RUN_SPECS = [
    {
        "model": "GPT-4.1",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-5.1",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt51.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt51.jsonl",
        "baseline_variation": "baseline_joint_reasoning_rep1",
    },
    {
        "model": "GPT-5 Mini",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt5mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning_rep1",
    },
    {
        "model": "GPT-5 Nano",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_extended2011_joint_gpt5nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_literature_joint_suite_reps1to5_gpt5nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning_rep1",
    },
]


def load_validation() -> tuple[np.ndarray, np.ndarray]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth = (df["efficiency_p"].to_numpy(dtype=float) * 100.0).astype(np.float32)
    control = (df["efficiency_np"].to_numpy(dtype=float) * 100.0).astype(np.float32)
    return truth, control


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
                    "best_sig_improve_source_id": best_improve["source_id"] if best_improve is not None else "",
                    "best_sig_improve_delta": float(best_improve[f"delta_{metric}"]) if best_improve is not None else np.nan,
                    "worst_sig_worsen_source_id": worst_worsen["source_id"] if worst_worsen is not None else "",
                    "worst_sig_worsen_delta": float(worst_worsen[f"delta_{metric}"]) if worst_worsen is not None else np.nan,
                }
            )
    return pd.DataFrame(out_rows).sort_values(["model", "metric"]).reset_index(drop=True)


def analyze_significance(
    n_boot: int = 5000,
    seed: int = 42,
    chunk_size: int = 64,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    truth, control = load_validation()
    meta = load_metadata()

    true_dir = np.sign(truth - control).astype(np.float32)
    null_mse_full = float(np.mean((truth - control) ** 2))

    rng = np.random.default_rng(seed)
    boot_idx = rng.integers(0, len(truth), size=(n_boot, len(truth)), dtype=np.int16)
    truth_bs = truth[boot_idx].astype(np.float32)
    control_bs = control[boot_idx].astype(np.float32)
    true_dir_bs = np.sign(truth_bs - control_bs).astype(np.float32)
    null_mse_bs = np.mean((truth_bs - control_bs) ** 2, axis=1).astype(np.float32)
    truth_mean_bs = truth_bs.mean(axis=1, keepdims=True)
    truth_center_bs = truth_bs - truth_mean_bs
    truth_ss_bs = np.sum(truth_center_bs**2, axis=1).astype(np.float32)

    rows: list[dict[str, object]] = []

    for spec in RUN_SPECS:
        if not spec["output_path"].exists() or not spec["baseline_path"].exists():
            continue

        pred_df = jsonl_to_dataframe(spec["output_path"]).reindex(columns=Q_COLS)
        base_df = jsonl_to_dataframe(spec["baseline_path"]).reindex(columns=Q_COLS)
        if spec["baseline_variation"] not in base_df.index:
            continue

        source_ids = [str(value).split("/", 1)[-1] for value in pred_df.index]
        preds = pred_df.to_numpy(dtype=np.float32)
        base = base_df.loc[spec["baseline_variation"]].to_numpy(dtype=np.float32)
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
            np.sign(preds - control[None, :]) == true_dir[None, :], axis=1
        )

        for start in range(0, preds.shape[0], chunk_size):
            end = min(start + chunk_size, preds.shape[0])
            pred_chunk = preds[start:end]
            id_chunk = source_ids[start:end]

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
                    "model": spec["model"],
                    "mode": "joint_reasoning",
                    "source_id": source_id,
                    "title": info.get("Article Title", ""),
                    "journal": info.get("Source Title", ""),
                    "year": info.get("Publication Year", ""),
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
    detail, summary = analyze_significance()
    detail_path = RESULTS_DIR / "validation_literature_analysis_report_source_significance.csv"
    summary_path = RESULTS_DIR / "validation_literature_analysis_report_source_significance_summary.csv"
    detail.to_csv(detail_path, index=False)
    summary.to_csv(summary_path, index=False)
    print(detail_path)
    print(summary_path)


if __name__ == "__main__":
    main()
