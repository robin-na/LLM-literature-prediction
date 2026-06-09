from __future__ import annotations

import math
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from prediction_metrics import _directional_accuracy_np  # noqa: E402
from plot_paths import (  # noqa: E402
    VALIDATION_REASONING_REPEAT_SUMMARY_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (  # noqa: E402
    VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS as RESULTS,
)


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "openAI_batch_output"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"

FILE_MODEL_MAP = {
    "35turbo": "GPT-3.5 Turbo",
    "41nano": "GPT-4.1 Nano",
    "41mini": "GPT-4.1 Mini",
    "4omini": "GPT-4o Mini",
    "4o": "GPT-4o",
    "o3": "o3",
    "o4mini": "o4-mini",
    "41": "GPT-4.1",
    "gpt51": "GPT-5.1",
}

MODEL_ORDER = [
    "GPT-3.5 Turbo",
    "GPT-4.1 Nano",
    "GPT-4.1 Mini",
    "GPT-4o Mini",
    "GPT-4o",
    "o3",
    "o4-mini",
    "GPT-4.1",
    "GPT-5.1",
]

MODE_ORDER = ["reasoning", "joint_reasoning"]
MODE_LABELS = {
    "reasoning": "with explanation",
    "joint_reasoning": "joint with explanation",
}
METRICS = ["rmse", "correlation", "r2", "directional_accuracy"]
METRIC_LABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$",
    "directional_accuracy": "Directional Accuracy",
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
BETTER_HIGHER = {
    "rmse": False,
    "correlation": True,
    "r2": True,
    "directional_accuracy": True,
}


def _preferred_order(values: list[str], preferred: list[str]) -> list[str]:
    rank = {value: idx for idx, value in enumerate(preferred)}
    return sorted(values, key=lambda value: (rank.get(value, 10_000), value))


def _model_from_path(path: Path) -> str | None:
    match = re.match(r"prediction_positive_case_reasoning_repeats_(.+)\.jsonl$", path.name)
    if not match:
        return None
    return FILE_MODEL_MAP.get(match.group(1))


def _parse_repeat_row_id(row_id: str) -> tuple[str, str, str, int | None]:
    match = re.match(r"^(.*)_(rep(\d+)|temp0)$", row_id)
    if not match:
        raise ValueError(f"Unexpected repeat row id: {row_id}")
    condition = match.group(1)
    run_label = match.group(2)
    rep_idx = int(match.group(3)) if match.group(3) else None

    if condition.endswith("_joint_reasoning"):
        variant = condition[: -len("_joint_reasoning")]
        mode = "joint_reasoning"
    elif condition.endswith("_reasoning"):
        variant = condition[: -len("_reasoning")]
        mode = "reasoning"
    else:
        raise ValueError(f"Could not parse mode from row id: {row_id}")
    return variant, mode, run_label, rep_idx


def _safe_corr(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2:
        return float("nan")
    if np.isclose(np.std(y_true), 0.0) or np.isclose(np.std(y_pred), 0.0):
        return float("nan")
    return float(np.corrcoef(y_true, y_pred)[0, 1])


def _row_metrics(
    preds: pd.Series,
    target: pd.Series,
    control: pd.Series,
) -> dict[str, float]:
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
    null_mse = float(np.mean((y_ctrl - y_true) ** 2))
    r2 = float("nan") if np.isclose(null_mse, 0.0) else 1.0 - mse / null_mse

    return {
        "n_questions": n_questions,
        "rmse": rmse,
        "correlation": _safe_corr(y_true, y_pred),
        "r2": r2,
        "directional_accuracy": _directional_accuracy_np(y_pred, y_true, y_ctrl),
    }


def load_targets() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId").reset_index(drop=True)
    labels = [f"Q{i}" for i in range(1, len(df) + 1)]
    target = pd.Series(100 * df["efficiency_p"].to_numpy(dtype=float), index=labels)
    control = pd.Series(100 * df["efficiency_np"].to_numpy(dtype=float), index=labels)
    return target, control


def load_repeat_rows(target: pd.Series, control: pd.Series) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted(INPUT_DIR.glob("prediction_positive_case_reasoning_repeats_*.jsonl")):
        model = _model_from_path(path)
        if model is None:
            continue
        df = jsonl_to_dataframe(path)
        df = df.reindex(columns=target.index)
        for row_id, row in df.iterrows():
            variant, mode, run_label, rep_idx = _parse_repeat_row_id(str(row_id))
            metrics = _row_metrics(row, target, control)
            rows.append(
                {
                    "source_file": path.name,
                    "model": model,
                    "variant": variant,
                    "mode": mode,
                    "run_label": run_label,
                    "run_kind": "temp0" if run_label == "temp0" else "repeat",
                    "rep_idx": rep_idx,
                    **metrics,
                }
            )
    if not rows:
        raise FileNotFoundError("No repeat output files found in openAI_batch_output.")
    out = pd.DataFrame(rows)
    out["model"] = pd.Categorical(out["model"], categories=MODEL_ORDER, ordered=True)
    out["mode"] = pd.Categorical(out["mode"], categories=MODE_ORDER, ordered=True)
    out["variant"] = pd.Categorical(
        out["variant"],
        categories=_preferred_order(out["variant"].dropna().astype(str).unique().tolist(), VARIANT_ORDER),
        ordered=True,
    )
    return out.sort_values(["model", "mode", "variant", "run_kind", "rep_idx"])


def _pairwise_beat_rate(metric: str, augmented: np.ndarray, baseline: np.ndarray) -> float:
    augmented = augmented[np.isfinite(augmented)]
    baseline = baseline[np.isfinite(baseline)]
    if len(augmented) == 0 or len(baseline) == 0:
        return float("nan")
    comp = augmented[:, None] > baseline[None, :]
    if metric == "rmse":
        comp = augmented[:, None] < baseline[None, :]
    return float(np.mean(comp))


def summarize_repeat_rows(rows: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for (model, mode, variant), group in rows.groupby(["model", "mode", "variant"], observed=True):
        repeat_group = group.loc[group["run_kind"] == "repeat"].copy()
        temp0_group = group.loc[group["run_kind"] == "temp0"].copy()
        record: dict[str, object] = {
            "model": model,
            "mode": mode,
            "variant": variant,
            "n_repeat_rows": len(repeat_group),
            "n_repeat_complete_rows": int((repeat_group["n_questions"] == 20).sum()),
            "min_questions_seen": int(group["n_questions"].min()),
            "has_temp0": not temp0_group.empty,
        }
        temp0_row = temp0_group.iloc[0] if not temp0_group.empty else None
        for metric in METRICS:
            repeat_vals = repeat_group[metric].to_numpy(dtype=float)
            record[f"repeat_mean_{metric}"] = float(np.nanmean(repeat_vals))
            record[f"repeat_sd_{metric}"] = float(np.nanstd(repeat_vals, ddof=0))
            record[f"repeat_min_{metric}"] = float(np.nanmin(repeat_vals))
            record[f"repeat_max_{metric}"] = float(np.nanmax(repeat_vals))
            record[f"temp0_{metric}"] = float(temp0_row[metric]) if temp0_row is not None else float("nan")
            record[f"repeat_mean_minus_temp0_{metric}"] = (
                float(record[f"repeat_mean_{metric}"] - record[f"temp0_{metric}"])
                if temp0_row is not None and np.isfinite(record[f"temp0_{metric}"])
                else float("nan")
            )
        records.append(record)

    summary = pd.DataFrame(records)
    baseline = summary.loc[summary["variant"] == "baseline"].copy()
    baseline = baseline.rename(
        columns={
            f"repeat_mean_{metric}": f"baseline_repeat_mean_{metric}" for metric in METRICS
        }
        | {
            f"repeat_sd_{metric}": f"baseline_repeat_sd_{metric}" for metric in METRICS
        }
        | {f"temp0_{metric}": f"baseline_temp0_{metric}" for metric in METRICS}
    )
    keep_cols = ["model", "mode"] + [col for col in baseline.columns if col.startswith("baseline_")]
    summary = summary.merge(baseline[keep_cols], on=["model", "mode"], how="left")

    for metric in METRICS:
        summary[f"delta_repeat_mean_{metric}"] = (
            summary[f"repeat_mean_{metric}"] - summary[f"baseline_repeat_mean_{metric}"]
        )
        summary[f"delta_temp0_{metric}"] = (
            summary[f"temp0_{metric}"] - summary[f"baseline_temp0_{metric}"]
        )

    beat_cols: list[pd.Series] = []
    for (model, mode), part in rows.groupby(["model", "mode"], observed=True):
        baseline_part = part.loc[(part["variant"] == "baseline") & (part["run_kind"] == "repeat")].copy()
        for variant, variant_part in part.groupby("variant", observed=True):
            for metric in METRICS:
                beat_rate = _pairwise_beat_rate(
                    metric,
                    variant_part.loc[variant_part["run_kind"] == "repeat", metric].to_numpy(dtype=float),
                    baseline_part[metric].to_numpy(dtype=float),
                )
                beat_cols.append(
                    pd.Series(
                        {
                            "model": model,
                            "mode": mode,
                            "variant": variant,
                            "metric": metric,
                            "pairwise_beat_rate": beat_rate,
                        }
                    )
                )
    beat_df = pd.DataFrame(beat_cols)
    beat_wide = beat_df.pivot_table(
        index=["model", "mode", "variant"],
        columns="metric",
        values="pairwise_beat_rate",
        aggfunc="first",
    ).reset_index()
    beat_wide = beat_wide.rename(
        columns={metric: f"pairwise_beat_rate_{metric}" for metric in METRICS}
    )
    summary = summary.merge(beat_wide, on=["model", "mode", "variant"], how="left")
    return summary.sort_values(["model", "mode", "variant"])


def build_best_variant_summary(summary: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    augmented = summary.loc[summary["variant"] != "baseline"].copy()
    for (model, mode), part in augmented.groupby(["model", "mode"], observed=True):
        for metric in METRICS:
            score_col = f"repeat_mean_{metric}"
            if BETTER_HIGHER[metric]:
                best_idx = part[score_col].astype(float).idxmax()
            else:
                best_idx = part[score_col].astype(float).idxmin()
            best = part.loc[best_idx]
            rows.append(
                {
                    "model": model,
                    "mode": mode,
                    "metric": metric,
                    "best_variant": best["variant"],
                    "repeat_mean": best[score_col],
                    "repeat_sd": best[f"repeat_sd_{metric}"],
                    "temp0": best[f"temp0_{metric}"],
                    "baseline_repeat_mean": best[f"baseline_repeat_mean_{metric}"],
                    "baseline_temp0": best[f"baseline_temp0_{metric}"],
                    "delta_repeat_mean": best[f"delta_repeat_mean_{metric}"],
                    "delta_temp0": best[f"delta_temp0_{metric}"],
                    "pairwise_beat_rate": best[f"pairwise_beat_rate_{metric}"],
                }
            )
    return pd.DataFrame(rows).sort_values(["metric", "mode", "model"])


def _format_cell(value: float) -> str:
    if not np.isfinite(value):
        return ""
    return f"{value:.2f}" if abs(value) < 10 else f"{value:.1f}"


def plot_delta_heatmap(summary: pd.DataFrame, metric: str) -> None:
    pivot = summary.copy()
    pivot["column"] = pivot["model"].astype(str) + "\n" + pivot["mode"].map(MODE_LABELS)
    column_order = []
    present = set(pivot["column"])
    for model in MODEL_ORDER:
        for mode in MODE_ORDER:
            col = f"{model}\n{MODE_LABELS[mode]}"
            if col in present:
                column_order.append(col)

    row_order = _preferred_order(pivot["variant"].astype(str).unique().tolist(), VARIANT_ORDER)

    delta_wide = pivot.pivot(index="variant", columns="column", values=f"delta_repeat_mean_{metric}")
    temp0_wide = pivot.pivot(index="variant", columns="column", values=f"delta_temp0_{metric}")
    delta_wide = delta_wide.reindex(index=row_order, columns=column_order)
    temp0_wide = temp0_wide.reindex(index=row_order, columns=column_order)

    values = delta_wide.to_numpy(dtype=float)
    finite = values[np.isfinite(values)]
    vmax = float(np.nanpercentile(np.abs(finite), 95)) if finite.size else 1.0
    vmax = max(vmax, 0.01)

    fig, ax = plt.subplots(figsize=(2.35 * len(column_order) + 2.8, 0.48 * len(row_order) + 2.8))
    im = ax.imshow(values, aspect="auto", cmap="coolwarm", vmin=-vmax, vmax=vmax)

    ax.set_xticks(np.arange(len(column_order)))
    ax.set_xticklabels(column_order, fontsize=9)
    ax.set_yticks(np.arange(len(row_order)))
    ax.set_yticklabels(row_order, fontsize=9)
    ax.set_xticks(np.arange(-0.5, len(column_order), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(row_order), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=0.8, alpha=0.8)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i, variant in enumerate(row_order):
        for j, column in enumerate(column_order):
            delta_val = delta_wide.loc[variant, column]
            temp0_val = temp0_wide.loc[variant, column]
            if not np.isfinite(delta_val) and not np.isfinite(temp0_val):
                continue
            text = f"{_format_cell(delta_val)}\n({_format_cell(temp0_val)})"
            color = "white" if np.isfinite(delta_val) and abs(delta_val) > 0.55 * vmax else "0.15"
            ax.text(
                j,
                i,
                text,
                ha="center",
                va="center",
                fontsize=7.2,
                color=color,
                linespacing=0.9,
            )

    metric_title = METRIC_LABELS[metric]
    direction = "lower is better" if metric == "rmse" else "higher is better"
    ax.set_title(
        f"Validation Reasoning Repeats: Δ{metric_title} vs Matched Baseline\n"
        "Cell = mean repeat delta; parentheses = temp0 delta",
        fontsize=14,
        pad=12,
    )
    fig.text(
        0.5,
        0.015,
        f"{metric_title} delta relative to matched no-augmentation within mode; {direction}.",
        ha="center",
        va="bottom",
        fontsize=9,
        color="0.3",
    )
    cbar = fig.colorbar(im, ax=ax, fraction=0.028, pad=0.015)
    cbar.set_label(f"Δ{metric_title} vs baseline", rotation=90)
    fig.tight_layout(rect=[0.02, 0.04, 0.98, 0.95])
    out = PLOTS / f"validation_reasoning_repeats_delta_{metric}.png"
    fig.savefig(out, dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_mean_vs_temp0(summary: pd.DataFrame) -> None:
    fig, axes = plt.subplots(len(METRICS), 2, figsize=(13.2, 4.0 * len(METRICS)), constrained_layout=False)
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
                & np.isfinite(summary[f"repeat_mean_{metric}"])
            ].copy()
            if part.empty:
                ax.set_visible(False)
                continue

            x = part[f"temp0_{metric}"].to_numpy(dtype=float)
            y = part[f"repeat_mean_{metric}"].to_numpy(dtype=float)
            lo = float(min(np.nanmin(x), np.nanmin(y)))
            hi = float(max(np.nanmax(x), np.nanmax(y)))
            pad = 0.05 * (hi - lo if hi > lo else 1.0)
            ax.plot([lo - pad, hi + pad], [lo - pad, hi + pad], color="0.35", linestyle="--", linewidth=1.2)

            for _, row in part.iterrows():
                marker = "s" if row["variant"] == "baseline" else "o"
                ax.scatter(
                    row[f"temp0_{metric}"],
                    row[f"repeat_mean_{metric}"],
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
                ax.set_ylabel(f"Repeat mean {METRIC_LABELS[metric]}")
            ax.set_xlabel(f"temp0 {METRIC_LABELS[metric]}")

    handles = [
        plt.Line2D([], [], color=color, marker="o", linestyle="None", markersize=6, label=model)
        for model, color in color_map.items()
        if model in summary["model"].astype(str).unique()
    ]
    handles.extend(
        [
            plt.Line2D([], [], color="0.25", marker="s", linestyle="None", markersize=6, label="Baseline"),
            plt.Line2D([], [], color="0.25", marker="o", linestyle="None", markersize=6, label="Augmented"),
        ]
    )
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        "Validation Reasoning Repeats: Repeat Mean vs temp0 Anchor",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Each point is one model x input-variant condition. Dashed line is identity.",
        ha="center",
        va="bottom",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(PLOTS / "validation_reasoning_repeats_mean_vs_temp0.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    RESULTS.mkdir(parents=True, exist_ok=True)

    target, control = load_targets()
    rows = load_repeat_rows(target, control)
    summary = summarize_repeat_rows(rows)
    best = build_best_variant_summary(summary)

    rows.to_csv(RESULTS / "validation_reasoning_repeat_rows.csv", index=False)
    summary.to_csv(RESULTS / "validation_reasoning_repeat_summary.csv", index=False)
    best.to_csv(RESULTS / "validation_reasoning_repeat_best_variants.csv", index=False)

    incomplete = rows.loc[rows["n_questions"] < 20].copy()
    incomplete.to_csv(RESULTS / "validation_reasoning_repeat_incomplete_rows.csv", index=False)

    for metric in METRICS:
        plot_delta_heatmap(summary, metric)
    plot_mean_vs_temp0(summary)


if __name__ == "__main__":
    main()
