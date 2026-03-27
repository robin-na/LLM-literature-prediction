from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize

ANALYSIS_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe
from plot_paths import (
    VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from prediction_metrics import _directional_accuracy_np
from result_paths import (
    VALIDATION_AUGMENTATION_DELTA_MODEL_RESULTS as BENCHMARK_RESULTS,
    VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_RESULTS as RESULTS,
    ensure_results_dir,
)
from prediction_metrics import _corr_np


ROOT = PROJECT_ROOT
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"

MODEL_SPECS = [
    {}
]

VARIANTS = ["paper_only_narrative", "paper_only_decision"]
VARIANT_LABELS = {
    "paper_only_narrative": "narrative",
    "paper_only_decision": "decision",
}
MODES = ["single", "reasoning", "joint", "joint_reasoning"]
MODE_LABELS = {
    "single": "single w/o explanation",
    "reasoning": "single with explanation",
    "joint": "joint w/o explanation",
    "joint_reasoning": "joint with explanation",
}
METRIC_SPECS = [
    {
        "key": "rmse",
        "label": "RMSE",
        "delta_label": "ΔRMSE",
        "higher_is_better": False,
        "benchmark_col": "rmse",
        "stem": "validation_positive_case_literature_design_space_delta_rmse",
    },
    {
        "key": "r2",
        "label": r"$R^2$",
        "delta_label": "ΔR²",
        "higher_is_better": True,
        "benchmark_col": "r2_vs_control_null",
        "stem": "validation_positive_case_literature_design_space_delta_r2",
    },
    {
        "key": "directional_accuracy",
        "label": "Directional Accuracy",
        "delta_label": "ΔDirectional Accuracy",
        "higher_is_better": True,
        "benchmark_col": "directional_accuracy",
        "stem": "validation_positive_case_literature_design_space_delta_directional_accuracy",
    },
    {
        "key": "correlation",
        "label": "Correlation",
        "delta_label": "ΔCorrelation",
        "higher_is_better": True,
        "benchmark_col": "correlation",
        "stem": "validation_positive_case_literature_design_space_delta_correlation",
    },
]
METRIC_STEM_SUFFIXES = {
    "rmse": "delta_rmse",
    "r2": "delta_r2",
    "directional_accuracy": "delta_directional_accuracy",
    "correlation": "delta_correlation",
}

ROWS_OUTPUT = RESULTS / "validation_positive_case_literature_design_space_rows.csv"
CONVERGENCE_OUTPUT = RESULTS / "validation_positive_case_literature_design_space_convergence.csv"
CORRELATION_SIG_OUTPUT = (
    RESULTS / "validation_positive_case_literature_design_space_correlation_significance.csv"
)
N_BOOT = 10000
OUTPUT_STEM_PREFIX = "validation_positive_case_literature_design_space"
PLOT_CONTEXT_LABEL = "Positive Case Design Space"
HEATMAP_TITLE_PREFIX = "Validation Paper-Only Narrative/Decision"


def _build_model_specs(new_output_prefix: str) -> list[dict[str, object]]:
    return [
        {
            "model": "GPT-4.1",
            "new_output": OPENAI_BATCH_OUTPUT / f"{new_output_prefix}_41.jsonl",
            "baseline_output": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
            "baseline_repeats": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41.jsonl",
        },
        {
            "model": "GPT-4.1 Mini",
            "new_output": OPENAI_BATCH_OUTPUT / f"{new_output_prefix}_41mini.jsonl",
            "baseline_output": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
            "baseline_repeats": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41mini.jsonl",
        },
        {
            "model": "GPT-4.1 Nano",
            "new_output": OPENAI_BATCH_OUTPUT / f"{new_output_prefix}_41nano.jsonl",
            "baseline_output": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
            "baseline_repeats": OPENAI_BATCH_OUTPUT / "prediction_positive_case_reasoning_repeats_41nano.jsonl",
        },
    ]


def configure_context(
    *,
    new_output_prefix: str = "prediction_positive_case_paper_only_narrative-decision",
    results_dir: Path | None = None,
    plots_dir: Path | None = None,
    output_stem_prefix: str = "validation_positive_case_literature_design_space",
    plot_context_label: str = "Positive Case Design Space",
    heatmap_title_prefix: str = "Validation Paper-Only Narrative/Decision",
    modes: list[str] | None = None,
) -> None:
    global MODEL_SPECS
    global RESULTS
    global PLOTS
    global ROWS_OUTPUT
    global CONVERGENCE_OUTPUT
    global CORRELATION_SIG_OUTPUT
    global MODES
    global OUTPUT_STEM_PREFIX
    global PLOT_CONTEXT_LABEL
    global HEATMAP_TITLE_PREFIX

    MODEL_SPECS = _build_model_specs(new_output_prefix)
    RESULTS = Path(results_dir) if results_dir is not None else RESULTS
    PLOTS = Path(plots_dir) if plots_dir is not None else PLOTS
    OUTPUT_STEM_PREFIX = output_stem_prefix
    PLOT_CONTEXT_LABEL = plot_context_label
    HEATMAP_TITLE_PREFIX = heatmap_title_prefix
    if modes is not None:
        MODES = list(modes)
    for spec in METRIC_SPECS:
        spec["stem"] = f"{OUTPUT_STEM_PREFIX}_{METRIC_STEM_SUFFIXES[spec['key']]}"
    ROWS_OUTPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_rows.csv"
    CONVERGENCE_OUTPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_convergence.csv"
    CORRELATION_SIG_OUTPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_correlation_significance.csv"


configure_context()


def _available_specs() -> list[dict[str, object]]:
    specs: list[dict[str, object]] = []
    for spec in MODEL_SPECS:
        if spec["new_output"].exists() and spec["baseline_output"].exists() and spec["baseline_repeats"].exists():
            specs.append(spec)
    return specs


def load_targets() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId").reset_index(drop=True)
    labels = [f"Q{i}" for i in range(1, len(df) + 1)]
    truth = pd.Series(100.0 * df["efficiency_p"].to_numpy(dtype=float), index=labels, name="truth")
    control = pd.Series(100.0 * df["efficiency_np"].to_numpy(dtype=float), index=labels, name="control")
    return truth, control


def _safe_corr(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2:
        return float("nan")
    if np.isclose(np.std(y_true), 0.0) or np.isclose(np.std(y_pred), 0.0):
        return float("nan")
    return float(np.corrcoef(y_true, y_pred)[0, 1])


def metric_values(pred: pd.Series, truth: pd.Series, control: pd.Series) -> dict[str, float]:
    valid = pred.notna() & truth.notna() & control.notna()
    if not valid.any():
        return {
            "n_questions": 0,
            "rmse": float("nan"),
            "r2": float("nan"),
            "directional_accuracy": float("nan"),
            "correlation": float("nan"),
        }

    y_pred = pred.loc[valid].to_numpy(dtype=float)
    y_true = truth.loc[valid].to_numpy(dtype=float)
    y_ctrl = control.loc[valid].to_numpy(dtype=float)
    mse = float(np.mean((y_pred - y_true) ** 2))
    null_mse = float(np.mean((y_true - y_ctrl) ** 2))
    return {
        "n_questions": int(valid.sum()),
        "rmse": float(np.sqrt(mse)),
        "r2": float("nan") if np.isclose(null_mse, 0.0) else float(1.0 - mse / null_mse),
        "directional_accuracy": float(_directional_accuracy_np(y_pred, y_true, y_ctrl)),
        "correlation": _safe_corr(y_true, y_pred),
    }


def _paired_delta_bootstrap(
    metric_fn,
    pred_arr: np.ndarray,
    base_arr: np.ndarray,
    truth_arr: np.ndarray,
    control_arr: np.ndarray | None,
    mask: np.ndarray,
    rng: np.random.Generator,
    n_boot: int,
) -> tuple[float, float, float, float]:
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return float("nan"), float("nan"), float("nan"), float("nan")

    if control_arr is None:
        pred_val = metric_fn(pred_arr[idx], truth_arr[idx])
        base_val = metric_fn(base_arr[idx], truth_arr[idx])
    else:
        pred_val = metric_fn(pred_arr[idx], truth_arr[idx], control_arr[idx])
        base_val = metric_fn(base_arr[idx], truth_arr[idx], control_arr[idx])
    delta = float(pred_val - base_val)

    if n_boot <= 0:
        return delta, float("nan"), float("nan"), float("nan")

    boot = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = rng.choice(idx, size=idx.size, replace=True)
        if control_arr is None:
            m_pred = metric_fn(pred_arr[sample], truth_arr[sample])
            m_base = metric_fn(base_arr[sample], truth_arr[sample])
        else:
            m_pred = metric_fn(pred_arr[sample], truth_arr[sample], control_arr[sample])
            m_base = metric_fn(base_arr[sample], truth_arr[sample], control_arr[sample])
        boot[i] = m_pred - m_base
    finite_boot = boot[np.isfinite(boot)]
    if finite_boot.size == 0:
        return delta, float("nan"), float("nan"), float("nan")
    lo, hi = np.nanpercentile(finite_boot, [2.5, 97.5])
    sd = float(np.nanstd(finite_boot, ddof=1)) if finite_boot.size > 1 else 0.0
    return delta, float(lo), float(hi), sd


def _parse_new_explanation_row_ids(row_id: str) -> tuple[str, str] | None:
    match = re.match(r"^(paper_only_(?:narrative|decision))_joint_explanation_rep(\d+)$", row_id)
    if match:
        return match.group(1), "joint_reasoning"
    match = re.match(r"^(paper_only_(?:narrative|decision))_explanation_rep(\d+)$", row_id)
    if match:
        return match.group(1), "reasoning"
    return None


def _baseline_initial_id(mode: str) -> str:
    return {
        "reasoning": "baseline_reasoning",
        "joint_reasoning": "baseline_joint_reasoning",
    }[mode]


def _baseline_repeat_ids(mode: str) -> list[str]:
    prefix = {
        "reasoning": "baseline_reasoning",
        "joint_reasoning": "baseline_joint_reasoning",
    }[mode]
    return [f"{prefix}_rep{i}" for i in range(1, 5)]


def _new_repeat_ids(variant: str, mode: str) -> list[str]:
    prefix = {
        "reasoning": f"{variant}_explanation",
        "joint_reasoning": f"{variant}_joint_explanation",
    }[mode]
    return [f"{prefix}_rep{i}" for i in range(1, 6)]


def _baseline_direct_id(mode: str) -> str:
    return {"single": "baseline", "joint": "baseline_joint"}[mode]


def _new_direct_id(variant: str, mode: str) -> str:
    return {"single": variant, "joint": f"{variant}_joint"}[mode]


def _series_average(series_list: list[pd.Series], labels: pd.Index) -> pd.Series:
    if not series_list:
        return pd.Series(np.nan, index=labels, dtype=float)
    frame = pd.concat(series_list, axis=1).reindex(index=labels)
    return frame.mean(axis=1, skipna=True)


def build_rows() -> pd.DataFrame:
    truth, control = load_targets()
    labels = truth.index
    rows: list[dict[str, object]] = []

    for spec in _available_specs():
        model = str(spec["model"])
        baseline_df = jsonl_to_dataframe(spec["baseline_output"]).reindex(columns=labels)
        repeat_df = jsonl_to_dataframe(spec["baseline_repeats"]).reindex(columns=labels)
        new_df = jsonl_to_dataframe(spec["new_output"]).reindex(columns=labels)

        for mode in [mode for mode in ["single", "joint"] if mode in MODES]:
            baseline_row_id = _baseline_direct_id(mode)
            if baseline_row_id not in baseline_df.index:
                continue
            baseline_pred = baseline_df.loc[_baseline_direct_id(mode)].astype(float)
            baseline_metrics = metric_values(baseline_pred, truth, control)
            for variant in VARIANTS:
                new_row_id = _new_direct_id(variant, mode)
                if new_row_id not in new_df.index:
                    continue
                new_pred = new_df.loc[new_row_id].astype(float)
                augmented_metrics = metric_values(new_pred, truth, control)
                row = {
                    "model": model,
                    "variant": variant,
                    "mode": mode,
                    "baseline_n_runs": 1,
                    "augmented_n_runs": 1,
                }
                for metric in ["rmse", "r2", "directional_accuracy", "correlation"]:
                    row[f"baseline_{metric}"] = baseline_metrics[metric]
                    row[f"augmented_{metric}"] = augmented_metrics[metric]
                    row[f"delta_{metric}"] = augmented_metrics[metric] - baseline_metrics[metric]
                rows.append(row)

        for mode in [mode for mode in ["reasoning", "joint_reasoning"] if mode in MODES]:
            baseline_runs = [baseline_df.loc[_baseline_initial_id(mode)].astype(float)]
            baseline_runs.extend(
                repeat_df.loc[row_id].astype(float)
                for row_id in _baseline_repeat_ids(mode)
                if row_id in repeat_df.index
            )
            if not baseline_runs:
                continue
            baseline_pred = _series_average(baseline_runs, labels)
            baseline_metrics = metric_values(baseline_pred, truth, control)

            for variant in VARIANTS:
                aug_runs = [
                    new_df.loc[row_id].astype(float)
                    for row_id in _new_repeat_ids(variant, mode)
                    if row_id in new_df.index
                ]
                if not aug_runs:
                    continue
                augmented_pred = _series_average(aug_runs, labels)
                augmented_metrics = metric_values(augmented_pred, truth, control)
                row = {
                    "model": model,
                    "variant": variant,
                    "mode": mode,
                    "baseline_n_runs": len(baseline_runs),
                    "augmented_n_runs": len(aug_runs),
                }
                for metric in ["rmse", "r2", "directional_accuracy", "correlation"]:
                    row[f"baseline_{metric}"] = baseline_metrics[metric]
                    row[f"augmented_{metric}"] = augmented_metrics[metric]
                    row[f"delta_{metric}"] = augmented_metrics[metric] - baseline_metrics[metric]
                rows.append(row)

    out = pd.DataFrame(rows)
    model_order = [spec["model"] for spec in MODEL_SPECS if spec in _available_specs()]
    out["model"] = pd.Categorical(out["model"], categories=model_order, ordered=True)
    out["variant"] = pd.Categorical(out["variant"], categories=VARIANTS, ordered=True)
    out["mode"] = pd.Categorical(out["mode"], categories=MODES, ordered=True)
    return out.sort_values(["model", "variant", "mode"]).reset_index(drop=True)


def build_correlation_significance() -> pd.DataFrame:
    truth, _ = load_targets()
    labels = truth.index
    records: list[dict[str, object]] = []

    for spec in _available_specs():
        model = str(spec["model"])
        baseline_df = jsonl_to_dataframe(spec["baseline_output"]).reindex(columns=labels)
        repeat_df = jsonl_to_dataframe(spec["baseline_repeats"]).reindex(columns=labels)
        new_df = jsonl_to_dataframe(spec["new_output"]).reindex(columns=labels)

        for mode in [mode for mode in ["reasoning", "joint_reasoning"] if mode in MODES]:
            baseline_runs = [baseline_df.loc[_baseline_initial_id(mode)].astype(float)]
            baseline_runs.extend(
                repeat_df.loc[row_id].astype(float)
                for row_id in _baseline_repeat_ids(mode)
                if row_id in repeat_df.index
            )
            if not baseline_runs:
                continue
            baseline_pred = _series_average(baseline_runs, labels)
            baseline_arr = baseline_pred.to_numpy(dtype=float)
            truth_arr = truth.to_numpy(dtype=float)

            for variant in VARIANTS:
                aug_runs = [
                    new_df.loc[row_id].astype(float)
                    for row_id in _new_repeat_ids(variant, mode)
                    if row_id in new_df.index
                ]
                if not aug_runs:
                    continue
                augmented_pred = _series_average(aug_runs, labels)
                pred_arr = augmented_pred.to_numpy(dtype=float)
                mask = ~np.isnan(pred_arr) & ~np.isnan(baseline_arr) & ~np.isnan(truth_arr)
                rng = np.random.default_rng(7)
                delta, ci_low, ci_high, boot_sd = _paired_delta_bootstrap(
                    _corr_np,
                    pred_arr,
                    baseline_arr,
                    truth_arr,
                    None,
                    mask,
                    rng,
                    N_BOOT,
                )
                records.append(
                    {
                        "model": model,
                        "variant": variant,
                        "mode": mode,
                        "baseline_correlation": float(_corr_np(baseline_arr[mask], truth_arr[mask])),
                        "augmented_correlation": float(_corr_np(pred_arr[mask], truth_arr[mask])),
                        "delta_correlation": float(delta),
                        "delta_correlation_ci_low": float(ci_low),
                        "delta_correlation_ci_high": float(ci_high),
                        "delta_correlation_boot_sd": float(boot_sd),
                        "delta_correlation_boot_var": float(boot_sd**2) if np.isfinite(boot_sd) else float("nan"),
                        "verdict_95": (
                            "better"
                            if np.isfinite(ci_low) and ci_low > 0
                            else "worse"
                            if np.isfinite(ci_high) and ci_high < 0
                            else "inconclusive"
                        ),
                        "n_questions": int(mask.sum()),
                        "n_boot": N_BOOT,
                    }
                )

    out = pd.DataFrame(records)
    if out.empty:
        return out
    out["model"] = pd.Categorical(
        out["model"],
        categories=[spec["model"] for spec in _available_specs()],
        ordered=True,
    )
    out["variant"] = pd.Categorical(out["variant"], categories=VARIANTS, ordered=True)
    out["mode"] = pd.Categorical(
        out["mode"],
        categories=["reasoning", "joint_reasoning"],
        ordered=True,
    )
    return out.sort_values(["mode", "model", "variant"]).reset_index(drop=True)


def build_convergence_table(rows: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for mode in MODES:
        part_mode = rows.loc[rows["mode"] == mode].copy()
        for spec in METRIC_SPECS:
            metric = spec["key"]
            part = part_mode.loc[:, ["model", "variant", f"baseline_{metric}", f"delta_{metric}"]].dropna()
            if len(part) >= 2:
                r = float(
                    np.corrcoef(
                        part[f"baseline_{metric}"].to_numpy(dtype=float),
                        part[f"delta_{metric}"].to_numpy(dtype=float),
                    )[0, 1]
                )
            else:
                r = float("nan")
            records.append(
                {
                    "mode": mode,
                    "metric": metric,
                    "n_points": int(len(part)),
                    "r_baseline_vs_delta": r,
                }
            )
    out = pd.DataFrame(records)
    out["mode"] = pd.Categorical(out["mode"], categories=MODES, ordered=True)
    return out.sort_values(["mode", "metric"]).reset_index(drop=True)


def load_benchmarks() -> pd.DataFrame:
    return pd.read_csv(
        BENCHMARK_RESULTS / "validation_augmentation_delta_by_model_benchmarks.csv"
    )


def _format_number(value: float) -> str:
    if not np.isfinite(value):
        return ""
    return f"{value:.2f}" if abs(value) < 10 else f"{value:.1f}"


def plot_delta_heatmaps(rows: pd.DataFrame, benchmarks: pd.DataFrame) -> None:
    models = [model for model in rows["model"].cat.categories if model in set(rows["model"].astype(str))]
    mode_labels = [MODE_LABELS[m] for m in MODES]

    for spec in METRIC_SPECS:
        metric = spec["key"]
        fig, axes = plt.subplots(
            len(models),
            1,
            figsize=(11.6, 2.6 * len(models) + 1.8),
            constrained_layout=False,
        )
        axes = np.atleast_1d(axes)

        values_all = rows[f"delta_{metric}"].to_numpy(dtype=float)
        finite = values_all[np.isfinite(values_all)]
        vmax = float(np.nanpercentile(np.abs(finite), 95)) if finite.size else 1.0
        vmax = max(vmax, 0.01)
        norm = Normalize(vmin=-vmax, vmax=vmax)
        cmap = plt.get_cmap("coolwarm")

        for ax, model in zip(axes, models, strict=False):
            part = rows.loc[rows["model"] == model].copy()
            delta = (
                part.pivot(index="variant", columns="mode", values=f"delta_{metric}")
                .reindex(index=VARIANTS, columns=MODES)
            )
            raw = (
                part.pivot(index="variant", columns="mode", values=f"augmented_{metric}")
                .reindex(index=VARIANTS, columns=MODES)
            )
            im = ax.imshow(delta.to_numpy(dtype=float), cmap=cmap, norm=norm, aspect="auto")
            ax.set_title(str(model), fontsize=12, loc="left")
            ax.set_xticks(np.arange(len(MODES)))
            ax.set_xticklabels(mode_labels, fontsize=9)
            ax.set_yticks(np.arange(len(VARIANTS)))
            ax.set_yticklabels([VARIANT_LABELS[v] for v in VARIANTS], fontsize=10)
            ax.set_xticks(np.arange(-0.5, len(MODES), 1), minor=True)
            ax.set_yticks(np.arange(-0.5, len(VARIANTS), 1), minor=True)
            ax.grid(which="minor", color="white", linestyle="-", linewidth=0.8, alpha=0.85)
            ax.tick_params(which="minor", bottom=False, left=False)
            for i, variant in enumerate(VARIANTS):
                for j, mode in enumerate(MODES):
                    dval = delta.loc[variant, mode]
                    rval = raw.loc[variant, mode]
                    color = "white" if np.isfinite(dval) and abs(dval) > 0.55 * vmax else "0.15"
                    ax.text(
                        j,
                        i,
                        f"{_format_number(dval)}\n({_format_number(rval)})",
                        ha="center",
                        va="center",
                        fontsize=8,
                        color=color,
                        linespacing=0.92,
                    )

        cbar = fig.colorbar(im, ax=axes, fraction=0.028, pad=0.02)
        direction = "lower is better" if not spec["higher_is_better"] else "higher is better"
        cbar.set_label(f"{spec['delta_label']} vs matched baseline ({direction})")

        footer_parts = []
        for bench_name in ["E-Net", "Noise ceiling"]:
            bench_series = benchmarks.loc[benchmarks["benchmark"] == bench_name, spec["benchmark_col"]]
            if not bench_series.empty and np.isfinite(float(bench_series.iloc[0])):
                footer_parts.append(f"{bench_name}: {float(bench_series.iloc[0]):.2f}")
        fig.suptitle(
            f"{HEATMAP_TITLE_PREFIX}: {spec['delta_label']}",
            fontsize=15,
            y=0.98,
        )
        fig.text(
            0.5,
            0.015,
            "Cell = augmentation delta vs matched baseline; parentheses = augmented raw value."
            + (f" {' | '.join(footer_parts)}" if footer_parts else ""),
            ha="center",
            fontsize=9,
            color="0.3",
        )
        fig.tight_layout(rect=[0.03, 0.05, 1, 0.95])
        fig.savefig(PLOTS / f"{spec['stem']}.png", dpi=220, bbox_inches="tight")
        plt.close(fig)


def _fit_line(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    if len(x) < 2:
        return None
    slope, intercept = np.polyfit(x, y, 1)
    xs = np.linspace(float(np.min(x)), float(np.max(x)), 100)
    return xs, slope * xs + intercept


def plot_convergence(rows: pd.DataFrame, convergence: pd.DataFrame) -> None:
    fig, axes = plt.subplots(
        len(METRIC_SPECS),
        len(MODES),
        figsize=(4.0 * len(MODES), 3.4 * len(METRIC_SPECS)),
        constrained_layout=False,
    )
    variant_colors = {
        "paper_only_narrative": "#1f77b4",
        "paper_only_decision": "#d95f02",
    }

    for row_idx, spec in enumerate(METRIC_SPECS):
        metric = spec["key"]
        for col_idx, mode in enumerate(MODES):
            ax = axes[row_idx, col_idx]
            part = rows.loc[rows["mode"] == mode].copy()
            x = part[f"baseline_{metric}"].to_numpy(dtype=float)
            y = part[f"delta_{metric}"].to_numpy(dtype=float)
            ax.axhline(0.0, color="0.7", linewidth=1.0, linestyle="--", zorder=0)
            fit = _fit_line(x, y)
            if fit is not None:
                xs, ys = fit
                ax.plot(xs, ys, color="0.25", linewidth=1.2, zorder=1)
            for _, row in part.iterrows():
                label = f"{str(row['model']).replace('GPT-', '').replace('GPT', '').strip()} / {VARIANT_LABELS[str(row['variant'])]}"
                ax.scatter(
                    row[f"baseline_{metric}"],
                    row[f"delta_{metric}"],
                    s=78,
                    color=variant_colors[str(row["variant"])],
                    edgecolors="white",
                    linewidths=0.8,
                    zorder=3,
                )
                ax.annotate(
                    label,
                    (row[f"baseline_{metric}"], row[f"delta_{metric}"]),
                    xytext=(4, 4),
                    textcoords="offset points",
                    fontsize=8,
                    color="0.25",
                )
            corr_row = convergence.loc[
                (convergence["mode"] == mode) & (convergence["metric"] == metric)
            ].iloc[0]
            ax.text(
                0.03,
                0.96,
                f"r = {corr_row['r_baseline_vs_delta']:.2f}\nn = {int(corr_row['n_points'])}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9.2,
                bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none", "pad": 1.5},
            )
            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode], fontsize=11)
            if col_idx == 0:
                direction = "lower is better" if not spec["higher_is_better"] else "higher is better"
                ax.set_ylabel(f"{spec['delta_label']}\n({direction})")
            ax.set_xlabel(f"Baseline {spec['label']}")
            ax.grid(alpha=0.18, zorder=0)

    legend_handles = [
        plt.Line2D([], [], color="#1f77b4", marker="o", linestyle="None", markersize=7, label="narrative"),
        plt.Line2D([], [], color="#d95f02", marker="o", linestyle="None", markersize=7, label="decision"),
    ]
    fig.legend(handles=legend_handles, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        f"{PLOT_CONTEXT_LABEL}: Baseline Performance vs Augmentation Delta",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Points are model-variant pairs. More negative r implies stronger convergence: weaker baselines gain more.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(
        PLOTS / f"{OUTPUT_STEM_PREFIX}_convergence.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def plot_dumbbells(rows: pd.DataFrame, benchmarks: pd.DataFrame) -> None:
    fig, axes = plt.subplots(
        len(METRIC_SPECS),
        len(MODES),
        figsize=(4.1 * len(MODES), 3.6 * len(METRIC_SPECS)),
        constrained_layout=False,
    )
    point_colors = {"baseline": "#6c757d", "augmented": "#2b8cbe"}
    arrow_colors = {"better": "#d7301f", "worse": "#3182bd"}
    best_line_color = "#222222"
    benchmark_colors = {"E-Net": "#111111", "Noise ceiling": "#31a354"}

    for row_idx, spec in enumerate(METRIC_SPECS):
        metric = spec["key"]
        higher_is_better = spec["higher_is_better"]
        for col_idx, mode in enumerate(MODES):
            ax = axes[row_idx, col_idx]
            part = rows.loc[rows["mode"] == mode].copy()
            model_labels = (
                part["model"]
                .astype(str)
                .str.replace("GPT-", "", regex=False)
                .str.replace("GPT", "", regex=False)
                .str.strip()
            )
            variant_labels = part["variant"].astype(str).map(VARIANT_LABELS)
            part["label"] = model_labels + "\n" + variant_labels
            part = part.sort_values(
                f"baseline_{metric}",
                ascending=not higher_is_better,
                kind="mergesort",
            ).reset_index(drop=True)
            x = np.arange(len(part))
            baseline = part[f"baseline_{metric}"].to_numpy(dtype=float)
            augmented = part[f"augmented_{metric}"].to_numpy(dtype=float)
            best_baseline = np.nanmin(baseline) if metric == "rmse" else np.nanmax(baseline)

            ax.axhline(best_baseline, color=best_line_color, linestyle="--", linewidth=1.1, alpha=0.9, zorder=0)
            for bench_name in ["E-Net", "Noise ceiling"]:
                bench_series = benchmarks.loc[benchmarks["benchmark"] == bench_name, spec["benchmark_col"]]
                if bench_series.empty:
                    continue
                bench_value = float(bench_series.iloc[0])
                if not np.isfinite(bench_value):
                    continue
                ax.axhline(
                    bench_value,
                    color=benchmark_colors[bench_name],
                    linestyle="--",
                    linewidth=1.1,
                    alpha=0.9,
                    zorder=0,
                )

            for i in range(len(part)):
                improved = augmented[i] < baseline[i] if metric == "rmse" else augmented[i] > baseline[i]
                ax.annotate(
                    "",
                    xy=(x[i], augmented[i]),
                    xytext=(x[i], baseline[i]),
                    arrowprops={
                        "arrowstyle": "-|>",
                        "color": arrow_colors["better" if improved else "worse"],
                        "lw": 1.5,
                        "shrinkA": 4,
                        "shrinkB": 4,
                        "mutation_scale": 10,
                    },
                    zorder=1,
                )

            ax.scatter(x, baseline, s=52, color=point_colors["baseline"], edgecolors="white", linewidths=0.8, zorder=3)
            ax.scatter(x, augmented, s=56, color=point_colors["augmented"], edgecolors="white", linewidths=0.8, zorder=4)
            ax.set_xticks(x)
            ax.set_xticklabels(part["label"], rotation=45, ha="right", fontsize=8.4)
            ax.grid(axis="y", alpha=0.18, zorder=0)
            ax.set_axisbelow(True)
            if row_idx == 0:
                ax.set_title(MODE_LABELS[mode], fontsize=11)
            if col_idx == 0:
                direction = "lower is better" if not higher_is_better else "higher is better"
                ax.set_ylabel(f"{spec['label']}\n({direction})")

    handles = [
        plt.Line2D([], [], color=point_colors["baseline"], marker="o", linestyle="None", markersize=7, label="No augmentation"),
        plt.Line2D([], [], color=point_colors["augmented"], marker="o", linestyle="None", markersize=7, label="Augmented"),
        plt.Line2D([], [], color=arrow_colors["better"], linewidth=2, label="Improved"),
        plt.Line2D([], [], color=arrow_colors["worse"], linewidth=2, label="Worsened"),
        plt.Line2D([], [], color=best_line_color, linestyle="--", linewidth=1.5, label="Best no-augmentation"),
        plt.Line2D([], [], color=benchmark_colors["E-Net"], linestyle="--", linewidth=1.5, label="E-Net"),
        plt.Line2D([], [], color=benchmark_colors["Noise ceiling"], linestyle="--", linewidth=1.5, label="Noise ceiling"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=7, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle(
        f"{PLOT_CONTEXT_LABEL}: Baseline to Augmented Levels",
        fontsize=16,
        y=0.98,
    )
    fig.text(
        0.5,
        0.045,
        "Within each panel, model-variant conditions are ordered by no-augmentation performance. Arrows point from the matched baseline value to the augmented value.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(
        PLOTS / f"{OUTPUT_STEM_PREFIX}_dumbbells.png",
        dpi=220,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    ensure_results_dir(RESULTS)
    ensure_plot_dir(PLOTS)

    rows = build_rows()
    if rows.empty:
        raise FileNotFoundError("No matching paper_only_narrative-decision output files with corresponding baselines were found.")
    convergence = build_convergence_table(rows)
    corr_sig = build_correlation_significance()
    benchmarks = load_benchmarks()

    rows.to_csv(ROWS_OUTPUT, index=False)
    convergence.to_csv(CONVERGENCE_OUTPUT, index=False)
    corr_sig.to_csv(CORRELATION_SIG_OUTPUT, index=False)

    plot_delta_heatmaps(rows, benchmarks)
    plot_convergence(rows, convergence)
    plot_dumbbells(rows, benchmarks)

    print(ROWS_OUTPUT)
    print(CONVERGENCE_OUTPUT)
    print(CORRELATION_SIG_OUTPUT)
    for spec in METRIC_SPECS:
        print(PLOTS / f"{spec['stem']}.png")
    print(PLOTS / f"{OUTPUT_STEM_PREFIX}_convergence.png")
    print(PLOTS / f"{OUTPUT_STEM_PREFIX}_dumbbells.png")


if __name__ == "__main__":
    main()
