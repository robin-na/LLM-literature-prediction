from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from plot_paths import (  # noqa: E402
    VALIDATION_REASONING_REPEAT_SUMMARY_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (  # noqa: E402
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS as RESULTS,
)
from plot_validation_reasoning_repeat_summary import (  # noqa: E402
    FILE_MODEL_MAP,
    METRICS,
    METRIC_LABELS,
    MODE_LABELS,
    MODE_ORDER,
    MODEL_ORDER,
    ROOT,
    VALIDATION_CSV,
    _model_from_path,
    _parse_repeat_row_id,
    _preferred_order,
    _row_metrics,
)

INPUT_DIR = ROOT / "openAI_batch_output"

INITIAL_MODEL_PATHS = {
    "GPT-3.5 Turbo": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_35turbo.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_35turbo.jsonl",
    },
    "GPT-4.1 Nano": {
        "reasoning": INPUT_DIR / "prediction_crosswave_variations_41nano.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_crosswave_variations_41nano.jsonl",
    },
    "GPT-4.1 Mini": {
        "reasoning": INPUT_DIR / "prediction_crosswave_variations_41mini.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_crosswave_variations_41mini.jsonl",
    },
    "GPT-4o Mini": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_4omini.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_4omini.jsonl",
    },
    "GPT-4o": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_4o.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_4o.jsonl",
    },
    "o3": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_o3.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_o3.jsonl",
    },
    "o4-mini": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_o4mini.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_o4mini.jsonl",
    },
    "GPT-4.1": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variations_41.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variations_41.jsonl",
    },
    "GPT-5.1": {
        "reasoning": INPUT_DIR / "prediction_positive_case_variants_single_gpt51.jsonl",
        "joint_reasoning": INPUT_DIR / "prediction_positive_case_variants_joint_gpt51.jsonl",
    },
}

VARIANT_ORDER = [
    "baseline",
    "both_contrastive",
    "both_ensemble",
    "both_freeform",
    "both_quantitative",
    "both_refined",
    "both_rules",
    "both_structured",
    "both_uncertainty",
    "paper_only_freeform",
    "paper_only_quantitative",
    "paper_only_structured",
    "data_only_freeform",
    "data_only_quantitative",
    "data_only_structured",
]


def load_targets() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId").reset_index(drop=True)
    labels = [f"Q{i}" for i in range(1, len(df) + 1)]
    target = pd.Series(100 * df["efficiency_p"].to_numpy(dtype=float), index=labels)
    control = pd.Series(100 * df["efficiency_np"].to_numpy(dtype=float), index=labels)
    return target, control


def _parse_initial_row_id(row_id: str, mode: str) -> str | None:
    if mode == "reasoning":
        if row_id == "baseline_reasoning":
            return "baseline"
        if row_id.endswith("_reasoning") and not row_id.endswith("_joint_reasoning"):
            return row_id[: -len("_reasoning")]
        return None
    if mode == "joint_reasoning":
        if row_id == "baseline_joint_reasoning":
            return "baseline"
        if row_id.endswith("_joint_reasoning"):
            return row_id[: -len("_joint_reasoning")]
        return None
    return None


