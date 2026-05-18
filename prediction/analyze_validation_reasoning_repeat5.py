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
from plot_validation_reasoning_repeat5_summary import (  # noqa: E402
    INITIAL_MODEL_PATHS,
    METRICS,
    METRIC_LABELS,
    MODE_LABELS,
    MODE_ORDER,
    MODEL_ORDER,
    ROOT,
    VALIDATION_CSV,
    _model_from_path,
    _parse_initial_row_id,
)
from plot_validation_reasoning_repeat_summary import _parse_repeat_row_id  # noqa: E402
from prediction_metrics import _directional_accuracy_np  # noqa: E402

try:
    from scipy.stats import chi2
except Exception:  # pragma: no cover
    chi2 = None

INPUT_DIR = ROOT / "openAI_batch_output"
BETTER_HIGHER = {
    "rmse": False,
    "correlation": True,
    "r2": True,
    "directional_accuracy": True,
}


def load_targets() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId").reset_index(drop=True)
    labels = [f"Q{i}" for i in range(1, len(df) + 1)]
    target = pd.Series(100 * df["efficiency_p"].to_numpy(dtype=float), index=labels)
    control = pd.Series(100 * df["efficiency_np"].to_numpy(dtype=float), index=labels)
    return target, control


def _safe_corr(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2:
        return float("nan")
    if np.isclose(np.std(y_true), 0.0) or np.isclose(np.std(y_pred), 0.0):
        return float("nan")
    return float(np.corrcoef(y_true, y_pred)[0, 1])


def evaluate_predictions(preds: pd.Series, target: pd.Series, control: pd.Series) -> dict[str, float]:
    valid = preds.notna() & target.notna() & control.notna()
    n_questions = int(valid.sum())
    if n_questions == 0:
        return {
            "n_questions": 0,
            "rmse": float("nan"),
            "correlation": float("nan"),
            "r2": float("nan"),
            "directional_accuracy": float("nan"),
        }
    y_true = target.loc[valid].to_numpy(dtype=float)
    y_pred = preds.loc[valid].to_numpy(dtype=float)
    y_ctrl = control.loc[valid].to_numpy(dtype=float)
    mse = float(np.mean((y_pred - y_true) ** 2))
    rmse = math.sqrt(mse)
    null_mean = float(np.mean(y_true))
    null_mse = float(np.mean((y_true - null_mean) ** 2))
    r2 = float("nan") if np.isclose(null_mse, 0.0) else 1.0 - mse / null_mse
    return {
        "n_questions": n_questions,
        "rmse": rmse,
        "correlation": _safe_corr(y_true, y_pred),
        "r2": r2,
        "directional_accuracy": _directional_accuracy_np(y_pred, y_true, y_ctrl),
    }


def load_prediction_cube(target: pd.Series) -> dict[tuple[str, str, str, str], pd.Series]:
    cube: dict[tuple[str, str, str, str], pd.Series] = {}

    for path in sorted(INPUT_DIR.glob("prediction_positive_case_reasoning_repeats_*.jsonl")):
        model = _model_from_path(path)
        if model is None:
            continue
        df = jsonl_to_dataframe(path).reindex(columns=target.index)
        for row_id, row in df.iterrows():
            variant, mode, run_label, _ = _parse_repeat_row_id(str(row_id))
            cube[(model, mode, variant, run_label)] = row.astype(float)

    repeat_models = {key[0] for key in cube.keys()}
    for model, mode_map in INITIAL_MODEL_PATHS.items():
        if model not in repeat_models:
            continue
        for mode, path in mode_map.items():
            if not path.exists():
                continue
            df = jsonl_to_dataframe(path).reindex(columns=target.index)
            for row_id, row in df.iterrows():
                variant = _parse_initial_row_id(str(row_id), mode)
                if variant is None:
                    continue
                cube[(model, mode, variant, "initial")] = row.astype(float)
    return cube


def build_condition_table(
    cube: dict[tuple[str, str, str, str], pd.Series],
    target: pd.Series,
    control: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    keys = {(model, mode, variant) for model, mode, variant, _ in cube.keys()}
    condition_rows: list[dict[str, object]] = []
    run_rows: list[dict[str, object]] = []

    for model, mode, variant in sorted(keys, key=lambda x: (MODEL_ORDER.index(x[0]), MODE_ORDER.index(x[1]), x[2])):
        runs = {run_label: cube[(model, mode, variant, run_label)] for run_label in sorted({k[3] for k in cube.keys() if k[:3] == (model, mode, variant)})}
        temp1_labels = [label for label in ["initial", "rep1", "rep2", "rep3", "rep4"] if label in runs]
        temp0_present = "temp0" in runs
        temp1_preds = pd.concat([runs[label] for label in temp1_labels], axis=1)
        temp1_preds.columns = temp1_labels
        avg_preds = temp1_preds.mean(axis=1, skipna=True)
        avg_metrics = evaluate_predictions(avg_preds, target, control)

        per_run_metrics: dict[str, list[float]] = {metric: [] for metric in METRICS}
        for label in temp1_labels:
            metrics = evaluate_predictions(runs[label], target, control)
            run_rows.append(
                {
                    "model": model,
                    "mode": mode,
                    "variant": variant,
                    "run_label": label,
                    **metrics,
                }
            )
            for metric in METRICS:
                per_run_metrics[metric].append(metrics[metric])

        row: dict[str, object] = {
            "model": model,
            "mode": mode,
            "variant": variant,
            "n_temp1_runs": len(temp1_labels),
            "temp0_present": temp0_present,
        }
        for metric in METRICS:
            vals = np.asarray(per_run_metrics[metric], dtype=float)
            row[f"mean_run_metric_{metric}"] = float(np.nanmean(vals))
            row[f"sd_run_metric_{metric}"] = float(np.nanstd(vals, ddof=1)) if len(vals) > 1 else 0.0
            row[f"mean_prediction_metric_{metric}"] = float(avg_metrics[metric])
            row[f"mean_prediction_minus_mean_run_{metric}"] = float(
                row[f"mean_prediction_metric_{metric}"] - row[f"mean_run_metric_{metric}"]
            )
            row[f"sampling_var_{metric}"] = float((row[f"sd_run_metric_{metric}"] ** 2) / max(len(vals), 1))
            if temp0_present:
                temp0_metrics = evaluate_predictions(runs["temp0"], target, control)
                row[f"temp0_metric_{metric}"] = float(temp0_metrics[metric])
                row[f"mean_prediction_minus_temp0_{metric}"] = float(
                    row[f"mean_prediction_metric_{metric}"] - row[f"temp0_metric_{metric}"]
                )
            else:
                row[f"temp0_metric_{metric}"] = float("nan")
                row[f"mean_prediction_minus_temp0_{metric}"] = float("nan")
        condition_rows.append(row)

    conditions = pd.DataFrame(condition_rows)
    runs = pd.DataFrame(run_rows)
    conditions["model"] = pd.Categorical(conditions["model"], categories=MODEL_ORDER, ordered=True)
    conditions["mode"] = pd.Categorical(conditions["mode"], categories=MODE_ORDER, ordered=True)
    runs["model"] = pd.Categorical(runs["model"], categories=MODEL_ORDER, ordered=True)
    runs["mode"] = pd.Categorical(runs["mode"], categories=MODE_ORDER, ordered=True)
    return conditions.sort_values(["model", "mode", "variant"]), runs.sort_values(["model", "mode", "variant", "run_label"])


def build_comparison_summary(conditions: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (model, mode), part in conditions.groupby(["model", "mode"], observed=True):
        rec: dict[str, object] = {"model": model, "mode": mode, "n_conditions": len(part)}
        for metric in METRICS:
            diff_meanrun = part[f"mean_prediction_minus_mean_run_{metric}"].astype(float)
            rec[f"avg_meanpred_minus_meanrun_{metric}"] = float(diff_meanrun.mean())
            if BETTER_HIGHER[metric]:
                rec[f"meanpred_better_than_meanrun_count_{metric}"] = int((diff_meanrun > 0).sum())
            else:
                rec[f"meanpred_better_than_meanrun_count_{metric}"] = int((diff_meanrun < 0).sum())

            has_temp0 = part[f"temp0_metric_{metric}"].notna()
            if has_temp0.any():
                diff_temp0 = part.loc[has_temp0, f"mean_prediction_minus_temp0_{metric}"].astype(float)
                rec[f"avg_meanpred_minus_temp0_{metric}"] = float(diff_temp0.mean())
                if BETTER_HIGHER[metric]:
                    rec[f"meanpred_better_than_temp0_count_{metric}"] = int((diff_temp0 > 0).sum())
                else:
                    rec[f"meanpred_better_than_temp0_count_{metric}"] = int((diff_temp0 < 0).sum())
            else:
                rec[f"avg_meanpred_minus_temp0_{metric}"] = float("nan")
                rec[f"meanpred_better_than_temp0_count_{metric}"] = np.nan
        rows.append(rec)
    return pd.DataFrame(rows).sort_values(["mode", "model"])


def _cochrans_q(y: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    w = 1.0 / np.maximum(v, 1e-12)
    mu = float(np.sum(w * y) / np.sum(w))
    q = float(np.sum(w * (y - mu) ** 2))
    return q, mu


def build_heterogeneity_table(conditions: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    factor_defs = {
        "model": ["model"],
        "mode": ["mode"],
        "variant": ["variant"],
        "model_mode": ["model", "mode"],
        "mode_variant": ["mode", "variant"],
    }
    for metric in METRICS:
        y = conditions[f"mean_run_metric_{metric}"].to_numpy(dtype=float)
        v = conditions[f"sampling_var_{metric}"].to_numpy(dtype=float)
        q_total, mu = _cochrans_q(y, v)
        k = len(conditions)
        i2_total = max((q_total - (k - 1)) / q_total, 0.0) if q_total > 0 else float("nan")
        within_mean_sd = float(conditions[f"sd_run_metric_{metric}"].mean())
        overall_sd = float(np.nanstd(y, ddof=0))
        rows.append(
            {
                "metric": metric,
                "factor": "overall",
                "n_levels": k,
                "overall_mean": mu,
                "within_mean_sd": within_mean_sd,
                "between_level_sd": overall_sd,
                "q_total": q_total,
                "q_between": float("nan"),
                "i2_total": i2_total,
                "share_of_total_q": float("nan"),
                "p_value": float("nan"),
            }
        )

        for factor_name, cols in factor_defs.items():
            q_within = 0.0
            level_means = []
            for _, part in conditions.groupby(cols, observed=True):
                yg = part[f"mean_run_metric_{metric}"].to_numpy(dtype=float)
                vg = part[f"sampling_var_{metric}"].to_numpy(dtype=float)
                qg, mug = _cochrans_q(yg, vg)
                q_within += qg
                level_means.append(mug)
            q_between = max(q_total - q_within, 0.0)
            df_between = len(level_means) - 1
            p_value = float(chi2.sf(q_between, df_between)) if chi2 is not None and df_between > 0 else float("nan")
            rows.append(
                {
                    "metric": metric,
                    "factor": factor_name,
                    "n_levels": len(level_means),
                    "overall_mean": mu,
                    "within_mean_sd": within_mean_sd,
                    "between_level_sd": float(np.nanstd(level_means, ddof=0)),
                    "q_total": q_total,
                    "q_between": q_between,
                    "i2_total": i2_total,
                    "share_of_total_q": q_between / q_total if q_total > 0 else float("nan"),
                    "p_value": p_value,
                }
            )
    return pd.DataFrame(rows)


def build_ensemble_table(
    cube: dict[tuple[str, str, str, str], pd.Series],
    target: pd.Series,
    control: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    keys = {(mode, variant) for _, mode, variant, run_label in cube.keys() if run_label in {"initial", "rep1", "rep2", "rep3", "rep4"}}
    condition_rows: list[dict[str, object]] = []
    model_rows: list[dict[str, object]] = []

    for mode, variant in sorted(keys, key=lambda x: (MODE_ORDER.index(x[0]), x[1])):
        model_means: dict[str, pd.Series] = {}
        for model in MODEL_ORDER:
            labels = [label for label in ["initial", "rep1", "rep2", "rep3", "rep4"] if (model, mode, variant, label) in cube]
            if not labels:
                continue
            preds = pd.concat([cube[(model, mode, variant, label)] for label in labels], axis=1).mean(axis=1, skipna=True)
            model_means[model] = preds
            metrics = evaluate_predictions(preds, target, control)
            model_rows.append({"mode": mode, "variant": variant, "model": model, **metrics})

        if not model_means:
            continue
        ensemble_preds = pd.concat(model_means.values(), axis=1).mean(axis=1, skipna=True)
        ensemble_metrics = evaluate_predictions(ensemble_preds, target, control)
        row: dict[str, object] = {"mode": mode, "variant": variant, "n_models": len(model_means), **ensemble_metrics}
        model_df = pd.DataFrame(model_rows).loc[
            lambda d: (d["mode"] == mode) & (d["variant"] == variant)
        ].copy()
        for metric in METRICS:
            if BETTER_HIGHER[metric]:
                best_val = float(model_df[metric].max())
                row[f"best_individual_{metric}"] = best_val
                row[f"ensemble_minus_best_{metric}"] = float(row[metric] - best_val)
                row[f"ensemble_beats_best_{metric}"] = bool(row[metric] > best_val)
            else:
                best_val = float(model_df[metric].min())
                row[f"best_individual_{metric}"] = best_val
                row[f"ensemble_minus_best_{metric}"] = float(row[metric] - best_val)
                row[f"ensemble_beats_best_{metric}"] = bool(row[metric] < best_val)
        condition_rows.append(row)

    return pd.DataFrame(condition_rows).sort_values(["mode", "variant"]), pd.DataFrame(model_rows).sort_values(["mode", "variant", "model"])


def build_ensemble_summary(ensemble_conditions: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for mode, part in ensemble_conditions.groupby("mode", observed=True):
        rec: dict[str, object] = {"mode": mode, "n_conditions": len(part)}
        for metric in METRICS:
            rec[f"ensemble_mean_{metric}"] = float(part[metric].mean())
            rec[f"best_individual_mean_{metric}"] = float(part[f"best_individual_{metric}"].mean())
            rec[f"ensemble_beats_best_count_{metric}"] = int(part[f"ensemble_beats_best_{metric}"].sum())
            rec[f"ensemble_minus_best_mean_{metric}"] = float(part[f"ensemble_minus_best_{metric}"].mean())
        rows.append(rec)
    return pd.DataFrame(rows).sort_values("mode")


def plot_meanpred_comparison(summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(len(METRICS), 2, figsize=(12.8, 3.6 * len(METRICS)), constrained_layout=False)
    if len(METRICS) == 1:
        axes = np.asarray(axes).reshape(1, 2)
    for row_idx, metric in enumerate(METRICS):
        for col_idx, mode in enumerate(MODE_ORDER):
            ax = axes[row_idx, col_idx]
            part = summary.loc[summary["mode"] == mode].copy()
            x = np.arange(len(part))
            width = 0.36
            y1 = part[f"avg_meanpred_minus_meanrun_{metric}"].to_numpy(dtype=float)
            y2 = part[f"avg_meanpred_minus_temp0_{metric}"].to_numpy(dtype=float)
            ax.axhline(0.0, color="0.6", linestyle="--", linewidth=1.0)
            ax.bar(x - width / 2, y1, width=width, color="#1f77b4", label="mean(predictions) - mean(run metrics)")
            valid = np.isfinite(y2)
            ax.bar(x[valid] + width / 2, y2[valid], width=width, color="#ff7f0e", label="mean(predictions) - temp0")
            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode])
            if col_idx == 0:
                direction = "lower is better" if metric == "rmse" else "higher is better"
                ax.set_ylabel(f"{METRIC_LABELS[metric]} diff\n({direction})")
            ax.set_xticks(x)
            ax.set_xticklabels(part["model"], rotation=45, ha="right", fontsize=9)
            ax.grid(alpha=0.2, axis="y")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle("Validation Reasoning Repeat5: mean(predictions) vs mean(run metrics) and temp0", fontsize=16, y=0.98)
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(PLOTS / "validation_reasoning_repeat5_meanpred_comparison.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_heterogeneity(heterogeneity: pd.DataFrame) -> None:
    part = heterogeneity.loc[heterogeneity["factor"] != "overall"].copy()
    factors = ["model", "mode", "variant", "model_mode", "mode_variant"]
    fig, axes = plt.subplots(1, len(METRICS), figsize=(4.8 * len(METRICS), 4.8), constrained_layout=False)
    axes = np.atleast_1d(axes)
    for ax, metric in zip(axes, METRICS):
        metric_part = part.loc[part["metric"] == metric].set_index("factor").reindex(factors).reset_index()
        ax.bar(np.arange(len(factors)), metric_part["share_of_total_q"], color="#2b8cbe")
        ax.set_xticks(np.arange(len(factors)))
        ax.set_xticklabels(factors, rotation=40, ha="right")
        ax.set_ylim(0, 1)
        ax.set_title(METRIC_LABELS[metric])
        ax.grid(alpha=0.2, axis="y")
        if metric == "rmse":
            ax.set_ylabel("Share of weighted heterogeneity (Q)")
    fig.suptitle(
        "Validation Reasoning Repeat5: Meta-analytic Heterogeneity Decomposition",
        fontsize=15,
        y=0.98,
    )
    fig.text(
        0.5,
        0.01,
        "Inverse-variance weighted subgroup decomposition using within-condition repeat variance as sampling error.",
        ha="center",
        va="bottom",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.07, 1, 0.92])
    fig.savefig(PLOTS / "validation_reasoning_repeat5_heterogeneity.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_ensemble(ensemble_summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, len(METRICS), figsize=(4.5 * len(METRICS), 4.8), constrained_layout=False)
    axes = np.atleast_1d(axes)
    for ax, metric in zip(axes, METRICS):
        part = ensemble_summary.copy()
        x = np.arange(len(part))
        width = 0.35
        ax.bar(x - width / 2, part[f"ensemble_mean_{metric}"], width=width, color="#2ca02c", label="Ensemble")
        ax.bar(x + width / 2, part[f"best_individual_mean_{metric}"], width=width, color="#7f7f7f", label="Best individual")
        ax.set_xticks(x)
        ax.set_xticklabels(part["mode"].map(MODE_LABELS), rotation=20, ha="right")
        ax.set_title(METRIC_LABELS[metric])
        ax.grid(alpha=0.2, axis="y")
        if metric == "rmse":
            ax.set_ylabel("Average over variants")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle("Validation Reasoning Repeat5: Equal-weight Model Ensemble vs Best Individual", fontsize=15, y=0.98)
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.93])
    fig.savefig(PLOTS / "validation_reasoning_repeat5_ensemble.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    RESULTS.mkdir(parents=True, exist_ok=True)
    target, control = load_targets()
    cube = load_prediction_cube(target)
    conditions, runs = build_condition_table(cube, target, control)
    comparison_summary = build_comparison_summary(conditions)
    heterogeneity = build_heterogeneity_table(conditions)
    ensemble_conditions, ensemble_models = build_ensemble_table(cube, target, control)
    ensemble_summary = build_ensemble_summary(ensemble_conditions)

    conditions.to_csv(RESULTS / "validation_reasoning_repeat5_condition_comparison.csv", index=False)
    runs.to_csv(RESULTS / "validation_reasoning_repeat5_run_metrics.csv", index=False)
    comparison_summary.to_csv(RESULTS / "validation_reasoning_repeat5_comparison_summary.csv", index=False)
    heterogeneity.to_csv(RESULTS / "validation_reasoning_repeat5_heterogeneity.csv", index=False)
    ensemble_conditions.to_csv(RESULTS / "validation_reasoning_repeat5_ensemble_conditions.csv", index=False)
    ensemble_models.to_csv(RESULTS / "validation_reasoning_repeat5_ensemble_models.csv", index=False)
    ensemble_summary.to_csv(RESULTS / "validation_reasoning_repeat5_ensemble_summary.csv", index=False)

    plot_meanpred_comparison(comparison_summary)
    plot_heterogeneity(heterogeneity)
    plot_ensemble(ensemble_summary)


if __name__ == "__main__":
    main()
