from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import transforms
from matplotlib.lines import Line2D


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427"

LLM_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_incremental_pgg_science_repeat30"
    / "incremental_pgg_science_avg_predictions.csv"
)
HUMAN_PREDICTIONS_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "prediction_survey.csv"
VALIDATION_CSV = ROOT / "input" / "pgg_CONFIGmerged_validation.csv"
NO_AUG_BENCHMARKS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "no_augmentation_model_comparison"
    / "validation_no_augmentation_model_comparison_benchmarks.csv"
)

OUT_STEM = "figure2_benchmark_vs_human_crowds_bar"
PLOT_ROWS_CSV = RESULTS_DIR / f"{OUT_STEM}_rows.csv"
REFERENCE_LINES_CSV = RESULTS_DIR / f"{OUT_STEM}_reference_lines.csv"
PAIR_SIGNIFICANCE_CSV = RESULTS_DIR / f"{OUT_STEM}_pair_significance.csv"
DOCUMENTATION_MD = RESULTS_DIR / f"{OUT_STEM}_documentation.md"

CONDITION_ORDER = ["baseline", "science_gpt41"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "Benchmark paper augmented",
}
COLORS = {
    "baseline": "#c9ced6",
    "science_gpt41": "#f2a65a",
    "Laypeople wisdom-of-the-crowd": "#caa27e",
    "Experts wisdom-of-the-crowd": "#8d6748",
}
HUMAN_ORDER = ["Laypeople wisdom-of-the-crowd", "Experts wisdom-of-the-crowd"]
MODEL_ORDER = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]
BOOTSTRAP_N = 10000
BOOTSTRAP_SEED = 260427
PAIR_BOOTSTRAP_N = 50000
Q_COLS = [f"Q{i}" for i in range(1, 21)]


def corr(pred: np.ndarray, truth: np.ndarray) -> float:
    pred = np.asarray(pred, dtype=float)
    truth = np.asarray(truth, dtype=float)
    mask = ~np.isnan(pred) & ~np.isnan(truth)
    pred = pred[mask]
    truth = truth[mask]
    pred_centered = pred - pred.mean()
    truth_centered = truth - truth.mean()
    denom = np.sqrt((pred_centered**2).sum() * (truth_centered**2).sum())
    if denom <= 0:
        return float("nan")
    return float((pred_centered @ truth_centered) / denom)


def load_truth() -> pd.Series:
    return (
        pd.read_csv(VALIDATION_CSV)
        .sort_values("CONFIG_configId")
        .set_index("CONFIG_configId")["efficiency_p"]
    )


def bootstrap_experiment_corr_ci(
    pred_vec: np.ndarray,
    truth: np.ndarray,
    rng: np.random.Generator,
) -> tuple[float, float]:
    n_experiments = pred_vec.shape[0]
    corrs = np.empty(BOOTSTRAP_N, dtype=float)
    for i in range(BOOTSTRAP_N):
        sample_idx = rng.integers(0, n_experiments, size=n_experiments)
        corrs[i] = corr(pred_vec[sample_idx], truth[sample_idx])
    return float(np.quantile(corrs, 0.025)), float(np.quantile(corrs, 0.975))


def load_no_treatment_reference() -> float:
    validation = pd.read_csv(VALIDATION_CSV).sort_values("CONFIG_configId")
    return corr(
        validation["efficiency_np"].to_numpy(dtype=float) * 100.0,
        validation["efficiency_p"].to_numpy(dtype=float) * 100.0,
    )


def load_noise_ceiling() -> float:
    benchmarks = pd.read_csv(NO_AUG_BENCHMARKS_CSV)
    return float(benchmarks.loc[benchmarks["benchmark"] == "Noise ceiling", "correlation"].iloc[0])