def load_repeat_rows(target: pd.Series, control: pd.Series) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    repeat_models: set[str] = set()

    for path in sorted(INPUT_DIR.glob("prediction_positive_case_reasoning_repeats_*.jsonl")):
        model = _model_from_path(path)
        if model is None:
            continue
        repeat_models.add(model)
        df = jsonl_to_dataframe(path).reindex(columns=target.index)
        for row_id, row in df.iterrows():
            variant, mode, run_label, rep_idx = _parse_repeat_row_id(str(row_id))
            metrics = _row_metrics(row, target, control)
            rows.append(
                {
                    "model": model,
                    "variant": variant,
                    "mode": mode,
                    "run_label": run_label,
                    "run_kind": "temp0" if run_label == "temp0" else "temp1",
                    "rep_idx": rep_idx,
                    **metrics,
                }
            )

    for model, path_map in INITIAL_MODEL_PATHS.items():
        if model not in repeat_models:
            continue
        for mode, path in path_map.items():
            if not path.exists():
                continue
            df = jsonl_to_dataframe(path).reindex(columns=target.index)
            for row_id, row in df.iterrows():
                variant = _parse_initial_row_id(str(row_id), mode)
                if variant is None:
                    continue
                metrics = _row_metrics(row, target, control)
                rows.append(
                    {
                        "model": model,
                        "variant": variant,
                        "mode": mode,
                        "run_label": "initial",
                        "run_kind": "temp1",
                        "rep_idx": 0,
                        **metrics,
                    }
                )

    out = pd.DataFrame(rows)
    if out.empty:
        raise FileNotFoundError("No repeat or initial reasoning files found.")
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["mode"] = pd.Categorical(out["mode"], categories=MODE_ORDER, ordered=True)
    out["variant"] = pd.Categorical(
        out["variant"],
        categories=_preferred_order(out["variant"].dropna().astype(str).unique().tolist(), VARIANT_ORDER),
        ordered=True,
    )
    return out.sort_values(["model", "mode", "variant", "run_kind", "rep_idx"])


