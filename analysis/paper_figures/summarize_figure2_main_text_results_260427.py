from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import numpy as np
import pandas as pd

from plot_figure2_main_text_260427 import (
    BOOTSTRAP_SEED,
    CONDITION_ORDER,
    HUMAN_PREDICTIONS_CSV,
    LLM_AVG_PRED_CSV,
    MODEL_ORDER,
    PAIR_BOOTSTRAP_N,
    Q_COLS,
    RESULTS_DIR,
    VALIDATION_CSV,
    build_human_rows,
    build_llm_rows,
    corr,
    load_noise_ceiling,
    load_no_treatment_reference,
)


BASELINE_VS_HUMAN_CSV = RESULTS_DIR / "figure2_baseline_llm_vs_human_woc_comparison.csv"
ALL_CONDITIONS_VS_HUMAN_CSV = RESULTS_DIR / "figure2_llm_vs_human_woc_all_conditions_bootstrap.csv"
UNAUGMENTED_PAIRWISE_CSV = RESULTS_DIR / "figure2_unaugmented_llm_pairwise_bootstrap.csv"
HUMAN_VS_NO_TREATMENT_CSV = RESULTS_DIR / "figure2_human_woc_vs_no_treatment_baseline_bootstrap.csv"
KEY_VALUES_CSV = RESULTS_DIR / "figure2_main_text_key_values.csv"
DOCUMENTATION_MD = RESULTS_DIR / "figure2_main_text_results_documentation.md"
PAIR_SIGNIFICANCE_CSV = RESULTS_DIR / "figure2_benchmark_vs_human_crowds_bar_pair_significance.csv"

ROUND_N = 6


def load_truth_vector() -> np.ndarray:
    return (
        pd.read_csv(VALIDATION_CSV)
        .sort_values("CONFIG_configId")["efficiency_p"]
        .to_numpy(dtype=float)
        * 100.0
    )


def load_no_treatment_vector() -> np.ndarray:
    return (
        pd.read_csv(VALIDATION_CSV)
        .sort_values("CONFIG_configId")["efficiency_np"]
        .to_numpy(dtype=float)
        * 100.0
    )


def load_human_prediction_vectors() -> tuple[dict[str, np.ndarray], dict[str, int]]:
    pred = pd.read_csv(HUMAN_PREDICTIONS_CSV)
    pred = pred.query("prediction.between(-0.2, 1.2) and n_predictions_made == 20").copy()

    vectors: dict[str, np.ndarray] = {}
    counts: dict[str, int] = {}
    for source, label in [("prolific", "Laypeople WoC"), ("sspp", "Experts WoC")]:
        wide = (
            pred.loc[pred["source"] == source, ["CONFIG_configId", "playerID", "prediction"]]
            .pivot_table(index="CONFIG_configId", columns="playerID", values="prediction", aggfunc="mean")
            .sort_index()
        )
        wide = wide.loc[:, wide.notna().all(axis=0)]
        vectors[label] = wide.mean(axis=1).to_numpy(dtype=float) * 100.0
        counts[label] = int(wide.shape[1])
    return vectors, counts


def load_llm_prediction_vectors() -> dict[tuple[str, str], np.ndarray]:
    avg = pd.read_csv(LLM_AVG_PRED_CSV)
    avg = avg.loc[avg["condition"].isin(CONDITION_ORDER) & avg["model"].isin(MODEL_ORDER)].copy()
    vectors: dict[tuple[str, str], np.ndarray] = {}
    for _, row in avg.iterrows():
        vectors[(str(row["model"]), str(row["condition"]))] = row[Q_COLS].to_numpy(dtype=float)
    return vectors


def corr_rows(pred_samples: np.ndarray, truth_samples: np.ndarray) -> np.ndarray:
    pred_centered = pred_samples - pred_samples.mean(axis=1, keepdims=True)
    truth_centered = truth_samples - truth_samples.mean(axis=1, keepdims=True)
    denom = np.sqrt((pred_centered**2).sum(axis=1) * (truth_centered**2).sum(axis=1))
    out = np.full(pred_samples.shape[0], np.nan, dtype=float)
    mask = denom > 0
    out[mask] = (pred_centered[mask] * truth_centered[mask]).sum(axis=1) / denom[mask]
    return out


