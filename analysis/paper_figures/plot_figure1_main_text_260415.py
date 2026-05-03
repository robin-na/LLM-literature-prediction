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


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260415"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260415"

LLM_AVG_PRED_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_incremental_pgg_science_repeat30"
    / "incremental_pgg_science_avg_predictions.csv"
)
LLM_REPEAT_ROWS_CSV = (
    ROOT
    / "results"
    / "validation"
    / "literature_incremental_pgg_science_repeat30"
    / "incremental_pgg_science_repeat_rows.csv"
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

OUT_STEM = "figure1_benchmark_vs_human_crowds_bar"
EXPERIMENT_OUT_STEM = "figure1_benchmark_vs_human_crowds_bar_experiment_bootstrap"
PAIR_SIGNIFICANCE_CSV = RESULTS_DIR / f"{OUT_STEM}_pair_significance.csv"

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
BOOTSTRAP_N = 10000
BOOTSTRAP_SEED = 260415
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


def bootstrap_corr_ci(pred_matrix: np.ndarray, truth: np.ndarray, rng: np.random.Generator) -> tuple[float, float]:
    n_units = pred_matrix.shape[0]
    corrs = np.empty(BOOTSTRAP_N, dtype=float)
    for i in range(BOOTSTRAP_N):
        sample_idx = rng.integers(0, n_units, size=n_units)
        mean_pred = pred_matrix[sample_idx].mean(axis=0)
        corrs[i] = corr(mean_pred, truth)
    return float(np.quantile(corrs, 0.025)), float(np.quantile(corrs, 0.975))


def bootstrap_experiment_corr_ci(pred_vec: np.ndarray, truth: np.ndarray, rng: np.random.Generator) -> tuple[float, float]:
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
    for source, label in [("prolific", "Laypeople wisdom-of-the-crowd"), ("sspp", "Experts wisdom-of-the-crowd")]:
        wide = (
            pred.loc[pred["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .sort_index()
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        participant_matrix = wide.to_numpy(dtype=float).T * 100.0
        mean_pred = participant_matrix.mean(axis=0)
        aligned_truth = truth.loc[wide.index].to_numpy(dtype=float) * 100.0
        ci_low, ci_high = bootstrap_corr_ci(participant_matrix, aligned_truth, rng)
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
    return pd.DataFrame(rows)


def build_llm_rows() -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    repeat_rows = pd.read_csv(LLM_REPEAT_ROWS_CSV)
    repeat_rows = repeat_rows.loc[
        repeat_rows["condition"].isin(CONDITION_ORDER) & repeat_rows["model"].isin(MODEL_ORDER)
    ].copy()
    truth = load_truth()
    aligned_truth = truth.to_numpy(dtype=float) * 100.0
    rng = np.random.default_rng(BOOTSTRAP_SEED + 1)

    rows: list[dict[str, object]] = []
    for _, row in avg.iterrows():
        pred_vec = row[Q_COLS].to_numpy(dtype=float)
        repeat_block = repeat_rows.loc[
            (repeat_rows["model"] == row["model"]) & (repeat_rows["condition"] == row["condition"]),
            Q_COLS,
        ].to_numpy(dtype=float)
        ci_low, ci_high = bootstrap_corr_ci(repeat_block, aligned_truth, rng)
        rows.append(
            {
                "group": "llm",
                "label": str(row["model"]),
                "condition": str(row["condition"]),
                "value": corr(pred_vec, aligned_truth),
                "ci_low": ci_low,
                "ci_high": ci_high,
                "n_runs": int(row["n_runs"]),
                "bootstrap_n": BOOTSTRAP_N,
            }
        )
    out = pd.DataFrame(rows)
    out["label"] = pd.Categorical(out["label"], categories=MODEL_ORDER, ordered=True)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["label", "condition"]).reset_index(drop=True)


def build_human_rows_experiment_bootstrap() -> pd.DataFrame:
    pred = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    pred = pred.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()
    truth = load_truth()
    rng = np.random.default_rng(BOOTSTRAP_SEED + 2)

    rows: list[dict[str, object]] = []
    for source, label in [("prolific", "Laypeople wisdom-of-the-crowd"), ("sspp", "Experts wisdom-of-the-crowd")]:
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
    return pd.DataFrame(rows)


def build_llm_rows_experiment_bootstrap() -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    truth = load_truth()
    aligned_truth = truth.to_numpy(dtype=float) * 100.0
    rng = np.random.default_rng(BOOTSTRAP_SEED + 3)

    rows: list[dict[str, object]] = []
    for _, row in avg.iterrows():
        pred_vec = row[Q_COLS].to_numpy(dtype=float)
        ci_low, ci_high = bootstrap_experiment_corr_ci(pred_vec, aligned_truth, rng)
        rows.append(
            {
                "group": "llm",
                "label": str(row["model"]),
                "condition": str(row["condition"]),
                "value": corr(pred_vec, aligned_truth),
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


def build_llm_pair_significance_experiment_bootstrap() -> pd.DataFrame:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    truth = load_truth().to_numpy(dtype=float) * 100.0
    rng = np.random.default_rng(BOOTSTRAP_SEED + 4)

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
    out_stem: str,
    human_df: pd.DataFrame,
    llm_df: pd.DataFrame,
    refs_df: pd.DataFrame,
    ci_description: list[str],
    pair_sig_df: pd.DataFrame | None = None,
) -> None:
    rows_df = pd.concat([human_df, llm_df], ignore_index=True)
    display_rows = rows_df[["group", "label", "condition", "value", "ci_low", "ci_high"]].copy()
    for col in ["value", "ci_low", "ci_high"]:
        display_rows[col] = display_rows[col].map(lambda x: f"{float(x):.6f}")
    refs_display = refs_df[["label", "value"]].copy()
    refs_display["value"] = refs_display["value"].map(lambda x: f"{float(x):.6f}")
    plot_rows_csv = RESULTS_DIR / f"{out_stem}_rows.csv"
    reference_lines_csv = RESULTS_DIR / f"{out_stem}_reference_lines.csv"
    documentation_md = RESULTS_DIR / f"{out_stem}_documentation.md"
    ci_bullets = "\n".join([f"   - {line}" for line in ci_description])

    doc = f"""# {out_stem}

## Purpose
Figure 1 for `main_text_260415`. This plot compares human wisdom-of-the-crowd bars with LLM baseline and benchmark-paper-augmented bars on the same scale: Pearson correlation with the true treatment outcome across the 20 validation questions.

## Output files
- Plot PNG: `{(PLOTS_DIR / f"{out_stem}.png").relative_to(ROOT)}`
- Plot rows: `{plot_rows_csv.relative_to(ROOT)}`
- Reference lines: `{reference_lines_csv.relative_to(ROOT)}`
{"- Pair significance: `" + str(PAIR_SIGNIFICANCE_CSV.relative_to(ROOT)) + "`" if pair_sig_df is not None and out_stem == OUT_STEM else ""}
- Script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- LLM 30-run mean predictions: `{LLM_AVG_PRED_CSV.relative_to(ROOT)}`
- LLM repeat-level predictions: `{LLM_REPEAT_ROWS_CSV.relative_to(ROOT)}`
- Human forecasts: `{HUMAN_PREDICTIONS_CSV.relative_to(ROOT)}`
- Validation outcomes: `{VALIDATION_CSV.relative_to(ROOT)}`
- Noise ceiling benchmark table: `{NO_AUG_BENCHMARKS_CSV.relative_to(ROOT)}`

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
   - keep only the 8 displayed models: Claude Sonnet 4.6, GPT-5.1, GPT-4.1 Mini, GPT-4.1, GPT-5 Nano, GPT-5 Mini, GPT-4.1 Nano, Gemini 2.5 Pro
   - each row already contains the mean prediction vector across 30 runs for one model-condition pair
   - compute Pearson correlation between the 30-run mean prediction vector (`Q1`-`Q20`) and the true outcome vector
4. Add two horizontal reference lines:
   - `No-treatment outcome baseline` = Pearson correlation between `efficiency_np` and `efficiency_p` from `{VALIDATION_CSV.name}`
   - `Noise ceiling` = the `Noise ceiling` correlation from `{NO_AUG_BENCHMARKS_CSV.name}`
5. Plot order:
   - first two bars: `Laypeople wisdom-of-the-crowd`, `Experts wisdom-of-the-crowd`
   - then the 8 LLMs in the fixed presentation order used in the figure
   - within each model, show `baseline` and `science_gpt41`
6. Error bars:
{ci_bullets}
   - interval shown: percentile bootstrap 95% CI (`2.5%`, `97.5%`)
7. Pair significance:
   - only for LLM baseline vs benchmark-paper pairs
   - compute paired bootstrap resamples over the same 20 experiments for both bars
   - significance stars reflect whether the paired bootstrap CI for `corr_augmented - corr_baseline` excludes `0`
   - `*` = 95% CI excludes 0, `**` = 99% CI excludes 0, `***` = 99.9% CI excludes 0

## Notes
- LLM estimand: `corr(mean across 30 runs, truth)`. This is **not** the mean of per-run correlations.
- Human wisdom-of-the-crowd estimand: `corr(mean across complete human forecasters, truth)`.
- Error bars are percentile bootstrap 95% CIs on the plotted estimand itself.

## Values used in the plot
### Bars
{display_rows.to_markdown(index=False)}

### Reference lines
{refs_display.to_markdown(index=False)}
"""
    if pair_sig_df is not None and not pair_sig_df.empty:
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
        doc += f"\n### Pair Significance\n{pair_display.to_markdown(index=False)}\n"
    documentation_md.write_text(doc)


def plot_figure(
    out_stem: str,
    human_df: pd.DataFrame,
    llm_df: pd.DataFrame,
    refs_df: pd.DataFrame,
    pair_sig_df: pd.DataFrame | None = None,
) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(13.6, 7.6))

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
            ecolor=(55 / 255, 65 / 255, 81 / 255, 0.35),
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
                ecolor=(55 / 255, 65 / 255, 81 / 255, 0.35),
                elinewidth=1.1,
                capsize=2.5,
                zorder=4,
            )

    if pair_sig_df is not None and not pair_sig_df.empty:
        sig_lookup = pair_sig_df.set_index("model")
        for idx, model in enumerate(model_order):
            if model not in sig_lookup.index:
                continue
            sig = str(sig_lookup.loc[model, "sig_label"])
            if sig == "n.s.":
                continue
            base_y = float(llm_lookup.loc[(model, "baseline"), "ci_high"])
            aug_y = float(llm_lookup.loc[(model, "science_gpt41"), "ci_high"])
            y = max(base_y, aug_y) + 0.018
            x0 = model_x[idx] - width / 2
            x1 = model_x[idx] + width / 2
            h = 0.012
            ax.plot([x0, x0, x1, x1], [y - h, y, y, y - h], color="#4b5563", linewidth=1.1, zorder=5)
            ax.text(
                (x0 + x1) / 2.0,
                y + 0.006,
                sig,
                ha="center",
                va="bottom",
                fontsize=11.5,
                color="#374151",
                zorder=6,
                bbox={"boxstyle": "round,pad=0.06", "facecolor": (1, 1, 1, 0.72), "edgecolor": "none"},
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
    ceiling = refs_df.loc[refs_df["label"] == "Noise ceiling"].iloc[0]
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
        float(ceiling["value"]) + 0.01,
        f"{ceiling['label']} ({float(ceiling['value']):.3f})",
        transform=blend,
        ha="right",
        va="bottom",
        fontsize=10.2,
        color="#111111",
        bbox={"boxstyle": "round,pad=0.12", "facecolor": (1, 1, 1, 0.82), "edgecolor": "none"},
    )

    xticks = list(human_x) + list(model_x)
    human_ticklabels = [label.replace(" wisdom-of-the-crowd", "\nwisdom-of-the-crowd") for label in HUMAN_ORDER]
    xticklabels = human_ticklabels + model_order
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45, ha="right")
    ax.set_xlim(-0.8, model_x[-1] + 0.9)
    ax.set_ylim(0.0, 1.08)
    ax.set_yticks(np.arange(0.0, 1.01, 0.1))
    ax.set_ylabel(r"$\mathrm{Corr}(y_{\mathrm{true}},\, y_{\mathrm{pred}})$")
    ax.set_xlabel("")
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
    ]
    fig.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.28, 0.94),
        ncol=1,
        labelspacing=0.35,
        columnspacing=1.0,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.56,
        0.93,
        "* 95% CI of difference in correlation excludes 0\n"
        "** 99% CI of difference in correlation excludes 0\n"
        "*** 99.9% CI of difference in correlation excludes 0",
        ha="left",
        va="top",
        fontsize=9.4,
        color="#374151",
        linespacing=1.25,
    )

    fig.subplots_adjust(bottom=0.20, top=0.86, right=0.98)

    fig.savefig(PLOTS_DIR / f"{out_stem}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    human_df = build_human_rows_experiment_bootstrap()
    llm_df = build_llm_rows_experiment_bootstrap()
    pair_sig_df = build_llm_pair_significance_experiment_bootstrap()
    refs_df = build_reference_lines()
    pd.concat([human_df, llm_df], ignore_index=True).to_csv(RESULTS_DIR / f"{OUT_STEM}_rows.csv", index=False)
    refs_df.to_csv(RESULTS_DIR / f"{OUT_STEM}_reference_lines.csv", index=False)
    pair_sig_df.to_csv(PAIR_SIGNIFICANCE_CSV, index=False)
    write_documentation(
        OUT_STEM,
        human_df,
        llm_df,
        refs_df,
        [
            "human wisdom-of-the-crowd bars: bootstrap the 20 experiments with replacement, then recompute the crowd-level correlation",
            "LLM bars: bootstrap the 20 experiments with replacement, then recompute the model-level correlation",
        ],
        pair_sig_df=pair_sig_df,
    )
    plot_figure(OUT_STEM, human_df, llm_df, refs_df, pair_sig_df=pair_sig_df)


if __name__ == "__main__":
    main()
