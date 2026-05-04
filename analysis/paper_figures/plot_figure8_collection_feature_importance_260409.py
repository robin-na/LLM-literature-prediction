from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import pandas as pd

from plot_figure8_collection_feature_importance_gpt41 import (
    FEATURE_KEYS,
    compute_permutation_importance,
    compute_shap_tables,
    draw_figure,
    load_collection_feature_frame as load_current_figure8_collection_df,
)


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"
BEST_NONLINEAR_CSV = RESULTS_DIR / "figure8_collection_best_nonlinear_model_by_model.csv"


def slugify_model_name(model_name: str) -> str:
    text = model_name.lower()
    text = text.replace("claude sonnet 4.6", "claude_sonnet46")
    text = text.replace("gpt-5.1", "gpt51")
    text = text.replace("gpt-4.1", "gpt41")
    text = text.replace("mini", "mini")
    text = text.replace("nano", "nano")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def build_feature_target_frame() -> pd.DataFrame:
    current_df = load_current_figure8_collection_df().drop(columns=["delta_correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("variant_id", keep="first")
    )
    metrics_df = pd.read_csv(COLLECTION_METRICS_CSV)
    return metrics_df.loc[:, ["model", "variant_id", "delta_correlation"]].merge(
        base_feature_df,
        on="variant_id",
        how="left",
        validate="many_to_one",
    )


def resolve_best_estimator(model_name: str) -> str:
    best = pd.read_csv(BEST_NONLINEAR_CSV)
    part = best.loc[best["scope_name"] == model_name, "model_name"]
    if part.empty:
        raise KeyError(f"No best nonlinear model recorded for {model_name}.")
    return str(part.iloc[0])


def generate(model_name: str) -> tuple[Path, Path]:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    estimator_name = resolve_best_estimator(model_name)
    df = build_feature_target_frame()
    df = df.loc[df["model"] == model_name].sort_values("variant_id").reset_index(drop=True)
    if df.empty:
        raise ValueError(f"No collection rows found for {model_name}.")

    X = df[FEATURE_KEYS].apply(pd.to_numeric, errors="coerce")
    X = X.fillna(X.median(numeric_only=True))
    y = pd.to_numeric(df["delta_correlation"], errors="coerce").to_numpy(dtype=float)
    groups = df["variant_id"].astype(str).to_numpy()

    perm_df = compute_permutation_importance(X, y, groups, estimator_name)
    shap_points, shap_summary = compute_shap_tables(X, y, perm_df["feature_key"].tolist(), estimator_name)

    stem = f"figure8_collection_feature_importance_{slugify_model_name(model_name)}"
    out_png = PLOTS_DIR / f"{stem}.png"
    out_pdf = PLOTS_DIR / f"{stem}.pdf"
    perm_csv = RESULTS_DIR / f"{stem}_permutation.csv"
    shap_points_csv = RESULTS_DIR / f"{stem}_shap_points.csv"
    shap_summary_csv = RESULTS_DIR / f"{stem}_shap_summary.csv"

    perm_df.to_csv(perm_csv, index=False)
    shap_points.to_csv(shap_points_csv, index=False)
    shap_summary.to_csv(shap_summary_csv, index=False)
    draw_figure(model_name, estimator_name, perm_df, shap_points, out_png, out_pdf)
    return out_png, out_pdf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Model label, e.g. 'GPT-5.1'")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_png, out_pdf = generate(args.model)
    print(out_png)
    print(out_pdf)


if __name__ == "__main__":
    main()
