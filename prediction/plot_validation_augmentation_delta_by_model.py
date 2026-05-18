from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import Normalize


ROOT = Path(__file__).resolve().parents[1]
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"

sys.path.append(str(ROOT / "analysis"))
from jsonl_parser import jsonl_to_dataframe  # noqa: E402
from noise_ceiling import compute_metrics as compute_noise_metrics  # noqa: E402
from noise_ceiling import load_pairs  # noqa: E402
from plot_paths import (  # noqa: E402
    VALIDATION_AUGMENTATION_DELTA_MODEL_PLOTS as PLOTS,
    VALIDATION_AUGMENTATION_DELTA_MODEL_SPLIT_PLOTS as SPLIT_PLOTS,
    ensure_plot_dir,
)
from prediction_metrics import _directional_accuracy_np  # noqa: E402
from result_paths import (  # noqa: E402
    VALIDATION_AUGMENTATION_DELTA_MODEL_RESULTS as RESULTS,
)


RAW_MODEL_SPECS = [
    {
        "model": "GPT-3.5 Turbo",
        "path_candidates": ["prediction_positive_case_variants_single_35turbo.jsonl"],
    },
    {
        "model": "GPT-4.1 Nano",
        "path_candidates": ["prediction_crosswave_variations_41nano.jsonl"],
    },
    {
        "model": "GPT-4.1 Mini",
        "path_candidates": ["prediction_crosswave_variations_41mini.jsonl"],
    },
    {
        "model": "GPT-4o",
        "path_candidates": ["prediction_positive_case_variants_single_4o.jsonl"],
    },
    {
        "model": "o4-mini",
        "path_candidates": ["prediction_positive_case_variants_single_o4mini.jsonl"],
    },
    {
        "model": "o3",
        "path_candidates": [
            "prediction_positive_case_variants_single_o3.jsonl",
            "prediction_positive_case_variants_single_reasoning_o3.jsonl",
        ],
    },
    {
        "model": "GPT-4.1",
        "path_candidates": ["prediction_positive_case_variations_41.jsonl"],
    },
    {
        "model": "GPT-5.1",
        "path_candidates": ["prediction_positive_case_variants_single_gpt51.jsonl"],
    },
]

INPUT_GROUPS = ["both", "paper_only", "data_only"]
MODES = ["single", "reasoning"]
MODE_LABELS = {"single": "w/o explanation", "reasoning": "with explanation"}
Q_COLS = [f"Q{i}" for i in range(1, 21)]

METRIC_SPECS = [
    {
        "col": "delta_rmse",
        "title": "Validation Augmentation Deltas by Model: ΔRMSE",
        "cbar": "ΔRMSE vs matched no-augmentation (lower is better)",
        "stem": "validation_augmentation_delta_by_model_rmse",
        "benchmark_col": "rmse",
        "short": "ΔRMSE",
    },
    {
        "col": "delta_r2",
        "title": "Validation Augmentation Deltas by Model: ΔR²",
        "cbar": "ΔR² vs matched no-augmentation (higher is better)",
        "stem": "validation_augmentation_delta_by_model_r2",
        "benchmark_col": "r2_vs_control_null",
        "short": "ΔR²",
    },
    {
        "col": "delta_correlation",
        "title": "Validation Augmentation Deltas by Model: ΔCorrelation",
        "cbar": "ΔCorrelation vs matched no-augmentation (higher is better)",
        "stem": "validation_augmentation_delta_by_model_correlation",
        "benchmark_col": "correlation",
        "short": "ΔCorrelation",
    },
    {
        "col": "delta_directional_accuracy",
        "title": "Validation Augmentation Deltas by Model: ΔDirectional Accuracy",
        "cbar": "ΔDirectional Accuracy vs matched no-augmentation (higher is better)",
        "stem": "validation_augmentation_delta_by_model_directional_accuracy",
        "benchmark_col": "directional_accuracy",
        "short": "ΔDA",
    },
]