def bootstrap_delta(
    vec_a: np.ndarray,
    vec_b: np.ndarray,
    truth: np.ndarray,
    rng: np.random.Generator,
) -> dict[str, float]:
    n = len(truth)
    sample_idx = rng.integers(0, n, size=(PAIR_BOOTSTRAP_N, n))
    truth_s = truth[sample_idx]
    a_s = vec_a[sample_idx]
    b_s = vec_b[sample_idx]
    delta_boot = corr_rows(a_s, truth_s) - corr_rows(b_s, truth_s)

    ci95_low, ci95_high = np.quantile(delta_boot, [0.025, 0.975])
    ci99_low, ci99_high = np.quantile(delta_boot, [0.005, 0.995])
    ci999_low, ci999_high = np.quantile(delta_boot, [0.0005, 0.9995])
    p_two = float(2.0 * min((delta_boot <= 0).mean(), (delta_boot >= 0).mean()))

    return {
        "delta": float(corr(vec_a, truth) - corr(vec_b, truth)),
        "ci95_low": float(ci95_low),
        "ci95_high": float(ci95_high),
        "ci99_low": float(ci99_low),
        "ci99_high": float(ci99_high),
        "ci999_low": float(ci999_low),
        "ci999_high": float(ci999_high),
        "p_two": p_two,
        "significant_95": bool(ci95_low > 0 or ci95_high < 0),
    }


def build_baseline_vs_human_df(
    llm_vectors: dict[tuple[str, str], np.ndarray],
    human_vectors: dict[str, np.ndarray],
    truth: np.ndarray,
) -> pd.DataFrame:
    rng = np.random.default_rng(BOOTSTRAP_SEED + 100)
    rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        model_vec = llm_vectors[(model, "baseline")]
        for human_label in ["Laypeople WoC", "Experts WoC"]:
            stats = bootstrap_delta(model_vec, human_vectors[human_label], truth, rng)
            rows.append(
                {
                    "model": model,
                    "human_reference": human_label,
                    "model_corr": float(corr(model_vec, truth)),
                    "human_corr": float(corr(human_vectors[human_label], truth)),
                    "delta_corr_model_minus_human": stats["delta"],
                    "delta_ci95_low": stats["ci95_low"],
                    "delta_ci95_high": stats["ci95_high"],
                    "delta_ci99_low": stats["ci99_low"],
                    "delta_ci99_high": stats["ci99_high"],
                    "delta_ci999_low": stats["ci999_low"],
                    "delta_ci999_high": stats["ci999_high"],
                    "p_bootstrap_two_sided": stats["p_two"],
                    "verdict": "significant" if stats["significant_95"] else "n.s.",
                    "n_boot": PAIR_BOOTSTRAP_N,
                }
            )
    return pd.DataFrame(rows)


def build_all_conditions_vs_human_df(
    llm_vectors: dict[tuple[str, str], np.ndarray],
    human_vectors: dict[str, np.ndarray],
    truth: np.ndarray,
) -> pd.DataFrame:
    rng = np.random.default_rng(BOOTSTRAP_SEED + 101)
    rows: list[dict[str, object]] = []
    for model in MODEL_ORDER:
        for condition in CONDITION_ORDER:
            model_vec = llm_vectors[(model, condition)]
            for human_label in ["Laypeople WoC", "Experts WoC"]:
                stats = bootstrap_delta(model_vec, human_vectors[human_label], truth, rng)
                rows.append(
                    {
                        "model": model,
                        "condition": condition,
                        "human_reference": human_label,
                        "model_corr": float(corr(model_vec, truth)),
                        "human_corr": float(corr(human_vectors[human_label], truth)),
                        "delta_model_minus_human": stats["delta"],
                        "delta_ci95_low": stats["ci95_low"],
                        "delta_ci95_high": stats["ci95_high"],
                        "p_bootstrap_two_sided": stats["p_two"],
                        "significant_95": stats["significant_95"],
                        "n_boot": PAIR_BOOTSTRAP_N,
                    }
                )
    return pd.DataFrame(rows)


