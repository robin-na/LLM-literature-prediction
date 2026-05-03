from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from analyze_validation_collection_analysis_reports_repeat5 import (
    Q_COLS,
    compute_metrics,
    load_learning_treatment_mean,
    load_truth,
)
from jsonl_parser import jsonl_to_dataframe
from plot_paper_main_text_figures import (
    NO_AUG_BENCHMARKS_CSV,
    VALIDATION_CSV,
    corr_with_question_bootstrap_ci,
    paired_corr_delta_bootstrap,
)


OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
GEMINI_BATCH_OUTPUT = ROOT / "gemini_batch_output"
CLAUDE_BATCH_OUTPUT = ROOT / "claude_batch_output"

LEGACY_OPENAI_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
LEGACY_GEMINI_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "gemini_literature_baseline_benchmark_repeat5"
    / "gemini_literature_baseline_benchmark_repeat_rows.csv"
)
LEGACY_CLAUDE_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "claude_literature_baseline_benchmark_repeat5"
    / "claude_literature_baseline_benchmark_repeat_rows.csv"
)

RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"

CONDITION_ORDER = ["baseline", "science_gpt41", "science_gpt51"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "PGG Science report (GPT-4.1)",
    "science_gpt51": "PGG Science report (GPT-5.1)",
}
CONDITION_COLORS = {
    "baseline": "#c9ced6",
    "science_gpt41": "#4c78a8",
    "science_gpt51": "#f28e2b",
}

OPENAI_COMPLETED_SPECS = [
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-4.1",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-4.1 Mini",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41mini.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-4.1 Nano",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41nano.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-5.1",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt51.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-5 Mini",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt5mini.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "openai",
        "platform": "openai",
        "model": "GPT-5 Nano",
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt5nano.jsonl",
        "expected_rows": 85,
    },
]

GEMINI_COMPLETED_SPECS = [
    {
        "provider": "gemini",
        "platform": "gemini",
        "model": "Gemini 2.5 Flash",
        "output_path": GEMINI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gemini25flash.jsonl",
        "expected_rows": 85,
    },
    {
        "provider": "gemini",
        "platform": "gemini",
        "model": "Gemini 2.5 Pro",
        "output_path": GEMINI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gemini25pro.jsonl",
        "expected_rows": 85,
    },
]

CLAUDE_COMPLETED_SPECS = [
    {
        "provider": "claude",
        "platform": "claude",
        "model": "Claude Opus 4.6",
        "tag": "opus46",
    },
    {
        "provider": "claude",
        "platform": "claude",
        "model": "Claude Sonnet 4.6",
        "tag": "sonnet46",
    },
    {
        "provider": "claude",
        "platform": "claude",
        "model": "Claude Haiku 4.5",
        "tag": "haiku45",
    },
]

CLAUDE_MERGED_OUTPUT = (
    CLAUDE_BATCH_OUTPUT
    / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_reasoning_anthropic_merged_allmodels.jsonl"
)

JOB_FILE_SPECS = [
    {
        "provider": "openai",
        "model": "GPT-4.1",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41.jsonl",
    },
    {
        "provider": "openai",
        "model": "GPT-4.1 Mini",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41mini.jsonl",
    },
    {
        "provider": "openai",
        "model": "GPT-4.1 Nano",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_41nano.jsonl",
    },
    {
        "provider": "openai",
        "model": "GPT-5.1",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt51.jsonl",
    },
    {
        "provider": "openai",
        "model": "GPT-5 Mini",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt5mini.jsonl",
    },
    {
        "provider": "openai",
        "model": "GPT-5 Nano",
        "platform": "openai",
        "expected_rows": 85,
        "output_path": OPENAI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gpt5nano.jsonl",
    },
    {
        "provider": "gemini",
        "model": "Gemini 2.5 Flash",
        "platform": "gemini",
        "expected_rows": 85,
        "output_path": GEMINI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gemini25flash.jsonl",
    },
    {
        "provider": "gemini",
        "model": "Gemini 2.5 Pro",
        "platform": "gemini",
        "expected_rows": 85,
        "output_path": GEMINI_BATCH_OUTPUT
        / "prediction_literature_incremental_baseline_reps6to30_pgg_science_gpt41-gpt51_joint_gemini25pro.jsonl",
    },
    {
        "provider": "claude",
        "model": "Claude merged all models",
        "platform": "claude",
        "expected_rows": 255,
        "output_path": CLAUDE_MERGED_OUTPUT,
    },
]