def summarize(rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    records: list[dict[str, object]] = []
    for (model, mode, variant), group in rows.groupby(["model", "mode", "variant"], observed=True):
        temp1_group = group.loc[group["run_kind"] == "temp1"].copy()
        temp0_group = group.loc[group["run_kind"] == "temp0"].copy()
        rec: dict[str, object] = {
            "model": model,
            "mode": mode,
            "variant": variant,
            "n_temp1_runs": len(temp1_group),
            "has_temp0": not temp0_group.empty,
        }
        temp0_row = temp0_group.iloc[0] if not temp0_group.empty else None
        for metric in METRICS:
            vals = temp1_group[metric].to_numpy(dtype=float)
            rec[f"temp1_mean_{metric}"] = float(np.nanmean(vals))
            rec[f"temp1_sd_{metric}"] = float(np.nanstd(vals, ddof=0))
            rec[f"temp1_min_{metric}"] = float(np.nanmin(vals))
            rec[f"temp1_max_{metric}"] = float(np.nanmax(vals))
            rec[f"temp0_{metric}"] = float(temp0_row[metric]) if temp0_row is not None else float("nan")
            rec[f"temp1_mean_minus_temp0_{metric}"] = (
                float(rec[f"temp1_mean_{metric}"] - rec[f"temp0_{metric}"])
                if temp0_row is not None and np.isfinite(rec[f"temp0_{metric}"])
                else float("nan")
            )
        records.append(rec)

    summary = pd.DataFrame(records).sort_values(["model", "mode", "variant"])

    model_records: list[dict[str, object]] = []
    for (model, mode), part in summary.groupby(["model", "mode"], observed=True):
        rec: dict[str, object] = {"model": model, "mode": mode, "n_conditions": len(part)}
        for metric in METRICS:
            temp1_mean = part[f"temp1_mean_{metric}"].to_numpy(dtype=float)
            temp1_sd = part[f"temp1_sd_{metric}"].to_numpy(dtype=float)
            temp0 = part[f"temp0_{metric}"].to_numpy(dtype=float)
            gap = part[f"temp1_mean_minus_temp0_{metric}"].to_numpy(dtype=float)
            valid = np.isfinite(temp1_mean) & np.isfinite(temp0)
            rec[f"mean_temp1_sd_{metric}"] = float(np.nanmean(temp1_sd))
            rec[f"median_temp1_sd_{metric}"] = float(np.nanmedian(temp1_sd))
            if np.isfinite(gap).any():
                rec[f"mean_abs_gap_to_temp0_{metric}"] = float(np.nanmean(np.abs(gap)))
                rec[f"median_abs_gap_to_temp0_{metric}"] = float(np.nanmedian(np.abs(gap)))
                rec[f"max_abs_gap_to_temp0_{metric}"] = float(np.nanmax(np.abs(gap)))
            else:
                rec[f"mean_abs_gap_to_temp0_{metric}"] = float("nan")
                rec[f"median_abs_gap_to_temp0_{metric}"] = float("nan")
                rec[f"max_abs_gap_to_temp0_{metric}"] = float("nan")
            if valid.sum() >= 2:
                rec[f"corr_temp1mean_vs_temp0_{metric}"] = float(
                    np.corrcoef(temp1_mean[valid], temp0[valid])[0, 1]
                )
            else:
                rec[f"corr_temp1mean_vs_temp0_{metric}"] = float("nan")
        model_records.append(rec)
    model_summary = pd.DataFrame(model_records).sort_values(["mode", "model"])
    return summary, model_summary


def plot_mean_vs_temp0(summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(len(METRICS), 2, figsize=(13.4, 4.0 * len(METRICS)), constrained_layout=False)
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(1, 2)
    color_map = {
        "GPT-3.5 Turbo": "#6c757d",
        "GPT-4.1 Nano": "#8c564b",
        "GPT-4.1 Mini": "#1f77b4",
        "GPT-4o Mini": "#17becf",
        "GPT-4o": "#2ca02c",
        "o3": "#d62728",
        "o4-mini": "#9467bd",
        "GPT-4.1": "#ff7f0e",
        "GPT-5.1": "#1b9e77",
    }

    for row_idx, metric in enumerate(METRICS):
        for col_idx, mode in enumerate(MODE_ORDER):
            ax = axes[row_idx, col_idx]
            part = summary.loc[
                (summary["mode"] == mode)
                & np.isfinite(summary[f"temp0_{metric}"])
                & np.isfinite(summary[f"temp1_mean_{metric}"])
            ].copy()
            if part.empty:
                ax.set_visible(False)
                continue

            x = part[f"temp0_{metric}"].to_numpy(dtype=float)
            y = part[f"temp1_mean_{metric}"].to_numpy(dtype=float)
            lo = float(min(np.nanmin(x), np.nanmin(y)))
            hi = float(max(np.nanmax(x), np.nanmax(y)))
            pad = 0.05 * (hi - lo if hi > lo else 1.0)
            ax.plot([lo - pad, hi + pad], [lo - pad, hi + pad], color="0.35", linestyle="--", linewidth=1.2)

            for _, row in part.iterrows():
                marker = "s" if row["variant"] == "baseline" else "o"
                ax.scatter(
                    row[f"temp0_{metric}"],
                    row[f"temp1_mean_{metric}"],
                    s=52 if marker == "o" else 68,
                    marker=marker,
                    color=color_map.get(str(row["model"]), "#444444"),
                    edgecolors="white",
                    linewidths=0.7,
                    alpha=0.88,
                )

            corr = float(np.corrcoef(x, y)[0, 1]) if len(part) >= 2 else float("nan")
            ax.text(
                0.03,
                0.96,
                f"$r = {corr:.2f}$",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=10,
                bbox={"facecolor": "white", "alpha": 0.75, "edgecolor": "none", "pad": 1.5},
            )
            ax.grid(alpha=0.2)
            ax.set_xlim(lo - pad, hi + pad)
            ax.set_ylim(lo - pad, hi + pad)
            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode])
            if col_idx == 0:
                ax.set_ylabel(f"Mean of 5 temp1 runs: {METRIC_LABELS[metric]}")
            ax.set_xlabel(f"temp0 {METRIC_LABELS[metric]}")

    fig.suptitle(
        "Validation Reasoning: Mean of 5 temp1 Runs vs temp0",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.035,
        "Each point is one model x input-variant condition. Square = baseline, circle = augmented. Dashed line = identity.",
        ha="center",
        va="bottom",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.06, 1, 0.95])
    fig.savefig(PLOTS / "validation_reasoning_repeat5_mean_vs_temp0.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    RESULTS.mkdir(parents=True, exist_ok=True)
    target, control = load_targets()
    rows = load_repeat_rows(target, control)
    summary, model_summary = summarize(rows)

    rows.to_csv(RESULTS / "validation_reasoning_repeat5_rows.csv", index=False)
    summary.to_csv(RESULTS / "validation_reasoning_repeat5_summary.csv", index=False)
    model_summary.to_csv(RESULTS / "validation_reasoning_repeat5_model_summary.csv", index=False)
    plot_mean_vs_temp0(summary)


if __name__ == "__main__":
    main()