def build_unaugmented_pairwise_df(
    llm_vectors: dict[tuple[str, str], np.ndarray],
    truth: np.ndarray,
) -> pd.DataFrame:
    rng = np.random.default_rng(BOOTSTRAP_SEED + 102)
    rows: list[dict[str, object]] = []
    baseline_order = MODEL_ORDER.copy()
    for i, model_a in enumerate(baseline_order):
        for model_b in baseline_order[i + 1 :]:
            vec_a = llm_vectors[(model_a, "baseline")]
            vec_b = llm_vectors[(model_b, "baseline")]
            stats = bootstrap_delta(vec_a, vec_b, truth, rng)
            rows.append(
                {
                    "model_a": model_a,
                    "model_b": model_b,
                    "corr_a": float(corr(vec_a, truth)),
                    "corr_b": float(corr(vec_b, truth)),
                    "delta_a_minus_b": stats["delta"],
                    "delta_ci95_low": stats["ci95_low"],
                    "delta_ci95_high": stats["ci95_high"],
                    "p_bootstrap_two_sided": stats["p_two"],
                    "significant_95": stats["significant_95"],
                    "n_boot": PAIR_BOOTSTRAP_N,
                }
            )
    return pd.DataFrame(rows)


def build_human_vs_no_treatment_df(
    human_vectors: dict[str, np.ndarray],
    no_treatment_vec: np.ndarray,
    truth: np.ndarray,
) -> pd.DataFrame:
    rng = np.random.default_rng(BOOTSTRAP_SEED + 103)
    rows: list[dict[str, object]] = []
    for human_label in ["Laypeople WoC", "Experts WoC"]:
        human_vec = human_vectors[human_label]
        stats = bootstrap_delta(human_vec, no_treatment_vec, truth, rng)
        rows.append(
            {
                "human_reference": human_label,
                "human_corr": float(corr(human_vec, truth)),
                "no_treatment_corr": float(corr(no_treatment_vec, truth)),
                "delta_human_minus_no_treatment": stats["delta"],
                "delta_ci95_low": stats["ci95_low"],
                "delta_ci95_high": stats["ci95_high"],
                "delta_ci99_low": stats["ci99_low"],
                "delta_ci99_high": stats["ci99_high"],
                "delta_ci999_low": stats["ci999_low"],
                "delta_ci999_high": stats["ci999_high"],
                "p_bootstrap_two_sided": stats["p_two"],
                "significant_95": stats["significant_95"],
                "n_boot": PAIR_BOOTSTRAP_N,
            }
        )
    return pd.DataFrame(rows)


