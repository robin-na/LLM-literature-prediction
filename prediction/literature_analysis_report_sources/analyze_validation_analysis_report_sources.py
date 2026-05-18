from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from jsonl_parser import jsonl_to_dataframe
from prediction_metrics import _directional_accuracy_np


ROOT = ANALYSIS_ROOT.parent
OPENAI_BATCH_OUTPUT = ROOT / "openAI_batch_output"
INPUT = ROOT / "input"
RESULTS_DIR = ROOT / "results" / "validation" / "literature_analysis_report_sources"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_analysis_report_sources"
METADATA_CSV = ROOT / "paper_collection" / "WoS_251031_fileInfo.csv"

Q_COLS = [f"Q{i}" for i in range(1, 21)]
METRIC_ORDER = ["rmse", "correlation", "r2", "directional_accuracy"]
METRIC_LABELS = {
    "rmse": "RMSE",
    "correlation": "Correlation",
    "r2": r"$R^2$ vs control baseline",
    "directional_accuracy": "Directional Accuracy",
}
LOWER_IS_BETTER = {"rmse"}
PGG_MS_ID = "PGG_MS_202502"
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#7bccc4",
    "GPT-4.1 Nano": "#8c564b",
}

RUN_SPECS = [
    {
        "model": "GPT-4.1",
        "mode": "reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_positive_case_variations_41.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "mode": "reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1 Mini",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41mini.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41mini.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "mode": "reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_reasoning",
    },
    {
        "model": "GPT-4.1 Nano",
        "mode": "joint_reasoning",
        "output_path": OPENAI_BATCH_OUTPUT / "prediction_literature_analysis_report_strict243_joint_41nano.jsonl",
        "baseline_path": OPENAI_BATCH_OUTPUT / "prediction_crosswave_variations_41nano.jsonl",
        "baseline_variation": "baseline_joint_reasoning",
    },
]


