from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
GPT_REPEAT5_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_collection_analysis_reports_repeat5_model_sampling"
    / "validation_literature_collection_analysis_report_repeat5_model_sampling_repeat_rows.csv"
)
OPENAI_WIDE_CSV = ROOT / "openAI_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_wide.csv"
CLAUDE_WIDE_CSV = ROOT / "claude_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_wide.csv"
GEMINI_WIDE_CSV = ROOT / "gemini_batch_output" / "prediction_outputs_2026" / "prediction_outputs_2026_wide.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

Q_COLS = [f"Q{i}" for i in range(1, 21)]
GPT_MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-4.1 Nano", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano"]
CLAUDE_MODELS = ["Claude Opus 4.6", "Claude Sonnet 4.6", "Claude Haiku 4.5"]
GEMINI_MODELS = ["Gemini 2.5 Pro", "Gemini 2.5 Flash"]
LLM_GROUP_LABEL = "LLMs"

GROUP_ORDER = ["Laypeople", "Experts", LLM_GROUP_LABEL]
GROUP_COLORS = {
    "Laypeople": "#caa27e",
    "Experts": "#8d6748",
    LLM_GROUP_LABEL: "#6f86a6",
}

OUT_PNG = PLOTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30.png"
OUT_PDF = PLOTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30.pdf"
ROWS_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_rows.csv"
LLM_SUMMARY_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_model_summary.csv"
REFERENCE_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_reference.csv"
PERCENTILES_CSV = RESULTS_DIR / "figure1_panel_b_baseline_vs_humans_correlation_cdf_llm_mean30_percentiles.csv"


def corr_rows(mat: np.ndarray, truth: np.ndarray) -> np.ndarray:
    centered_mat = mat - mat.mean(axis=1, keepdims=True)
    centered_truth = truth - truth.mean()
    denom = np.sqrt((centered_mat**2).sum(axis=1) * (centered_truth**2).sum())
    out = np.full(mat.shape[0], np.nan, dtype=float)
    valid = denom > 0
    out[valid] = (centered_mat[valid] @ centered_truth) / denom[valid]
    return out


def load_truth_vectors() -> tuple[np.ndarray, float, float]:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    truth_vec = validation["efficiency_p"].to_numpy(dtype=float) * 100.0
    control_vec = validation["efficiency_np"].to_numpy(dtype=float) * 100.0
    null_value = float(np.corrcoef(control_vec, truth_vec)[0, 1])
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    ceiling_value = float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])
    return truth_vec, null_value, ceiling_value