def build_human_rows() -> pd.DataFrame:
    pred = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    pred = pred.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth = load_truth()
    rng = np.random.default_rng(BOOTSTRAP_SEED)

    rows: list[dict[str, object]] = []
    for source, label in [("prolific", HUMAN_ORDER[0]), ("sspp", HUMAN_ORDER[1])]:
        wide = (
            pred.loc[pred["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .sort_index()
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        mean_pred = wide.mean(axis=1).to_numpy(dtype=float) * 100.0
        aligned_truth = truth.loc[wide.index].to_numpy(dtype=float) * 100.0
        ci_low, ci_high = bootstrap_experiment_corr_ci(mean_pred, aligned_truth, rng)
        rows.append(
            {
                "group": "human_crowd",
                "label": label,
                "condition": label,
                "value": corr(mean_pred, aligned_truth),
                "ci_low": ci_low,
                "ci_high": ci_high,
                "n_complete_participants": int(wide.shape[1]),
                "n_questions": int(wide.shape[0]),
                "bootstrap_n": BOOTSTRAP_N,
            }
        )

    out = pd.DataFrame(rows)
    out["label"] = pd.Categorical(out["label"], categories=HUMAN_ORDER, ordered=True)
    return out.sort_values("label").reset_index(drop=True)


def build_llm_rows() -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    truth = load_truth().to_numpy(dtype=float) * 100.0
    rng = np.random.default_rng(BOOTSTRAP_SEED + 1)

    rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        for condition in CONDITION_ORDER:
            row = avg.loc[(avg["model"] == model) & (avg["condition"] == condition)]
            if row.empty:
                continue
            row = row.iloc[0]
            pred_vec = row[Q_COLS].to_numpy(dtype=float)
            ci_low, ci_high = bootstrap_experiment_corr_ci(pred_vec, truth, rng)
            rows.append(
                {
                    "group": "llm",
                    "label": model,
                    "condition": condition,
                    "value": corr(pred_vec, truth),
                    "ci_low": ci_low,
                    "ci_high": ci_high,
                    "n_runs": int(row["n_runs"]),
                    "n_questions": len(Q_COLS),
                    "bootstrap_n": BOOTSTRAP_N,
                }
            )

    out = pd.DataFrame(rows)
    out["label"] = pd.Categorical(out["label"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["label", "condition"]).reset_index(drop=True)


def build_llm_pair_significance() -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    truth = load_truth().to_numpy(dtype=float) * 100.0
    rng = np.random.default_rng(BOOTSTRAP_SEED + 2)

    rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        base = avg.loc[(avg["model"] == model) & (avg["condition"] == "baseline"), Q_COLS]
        aug = avg.loc[(avg["model"] == model) & (avg["condition"] == "science_gpt41"), Q_COLS]
        if base.empty or aug.empty:
            continue
        base_vec = base.iloc[0].to_numpy(dtype=float)
        aug_vec = aug.iloc[0].to_numpy(dtype=float)
        delta = corr(aug_vec, truth) - corr(base_vec, truth)
        delta_boot = np.empty(PAIR_BOOTSTRAP_N, dtype=float)
        for i in range(PAIR_BOOTSTRAP_N):
            sample_idx = rng.integers(0, len(truth), size=len(truth))
            truth_s = truth[sample_idx]
            delta_boot[i] = corr(aug_vec[sample_idx], truth_s) - corr(base_vec[sample_idx], truth_s)

        ci95_low, ci95_high = np.quantile(delta_boot, [0.025, 0.975])
        ci99_low, ci99_high = np.quantile(delta_boot, [0.005, 0.995])
        ci999_low, ci999_high = np.quantile(delta_boot, [0.0005, 0.9995])
        p_two = float(2.0 * min((delta_boot <= 0).mean(), (delta_boot >= 0).mean()))
        if ci999_low > 0 or ci999_high < 0:
            sig = "***"
        elif ci99_low > 0 or ci99_high < 0:
            sig = "**"
        elif ci95_low > 0 or ci95_high < 0:
            sig = "*"
        else:
            sig = "n.s."

        rows.append(
            {
                "model": model,
                "baseline_corr": float(corr(base_vec, truth)),
                "benchmark_corr": float(corr(aug_vec, truth)),
                "delta_corr": float(delta),
                "delta_ci95_low": float(ci95_low),
                "delta_ci95_high": float(ci95_high),
                "delta_ci99_low": float(ci99_low),
                "delta_ci99_high": float(ci99_high),
                "delta_ci999_low": float(ci999_low),
                "delta_ci999_high": float(ci999_high),
                "p_bootstrap_two_sided": p_two,
                "sig_label": sig,
                "n_boot": PAIR_BOOTSTRAP_N,
            }
        )

    return pd.DataFrame(rows)


def build_reference_lines() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "label": "No-treatment outcome baseline",
                "value": load_no_treatment_reference(),
                "color": "#111111",
                "linestyle": "--",
            },
            {
                "label": "Noise ceiling",
                "value": load_noise_ceiling(),
                "color": "#111111",
                "linestyle": ":",
            },
        ]
    )


def write_documentation(
    human_df: pd.DataFrame,
    llm_df: pd.DataFrame,
    refs_df: pd.DataFrame,
    pair_sig_df: pd.DataFrame,
) -> None:
    rows_df = pd.concat([human_df, llm_df], ignore_index=True)
    display_rows = rows_df[["group", "label", "condition", "value", "ci_low", "ci_high"]].copy()
    for col in ["value", "ci_low", "ci_high"]:
        display_rows[col] = display_rows[col].map(lambda x: f"{float(x):.6f}")

    refs_display = refs_df[["label", "value"]].copy()
    refs_display["value"] = refs_display["value"].map(lambda x: f"{float(x):.6f}")

    pair_display = pair_sig_df.copy()
    for col in [
        "baseline_corr",
        "benchmark_corr",
        "delta_corr",
        "delta_ci95_low",
        "delta_ci95_high",
        "delta_ci99_low",
        "delta_ci99_high",
        "delta_ci999_low",
        "delta_ci999_high",
        "p_bootstrap_two_sided",
    ]:
        pair_display[col] = pair_display[col].map(lambda x: f"{float(x):.6f}")

    doc = f"""# {OUT_STEM}

## Purpose
Figure 2 for `main_text_260427`. This plot compares human wisdom-of-the-crowd performance with three LLM baselines and their benchmark-paper-augmented counterparts on the same Pearson-correlation scale across the 20 validation questions.

## Inheritance
- Semantic figure ID: `benchmark_vs_human_crowds_bar`
- Adapted from `main_text_260415` Figure 1 into the `main_text_260427` Figure 2 slot
- Parent assets:
  - Plot PNG: `plots/paper/main_text_260415/figure1_benchmark_vs_human_crowds_bar.png`
  - Rows CSV: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_rows.csv`
  - Documentation: `results/paper/main_text_figures_260415/figure1_benchmark_vs_human_crowds_bar_documentation.md`

## Output files
- Plot PNG: `{(PLOTS_DIR / f"{OUT_STEM}.png").relative_to(ROOT)}`
- Plot rows: `{PLOT_ROWS_CSV.relative_to(ROOT)}`
- Reference lines: `{REFERENCE_LINES_CSV.relative_to(ROOT)}`
- Pair significance: `{PAIR_SIGNIFICANCE_CSV.relative_to(ROOT)}`
- Documentation: `{DOCUMENTATION_MD.relative_to(ROOT)}`
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- LLM 30-run mean predictions: `{LLM_AVG_PRED_CSV.relative_to(ROOT)}`
- Human forecasts: `{HUMAN_PREDICTIONS_CSV.relative_to(ROOT)}`
- Validation outcomes: `{VALIDATION_CSV.relative_to(ROOT)}`
- Noise ceiling benchmark table: `{NO_AUG_BENCHMARKS_CSV.relative_to(ROOT)}`

## Estimand
- Human wisdom-of-the-crowd bars: `corr(mean human prediction across complete forecasters, true outcome)`
- LLM bars: `corr(mean prediction across 30 runs, true outcome)`

## Construction
1. Load the 20 validation outcomes from `efficiency_p` in `{VALIDATION_CSV.name}` and sort by `CONFIG_configId`.
2. Build the two human wisdom-of-the-crowd bars from `{HUMAN_PREDICTIONS_CSV.name}`:
   - keep rows with `prediction` between `-0.2` and `1.2`
   - keep respondents with `n_predictions_made == 20`
   - split by source: `prolific` = laypeople, `sspp` = experts
   - pivot to `CONFIG_configId x playerID`
   - keep only complete participants with non-missing predictions for all 20 questions
   - average predictions across participants within source for each question
   - compute Pearson correlation between that mean prediction vector and the true outcome vector
3. Build the LLM bars from `{LLM_AVG_PRED_CSV.name}`:
   - use only `condition in ["baseline", "science_gpt41"]`
   - keep only the three displayed models: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
   - each row already contains the mean prediction vector across 30 runs for one model-condition pair
   - compute Pearson correlation between the 30-run mean prediction vector (`Q1`-`Q20`) and the true outcome vector
4. Add two vertical reference lines:
   - `No-treatment outcome baseline` = Pearson correlation between `efficiency_np` and `efficiency_p` from `{VALIDATION_CSV.name}`
   - `Noise ceiling` = the `Noise ceiling` correlation from `{NO_AUG_BENCHMARKS_CSV.name}`
5. Plot layout:
   - horizontal orientation relative to the `260415` parent
   - first two rows: `Laypeople wisdom-of-the-crowd`, `Experts wisdom-of-the-crowd`
   - next three rows: `Claude Sonnet 4.6`, `GPT-4.1`, `Gemini 2.5 Pro`
   - within each LLM row, show `baseline` and `science_gpt41`
6. Error bars:
   - bootstrap the 20 experiments with replacement
   - recompute the plotted correlation on each bootstrap sample
   - interval shown: percentile bootstrap 95% CI (`2.5%`, `97.5%`)
7. Pair significance:
   - only for LLM baseline vs benchmark-paper pairs
   - compute paired bootstrap resamples over the same 20 experiments for both bars
   - draw significance stars next to rows where the paired bootstrap CI for `corr_augmented - corr_baseline` excludes `0`
   - the explanatory threshold text is intentionally omitted from the figure and belongs in the manuscript caption

## Notes
- This figure intentionally drops the five omitted models from the `260415` parent to reduce visual density in the main text.
- The starred LLM comparisons are still computed from the full paired bootstrap distribution even though the threshold key is not printed in-panel.

## Values used in the plot
### Bars
{display_rows.to_markdown(index=False)}

### Reference lines
{refs_display.to_markdown(index=False)}

### Pair Significance
{pair_display.to_markdown(index=False)}
"""
    DOCUMENTATION_MD.write_text(doc)


def plot_figure(
    human_df: pd.DataFrame,
    llm_df: pd.DataFrame,
    refs_df: pd.DataFrame,
    pair_sig_df: pd.DataFrame,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(8.6, 5.0))

    human_y = np.array([0.0, 0.9])
    llm_y = np.array([2.0, 3.0, 4.0])
    llm_offsets = {"baseline": -0.18, "science_gpt41": 0.18}

    human_lookup = human_df.set_index("label")
    for idx, label in enumerate(HUMAN_ORDER):
        x = float(human_lookup.loc[label, "value"])
        ci_low = float(human_lookup.loc[label, "ci_low"])
        ci_high = float(human_lookup.loc[label, "ci_high"])
        ax.barh(
            human_y[idx],
            x,
            height=0.48,
            color=COLORS[label],
            edgecolor="#4b5563",
            linewidth=0.8,
            zorder=3,
        )
        ax.errorbar(
            x,
            human_y[idx],
            xerr=[[x - ci_low], [ci_high - x]],
            fmt="none",
            ecolor=(55 / 255, 65 / 255, 81 / 255, 0.35),
            elinewidth=1.15,
            capsize=3,
            zorder=4,
        )

    llm_lookup = llm_df.set_index(["label", "condition"])
    for idx, model in enumerate(MODEL_ORDER):
        for condition in CONDITION_ORDER:
            x = float(llm_lookup.loc[(model, condition), "value"])
            ci_low = float(llm_lookup.loc[(model, condition), "ci_low"])
            ci_high = float(llm_lookup.loc[(model, condition), "ci_high"])
            y = llm_y[idx] + llm_offsets[condition]
            ax.barh(
                y,
                x,
                height=0.28,
                color=COLORS[condition],
                edgecolor="#4b5563",
                linewidth=0.8,
                zorder=3,
            )
            ax.errorbar(
                x,
                y,
                xerr=[[x - ci_low], [ci_high - x]],
                fmt="none",
                ecolor=(55 / 255, 65 / 255, 81 / 255, 0.32),
                elinewidth=1.05,
                capsize=2.4,
                zorder=4,
            )

    for _, row in refs_df.iterrows():
        ax.axvline(
            float(row["value"]),
            color=str(row["color"]),
            linestyle=str(row["linestyle"]),
            linewidth=1.35,
            zorder=1,
        )

    sig_lookup = pair_sig_df.set_index("model")
    for idx, model in enumerate(MODEL_ORDER):
        if model not in sig_lookup.index:
            continue
        sig = str(sig_lookup.loc[model, "sig_label"])
        if sig == "n.s.":
            continue
        base_ci = float(llm_lookup.loc[(model, "baseline"), "ci_high"])
        aug_ci = float(llm_lookup.loc[(model, "science_gpt41"), "ci_high"])
        x0 = max(base_ci, aug_ci) + 0.014
        x1 = x0 + 0.014
        y0 = llm_y[idx] + llm_offsets["baseline"]
        y1 = llm_y[idx] + llm_offsets["science_gpt41"]
        ax.plot([x0, x1, x1, x0], [y0, y0, y1, y1], color="#4b5563", linewidth=1.05, zorder=5)
        ax.text(
            x1 + 0.012,
            (y0 + y1) / 2.0,
            sig,
            ha="left",
            va="center",
            fontsize=11.5,
            color="#374151",
            zorder=6,
        )

    blend = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    ref_label_specs = {
        "No-treatment outcome baseline": {"x_offset": -0.012, "ha": "right"},
        "Noise ceiling": {"x_offset": 0.012, "ha": "left"},
    }
    for _, row in refs_df.iterrows():
        spec = ref_label_specs[str(row["label"])]
        ax.text(
            float(row["value"]) + float(spec["x_offset"]),
            1.005,
            f"{row['label']} ({float(row['value']):.3f})",
            transform=blend,
            ha=str(spec["ha"]),
            va="bottom",
            fontsize=8.8,
            color="#111111",
            bbox={"boxstyle": "round,pad=0.16", "facecolor": (1, 1, 1, 0.88), "edgecolor": "none"},
        )

    legend_items = [
        Line2D([0], [0], color=COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
    ]
    fig.legend(
        handles=legend_items,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.56, 0.985),
        ncol=2,
        columnspacing=1.4,
        handlelength=2.0,
        handletextpad=0.6,
        fontsize=9.8,
        borderaxespad=0.0,
    )

    ax.set_xlim(0.0, 1.02)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel(r"Correlation coefficient with the true outcome ($r$)")
    ax.set_yticks(
        list(human_y) + list(llm_y),
        [
            "Laypeople WoC",
            "Experts WoC",
            "Claude Sonnet 4.6",
            "GPT-4.1",
            "Gemini 2.5 Pro",
        ],
    )
    ax.invert_yaxis()
    ax.set_ylim(4.55, -0.55)
    ax.tick_params(axis="y", pad=5)
    ax.grid(False)
    sns.despine(ax=ax, left=False, bottom=False)

    fig.subplots_adjust(left=0.18, right=0.985, top=0.87, bottom=0.16)
    fig.savefig(PLOTS_DIR / f"{OUT_STEM}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    human_df = build_human_rows()
    llm_df = build_llm_rows()
    pair_sig_df = build_llm_pair_significance()
    refs_df = build_reference_lines()

    pd.concat([human_df, llm_df], ignore_index=True).to_csv(PLOT_ROWS_CSV, index=False)
    refs_df.to_csv(REFERENCE_LINES_CSV, index=False)
    pair_sig_df.to_csv(PAIR_SIGNIFICANCE_CSV, index=False)
    write_documentation(human_df, llm_df, refs_df, pair_sig_df)
    plot_figure(human_df, llm_df, refs_df, pair_sig_df)


if __name__ == "__main__":
    main()