def build_key_values(
    human_rows: pd.DataFrame,
    llm_rows: pd.DataFrame,
    baseline_vs_human_df: pd.DataFrame,
    all_conditions_vs_human_df: pd.DataFrame,
    unaugmented_pairwise_df: pd.DataFrame,
    human_vs_no_treatment_df: pd.DataFrame,
    benchmark_gain_df: pd.DataFrame,
    human_counts: dict[str, int],
) -> pd.DataFrame:
    human_lookup = human_rows.set_index("label")
    llm_lookup = llm_rows.set_index(["label", "condition"])

    rows: list[dict[str, object]] = []

    def add(key: str, value: object, description: str, source_table: str) -> None:
        rows.append(
            {
                "key": key,
                "value": value,
                "description": description,
                "source_table": source_table,
            }
        )

    add("laypeople_woc_corr", human_lookup.loc["Laypeople wisdom-of-the-crowd", "value"], "Laypeople wisdom-of-the-crowd correlation", "figure2 rows")
    add("experts_woc_corr", human_lookup.loc["Experts wisdom-of-the-crowd", "value"], "Experts wisdom-of-the-crowd correlation", "figure2 rows")
    add("laypeople_complete_n", human_counts["Laypeople WoC"], "Number of laypeople with complete 20-question forecasts", "human prediction survey")
    add("experts_complete_n", human_counts["Experts WoC"], "Number of experts with complete 20-question forecasts", "human prediction survey")

    for model in MODEL_ORDER:
        base = llm_lookup.loc[(model, "baseline"), "value"]
        bench = llm_lookup.loc[(model, "science_gpt41"), "value"]
        add(f"{model.lower().replace(' ', '_').replace('.', '').replace('-', '_')}_baseline_corr", base, f"{model} baseline correlation", "figure2 rows")
        add(f"{model.lower().replace(' ', '_').replace('.', '').replace('-', '_')}_benchmark_corr", bench, f"{model} benchmark-augmented correlation", "figure2 rows")

    add("no_treatment_baseline_corr", load_no_treatment_reference(), "No-treatment outcome baseline correlation", "figure2 reference line")
    add("noise_ceiling_corr", load_noise_ceiling(), "Noise ceiling correlation", "figure2 reference line")

    lay_no_treat = human_vs_no_treatment_df.query("human_reference == 'Laypeople WoC'").iloc[0]
    exp_no_treat = human_vs_no_treatment_df.query("human_reference == 'Experts WoC'").iloc[0]
    add("laypeople_minus_no_treatment_delta", lay_no_treat["delta_human_minus_no_treatment"], "Laypeople WoC minus no-treatment baseline correlation", "human vs no-treatment bootstrap")
    add("laypeople_minus_no_treatment_ci95_low", lay_no_treat["delta_ci95_low"], "Lower 95% CI for laypeople WoC minus no-treatment baseline", "human vs no-treatment bootstrap")
    add("laypeople_minus_no_treatment_ci95_high", lay_no_treat["delta_ci95_high"], "Upper 95% CI for laypeople WoC minus no-treatment baseline", "human vs no-treatment bootstrap")
    add("experts_minus_no_treatment_delta", exp_no_treat["delta_human_minus_no_treatment"], "Experts WoC minus no-treatment baseline correlation", "human vs no-treatment bootstrap")
    add("experts_minus_no_treatment_ci95_low", exp_no_treat["delta_ci95_low"], "Lower 95% CI for experts WoC minus no-treatment baseline", "human vs no-treatment bootstrap")
    add("experts_minus_no_treatment_ci95_high", exp_no_treat["delta_ci95_high"], "Upper 95% CI for experts WoC minus no-treatment baseline", "human vs no-treatment bootstrap")

    claude_lay = baseline_vs_human_df.query("model == 'Claude Sonnet 4.6' and human_reference == 'Laypeople WoC'").iloc[0]
    claude_exp = baseline_vs_human_df.query("model == 'Claude Sonnet 4.6' and human_reference == 'Experts WoC'").iloc[0]
    add("claude_baseline_minus_laypeople_delta", claude_lay["delta_corr_model_minus_human"], "Claude Sonnet 4.6 baseline minus laypeople WoC correlation", "baseline vs human bootstrap")
    add("claude_baseline_minus_laypeople_ci95_low", claude_lay["delta_ci95_low"], "Lower 95% CI for Claude baseline minus laypeople WoC", "baseline vs human bootstrap")
    add("claude_baseline_minus_laypeople_ci95_high", claude_lay["delta_ci95_high"], "Upper 95% CI for Claude baseline minus laypeople WoC", "baseline vs human bootstrap")
    add("claude_baseline_minus_experts_delta", claude_exp["delta_corr_model_minus_human"], "Claude Sonnet 4.6 baseline minus experts WoC correlation", "baseline vs human bootstrap")
    add("claude_baseline_minus_experts_ci95_low", claude_exp["delta_ci95_low"], "Lower 95% CI for Claude baseline minus experts WoC", "baseline vs human bootstrap")
    add("claude_baseline_minus_experts_ci95_high", claude_exp["delta_ci95_high"], "Upper 95% CI for Claude baseline minus experts WoC", "baseline vs human bootstrap")

    claude_gemini = unaugmented_pairwise_df.query("model_a == 'Claude Sonnet 4.6' and model_b == 'Gemini 2.5 Pro'").iloc[0]
    add("claude_minus_gemini_baseline_delta", claude_gemini["delta_a_minus_b"], "Claude Sonnet 4.6 baseline minus Gemini 2.5 Pro baseline correlation", "unaugmented pairwise bootstrap")
    add("claude_minus_gemini_baseline_ci95_low", claude_gemini["delta_ci95_low"], "Lower 95% CI for Claude minus Gemini baseline delta", "unaugmented pairwise bootstrap")
    add("claude_minus_gemini_baseline_ci95_high", claude_gemini["delta_ci95_high"], "Upper 95% CI for Claude minus Gemini baseline delta", "unaugmented pairwise bootstrap")

    for model in ["Gemini 2.5 Pro", "GPT-4.1", "Claude Sonnet 4.6"]:
        bench_gain = benchmark_gain_df.query("model == @model").iloc[0]
        prefix = model.lower().replace(" ", "_").replace(".", "").replace("-", "_")
        add(f"{prefix}_benchmark_gain_delta", bench_gain["delta_corr"], f"{model} benchmark minus baseline delta", "figure2 pair significance")
        add(f"{prefix}_benchmark_gain_ci95_low", bench_gain["delta_ci95_low"], f"Lower 95% CI for {model} benchmark gain", "figure2 pair significance")
        add(f"{prefix}_benchmark_gain_ci95_high", bench_gain["delta_ci95_high"], f"Upper 95% CI for {model} benchmark gain", "figure2 pair significance")

    gpt_bench_lay = all_conditions_vs_human_df.query(
        "model == 'GPT-4.1' and condition == 'science_gpt41' and human_reference == 'Laypeople WoC'"
    ).iloc[0]
    gpt_bench_exp = all_conditions_vs_human_df.query(
        "model == 'GPT-4.1' and condition == 'science_gpt41' and human_reference == 'Experts WoC'"
    ).iloc[0]
    add("gpt41_benchmark_minus_laypeople_delta", gpt_bench_lay["delta_model_minus_human"], "GPT-4.1 benchmark minus laypeople WoC correlation", "all conditions vs human bootstrap")
    add("gpt41_benchmark_minus_laypeople_ci95_low", gpt_bench_lay["delta_ci95_low"], "Lower 95% CI for GPT-4.1 benchmark minus laypeople WoC", "all conditions vs human bootstrap")
    add("gpt41_benchmark_minus_laypeople_ci95_high", gpt_bench_lay["delta_ci95_high"], "Upper 95% CI for GPT-4.1 benchmark minus laypeople WoC", "all conditions vs human bootstrap")
    add("gpt41_benchmark_minus_experts_delta", gpt_bench_exp["delta_model_minus_human"], "GPT-4.1 benchmark minus experts WoC correlation", "all conditions vs human bootstrap")
    add("gpt41_benchmark_minus_experts_ci95_low", gpt_bench_exp["delta_ci95_low"], "Lower 95% CI for GPT-4.1 benchmark minus experts WoC", "all conditions vs human bootstrap")
    add("gpt41_benchmark_minus_experts_ci95_high", gpt_bench_exp["delta_ci95_high"], "Upper 95% CI for GPT-4.1 benchmark minus experts WoC", "all conditions vs human bootstrap")

    out = pd.DataFrame(rows)
    return out