def load_human_plot_rows(truth_vec: np.ndarray) -> pd.DataFrame:
    rows = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    rows = rows.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()

    plot_rows: list[dict[str, object]] = []
    for source, group in [("prolific", "Laypeople"), ("sspp", "Experts")]:
        wide = (
            rows.loc[rows["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .sort_index()
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        participant_corr = corr_rows(wide.to_numpy(dtype=float).T * 100.0, truth_vec)
        plot_rows.extend(
            {
                "group": group,
                "value": float(value),
                "kind": "individual_human",
                "label": group,
            }
            for value in participant_corr
            if np.isfinite(value)
        )

    plot_df = pd.DataFrame(plot_rows)
    plot_df["group"] = pd.Categorical(plot_df["group"], categories=GROUP_ORDER, ordered=True)
    return plot_df.sort_values(["group", "value"]).reset_index(drop=True)


def load_gpt_repeat_rows_1to5() -> pd.DataFrame:
    df = pd.read_csv(GPT_REPEAT5_ROWS_CSV, usecols=["model", "condition", "repeat", *Q_COLS])
    df = df.loc[(df["condition"] == "baseline") & (df["model"].isin(GPT_MODELS))].copy()
    df = df.rename(columns={"model": "model_label", "repeat": "repeat_index"})
    df["source_family"] = "gpt_repeat5_validation"
    return df.loc[:, ["model_label", "repeat_index", "source_family", *Q_COLS]].reset_index(drop=True)


def load_openai_repeat_rows_6to30() -> pd.DataFrame:
    usecols = ["source_file", "model_label", "condition_stem", "prompt_elicitation", "repeat_index", *Q_COLS]
    df = pd.read_csv(OPENAI_WIDE_CSV, usecols=lambda c: c in usecols)
    df = df.loc[
        df["source_file"].astype(str).str.startswith("prediction_literature_incremental_baseline_reps6to30_")
        & (df["condition_stem"] == "baseline")
        & (df["prompt_elicitation"] == "joint_reasoning")
        & (df["model_label"].isin(GPT_MODELS))
        & df["repeat_index"].between(6, 30)
    ].copy()
    df["source_family"] = "openai_2026_incremental"
    return df.loc[:, ["model_label", "repeat_index", "source_family", *Q_COLS]].reset_index(drop=True)


def load_claude_repeat_rows_1to30() -> pd.DataFrame:
    usecols = ["source_file", "model_label", "condition_stem", "prompt_elicitation", "repeat_index", *Q_COLS]
    df = pd.read_csv(CLAUDE_WIDE_CSV, usecols=lambda c: c in usecols)
    df = df.loc[
        df["source_file"].astype(str).str.startswith("prediction_literature_")
        & (df["condition_stem"] == "baseline")
        & (df["prompt_elicitation"] == "joint_reasoning")
        & (df["model_label"].isin(CLAUDE_MODELS))
        & df["repeat_index"].between(1, 30)
    ].copy()
    df["source_family"] = "claude_2026"
    return df.loc[:, ["model_label", "repeat_index", "source_family", *Q_COLS]].reset_index(drop=True)


def load_gemini_repeat_rows_1to30() -> pd.DataFrame:
    usecols = ["source_file", "model_label", "condition_stem", "prompt_elicitation", "repeat_index", *Q_COLS]
    df = pd.read_csv(GEMINI_WIDE_CSV, usecols=lambda c: c in usecols)
    df = df.loc[
        df["source_file"].astype(str).str.startswith("prediction_literature_")
        & (df["condition_stem"] == "baseline")
        & (df["prompt_elicitation"] == "joint_reasoning")
        & (df["model_label"].isin(GEMINI_MODELS))
        & df["repeat_index"].between(1, 30)
    ].copy()
    df["source_family"] = "gemini_2026"
    return df.loc[:, ["model_label", "repeat_index", "source_family", *Q_COLS]].reset_index(drop=True)


def build_llm_summary(truth_vec: np.ndarray) -> pd.DataFrame:
    repeat_rows = pd.concat(
        [
            load_gpt_repeat_rows_1to5(),
            load_openai_repeat_rows_6to30(),
            load_claude_repeat_rows_1to30(),
            load_gemini_repeat_rows_1to30(),
        ],
        ignore_index=True,
    )
    repeat_rows[Q_COLS] = repeat_rows[Q_COLS].apply(pd.to_numeric, errors="coerce")

    summary_rows: list[dict[str, object]] = []
    for model, part in repeat_rows.groupby("model_label", sort=True):
        part = part.sort_values("repeat_index").reset_index(drop=True)
        dupes = part["repeat_index"].duplicated(keep=False)
        if dupes.any():
            dup_repeats = sorted(part.loc[dupes, "repeat_index"].unique().tolist())
            raise ValueError(f"Duplicate repeats remain for {model}: {dup_repeats}")

        expected_repeats = set(range(1, 31))
        seen_repeats = set(part["repeat_index"].tolist())
        if seen_repeats != expected_repeats:
            missing = sorted(expected_repeats - seen_repeats)
            extra = sorted(seen_repeats - expected_repeats)
            raise ValueError(f"Repeat coverage mismatch for {model}: missing={missing}, extra={extra}")

        pred_mat = part.loc[:, Q_COLS].to_numpy(dtype=float)
        mean_pred = np.nanmean(pred_mat, axis=0)
        repeat_corr = corr_rows(pred_mat, truth_vec)
        corr_mean_prediction = float(corr_rows(mean_pred[None, :], truth_vec)[0])

        summary_rows.append(
            {
                "model": model,
                "n_repeats": int(part.shape[0]),
                "min_repeat": int(part["repeat_index"].min()),
                "max_repeat": int(part["repeat_index"].max()),
                "correlation_mean_prediction": corr_mean_prediction,
                "correlation_mean_repeat": float(np.nanmean(repeat_corr)),
                "repeat_correlation_sd": float(np.nanstd(repeat_corr, ddof=1)),
                "source_families": " + ".join(sorted(part["source_family"].astype(str).unique().tolist())),
                **{q: float(mean_pred[i]) for i, q in enumerate(Q_COLS)},
            }
        )

    summary_df = pd.DataFrame(summary_rows).sort_values("correlation_mean_prediction", ascending=False).reset_index(drop=True)
    return summary_df


def build_percentile_rows(
    plot_df: pd.DataFrame,
    llm_summary: pd.DataFrame,
    null_value: float,
    ceiling_value: float,
) -> pd.DataFrame:
    percentile_rows: list[dict[str, object]] = []
    human_groups = ["Laypeople", "Experts"]
    for row in llm_summary.itertuples(index=False):
        record = {
            "label": row.model,
            "value": float(row.correlation_mean_prediction),
            "kind": "llm_model_mean30",
        }
        for group in human_groups:
            group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
            record[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= record["value"]))
        percentile_rows.append(record)

    null_record = {
        "label": "No treatment effect",
        "value": float(null_value),
        "kind": "null_baseline",
    }
    for group in human_groups:
        group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        null_record[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= null_value))
    percentile_rows.append(null_record)

    ceiling_record = {
        "label": "Estimated ceiling",
        "value": float(ceiling_value),
        "kind": "noise_ceiling",
    }
    for group in human_groups:
        group_vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        ceiling_record[f"share_{group.lower()}_below"] = float(np.mean(group_vals <= ceiling_value))
    percentile_rows.append(ceiling_record)

    out = pd.DataFrame(percentile_rows)
    out["pct_laypeople_below"] = out["share_laypeople_below"] * 100.0
    out["pct_experts_below"] = out["share_experts_below"] * 100.0
    return out.sort_values(["kind", "value"]).reset_index(drop=True)


def plot_cdf(plot_df: pd.DataFrame, llm_summary: pd.DataFrame, null_value: float, ceiling_value: float) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(8.2, 6.6), layout="constrained")
    counts = {
        group: int(plot_df.loc[plot_df["group"] == group].shape[0])
        for group in GROUP_ORDER
    }
    llm_sorted = llm_summary.sort_values("correlation_mean_prediction", ascending=True).reset_index(drop=True)

    for group in GROUP_ORDER:
        vals = plot_df.loc[plot_df["group"] == group, "value"].to_numpy(dtype=float)
        sns.ecdfplot(
            x=vals,
            stat="proportion",
            linewidth=2.5 if group != LLM_GROUP_LABEL else 2.8,
            color=GROUP_COLORS[group],
            label=group,
            ax=ax,
        )
        if group == LLM_GROUP_LABEL:
            vals_sorted = np.sort(vals)
            ys = np.arange(1, vals_sorted.size + 1, dtype=float) / vals_sorted.size
            ax.scatter(vals_sorted, ys, s=28, color=GROUP_COLORS[group], zorder=4)
            for x, y, label in zip(vals_sorted, ys, llm_sorted["model"]):
                y_nudged = min(y, 0.995)
                if str(label) == "Claude Sonnet 4.6":
                    xytext = (-6, 0)
                    ha = "right"
                else:
                    xytext = (6, 0)
                    ha = "left"
                ax.annotate(
                    str(label),
                    xy=(float(x), float(y_nudged)),
                    xytext=xytext,
                    textcoords="offset points",
                    ha=ha,
                    va="center",
                    fontsize=8.4,
                    color=GROUP_COLORS[group],
                    bbox={"boxstyle": "round,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.88},
                    zorder=5,
                    clip_on=False,
                )

    ax.axvline(null_value, color="#111111", linewidth=1.8, linestyle="-", alpha=0.95, zorder=2)
    ax.axvline(ceiling_value, color="#111111", linewidth=1.6, linestyle=":", alpha=0.95, zorder=2)

    ax.set_xlim(-0.7, 0.86)
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(np.arange(-0.7, 0.81, 0.1))
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Correlation with true treatment outcome")
    ax.set_ylabel("Cumulative share of forecasters")
    ax.grid(axis="y", color="#dddddd", linewidth=0.8)
    ax.grid(axis="x", visible=False)

    legend_items = [
        Line2D([0], [0], color=GROUP_COLORS["Laypeople"], linewidth=2.5, label=f"Laypeople (n={counts['Laypeople']})"),
        Line2D([0], [0], color=GROUP_COLORS["Experts"], linewidth=2.5, label=f"Experts (n={counts['Experts']})"),
        Line2D(
            [0],
            [0],
            color=GROUP_COLORS[LLM_GROUP_LABEL],
            linewidth=2.8,
            marker="o",
            markersize=4.5,
            label=f"LLMs (n={counts[LLM_GROUP_LABEL]} models; 30-run mean)",
        ),
        Line2D([0], [0], color="#111111", linewidth=1.8, linestyle="-", label="No-treatment-effect baseline"),
        Line2D([0], [0], color="#111111", linewidth=1.6, linestyle=":", label="Estimated ceiling"),
    ]
    ax.legend(handles=legend_items, frameon=False, loc="upper left")

    for ext, path in [("png", OUT_PNG), ("pdf", OUT_PDF)]:
        fig.savefig(path, dpi=300 if ext == "png" else None, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    truth_vec, null_value, ceiling_value = load_truth_vectors()
    human_df = load_human_plot_rows(truth_vec)
    llm_summary = build_llm_summary(truth_vec)

    llm_plot_rows = pd.DataFrame(
        {
            "group": LLM_GROUP_LABEL,
            "value": llm_summary["correlation_mean_prediction"].astype(float),
            "kind": "llm_model_mean30",
            "label": llm_summary["model"].astype(str),
        }
    )
    llm_plot_rows["group"] = pd.Categorical(llm_plot_rows["group"], categories=GROUP_ORDER, ordered=True)
    plot_df = pd.concat([human_df, llm_plot_rows], ignore_index=True)
    plot_df["group"] = pd.Categorical(plot_df["group"], categories=GROUP_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["group", "value"]).reset_index(drop=True)

    reference_df = pd.DataFrame(
        [
            {
                "label": "No treatment effect",
                "value": float(null_value),
                "kind": "null_baseline",
            },
            {
                "label": "Estimated ceiling",
                "value": float(ceiling_value),
                "kind": "noise_ceiling",
            },
        ]
    )
    percentile_df = build_percentile_rows(plot_df, llm_summary, null_value, ceiling_value)

    plot_df.to_csv(ROWS_CSV, index=False)
    llm_summary.to_csv(LLM_SUMMARY_CSV, index=False)
    reference_df.to_csv(REFERENCE_CSV, index=False)
    percentile_df.to_csv(PERCENTILES_CSV, index=False)
    plot_cdf(plot_df, llm_summary, null_value, ceiling_value)


if __name__ == "__main__":
    main()
