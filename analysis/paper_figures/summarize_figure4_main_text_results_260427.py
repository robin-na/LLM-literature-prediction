from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"

BEST_MODELS_CSV = RESULTS_DIR / "figure4_predictive_model_best.csv"
COEF_CSV = RESULTS_DIR / "figure4_metadata_coefficients_elastic_net_rows.csv"
PERM_CSV = RESULTS_DIR / "figure4_metadata_coefficients_elastic_net_permutation_rows.csv"

OUT_KEY_VALUES = RESULTS_DIR / "figure4_main_text_key_values.csv"
OUT_DOC = RESULTS_DIR / "figure4_main_text_results_documentation.md"

MODELS = ["Claude Sonnet 4.6", "GPT-4.1", "Gemini 2.5 Pro"]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def as_float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def fmt(x: float, digits: int = 3) -> str:
    return f"{x:.{digits}f}"


def main() -> None:
    best_rows = read_csv_rows(BEST_MODELS_CSV)
    coef_rows = read_csv_rows(COEF_CSV)
    perm_rows = read_csv_rows(PERM_CSV)

    best_by_model = {row["model"]: row for row in best_rows}
    empirical_coef = {row["model"]: row for row in coef_rows if row["feature_label"] == "Empirical"}
    empirical_perm = {row["model"]: row for row in perm_rows if row["feature_label"] == "Empirical"}

    perm_rank_by_model: dict[str, int] = {}
    perm_top_by_model: dict[str, dict[str, str]] = {}
    for model in MODELS:
        model_rows = [row for row in perm_rows if row["model"] == model]
        model_rows.sort(key=lambda r: as_float(r, "mean_importance"), reverse=True)
        perm_top_by_model[model] = model_rows[0]
        for idx, row in enumerate(model_rows, start=1):
            if row["feature_label"] == "Empirical":
                perm_rank_by_model[model] = idx
                break

    fieldnames = [
        "section",
        "model",
        "value_name",
        "value",
        "notes",
    ]
    out_rows: list[dict[str, str]] = []

    for model in MODELS:
        best = best_by_model[model]
        coef = empirical_coef[model]
        perm = empirical_perm[model]
        out_rows.extend(
            [
                {
                    "section": "predictive_performance",
                    "model": model,
                    "value_name": "best_model",
                    "value": best["predictive_model"],
                    "notes": "Best cross-validated predictive model among benchmarked estimators.",
                },
                {
                    "section": "predictive_performance",
                    "model": model,
                    "value_name": "cv_r2",
                    "value": best["cv_r2"],
                    "notes": "Out-of-sample R^2 for the best model (elastic net).",
                },
                {
                    "section": "empirical_coefficient",
                    "model": model,
                    "value_name": "coef",
                    "value": coef["coef"],
                    "notes": "Elastic-net standardized coefficient for empirical papers.",
                },
                {
                    "section": "empirical_coefficient",
                    "model": model,
                    "value_name": "ci_low",
                    "value": coef["ci_low"],
                    "notes": "Bootstrap 95% interval lower bound.",
                },
                {
                    "section": "empirical_coefficient",
                    "model": model,
                    "value_name": "ci_high",
                    "value": coef["ci_high"],
                    "notes": "Bootstrap 95% interval upper bound.",
                },
                {
                    "section": "empirical_importance",
                    "model": model,
                    "value_name": "mean_importance_pct_error_increase",
                    "value": perm["mean_importance"],
                    "notes": "Mean permutation importance: % increase in prediction error when the empirical feature is permuted.",
                },
                {
                    "section": "empirical_importance",
                    "model": model,
                    "value_name": "se_importance_pct_error_increase",
                    "value": perm["se_importance"],
                    "notes": "Standard error across folds.",
                },
                {
                    "section": "empirical_importance",
                    "model": model,
                    "value_name": "importance_rank",
                    "value": str(perm_rank_by_model[model]),
                    "notes": "Rank of empirical status among the 9 metadata features by permutation importance.",
                },
                {
                    "section": "empirical_importance",
                    "model": model,
                    "value_name": "top_feature",
                    "value": perm_top_by_model[model]["feature_label"],
                    "notes": "Highest-importance metadata feature for this model.",
                },
            ]
        )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_KEY_VALUES.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    doc = f"""# figure4_main_text_results

## Purpose
Main-text numerical summary for the Figure 4 results section in `main_text_260427`.

## Source files
- Predictive-model benchmark: `{BEST_MODELS_CSV.relative_to(ROOT)}`
- Elastic-net coefficients: `{COEF_CSV.relative_to(ROOT)}`
- Elastic-net permutation importance: `{PERM_CSV.relative_to(ROOT)}`

## Key manuscript values

### Best predictive model and out-of-sample R^2
- Claude Sonnet 4.6: elastic net, `R^2 = {fmt(as_float(best_by_model['Claude Sonnet 4.6'], 'cv_r2'))}`
- GPT-4.1: elastic net, `R^2 = {fmt(as_float(best_by_model['GPT-4.1'], 'cv_r2'))}`
- Gemini 2.5 Pro: elastic net, `R^2 = {fmt(as_float(best_by_model['Gemini 2.5 Pro'], 'cv_r2'))}`

### Empirical-paper coefficient (Elastic net, standardized)
- Claude Sonnet 4.6: `{fmt(as_float(empirical_coef['Claude Sonnet 4.6'], 'coef'), 4)}` with bootstrap interval `[{fmt(as_float(empirical_coef['Claude Sonnet 4.6'], 'ci_low'), 4)}, {fmt(as_float(empirical_coef['Claude Sonnet 4.6'], 'ci_high'), 4)}]`
- GPT-4.1: `{fmt(as_float(empirical_coef['GPT-4.1'], 'coef'), 4)}` with bootstrap interval `[{fmt(as_float(empirical_coef['GPT-4.1'], 'ci_low'), 4)}, {fmt(as_float(empirical_coef['GPT-4.1'], 'ci_high'), 4)}]`
- Gemini 2.5 Pro: `{fmt(as_float(empirical_coef['Gemini 2.5 Pro'], 'coef'), 4)}` with bootstrap interval `[{fmt(as_float(empirical_coef['Gemini 2.5 Pro'], 'ci_low'), 4)}, {fmt(as_float(empirical_coef['Gemini 2.5 Pro'], 'ci_high'), 4)}]`

### Empirical-paper permutation importance
- Claude Sonnet 4.6: `{fmt(as_float(empirical_perm['Claude Sonnet 4.6'], 'mean_importance'), 3)}%` increase in prediction error when permuted; rank `#{perm_rank_by_model['Claude Sonnet 4.6']}` of 9 features
- GPT-4.1: `{fmt(as_float(empirical_perm['GPT-4.1'], 'mean_importance'), 3)}%` increase in prediction error when permuted; rank `#{perm_rank_by_model['GPT-4.1']}` of 9 features
- Gemini 2.5 Pro: `{fmt(as_float(empirical_perm['Gemini 2.5 Pro'], 'mean_importance'), 3)}%` increase in prediction error when permuted; rank `#{perm_rank_by_model['Gemini 2.5 Pro']}` of 9 features

## Interpretation notes
- The best metadata-only predictive model is elastic net for all three displayed LLMs, but out-of-sample fit remains weak and never exceeds `R^2 = {fmt(max(as_float(best_by_model[m], 'cv_r2') for m in MODELS))}`.
- The empirical-paper indicator is directionally negative for all three displayed LLMs.
- Empirical status is the highest-importance metadata feature for GPT-4.1 and Gemini 2.5 Pro, and the third-highest for Claude Sonnet 4.6.
"""
    OUT_DOC.write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    main()