def _resolve_first_existing(candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = OPENAI_BATCH_OUTPUT / candidate
        if path.exists():
            return path
    return None


def _resolve_model_specs() -> tuple[list[dict[str, object]], list[str]]:
    resolved: list[dict[str, object]] = []
    skipped: list[str] = []
    for spec in RAW_MODEL_SPECS:
        path = _resolve_first_existing(spec["path_candidates"])
        if path is None:
            skipped.append(str(spec["model"]))
            continue
        resolved.append({"model": spec["model"], "path": path})
    return resolved, skipped


MODEL_SPECS, SKIPPED_MODELS = _resolve_model_specs()


def parse_variation(variation: str) -> tuple[str, str, str]:
    if variation == "baseline":
        return "baseline", "baseline", "single"
    if variation == "baseline_reasoning":
        return "baseline", "baseline", "reasoning"
    if variation == "baseline_joint":
        return "baseline", "baseline", "joint"
    if variation == "baseline_joint_reasoning":
        return "baseline", "baseline", "joint_reasoning"

    mode = "single"
    stem = variation
    for suffix, parsed_mode in [
        ("_joint_reasoning", "joint_reasoning"),
        ("_reasoning", "reasoning"),
        ("_joint", "joint"),
    ]:
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            mode = parsed_mode
            break

    for input_group in INPUT_GROUPS:
        prefix = f"{input_group}_"
        if stem.startswith(prefix):
            return input_group, stem[len(prefix) :], mode
    raise ValueError(f"Unrecognized variation format: {variation}")


def family_order(input_group: str) -> list[str]:
    if input_group == "both":
        return [
            "contrastive",
            "ensemble",
            "freeform",
            "quantitative",
            "refined",
            "rules",
            "structured",
            "uncertainty",
        ]
    return ["freeform", "quantitative", "structured"]


def load_validation_truth() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(ROOT / "input" / "pgg_CONFIGmerged_validation.csv").sort_values(
        "CONFIG_configId"
    )
    treatment = pd.Series(
        100.0 * df["efficiency_p"].to_numpy(dtype=float),
        index=Q_COLS,
        name="treatment",
    )
    control = pd.Series(
        100.0 * df["efficiency_np"].to_numpy(dtype=float),
        index=Q_COLS,
        name="control",
    )
    return treatment, control


def _rmse(pred: np.ndarray, truth: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    return float(np.sqrt(np.mean((pred - truth) ** 2)))


def _corr(pred: np.ndarray, truth: np.ndarray) -> float:
    if pred.size < 2:
        return float("nan")
    if np.std(pred) == 0 or np.std(truth) == 0:
        return float("nan")
    return float(np.corrcoef(pred, truth)[0, 1])


def _r2(pred: np.ndarray, truth: np.ndarray, control: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - control) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def _r2_against_constant(pred: np.ndarray, truth: np.ndarray, constant: float) -> float:
    if pred.size == 0:
        return float("nan")
    mse = float(np.mean((pred - truth) ** 2))
    null_mse = float(np.mean((truth - constant) ** 2))
    if null_mse <= 0:
        return float("nan")
    return float(1.0 - mse / null_mse)


def _directional_accuracy(pred: np.ndarray, truth: np.ndarray, control: np.ndarray) -> float:
    if pred.size == 0:
        return float("nan")
    return float(_directional_accuracy_np(pred, truth, control))


def paired_delta_metrics(
    pred_row: pd.Series,
    base_row: pd.Series,
    treatment: pd.Series,
    control: pd.Series,
) -> dict[str, float | int]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    base = pd.to_numeric(base_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    base_arr = base.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)

    mask = (
        ~np.isnan(pred_arr)
        & ~np.isnan(base_arr)
        & ~np.isnan(truth_arr)
        & ~np.isnan(ctrl_arr)
    )
    if mask.sum() == 0:
        return {
            "n": 0,
            "rmse": np.nan,
            "baseline_rmse": np.nan,
            "delta_rmse": np.nan,
            "correlation": np.nan,
            "baseline_correlation": np.nan,
            "delta_correlation": np.nan,
            "r2": np.nan,
            "baseline_r2": np.nan,
            "delta_r2": np.nan,
            "directional_accuracy": np.nan,
            "baseline_directional_accuracy": np.nan,
            "delta_directional_accuracy": np.nan,
        }

    pred_sub = pred_arr[mask]
    base_sub = base_arr[mask]
    truth_sub = truth_arr[mask]
    ctrl_sub = ctrl_arr[mask]

    rmse = _rmse(pred_sub, truth_sub)
    base_rmse = _rmse(base_sub, truth_sub)
    corr = _corr(pred_sub, truth_sub)
    base_corr = _corr(base_sub, truth_sub)
    r2 = _r2(pred_sub, truth_sub, ctrl_sub)
    base_r2 = _r2(base_sub, truth_sub, ctrl_sub)
    dir_acc = _directional_accuracy(pred_sub, truth_sub, ctrl_sub)
    base_dir_acc = _directional_accuracy(base_sub, truth_sub, ctrl_sub)

    return {
        "n": int(mask.sum()),
        "rmse": rmse,
        "baseline_rmse": base_rmse,
        "delta_rmse": rmse - base_rmse,
        "correlation": corr,
        "baseline_correlation": base_corr,
        "delta_correlation": corr - base_corr,
        "r2": r2,
        "baseline_r2": base_r2,
        "delta_r2": r2 - base_r2,
        "directional_accuracy": dir_acc,
        "baseline_directional_accuracy": base_dir_acc,
        "delta_directional_accuracy": dir_acc - base_dir_acc,
    }


def build_delta_table(treatment: pd.Series, control: pd.Series) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for spec in MODEL_SPECS:
        pred_df = jsonl_to_dataframe(spec["path"]).reindex(columns=Q_COLS)

        baseline_rows = {
            "single": "baseline" if "baseline" in pred_df.index else None,
            "reasoning": "baseline_reasoning" if "baseline_reasoning" in pred_df.index else None,
        }

        for variation in pred_df.index:
            try:
                input_group, family, mode = parse_variation(str(variation))
            except ValueError:
                continue

            if input_group == "baseline" or mode not in MODES:
                continue

            baseline_name = baseline_rows.get(mode)
            if baseline_name is None or baseline_name not in pred_df.index:
                continue

            metrics = paired_delta_metrics(
                pred_df.loc[variation],
                pred_df.loc[baseline_name],
                treatment,
                control,
            )
            rows.append(
                {
                    "model": spec["model"],
                    "variation": variation,
                    "input_group": input_group,
                    "family": family,
                    "mode": mode,
                    "baseline_variation": baseline_name,
                    **metrics,
                }
            )

    out = pd.DataFrame.from_records(rows)
    out["input_group"] = pd.Categorical(out["input_group"], categories=INPUT_GROUPS, ordered=True)
    out["mode"] = pd.Categorical(out["mode"], categories=MODES, ordered=True)
    return out.sort_values(["model", "input_group", "family", "mode"]).reset_index(drop=True)


def load_benchmark_reference(
    treatment: pd.Series,
    control: pd.Series,
) -> pd.DataFrame:
    df_val = pd.read_csv(
        ROOT / "science_data" / "data" / "processed_data" / "df_paired_val.csv"
    ).sort_values("CONFIG_configId")
    enet_pred = 100.0 * df_val["elastic_prereg_pred"].to_numpy(dtype=float)

    learn = pd.read_csv(
        ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"
    )
    train_mean = float(100.0 * learn["treatment_itt_efficiency"].mean())
    train_mean_pred = np.full(len(treatment), train_mean, dtype=float)

    truth_arr = treatment.to_numpy(dtype=float)
    ctrl_arr = control.to_numpy(dtype=float)

    noise = compute_noise_metrics(
        load_pairs(
            str(
                ROOT
                / "science_data"
                / "data"
                / "processed_data"
                / "df_analysis_val.csv"
            )
        )
    )
    rmse_noise = float(noise["rmse_min_y"] * 100.0)
    corr_noise = float(noise["r_max_y"])
    null_mse_control = float(np.mean((truth_arr - ctrl_arr) ** 2))
    null_mse_learning = float(np.mean((truth_arr - train_mean) ** 2))

    rows = [
        {
            "benchmark": "E-Net",
            "rmse": _rmse(enet_pred, truth_arr),
            "correlation": _corr(enet_pred, truth_arr),
            "r2_vs_control_null": _r2(enet_pred, truth_arr, ctrl_arr),
            "r2_vs_learning_mean": _r2_against_constant(enet_pred, truth_arr, train_mean),
            "directional_accuracy": _directional_accuracy(enet_pred, truth_arr, ctrl_arr),
            "note": "Elastic net on processed validation features",
        },
        {
            "benchmark": "Noise ceiling",
            "rmse": rmse_noise,
            "correlation": corr_noise,
            "r2_vs_control_null": float(1.0 - (rmse_noise**2) / null_mse_control),
            "r2_vs_learning_mean": float(1.0 - (rmse_noise**2) / null_mse_learning),
            "directional_accuracy": np.nan,
            "note": "Treatment-side RMSE floor and correlation ceiling",
        },
        {
            "benchmark": "Train mean baseline",
            "rmse": _rmse(train_mean_pred, truth_arr),
            "correlation": 0.0,
            "r2_vs_control_null": _r2(train_mean_pred, truth_arr, ctrl_arr),
            "r2_vs_learning_mean": 0.0,
            "directional_accuracy": _directional_accuracy(train_mean_pred, truth_arr, ctrl_arr),
            "note": f"Constant predictor at learning-wave treatment mean ({train_mean:.2f})",
        },
    ]
    return pd.DataFrame(rows)


def _annotation_labels(delta_pivot: pd.DataFrame, raw_pivot: pd.DataFrame) -> np.ndarray:
    labels = np.empty(delta_pivot.shape, dtype=object)
    for i, row in enumerate(delta_pivot.index):
        for j, col in enumerate(delta_pivot.columns):
            delta_value = delta_pivot.loc[row, col]
            raw_value = raw_pivot.loc[row, col]
            if pd.isna(delta_value):
                labels[i, j] = ""
                continue
            delta_text = f"{delta_value:.02f}" if abs(float(delta_value)) < 10 else f"{delta_value:.1f}"
            raw_text = f"{raw_value:.02f}" if abs(float(raw_value)) < 10 else f"{raw_value:.1f}"
            labels[i, j] = (
                f"{delta_text}\n({raw_text})"
            )
    return labels


def _baseline_rows_for_model(
    model_df: pd.DataFrame,
    input_group: str,
    raw_metric: str,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for mode in MODES:
        subset = model_df.loc[model_df["mode"] == mode]
        if subset.empty:
            continue
        baseline_col = f"baseline_{raw_metric}"
        raw_series = subset[baseline_col].replace([np.inf, -np.inf], np.nan).dropna()
        if raw_series.empty:
            continue
        rows.append(
            {
                "input_group": input_group,
                "family": "baseline",
                "mode": mode,
                metric_spec_col_name(raw_metric): 0.0,
                raw_metric: float(raw_series.iloc[0]),
            }
        )
    return pd.DataFrame(rows)


def metric_spec_col_name(raw_metric: str) -> str:
    return f"delta_{raw_metric}"


def _benchmark_footer(benchmark_df: pd.DataFrame, metric_spec: dict[str, str]) -> str:
    metric_col = metric_spec["benchmark_col"]
    preferred_order = ["E-Net", "Noise ceiling", "Train mean baseline"]
    parts: list[str] = []
    for benchmark in preferred_order:
        subset = benchmark_df.loc[benchmark_df["benchmark"] == benchmark, metric_col]
        if subset.empty or pd.isna(subset.iloc[0]):
            continue
        parts.append(f"{benchmark}: {float(subset.iloc[0]):.2f}")
    return " | ".join(parts)


def _panel_tables(
    model_df: pd.DataFrame,
    input_group: str,
    metric_spec: dict[str, str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw_metric = metric_spec["col"].replace("delta_", "")
    part = model_df.loc[model_df["input_group"] == input_group].copy()
    order = ["baseline"] + family_order(input_group)
    part = pd.concat(
        [
            _baseline_rows_for_model(model_df, input_group, raw_metric),
            part,
        ],
        ignore_index=True,
    )
    part["family"] = pd.Categorical(part["family"], categories=order, ordered=True)
    delta_pivot = part.pivot(index="family", columns="mode", values=metric_spec["col"])
    delta_pivot = delta_pivot.reindex(index=order, columns=MODES)
    raw_pivot = part.pivot(index="family", columns="mode", values=raw_metric)
    raw_pivot = raw_pivot.reindex(index=order, columns=MODES)
    return delta_pivot, raw_pivot


def _absmax_for_metric(delta_df: pd.DataFrame, metric_spec: dict[str, str]) -> float:
    finite = delta_df[metric_spec["col"]].replace([np.inf, -np.inf], np.nan).dropna()
    absmax = float(np.nanquantile(np.abs(finite), 0.95)) if not finite.empty else 0.1
    return 0.1 if absmax == 0 else absmax


def _model_slug(model: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", model.lower())


def plot_metric_heatmaps(
    delta_df: pd.DataFrame,
    benchmark_df: pd.DataFrame,
    metric_spec: dict[str, str],
) -> None:
    models = [spec["model"] for spec in MODEL_SPECS if spec["model"] in set(delta_df["model"])]
    n_rows = len(models)
    n_cols = len(INPUT_GROUPS)

    absmax = _absmax_for_metric(delta_df, metric_spec)

    cmap = sns.color_palette("RdBu_r", as_cmap=True)
    cmap.set_bad("#f3f3f3")

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(15.1, 2.15 * n_rows + 1.45),
        constrained_layout=False,
    )
    if n_rows == 1:
        axes = np.array([axes])

    for row_idx, model in enumerate(models):
        model_df = delta_df.loc[delta_df["model"] == model].copy()
        for col_idx, input_group in enumerate(INPUT_GROUPS):
            ax = axes[row_idx, col_idx]
            delta_pivot, raw_pivot = _panel_tables(model_df, input_group, metric_spec)

            sns.heatmap(
                delta_pivot,
                ax=ax,
                cmap=cmap,
                center=0,
                vmin=-absmax,
                vmax=absmax,
                annot=_annotation_labels(delta_pivot, raw_pivot),
                fmt="",
                annot_kws={"fontsize": 6.1, "linespacing": 0.82},
                linewidths=0.5,
                cbar=False,
                mask=delta_pivot.isna(),
            )

            if row_idx == 0:
                ax.set_title(f"Validation | {input_group}")
            else:
                ax.set_title("")
            if col_idx == 0:
                ax.text(
                    -0.62,
                    0.5,
                    model,
                    transform=ax.transAxes,
                    rotation=90,
                    ha="center",
                    va="center",
                    fontsize=11,
                    fontweight="bold",
                )
            ax.tick_params(axis="y", labelrotation=0, labelsize=8.5, pad=2)
            ax.set_xticklabels([MODE_LABELS.get(str(col.get_text()), str(col.get_text())) for col in ax.get_xticklabels()])
            ax.set_xlabel("")
            ax.set_ylabel("")

    fig.subplots_adjust(top=0.885, bottom=0.085, left=0.16, right=0.92, wspace=0.25, hspace=0.34)
    right_boxes = [axes[row_idx, -1].get_position() for row_idx in range(n_rows)]
    grid_top = max(box.y1 for box in right_boxes)
    grid_bottom = min(box.y0 for box in right_boxes)
    grid_mid = 0.5 * (grid_top + grid_bottom)
    cbar_height = min(0.22, 0.28 * (grid_top - grid_bottom))
    cax = fig.add_axes([0.935, grid_mid - 0.5 * cbar_height, 0.013, cbar_height])
    colorbar = fig.colorbar(
        plt.cm.ScalarMappable(norm=Normalize(vmin=-absmax, vmax=absmax), cmap=cmap),
        cax=cax,
    )
    colorbar.set_label(metric_spec["cbar"])

    fig.suptitle(
        f"{metric_spec['title']}\nRows are models; columns are input groups; cells show report-family deltas vs matched no-augmentation within mode.",
        fontsize=15,
        y=0.975,
    )
    fig.text(
        0.5,
        0.02,
        _benchmark_footer(benchmark_df, metric_spec),
        ha="center",
        va="bottom",
        fontsize=10,
        color="0.25",
    )
    stem = metric_spec["stem"]
    fig.savefig(PLOTS / f"{stem}.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_model_dashboard(
    model: str,
    delta_df: pd.DataFrame,
    benchmark_df: pd.DataFrame,
) -> None:
    model_df = delta_df.loc[delta_df["model"] == model].copy()
    cmap = sns.color_palette("RdBu_r", as_cmap=True)
    cmap.set_bad("#f3f3f3")

    fig, axes = plt.subplots(
        len(METRIC_SPECS),
        len(INPUT_GROUPS),
        figsize=(14.8, 12.6),
        constrained_layout=False,
    )

    absmax_map = {
        metric_spec["col"]: _absmax_for_metric(delta_df, metric_spec)
        for metric_spec in METRIC_SPECS
    }

    for row_idx, metric_spec in enumerate(METRIC_SPECS):
        absmax = absmax_map[metric_spec["col"]]
        for col_idx, input_group in enumerate(INPUT_GROUPS):
            ax = axes[row_idx, col_idx]
            delta_pivot, raw_pivot = _panel_tables(model_df, input_group, metric_spec)

            sns.heatmap(
                delta_pivot,
                ax=ax,
                cmap=cmap,
                center=0,
                vmin=-absmax,
                vmax=absmax,
                annot=_annotation_labels(delta_pivot, raw_pivot),
                fmt="",
                annot_kws={"fontsize": 6.6, "linespacing": 0.84},
                linewidths=0.5,
                cbar=False,
                mask=delta_pivot.isna(),
            )

            if row_idx == 0:
                ax.set_title(f"Validation | {input_group}")
            else:
                ax.set_title("")
            if col_idx == 0:
                ax.set_ylabel(metric_spec["short"], fontsize=11, fontweight="bold")
            else:
                ax.set_ylabel("")
            ax.tick_params(axis="y", labelrotation=0, labelsize=8.5, pad=2)
            ax.set_xticklabels([MODE_LABELS.get(str(col.get_text()), str(col.get_text())) for col in ax.get_xticklabels()])
            ax.set_xlabel("")

    fig.subplots_adjust(top=0.90, bottom=0.12, left=0.12, right=0.90, wspace=0.26, hspace=0.32)
    for row_idx, metric_spec in enumerate(METRIC_SPECS):
        row_boxes = [axes[row_idx, col_idx].get_position() for col_idx in range(len(INPUT_GROUPS))]
        row_top = max(box.y1 for box in row_boxes)
        row_bottom = min(box.y0 for box in row_boxes)
        row_mid = 0.5 * (row_top + row_bottom)
        row_height = row_top - row_bottom
        cax = fig.add_axes([0.915, row_mid - 0.28 * row_height, 0.015, 0.56 * row_height])
        colorbar = fig.colorbar(
            plt.cm.ScalarMappable(
                norm=Normalize(vmin=-absmax_map[metric_spec["col"]], vmax=absmax_map[metric_spec["col"]]),
                cmap=cmap,
            ),
            cax=cax,
        )
        colorbar.set_label(metric_spec["cbar"])

    footer_lines = [
        f"{metric_spec['short']}: {_benchmark_footer(benchmark_df, metric_spec)}"
        for metric_spec in METRIC_SPECS
    ]
    fig.suptitle(f"Validation Augmentation Deltas: {model}", fontsize=16, y=0.975)
    fig.text(
        0.5,
        0.03,
        "\n".join(footer_lines),
        ha="center",
        va="bottom",
        fontsize=9.5,
        color="0.25",
    )

    stem = f"validation_augmentation_delta_dashboard_{_model_slug(model)}"
    fig.savefig(SPLIT_PLOTS / f"{stem}.png", dpi=220, bbox_inches="tight")
    fig.savefig(SPLIT_PLOTS / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_plot_dir(PLOTS)
    ensure_plot_dir(SPLIT_PLOTS)
    treatment, control = load_validation_truth()
    delta_df = build_delta_table(treatment, control)
    delta_df.to_csv(RESULTS / "validation_augmentation_delta_by_model_table.csv", index=False)
    benchmark_df = load_benchmark_reference(treatment, control)
    benchmark_df.to_csv(
        RESULTS / "validation_augmentation_delta_by_model_benchmarks.csv",
        index=False,
    )

    for metric_spec in METRIC_SPECS:
        plot_metric_heatmaps(delta_df, benchmark_df, metric_spec)
    for model in [spec["model"] for spec in MODEL_SPECS if spec["model"] in set(delta_df["model"])]:
        plot_model_dashboard(model, delta_df, benchmark_df)

    print(RESULTS / "validation_augmentation_delta_by_model_table.csv")
    for metric_spec in METRIC_SPECS:
        print(PLOTS / f"{metric_spec['stem']}.png")
    if SKIPPED_MODELS:
        print("Skipped models with no matching output file:", ", ".join(SKIPPED_MODELS))


if __name__ == "__main__":
    main()