COMPLETED_MODELS = {
    spec["model"] for spec in OPENAI_COMPLETED_SPECS + GEMINI_COMPLETED_SPECS
}.union(spec["model"] for spec in CLAUDE_COMPLETED_SPECS)


def summarize_series(values: pd.Series) -> dict[str, float]:
    arr = values.to_numpy(dtype=float)
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    if n == 0:
        return {
            "count": 0,
            "mean": float("nan"),
            "sd": float("nan"),
            "se": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        }
    mean = float(arr.mean())
    sd = float(arr.std(ddof=1)) if n >= 2 else float("nan")
    se = float(sd / np.sqrt(n)) if n >= 2 else float("nan")
    return {
        "count": n,
        "mean": mean,
        "sd": sd,
        "se": se,
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def _question_cols(df: pd.DataFrame) -> list[str]:
    return [col for col in df.columns if re.fullmatch(r"Q\d+", str(col))]


def audit_downloaded_files() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for spec in JOB_FILE_SPECS:
        output_path = Path(spec["output_path"])
        row: dict[str, object] = {
            "provider": spec["provider"],
            "model": spec["model"],
            "output_path": str(output_path),
            "download_present": output_path.exists(),
            "expected_rows": spec["expected_rows"],
        }
        if not output_path.exists():
            row.update(
                {
                    "parsed_ok": False,
                    "observed_rows": 0,
                    "question_cols": 0,
                    "missing_prediction_cells": pd.NA,
                    "count_ok": False,
                    "include_in_analysis": False,
                }
            )
            rows.append(row)
            continue

        try:
            df = jsonl_to_dataframe(output_path, platform=str(spec["platform"])).reindex(columns=Q_COLS)
            missing_cells = int(df.isna().sum().sum())
            row.update(
                {
                    "parsed_ok": True,
                    "observed_rows": int(df.shape[0]),
                    "question_cols": len(_question_cols(df)),
                    "missing_prediction_cells": missing_cells,
                    "count_ok": int(df.shape[0]) == int(spec["expected_rows"]),
                    "include_in_analysis": int(df.shape[0]) == int(spec["expected_rows"]) and missing_cells == 0,
                }
            )
        except Exception as exc:
            row.update(
                {
                    "parsed_ok": False,
                    "observed_rows": 0,
                    "question_cols": 0,
                    "missing_prediction_cells": pd.NA,
                    "count_ok": False,
                    "include_in_analysis": False,
                    "parse_error": str(exc),
                }
            )
        rows.append(row)

    out = pd.DataFrame(rows).sort_values(["provider", "model"]).reset_index(drop=True)
    if "parse_error" not in out.columns:
        out["parse_error"] = ""
    out["parse_error"] = out["parse_error"].fillna("")
    return out


def load_legacy_baseline_rows() -> pd.DataFrame:
    frames = [
        pd.read_csv(LEGACY_OPENAI_REPEAT_ROWS_CSV),
        pd.read_csv(LEGACY_GEMINI_REPEAT_ROWS_CSV),
        pd.read_csv(LEGACY_CLAUDE_REPEAT_ROWS_CSV),
    ]
    out = pd.concat(frames, ignore_index=True)
    out = out.loc[(out["condition"] == "baseline") & (out["model"].isin(COMPLETED_MODELS))].copy()
    out["source_family"] = "legacy_repeat5"
    return out.loc[:, ["model", "condition", "repeat", "row_id", "source_family", "n", "rmse", "correlation", "r2", "directional_accuracy", *Q_COLS]]


def _build_condition_rows(
    df: pd.DataFrame,
    *,
    model: str,
    source_family: str,
    baseline_ids: list[tuple[int, str]],
    science_gpt41_ids: list[tuple[int, str]],
    science_gpt51_ids: list[tuple[int, str]],
) -> pd.DataFrame:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    rows: list[dict[str, object]] = []

    for condition, id_pairs in [
        ("baseline", baseline_ids),
        ("science_gpt41", science_gpt41_ids),
        ("science_gpt51", science_gpt51_ids),
    ]:
        missing = [row_id for _, row_id in id_pairs if row_id not in df.index]
        if missing:
            raise KeyError(f"Missing {condition} rows for {model}: {missing[:5]}")
        for repeat, row_id in id_pairs:
            pred_row = pd.to_numeric(df.loc[row_id], errors="coerce").reindex(Q_COLS)
            metrics = compute_metrics(pred_row, treatment, control, learning_mean)
            row: dict[str, object] = {
                "model": model,
                "condition": condition,
                "repeat": repeat,
                "row_id": row_id,
                "source_family": source_family,
                **metrics,
            }
            row.update({q: float(pred_row[q]) for q in Q_COLS})
            rows.append(row)
    return pd.DataFrame(rows)


def load_openai_incremental_rows() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for spec in OPENAI_COMPLETED_SPECS:
        df = jsonl_to_dataframe(spec["output_path"], platform="openai").reindex(columns=Q_COLS)
        frames.append(
            _build_condition_rows(
                df,
                model=str(spec["model"]),
                source_family="incremental_openai",
                baseline_ids=[(rep, f"baseline_joint_reasoning_rep{rep}") for rep in range(6, 31)],
                science_gpt41_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}/PGG_Science_gpt41") for rep in range(1, 31)
                ],
                science_gpt51_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}/PGG_Science_gpt51") for rep in range(1, 31)
                ],
            )
        )
    return pd.concat(frames, ignore_index=True)