def load_truth() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(INPUT / "pgg_CONFIGmerged_validation.csv").sort_values("CONFIG_configId")
    treatment = pd.Series(df["efficiency_p"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
    control = pd.Series(df["efficiency_np"].to_numpy(dtype=float) * 100.0, index=Q_COLS)
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


def compute_metrics(pred_row: pd.Series, treatment: pd.Series, control: pd.Series) -> dict[str, float | int]:
    pred = pd.to_numeric(pred_row, errors="coerce").reindex(Q_COLS)
    truth = treatment.reindex(Q_COLS)
    ctrl = control.reindex(Q_COLS)

    pred_arr = pred.to_numpy(dtype=float)
    truth_arr = truth.to_numpy(dtype=float)
    ctrl_arr = ctrl.to_numpy(dtype=float)
    mask = ~np.isnan(pred_arr) & ~np.isnan(truth_arr) & ~np.isnan(ctrl_arr)
    if mask.sum() == 0:
        return {"n": 0, "rmse": np.nan, "correlation": np.nan, "r2": np.nan, "directional_accuracy": np.nan}

    pred_sub = pred_arr[mask]
    truth_sub = truth_arr[mask]
    ctrl_sub = ctrl_arr[mask]
    return {
        "n": int(mask.sum()),
        "rmse": _rmse(pred_sub, truth_sub),
        "correlation": _corr(pred_sub, truth_sub),
        "r2": _r2(pred_sub, truth_sub, ctrl_sub),
        "directional_accuracy": float(_directional_accuracy_np(pred_sub, truth_sub, ctrl_sub)),
    }


def normalize_source_id(value: str) -> str:
    return Path(value).stem


def extract_source_id(variation: str) -> str:
    if "/" in variation:
        return variation.split("/", 1)[1]
    return variation


def load_metadata() -> dict[str, dict[str, str]]:
    df = pd.read_csv(METADATA_CSV)
    meta: dict[str, dict[str, str]] = {}
    for row in df.to_dict("records"):
        source_id = normalize_source_id(str(row.get("custom_id", "")))
        if source_id:
            meta[source_id] = {
                "title": str(row.get("Article Title", "") or ""),
                "authors": str(row.get("Authors", "") or ""),
                "journal": str(row.get("Source Title", "") or ""),
                "year": str(row.get("Publication Year", "") or ""),
            }
    meta["PGG_MS_202502"] = {
        "title": "Integrative Experiments Identify How Punishment Impacts Welfare in Public Goods Games",
        "authors": "Alsobaya, M; Rand, DG; Watts, DJ; Almaatouq, A",
        "journal": "",
        "year": "2025",
    }
    return meta


def build_rows(treatment: pd.Series, control: pd.Series, metadata: dict[str, dict[str, str]]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for spec in RUN_SPECS:
        output_path = spec["output_path"]
        baseline_path = spec["baseline_path"]
        if not output_path.exists() or not baseline_path.exists():
            continue

        pred_df = jsonl_to_dataframe(output_path).reindex(columns=Q_COLS)
        base_df = jsonl_to_dataframe(baseline_path).reindex(columns=Q_COLS)
        baseline_variation = spec["baseline_variation"]
        if baseline_variation not in base_df.index:
            continue

        baseline_metrics = compute_metrics(base_df.loc[baseline_variation], treatment, control)

        for variation, pred_row in pred_df.iterrows():
            source_id = extract_source_id(str(variation))
            source_meta = metadata.get(source_id, {})
            metrics = compute_metrics(pred_row, treatment, control)
            row = {
                "model": spec["model"],
                "mode": spec["mode"],
                "variation": variation,
                "source_id": source_id,
                "title": source_meta.get("title", ""),
                "authors": source_meta.get("authors", ""),
                "journal": source_meta.get("journal", ""),
                "year": source_meta.get("year", ""),
                "baseline_variation": baseline_variation,
                "baseline_n": baseline_metrics["n"],
                "n": metrics["n"],
            }
            for metric in METRIC_ORDER:
                row[metric] = metrics[metric]
                row[f"baseline_{metric}"] = baseline_metrics[metric]
                row[f"delta_{metric}"] = float(metrics[metric]) - float(baseline_metrics[metric])
                if metric in LOWER_IS_BETTER:
                    row[f"improved_{metric}"] = float(metrics[metric]) < float(baseline_metrics[metric])
                else:
                    row[f"improved_{metric}"] = float(metrics[metric]) > float(baseline_metrics[metric])
            rows.append(row)

    out = pd.DataFrame.from_records(rows)
    if out.empty:
        return out
    return out.sort_values(["model", "mode", "source_id"]).reset_index(drop=True)


def summarize(rows: pd.DataFrame) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = []
    for (model, mode), part in rows.groupby(["model", "mode"], dropna=False):
        record: dict[str, object] = {
            "model": model,
            "mode": mode,
            "n_sources": len(part),
        }
        for metric in METRIC_ORDER:
            record[f"baseline_{metric}"] = float(part[f"baseline_{metric}"].iloc[0])
            record[f"mean_{metric}"] = float(part[metric].mean())
            record[f"median_{metric}"] = float(part[metric].median())
            record[f"mean_delta_{metric}"] = float(part[f"delta_{metric}"].mean())
            record[f"median_delta_{metric}"] = float(part[f"delta_{metric}"].median())
            record[f"share_improved_{metric}"] = float(part[f"improved_{metric}"].mean())

            best_idx = part[f"delta_{metric}"].idxmin() if metric in LOWER_IS_BETTER else part[f"delta_{metric}"].idxmax()
            worst_idx = part[f"delta_{metric}"].idxmax() if metric in LOWER_IS_BETTER else part[f"delta_{metric}"].idxmin()
            best_row = part.loc[best_idx]
            worst_row = part.loc[worst_idx]
            record[f"best_source_{metric}"] = best_row["source_id"]
            record[f"best_delta_{metric}"] = float(best_row[f"delta_{metric}"])
            record[f"worst_source_{metric}"] = worst_row["source_id"]
            record[f"worst_delta_{metric}"] = float(worst_row[f"delta_{metric}"])
        summary_rows.append(record)
    return pd.DataFrame(summary_rows).sort_values(["model", "mode"]).reset_index(drop=True)


def build_top_bottom(rows: pd.DataFrame, k: int = 15) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for (model, mode), part in rows.groupby(["model", "mode"], dropna=False):
        for metric in METRIC_ORDER:
            ascending = metric in LOWER_IS_BETTER
            ranked = part.sort_values(f"delta_{metric}", ascending=ascending).reset_index(drop=True)
            top = ranked.head(k).copy()
            bottom = ranked.tail(k).copy()
            for bucket, df_bucket in [("top", top), ("bottom", bottom)]:
                for rank, (_, row) in enumerate(df_bucket.iterrows(), start=1):
                    out_rows.append(
                        {
                            "model": model,
                            "mode": mode,
                            "metric": metric,
                            "bucket": bucket,
                            "rank": rank,
                            "source_id": row["source_id"],
                            "title": row["title"],
                            "journal": row["journal"],
                            "year": row["year"],
                            "metric_value": row[metric],
                            "baseline_metric_value": row[f"baseline_{metric}"],
                            "delta_metric_value": row[f"delta_{metric}"],
                        }
                    )
    return pd.DataFrame(out_rows)


def build_context_table(rows: pd.DataFrame) -> pd.DataFrame:
    out_rows: list[dict[str, object]] = []
    for (model, mode), part in rows.groupby(["model", "mode"], dropna=False):
        pgg_part = part.loc[part["source_id"] == PGG_MS_ID]
        pgg_row = pgg_part.iloc[0] if not pgg_part.empty else None
        for metric in METRIC_ORDER:
            ascending = metric in LOWER_IS_BETTER
            best_row = part.sort_values(metric, ascending=ascending).iloc[0]
            record: dict[str, object] = {
                "model": model,
                "mode": mode,
                "metric": metric,
                "baseline_value": float(best_row[f"baseline_{metric}"]),
                "best_source_id": best_row["source_id"],
                "best_source_title": best_row["title"],
                "best_value": float(best_row[metric]),
                "best_delta": float(best_row[f"delta_{metric}"]),
            }
            if pgg_row is not None:
                record["pgg_ms_value"] = float(pgg_row[metric])
                record["pgg_ms_delta"] = float(pgg_row[f"delta_{metric}"])
                record["pgg_ms_is_best"] = bool(best_row["source_id"] == PGG_MS_ID)
            else:
                record["pgg_ms_value"] = np.nan
                record["pgg_ms_delta"] = np.nan
                record["pgg_ms_is_best"] = False
            out_rows.append(record)
    return pd.DataFrame(out_rows).sort_values(["metric", "model", "mode"]).reset_index(drop=True)


def build_delta_summary(rows: pd.DataFrame, n_boot: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    out_rows: list[dict[str, object]] = []
    for (model, mode), part in rows.groupby(["model", "mode"], dropna=False):
        for metric in METRIC_ORDER:
            deltas = part[f"delta_{metric}"].to_numpy(dtype=float)
            deltas = deltas[np.isfinite(deltas)]
            if deltas.size == 0:
                continue
            boot = np.empty(n_boot, dtype=float)
            for i in range(n_boot):
                idx = rng.integers(0, deltas.size, size=deltas.size)
                boot[i] = float(np.mean(deltas[idx]))
            ci_low, ci_high = np.percentile(boot, [2.5, 97.5])
            pgg_part = part.loc[part["source_id"] == PGG_MS_ID]
            pgg_delta = float(pgg_part[f"delta_{metric}"].iloc[0]) if not pgg_part.empty else np.nan
            out_rows.append(
                {
                    "model": model,
                    "mode": mode,
                    "metric": metric,
                    "baseline_value": float(part[f"baseline_{metric}"].iloc[0]),
                    "mean_delta": float(np.mean(deltas)),
                    "median_delta": float(np.median(deltas)),
                    "ci_low": float(ci_low),
                    "ci_high": float(ci_high),
                    "share_improved": float(part[f"improved_{metric}"].mean()),
                    "pgg_ms_delta": pgg_delta,
                }
            )
    return pd.DataFrame(out_rows).sort_values(["metric", "model", "mode"]).reset_index(drop=True)


def _model_mode_label(model: str, mode: str) -> str:
    return f"{model}\n{mode.replace('_', ' ')}"


def _metric_ordered_labels(rows: pd.DataFrame, metric: str, baseline_col: str | None = None) -> list[str]:
    higher_is_better = metric not in LOWER_IS_BETTER
    if baseline_col is None:
        baseline_col = f"baseline_{metric}"
    baseline_order = (
        rows.groupby(["model", "mode"], dropna=False)[baseline_col]
        .first()
        .reset_index()
        .sort_values(baseline_col, ascending=not higher_is_better, kind="mergesort")
    )
    return [_model_mode_label(str(r["model"]), str(r["mode"])) for _, r in baseline_order.iterrows()]


def plot_distributions(rows: pd.DataFrame) -> None:
    if rows.empty:
        return

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 12
    sns.set_theme(style="whitegrid")
    rows = rows.copy()
    rows["model_mode"] = rows["model"] + "\n" + rows["mode"]

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    axes = axes.flatten()
    color_map = {
        "GPT-4.1\njoint_reasoning": "#ff7f0e",
        "GPT-4.1\nreasoning": "#ffbb78",
        "GPT-4.1 Mini\njoint_reasoning": "#1f77b4",
        "GPT-4.1 Mini\nreasoning": "#9ecae1",
        "GPT-4.1 Nano\njoint_reasoning": "#8c564b",
        "GPT-4.1 Nano\nreasoning": "#c49c94",
    }

    for ax, metric in zip(axes, METRIC_ORDER):
        sns.boxplot(
            data=rows,
            x="model_mode",
            y=f"delta_{metric}",
            ax=ax,
            color="#d1d5db",
            fliersize=0,
        )
        sns.stripplot(
            data=rows,
            x="model_mode",
            y=f"delta_{metric}",
            ax=ax,
            hue="model_mode",
            palette=color_map,
            alpha=0.45,
            size=3,
            jitter=0.28,
            dodge=False,
            legend=False,
        )
        ax.axhline(0.0, color="black", linestyle="--", linewidth=1)
        ax.set_title(f"{METRIC_LABELS[metric]} delta vs matched baseline")
        ax.set_xlabel("")
        ax.set_ylabel(f"Δ{METRIC_LABELS[metric]}")
        ax.tick_params(axis="x", labelrotation=0)

    fig.suptitle("Validation augmentation deltas by paper-source analysis report", fontsize=15)
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "validation_literature_analysis_report_source_delta_distributions.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_context_dumbbells(rows: pd.DataFrame) -> None:
    if rows.empty:
        return

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 12
    sns.set_theme(style="whitegrid")

    point_colors = {
        "baseline": "#6c757d",
        "mean": "#2b8cbe",
        "pgg_ms": "#f28e2b",
        "improved": "#59a14f",
        "worsened": "#e15759",
    }
    line_colors = {"better": "#d7301f", "worse": "#3182bd"}

    fig, axes = plt.subplots(2, 2, figsize=(12, 8.5), constrained_layout=False)
    axes = axes.flatten()

    for ax, metric in zip(axes, METRIC_ORDER):
        higher_is_better = metric not in LOWER_IS_BETTER
        part = rows.copy()
        part["model_mode"] = [
            _model_mode_label(str(model), str(mode))
            for model, mode in zip(part["model"], part["mode"])
        ]
        order = _metric_ordered_labels(part, metric)
        part["improvement_bucket"] = np.where(
            part[f"improved_{metric}"], "Improved", "Worsened"
        )

        sns.violinplot(
            data=part,
            x="model_mode",
            y=metric,
            order=order,
            ax=ax,
            inner=None,
            cut=0,
            linewidth=0,
            color="#d9ecf7",
            alpha=0.75,
        )
        sns.boxplot(
            data=part,
            x="model_mode",
            y=metric,
            order=order,
            ax=ax,
            width=0.18,
            fliersize=0,
            boxprops={"facecolor": "#9ecae1", "alpha": 0.45},
            medianprops={"color": "#1f1f1f", "linewidth": 1.4},
            whiskerprops={"linewidth": 1.0},
            capprops={"linewidth": 1.0},
        )
        sns.stripplot(
            data=part,
            x="model_mode",
            y=metric,
            order=order,
            hue="improvement_bucket",
            palette={"Improved": point_colors["improved"], "Worsened": point_colors["worsened"]},
            dodge=False,
            jitter=0.18,
            size=2.6,
            alpha=0.35,
            ax=ax,
            zorder=2,
        )
        if ax.legend_ is not None:
            ax.legend_.remove()

        summary = (
            part.groupby("model_mode", dropna=False)
            .agg(
                baseline_value=(f"baseline_{metric}", "first"),
                mean_value=(metric, "mean"),
                share_improved=(f"improved_{metric}", "mean"),
            )
            .reindex(order)
            .reset_index()
        )
        pgg = part.loc[part["source_id"] == PGG_MS_ID, ["model_mode", metric]].rename(columns={metric: "pgg_value"})
        summary = summary.merge(pgg, on="model_mode", how="left")
        x = np.arange(len(summary))

        for i, (_, row) in enumerate(summary.iterrows()):
            baseline = float(row["baseline_value"])
            mean_value = float(row["mean_value"])
            improved = mean_value < baseline if metric in LOWER_IS_BETTER else mean_value > baseline
            ax.plot(
                [x[i], x[i]],
                [baseline, mean_value],
                color=line_colors["better" if improved else "worse"],
                linewidth=2.3,
                zorder=3,
            )
            ylim = ax.get_ylim()
            y_text = ylim[1] - 0.04 * (ylim[1] - ylim[0])
            ax.text(
                x[i],
                y_text,
                f"{100 * row['share_improved']:.0f}% improved\nmean Δ={mean_value - baseline:+.2f}",
                ha="center",
                va="top",
                fontsize=8.5,
                color="0.25",
            )

        ax.scatter(
            x,
            summary["baseline_value"],
            s=62,
            color=point_colors["baseline"],
            edgecolors="white",
            linewidths=0.8,
            zorder=4,
            label="No augmentation",
        )
        ax.scatter(
            x,
            summary["mean_value"],
            s=68,
            color=point_colors["mean"],
            edgecolors="white",
            linewidths=0.8,
            zorder=5,
            label="Mean augmented",
        )
        pgg_mask = summary["pgg_value"].notna()
        if pgg_mask.any():
            ax.scatter(
                x[pgg_mask.to_numpy()],
                summary.loc[pgg_mask, "pgg_value"],
                s=82,
                marker="D",
                color=point_colors["pgg_ms"],
                edgecolors="white",
                linewidths=0.9,
                zorder=6,
                label="PGG-MS",
            )

        ax.set_xticks(x)
        ax.set_xticklabels(summary["model_mode"], rotation=0, fontsize=9)
        direction = "lower is better" if metric in LOWER_IS_BETTER else "higher is better"
        ax.set_title(METRIC_LABELS[metric])
        ax.set_ylabel(f"{METRIC_LABELS[metric]}\n({direction})")
        ax.grid(axis="y", alpha=0.18, zorder=0)
        ax.set_axisbelow(True)

    handles = [
        Line2D([], [], color=point_colors["baseline"], marker="o", linestyle="None", markersize=7, label="No augmentation"),
        Line2D([], [], color=point_colors["mean"], marker="o", linestyle="None", markersize=7, label="Mean augmented"),
        Line2D([], [], color=point_colors["pgg_ms"], marker="D", linestyle="None", markersize=7, label="PGG-MS"),
        Line2D([], [], color=point_colors["improved"], marker="o", linestyle="None", markersize=5, alpha=0.6, label="Improved source"),
        Line2D([], [], color=point_colors["worsened"], marker="o", linestyle="None", markersize=5, alpha=0.6, label="Worsened source"),
        Line2D([], [], color=line_colors["better"], linewidth=2, label="Baseline to mean improved"),
        Line2D([], [], color=line_colors["worse"], linewidth=2, label="Baseline to mean worsened"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 0.005))
    fig.suptitle("Validation levels: baseline vs source distribution vs PGG-MS", fontsize=15, y=0.98)
    fig.text(
        0.5,
        0.045,
        "Within each panel, model-mode conditions are ordered by no-augmentation performance, with the stronger baseline at left. Violin and box show the full source distribution.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.09, 1, 0.95])
    fig.savefig(PLOTS_DIR / "validation_literature_analysis_report_source_dumbbells.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_delta_summary_forest(delta_summary: pd.DataFrame) -> None:
    if delta_summary.empty:
        return

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 12
    sns.set_theme(style="whitegrid")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8.5), constrained_layout=False)
    axes = axes.flatten()

    for ax, metric in zip(axes, METRIC_ORDER):
        higher_is_better = metric not in LOWER_IS_BETTER
        part = delta_summary.loc[delta_summary["metric"] == metric].copy()
        part["model_mode"] = [
            _model_mode_label(str(model), str(mode))
            for model, mode in zip(part["model"], part["mode"])
        ]
        order = _metric_ordered_labels(part, metric, baseline_col="baseline_value")
        part = part.set_index("model_mode").loc[order].reset_index()
        y = np.arange(len(part))

        ax.axvline(0.0, color="black", linewidth=1.0, linestyle="--", zorder=0)
        for i, (_, row) in enumerate(part.iterrows()):
            color = MODEL_COLORS.get(str(row["model"]), "#2b8cbe")
            ax.plot([row["ci_low"], row["ci_high"]], [y[i], y[i]], color=color, linewidth=2.0, zorder=2)
            ax.scatter(
                [row["mean_delta"]],
                [y[i]],
                s=70,
                color=color,
                edgecolors="white",
                linewidths=0.8,
                zorder=3,
            )
            if np.isfinite(float(row["pgg_ms_delta"])):
                ax.scatter(
                    [row["pgg_ms_delta"]],
                    [y[i]],
                    s=78,
                    marker="D",
                    color="#f28e2b",
                    edgecolors="white",
                    linewidths=0.9,
                    zorder=4,
                )
            ha = "left" if higher_is_better else "right"
            xpad = 0.01 * (part["ci_high"].max() - part["ci_low"].min() + 1e-9)
            x_text = max(row["ci_high"], row["mean_delta"]) + xpad if higher_is_better else min(row["ci_low"], row["mean_delta"]) - xpad
            ax.text(
                x_text,
                y[i],
                f"{100 * row['share_improved']:.0f}% improved",
                va="center",
                ha=ha,
                fontsize=9,
                color="0.25",
            )

        ax.set_yticks(y)
        ax.set_yticklabels(part["model_mode"])
        ax.invert_yaxis()
        direction = "lower is better" if metric in LOWER_IS_BETTER else "higher is better"
        ax.set_title(METRIC_LABELS[metric], loc="left")
        ax.set_xlabel(f"Mean Δ{METRIC_LABELS[metric]}\n({direction})")
        ax.grid(axis="x", alpha=0.18, zorder=0)
        ax.set_axisbelow(True)

    handles = [
        Line2D([], [], color="#2b8cbe", marker="o", linestyle="None", markersize=7, label="Mean source delta"),
        Line2D([], [], color="#2b8cbe", linewidth=2, label="95% bootstrap CI across sources"),
        Line2D([], [], color="#f28e2b", marker="D", linestyle="None", markersize=7, label="PGG-MS delta"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.suptitle("Validation delta summary by model-mode", fontsize=15, y=0.98)
    fig.text(
        0.5,
        0.045,
        "Points show the mean augmentation delta across all paper sources. Orange diamonds mark PGG-MS. Text shows the share of sources that improved the metric.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.95])
    fig.savefig(PLOTS_DIR / "validation_literature_analysis_report_source_delta_forest.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    treatment, control = load_truth()
    metadata = load_metadata()
    rows = build_rows(treatment, control, metadata)
    if rows.empty:
        raise FileNotFoundError("No analysis-report output files were found for the configured run specs.")

    summary = summarize(rows)
    top_bottom = build_top_bottom(rows, k=15)
    context = build_context_table(rows)
    delta_summary = build_delta_summary(rows)

    rows.to_csv(RESULTS_DIR / "validation_literature_analysis_report_source_rows.csv", index=False)
    summary.to_csv(RESULTS_DIR / "validation_literature_analysis_report_source_summary.csv", index=False)
    top_bottom.to_csv(RESULTS_DIR / "validation_literature_analysis_report_source_top_bottom.csv", index=False)
    context.to_csv(RESULTS_DIR / "validation_literature_analysis_report_source_context.csv", index=False)
    delta_summary.to_csv(RESULTS_DIR / "validation_literature_analysis_report_source_delta_summary.csv", index=False)

    plot_distributions(rows)
    plot_context_dumbbells(rows)
    plot_delta_summary_forest(delta_summary)

    print(RESULTS_DIR / "validation_literature_analysis_report_source_rows.csv")
    print(RESULTS_DIR / "validation_literature_analysis_report_source_summary.csv")
    print(RESULTS_DIR / "validation_literature_analysis_report_source_top_bottom.csv")
    print(RESULTS_DIR / "validation_literature_analysis_report_source_context.csv")
    print(RESULTS_DIR / "validation_literature_analysis_report_source_delta_summary.csv")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_delta_distributions.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_dumbbells.png")
    print(PLOTS_DIR / "validation_literature_analysis_report_source_delta_forest.png")


if __name__ == "__main__":
    main()
