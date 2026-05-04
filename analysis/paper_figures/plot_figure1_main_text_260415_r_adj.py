from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
if str(ROOT / "analysis") not in sys.path:
    sys.path.insert(0, str(ROOT / "analysis"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import transforms
from matplotlib.lines import Line2D

from adjusted_correlation import load_truth_and_sem, profile_likelihood_ci_adjusted_corr


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

LLM_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_incremental_pgg_science_repeat30"
    / "incremental_pgg_science_avg_predictions.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
PAIRED_VAL_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_paired_val.csv"

OUT_STEM = "figure1_benchmark_vs_human_crowds_bar_r_adj"
ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_rows.csv"
REFERENCE_LINES_CSV = RESULTS_DIR / f"{OUT_STEM}_reference_lines.csv"
DOCUMENTATION_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

CONDITION_ORDER = ["baseline", "science_gpt41"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "Benchmark paper augmented",
}
COLORS = {
    "baseline": "#c9ced6",
    "science_gpt41": "#f2a65a",
    "Laypeople WoC": "#caa27e",
    "Experts WoC": "#8d6748",
}
HUMAN_ORDER = ["Laypeople WoC", "Experts WoC"]
MODEL_ORDER = [
    "Claude Sonnet 4.6",
    "GPT-5.1",
    "GPT-4.1 Mini",
    "GPT-4.1",
    "GPT-5 Nano",
    "GPT-5 Mini",
    "GPT-4.1 Nano",
    "Gemini 2.5 Pro",
]
Q_COLS = [f"Q{i}" for i in range(1, 21)]


def build_human_rows(truth: np.ndarray, sem_y: np.ndarray, config_ids: np.ndarray) -> pd.DataFrame:
    pred = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    pred = pred.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()

    rows: list[dict[str, object]] = []
    for source, label in [("prolific", "Laypeople WoC"), ("sspp", "Experts WoC")]:
        wide = (
            pred.loc[pred["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .reindex(config_ids)
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        mean_pred = wide.mean(axis=1).to_numpy(dtype=float) * 100.0
        fit = profile_likelihood_ci_adjusted_corr(mean_pred, truth, sem_y)
        rows.append(
            {
                "group": "human_crowd",
                "label": label,
                "condition": label,
                "value": float(fit["r_adj"]),
                "ci_low": float(fit["ci_low"]),
                "ci_high": float(fit["ci_high"]),
                "n_complete_participants": int(wide.shape[1]),
                "n_questions": int(wide.shape[0]),
                "ci_method": "profile_likelihood",
            }
        )
    return pd.DataFrame(rows)


def build_llm_rows(truth: np.ndarray, sem_y: np.ndarray) -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()

    rows: list[dict[str, object]] = []
    for _, row in avg.iterrows():
        pred_vec = row[Q_COLS].to_numpy(dtype=float)
        fit = profile_likelihood_ci_adjusted_corr(pred_vec, truth, sem_y)
        rows.append(
            {
                "group": "llm",
                "label": str(row["model"]),
                "condition": str(row["condition"]),
                "value": float(fit["r_adj"]),
                "ci_low": float(fit["ci_low"]),
                "ci_high": float(fit["ci_high"]),
                "n_runs": int(row["n_runs"]),
                "n_questions": len(Q_COLS),
                "ci_method": "profile_likelihood",
            }
        )
    out = pd.DataFrame(rows)
    out["label"] = pd.Categorical(out["label"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["label", "condition"]).reset_index(drop=True)


def build_reference_lines(control: np.ndarray, truth: np.ndarray, sem_y: np.ndarray) -> pd.DataFrame:
    no_treat = profile_likelihood_ci_adjusted_corr(control, truth, sem_y)
    return pd.DataFrame(
        [
            {
                "label": "No-treatment outcome baseline",
                "value": float(no_treat["r_adj"]),
                "color": "#111111",
                "linestyle": "--",
            },
            {
                "label": "Adjusted ceiling",
                "value": 1.0,
                "color": "#111111",
                "linestyle": ":",
            },
        ]
    )


def write_documentation(human_df: pd.DataFrame, llm_df: pd.DataFrame, refs_df: pd.DataFrame) -> None:
    rows_df = pd.concat([human_df, llm_df], ignore_index=True)
    display_rows = rows_df[["group", "label", "condition", "value", "ci_low", "ci_high"]].copy()
    for col in ["value", "ci_low", "ci_high"]:
        display_rows[col] = display_rows[col].map(lambda x: f"{float(x):.6f}")
    refs_display = refs_df[["label", "value"]].copy()
    refs_display["value"] = refs_display["value"].map(lambda x: f"{float(x):.6f}")

    doc = f"""# {OUT_STEM}

## Purpose
Adjusted-correlation Figure 1 variant for `main_text_260415`. This version replaces raw correlation with `r_adj`, following the disattenuated-correlation logic described in Section 2.3 of the supplement at `/Users/robinna/Downloads/supplement.pdf`.

## Output files
- Plot PNG: `{(PLOTS_DIR / f"{OUT_STEM}.png").relative_to(ROOT)}`
- Plot rows: `{ROWS_CSV.relative_to(ROOT)}`
- Reference lines: `{REFERENCE_LINES_CSV.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- LLM 30-run mean predictions: `{LLM_AVG_PRED_CSV.relative_to(ROOT)}`
- Human forecasts: `{HUMAN_PREDICTIONS_CSV.relative_to(ROOT)}`
- Paired validation outcomes: `{PAIRED_VAL_CSV.relative_to(ROOT)}`
- Supplementary methods reference: `/Users/robinna/Downloads/supplement.pdf`

## Construction
1. Load the 20 paired validation outcomes and treatment-effect uncertainty from `df_paired_val.csv` and `adjusted_correlation.load_truth_and_sem()`.
2. For each human WoC bar:
   - keep complete forecasters only (`n_predictions_made == 20`)
   - average predictions within source (`prolific` or `sspp`) across participants
   - fit the latent-correlation model `profile_likelihood_ci_adjusted_corr(mean_prediction, truth, sem_y)`
3. For each LLM bar:
   - use the 30-run mean prediction vector from `incremental_pgg_science_avg_predictions.csv`
   - fit the same latent-correlation model against the 20 true outcomes with `sem_y`
4. Reference lines:
   - `No-treatment outcome baseline` = adjusted correlation between observed untreated outcome and observed treated outcome
   - `Adjusted ceiling` = `1.0`, because once outcome uncertainty is disattenuated, the raw attenuation ceiling at `0.7765` is no longer the right reference scale
5. Error bars:
   - `95%` profile-likelihood confidence intervals for the latent correlation parameter `rho`
   - this is closer to the supplement than bootstrap-over-experiments, because the interval comes from the same measurement-error model as the point estimate

## Notes
- This figure uses `r_adj`, not raw `Corr(y_true, y_pred)`.
- The point estimate is the latent correlation after adjusting for sampling uncertainty in the true treatment outcomes.
- Because this metric already corrects the outcome-side attenuation, the old raw noise ceiling line at `0.7765` should not be carried over.

## Values used in the plot
### Bars
{display_rows.to_markdown(index=False)}

### Reference lines
{refs_display.to_markdown(index=False)}
"""
    DOCUMENTATION_MD.write_text(doc)


def plot_figure(human_df: pd.DataFrame, llm_df: pd.DataFrame, refs_df: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(13.6, 7.2))

    model_order = llm_df["label"].cat.categories.tolist()
    human_x = np.array([0.0, 1.0])
    model_x = np.arange(len(model_order), dtype=float) + 2.35
    width = 0.32

    human_lookup = human_df.set_index("label")
    for idx, label in enumerate(HUMAN_ORDER):
        y = float(human_lookup.loc[label, "value"])
        ci_low = float(human_lookup.loc[label, "ci_low"])
        ci_high = float(human_lookup.loc[label, "ci_high"])
        ax.bar(
            human_x[idx],
            y,
            width=0.62,
            color=COLORS[label],
            edgecolor="#4b5563",
            linewidth=0.8,
            zorder=3,
        )
        ax.errorbar(
            human_x[idx],
            y,
            yerr=[[y - ci_low], [ci_high - y]],
            fmt="none",
            ecolor="#374151",
            elinewidth=1.2,
            capsize=3,
            zorder=4,
        )

    llm_lookup = llm_df.set_index(["label", "condition"])
    for idx, model in enumerate(model_order):
        for offset, condition in [(-width / 2, "baseline"), (width / 2, "science_gpt41")]:
            y = float(llm_lookup.loc[(model, condition), "value"])
            ci_low = float(llm_lookup.loc[(model, condition), "ci_low"])
            ci_high = float(llm_lookup.loc[(model, condition), "ci_high"])
            ax.bar(
                model_x[idx] + offset,
                y,
                width=width,
                color=COLORS[condition],
                edgecolor="#4b5563",
                linewidth=0.8,
                zorder=3,
            )
            ax.errorbar(
                model_x[idx] + offset,
                y,
                yerr=[[y - ci_low], [ci_high - y]],
                fmt="none",
                ecolor="#374151",
                elinewidth=1.1,
                capsize=2.5,
                zorder=4,
            )

    ax.axvline(1.82, color="#d1d5db", linewidth=1.2, zorder=1)

    for _, row in refs_df.iterrows():
        ax.axhline(
            float(row["value"]),
            color=str(row["color"]),
            linestyle=str(row["linestyle"]),
            linewidth=1.4,
            zorder=1,
        )

    blend = transforms.blended_transform_factory(ax.transAxes, ax.transData)
    no_treat = refs_df.loc[refs_df["label"] == "No-treatment outcome baseline"].iloc[0]
    ceiling = refs_df.loc[refs_df["label"] == "Adjusted ceiling"].iloc[0]
    ax.text(
        0.995,
        float(no_treat["value"]) - 0.01,
        f"{no_treat['label']} ({float(no_treat['value']):.3f})",
        transform=blend,
        ha="right",
        va="top",
        fontsize=10.2,
        color="#111111",
        bbox={"boxstyle": "round,pad=0.12", "facecolor": (1, 1, 1, 0.82), "edgecolor": "none"},
    )
    ax.text(
        0.995,
        float(ceiling["value"]) - 0.01,
        f"{ceiling['label']} ({float(ceiling['value']):.3f})",
        transform=blend,
        ha="right",
        va="top",
        fontsize=10.2,
        color="#111111",
        bbox={"boxstyle": "round,pad=0.12", "facecolor": (1, 1, 1, 0.82), "edgecolor": "none"},
    )

    xticks = list(human_x) + list(model_x)
    xticklabels = HUMAN_ORDER + model_order
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45, ha="right")
    ax.set_xlim(-0.8, model_x[-1] + 0.9)
    ax.set_ylim(0.0, 1.05)
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_ylabel(r"$r_{\mathrm{adj}}$")
    ax.set_xlabel("")
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )

    fig.subplots_adjust(bottom=0.20, top=0.84, right=0.98)
    fig.savefig(PLOTS_DIR / f"{OUT_STEM}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    truth, control, sem_y = load_truth_and_sem()
    config_ids = pd.read_csv(PAIRED_VAL_CSV).sort_values("CONFIG_configId")["CONFIG_configId"].to_numpy(dtype=int)

    human_df = build_human_rows(truth, sem_y, config_ids)
    llm_df = build_llm_rows(truth, sem_y)
    refs_df = build_reference_lines(control, truth, sem_y)

    pd.concat([human_df, llm_df], ignore_index=True).to_csv(ROWS_CSV, index=False)
    refs_df.to_csv(REFERENCE_LINES_CSV, index=False)
    write_documentation(human_df, llm_df, refs_df)
    plot_figure(human_df, llm_df, refs_df)


if __name__ == "__main__":
    main()