def load_gemini_incremental_rows() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for spec in GEMINI_COMPLETED_SPECS:
        df = jsonl_to_dataframe(spec["output_path"], platform="gemini").reindex(columns=Q_COLS)
        frames.append(
            _build_condition_rows(
                df,
                model=str(spec["model"]),
                source_family="incremental_gemini",
                baseline_ids=[(rep, f"baseline_joint_reasoning_rep{rep}") for rep in range(6, 31)],
                science_gpt41_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}/PGG_Science_gpt41") for rep in range(1, 31)
                ],
                science_gpt51_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}/PGG_Science_gpt51") for rep in range(1, 31)
                ],
            )
        )
    return pd.concat(frames, ignore_index=True)


def load_claude_incremental_rows() -> pd.DataFrame:
    df = jsonl_to_dataframe(CLAUDE_MERGED_OUTPUT, platform="claude").reindex(columns=Q_COLS)
    frames: list[pd.DataFrame] = []
    for spec in CLAUDE_COMPLETED_SPECS:
        tag = str(spec["tag"])
        frames.append(
            _build_condition_rows(
                df,
                model=str(spec["model"]),
                source_family="incremental_claude",
                baseline_ids=[(rep, f"baseline_joint_reasoning_rep{rep}__{tag}") for rep in range(6, 31)],
                science_gpt41_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}_PGG_Science_gpt41__{tag}") for rep in range(1, 31)
                ],
                science_gpt51_ids=[
                    (rep, f"paper_analysis_report_joint_rep{rep}_PGG_Science_gpt51__{tag}") for rep in range(1, 31)
                ],
            )
        )
    return pd.concat(frames, ignore_index=True)


def build_repeat_rows() -> pd.DataFrame:
    out = pd.concat(
        [
            load_legacy_baseline_rows(),
            load_openai_incremental_rows(),
            load_gemini_incremental_rows(),
            load_claude_incremental_rows(),
        ],
        ignore_index=True,
    )
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["model", "condition", "repeat"]).reset_index(drop=True)


def build_coverage_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    summary = (
        repeat_rows.groupby(["model", "condition"], observed=False)
        .agg(
            n_repeats=("repeat", "count"),
            min_repeat=("repeat", "min"),
            max_repeat=("repeat", "max"),
            mean_missing_predictions=("n", lambda s: float((20 - s).mean())),
        )
        .reset_index()
    )
    summary["expected_repeats"] = summary["condition"].map({"baseline": 30, "science_gpt41": 30, "science_gpt51": 30})
    summary["complete"] = summary["n_repeats"] == summary["expected_repeats"]
    return summary.sort_values(["model", "condition"]).reset_index(drop=True)


def build_repeat_metric_summary(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    metric_cols = ["rmse", "correlation", "r2", "directional_accuracy"]
    rows: list[dict[str, object]] = []
    for (model, condition), sub in repeat_rows.groupby(["model", "condition"], observed=False):
        for metric in metric_cols:
            summary = summarize_series(sub[metric])
            rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "metric": metric,
                    "n_repeats": summary["count"],
                    "mean": summary["mean"],
                    "sd": summary["sd"],
                    "se": summary["se"],
                    "min": summary["min"],
                    "max": summary["max"],
                }
            )
    return pd.DataFrame(rows).sort_values(["metric", "condition", "model"]).reset_index(drop=True)


def build_avg_predictions(repeat_rows: pd.DataFrame) -> pd.DataFrame:
    avg = (
        repeat_rows.groupby(["model", "condition"], as_index=False, observed=False)[Q_COLS]
        .mean()
        .sort_values(["model", "condition"])
        .reset_index(drop=True)
    )
    counts = (
        repeat_rows.groupby(["model", "condition"], as_index=False, observed=False)["repeat"]
        .count()
        .rename(columns={"repeat": "n_runs"})
    )
    avg = avg.merge(counts, on=["model", "condition"], how="left")
    return avg.loc[:, ["model", "condition", "n_runs", *Q_COLS]]