def format_float_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        if pd.api.types.is_float_dtype(out[col]):
            out[col] = out[col].map(lambda x: f"{float(x):.{ROUND_N}f}")
    return out


def write_documentation(
    human_rows: pd.DataFrame,
    llm_rows: pd.DataFrame,
    baseline_vs_human_df: pd.DataFrame,
    all_conditions_vs_human_df: pd.DataFrame,
    unaugmented_pairwise_df: pd.DataFrame,
    human_vs_no_treatment_df: pd.DataFrame,
    key_values_df: pd.DataFrame,
) -> None:
    llm_display = llm_rows[["label", "condition", "value"]].copy()
    human_display = human_rows[["label", "value"]].copy()

    key_display = key_values_df.copy()
    if "value" in key_display.columns:
        key_display["value"] = key_display["value"].map(
            lambda x: f"{float(x):.{ROUND_N}f}" if isinstance(x, (float, np.floating)) else str(x)
        )

    doc = f"""# figure2_main_text_results

## Purpose
This file documents the exact `260427` numerical values used to write the main-text Results prose for the canonical benchmark-versus-human figure.

## Relationship to the canonical figure
- Semantic figure ID: `benchmark_vs_human_crowds_bar`
- Canonical figure documentation: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_documentation.md`
- Canonical figure rows: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_rows.csv`
- Canonical figure pair significance: `results/paper/main_text_figures_260427/figure2_benchmark_vs_human_crowds_bar_pair_significance.csv`

## Output files
- Baseline LLM vs human WoC comparisons: `{BASELINE_VS_HUMAN_CSV.relative_to(ROOT)}`
- All-condition LLM vs human WoC comparisons: `{ALL_CONDITIONS_VS_HUMAN_CSV.relative_to(ROOT)}`
- Unaugmented LLM pairwise comparisons: `{UNAUGMENTED_PAIRWISE_CSV.relative_to(ROOT)}`
- Human WoC vs no-treatment baseline comparisons: `{HUMAN_VS_NO_TREATMENT_CSV.relative_to(ROOT)}`
- Main-text key values: `{KEY_VALUES_CSV.relative_to(ROOT)}`
- This documentation file: `{DOCUMENTATION_MD.relative_to(ROOT)}`
- Generating script: `{Path(__file__).resolve().relative_to(ROOT)}`

## Input files
- LLM 30-run mean predictions: `{LLM_AVG_PRED_CSV.relative_to(ROOT)}`
- Human forecasts: `{HUMAN_PREDICTIONS_CSV.relative_to(ROOT)}`
- Validation outcomes: `{VALIDATION_CSV.relative_to(ROOT)}`
- Canonical figure pair-significance table: `{PAIR_SIGNIFICANCE_CSV.relative_to(ROOT)}`

## Estimands
- Human WoC correlation: `corr(mean human prediction across complete forecasters, true outcome)`
- LLM correlation: `corr(mean prediction across 30 runs, true outcome)`
- Pairwise comparison delta: `corr(vector_a, truth) - corr(vector_b, truth)`, bootstrapped over the 20 experiments with paired resampling

## Notes for manuscript use
- Use the baseline-vs-human table for claims that off-the-shelf LLMs do not differ significantly from laypeople or experts.
- Use the unaugmented pairwise table for claims about the best unaugmented model versus the worst.
- Use the canonical figure pair-significance table for within-model benchmark-paper gains.
- Use the all-condition table for claims that benchmark-augmented models significantly outperform human WoC references.
- Use the human-vs-no-treatment table for claims that laypeople and experts outperform the no-treatment baseline.

## Core plotted values
### Human wisdom-of-the-crowd
{format_float_cols(human_display).to_markdown(index=False)}

### Displayed LLM bars
{format_float_cols(llm_display).to_markdown(index=False)}

## Baseline LLM vs human WoC
{format_float_cols(baseline_vs_human_df).to_markdown(index=False)}

## All displayed LLM conditions vs human WoC
{format_float_cols(all_conditions_vs_human_df).to_markdown(index=False)}

## Unaugmented LLM pairwise comparisons
{format_float_cols(unaugmented_pairwise_df).to_markdown(index=False)}

## Human WoC vs no-treatment baseline
{format_float_cols(human_vs_no_treatment_df).to_markdown(index=False)}

## Main-text key values
{key_display.to_markdown(index=False)}
"""
    DOCUMENTATION_MD.write_text(doc)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    truth = load_truth_vector()
    no_treatment_vec = load_no_treatment_vector()
    human_rows = build_human_rows()
    llm_rows = build_llm_rows()
    human_vectors, human_counts = load_human_prediction_vectors()
    llm_vectors = load_llm_prediction_vectors()
    benchmark_gain_df = pd.read_csv(PAIR_SIGNIFICANCE_CSV)

    baseline_vs_human_df = build_baseline_vs_human_df(llm_vectors, human_vectors, truth)
    all_conditions_vs_human_df = build_all_conditions_vs_human_df(llm_vectors, human_vectors, truth)
    unaugmented_pairwise_df = build_unaugmented_pairwise_df(llm_vectors, truth)
    human_vs_no_treatment_df = build_human_vs_no_treatment_df(human_vectors, no_treatment_vec, truth)
    key_values_df = build_key_values(
        human_rows,
        llm_rows,
        baseline_vs_human_df,
        all_conditions_vs_human_df,
        unaugmented_pairwise_df,
        human_vs_no_treatment_df,
        benchmark_gain_df,
        human_counts,
    )

    baseline_vs_human_df.to_csv(BASELINE_VS_HUMAN_CSV, index=False)
    all_conditions_vs_human_df.to_csv(ALL_CONDITIONS_VS_HUMAN_CSV, index=False)
    unaugmented_pairwise_df.to_csv(UNAUGMENTED_PAIRWISE_CSV, index=False)
    human_vs_no_treatment_df.to_csv(HUMAN_VS_NO_TREATMENT_CSV, index=False)
    key_values_df.to_csv(KEY_VALUES_CSV, index=False)
    write_documentation(
        human_rows,
        llm_rows,
        baseline_vs_human_df,
        all_conditions_vs_human_df,
        unaugmented_pairwise_df,
        human_vs_no_treatment_df,
        key_values_df,
    )

    print(f"Wrote {BASELINE_VS_HUMAN_CSV.relative_to(ROOT)}")
    print(f"Wrote {ALL_CONDITIONS_VS_HUMAN_CSV.relative_to(ROOT)}")
    print(f"Wrote {UNAUGMENTED_PAIRWISE_CSV.relative_to(ROOT)}")
    print(f"Wrote {HUMAN_VS_NO_TREATMENT_CSV.relative_to(ROOT)}")
    print(f"Wrote {KEY_VALUES_CSV.relative_to(ROOT)}")
    print(f"Wrote {DOCUMENTATION_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