def build_avg_prediction_metrics(avg_predictions: pd.DataFrame) -> pd.DataFrame:
    treatment, control = load_truth()
    learning_mean = load_learning_treatment_mean()
    rows: list[dict[str, object]] = []
    for _, row in avg_predictions.iterrows():
        pred_row = pd.Series({q: row[q] for q in Q_COLS})
        metrics = compute_metrics(pred_row, treatment, control, learning_mean)
        rows.append(
            {
                "model": row["model"],
                "condition": row["condition"],
                "n_runs": row["n_runs"],
                **metrics,
            }
        )
    return pd.DataFrame(rows).sort_values(["condition", "correlation", "model"], ascending=[True, False, True]).reset_index(drop=True)


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def build_ensemble_correlation_tables(
    avg_predictions: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth = validation["efficiency_p"].to_numpy(dtype=float) * 100.0

    plot_rows: list[dict[str, object]] = []
    delta_rows: list[dict[str, object]] = []
    model_list = sorted(avg_predictions["model"].unique().tolist())

    for seed_idx, model in enumerate(model_list):
        sub = avg_predictions.loc[avg_predictions["model"] == model].copy()
        baseline_row = sub.loc[sub["condition"] == "baseline"]
        if baseline_row.empty:
            continue
        baseline_vec = baseline_row.iloc[0][Q_COLS].to_numpy(dtype=float)

        for condition_idx, condition in enumerate(CONDITION_ORDER):
            cond_row = sub.loc[sub["condition"] == condition]
            if cond_row.empty:
                continue
            vec = cond_row.iloc[0][Q_COLS].to_numpy(dtype=float)
            corr, lo, hi = corr_with_question_bootstrap_ci(
                vec,
                truth,
                seed=1000 + 100 * seed_idx + condition_idx,
            )
            plot_rows.append(
                {
                    "model": model,
                    "condition": condition,
                    "correlation": corr,
                    "ci_low": lo,
                    "ci_high": hi,
                    "n_runs": int(cond_row.iloc[0]["n_runs"]),
                }
            )

        for comparison_idx, target_condition in enumerate(["science_gpt41", "science_gpt51"]):
            target_row = sub.loc[sub["condition"] == target_condition]
            if target_row.empty:
                continue
            target_vec = target_row.iloc[0][Q_COLS].to_numpy(dtype=float)
            delta_corr, delta_ci, sig_label = paired_corr_delta_bootstrap(
                baseline_vec,
                target_vec,
                truth,
                seed=2000 + 100 * seed_idx + comparison_idx,
            )
            delta_rows.append(
                {
                    "model": model,
                    "from_condition": "baseline",
                    "to_condition": target_condition,
                    "comparison": f"{target_condition}_vs_baseline",
                    "delta_correlation": delta_corr,
                    "delta_correlation_ci_low": delta_ci["ci95_low"],
                    "delta_correlation_ci_high": delta_ci["ci95_high"],
                    "delta_correlation_ci99_low": delta_ci["ci99_low"],
                    "delta_correlation_ci99_high": delta_ci["ci99_high"],
                    "delta_correlation_ci999_low": delta_ci["ci999_low"],
                    "delta_correlation_ci999_high": delta_ci["ci999_high"],
                    "paired_sig_label": sig_label,
                }
            )

        gpt41_row = sub.loc[sub["condition"] == "science_gpt41"]
        gpt51_row = sub.loc[sub["condition"] == "science_gpt51"]
        if not gpt41_row.empty and not gpt51_row.empty:
            gpt41_vec = gpt41_row.iloc[0][Q_COLS].to_numpy(dtype=float)
            gpt51_vec = gpt51_row.iloc[0][Q_COLS].to_numpy(dtype=float)
            delta_corr, delta_ci, sig_label = paired_corr_delta_bootstrap(
                gpt41_vec,
                gpt51_vec,
                truth,
                seed=3000 + seed_idx,
            )
            delta_rows.append(
                {
                    "model": model,
                    "from_condition": "science_gpt41",
                    "to_condition": "science_gpt51",
                    "comparison": "science_gpt51_vs_science_gpt41",
                    "delta_correlation": delta_corr,
                    "delta_correlation_ci_low": delta_ci["ci95_low"],
                    "delta_correlation_ci_high": delta_ci["ci95_high"],
                    "delta_correlation_ci99_low": delta_ci["ci99_low"],
                    "delta_correlation_ci99_high": delta_ci["ci99_high"],
                    "delta_correlation_ci999_low": delta_ci["ci999_low"],
                    "delta_correlation_ci999_high": delta_ci["ci999_high"],
                    "paired_sig_label": sig_label,
                }
            )

    plot_df = pd.DataFrame(plot_rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)["model"]
        .tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    plot_df["condition"] = pd.Categorical(plot_df["condition"], categories=CONDITION_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    delta_df = pd.DataFrame(delta_rows)
    if not delta_df.empty:
        delta_df["model"] = pd.Categorical(delta_df["model"], categories=baseline_order, ordered=True)
        delta_df = delta_df.sort_values(["comparison", "model"]).reset_index(drop=True)
    return plot_df, delta_df


def plot_ensemble_correlations(plot_df: pd.DataFrame, *, ceiling: float, output_stem: str) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.0, 7.8))
    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.25, "science_gpt41": 0.0, "science_gpt51": 0.25}

    ax.axvline(ceiling, color="#0f766e", linestyle="--", linewidth=1.4, zorder=1)

    for condition in CONDITION_ORDER:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        ax.barh(
            y,
            part["correlation"].to_numpy(dtype=float),
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.22,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack(
            [
                part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
                part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
            ]
        )
        ax.errorbar(
            part["correlation"].to_numpy(dtype=float),
            y,
            xerr=xerr,
            fmt="none",
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.3),
            elinewidth=0.9,
            capsize=2.5,
            zorder=3,
        )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
        Line2D([0], [0], color=CONDITION_COLORS["science_gpt51"], linewidth=8, label=CONDITION_LABELS["science_gpt51"]),
        Line2D([0], [0], color="#0f766e", linestyle="--", linewidth=1.4, label="Estimated noise ceiling"),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )

    fig.tight_layout()
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / f"{output_stem}.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / f"{output_stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def build_rankings(ensemble_plot_rows: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for condition in CONDITION_ORDER:
        sub = ensemble_plot_rows.loc[ensemble_plot_rows["condition"] == condition].copy()
        sub = sub.sort_values("correlation", ascending=False).reset_index(drop=True)
        for rank, (_, row) in enumerate(sub.iterrows(), start=1):
            rows.append(
                {
                    "condition": condition,
                    "rank": rank,
                    "model": row["model"],
                    "correlation": row["correlation"],
                    "ci_low": row["ci_low"],
                    "ci_high": row["ci_high"],
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    file_audit = audit_downloaded_files()
    repeat_rows = build_repeat_rows()
    coverage = build_coverage_summary(repeat_rows)
    repeat_metric_summary = build_repeat_metric_summary(repeat_rows)
    avg_predictions = build_avg_predictions(repeat_rows)
    avg_prediction_metrics = build_avg_prediction_metrics(avg_predictions)
    ensemble_plot_rows, ensemble_delta_summary = build_ensemble_correlation_tables(avg_predictions)
    ranking = build_rankings(ensemble_plot_rows)

    file_audit.to_csv(RESULTS_DIR / "incremental_pgg_science_job_file_audit.csv", index=False)
    repeat_rows.to_csv(RESULTS_DIR / "incremental_pgg_science_repeat_rows.csv", index=False)
    coverage.to_csv(RESULTS_DIR / "incremental_pgg_science_run_coverage.csv", index=False)
    repeat_metric_summary.to_csv(RESULTS_DIR / "incremental_pgg_science_repeat_metric_summary.csv", index=False)
    avg_predictions.to_csv(RESULTS_DIR / "incremental_pgg_science_avg_predictions.csv", index=False)
    avg_prediction_metrics.to_csv(RESULTS_DIR / "incremental_pgg_science_avg_prediction_metrics.csv", index=False)
    ensemble_plot_rows.to_csv(RESULTS_DIR / "incremental_pgg_science_ensemble_correlation_summary.csv", index=False)
    ensemble_delta_summary.to_csv(RESULTS_DIR / "incremental_pgg_science_ensemble_delta_summary.csv", index=False)
    ranking.to_csv(RESULTS_DIR / "incremental_pgg_science_ensemble_rankings.csv", index=False)

    plot_ensemble_correlations(
        ensemble_plot_rows,
        ceiling=load_noise_ceiling(),
        output_stem="incremental_pgg_science_ensemble_correlation",
    )


if __name__ == "__main__":
    main()
