from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "analysis"
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import pandas as pd

import plot_figure7_metadata_effect_robustness as fig7_module
from plot_figure8_collection_feature_importance_gpt41 import load_collection_feature_frame as load_current_figure8_collection_df


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260409"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260409"

COLLECTION_METRICS_CSV = RESULTS_DIR / "collection_repeat_correlation_metrics.csv"
ROWS_CSV = RESULTS_DIR / "figure8_collection_metadata_effect_robustness_rows.csv"
PNG = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.png"
PDF = PLOTS_DIR / "figure8_collection_metadata_effect_robustness.pdf"

MODELS = ["GPT-4.1", "GPT-4.1 Mini", "GPT-5.1", "GPT-5 Mini", "GPT-5 Nano", "Claude Sonnet 4.6", "Gemini 2.5 Pro"]
MODEL_COLORS = {
    "GPT-4.1": "#2b8cbe",
    "GPT-4.1 Mini": "#1b9e77",
    "GPT-5.1": "#d95f02",
    "GPT-5 Mini": "#7570b3",
    "GPT-5 Nano": "#e7298a",
    "Claude Sonnet 4.6": "#9c755f",
    "Gemini 2.5 Pro": "#a6761d",
}


def build_collection_df() -> pd.DataFrame:
    current_df = load_current_figure8_collection_df().drop(columns=["delta_correlation", "correlation"])
    base_feature_df = (
        current_df.loc[current_df["model"] == "GPT-4.1"]
        .drop(columns=["model"])
        .drop_duplicates("variant_id", keep="first")
    )
    metrics_df = pd.read_csv(COLLECTION_METRICS_CSV)
    return metrics_df.loc[:, ["model", "variant_id", "correlation", "delta_correlation"]].merge(
        base_feature_df,
        on="variant_id",
        how="left",
        validate="many_to_one",
    )


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    fig7_module.MODELS = MODELS
    fig7_module.MODEL_COLORS = MODEL_COLORS

    rows = fig7_module.build_rows(
        build_collection_df(),
        item_type="Collections",
        feature_cols=fig7_module.COLLECTION_FEATURES,
    )
    rows.to_csv(ROWS_CSV, index=False)
    fig7_module.draw_figure(rows, "Collections", PNG, PDF)


if __name__ == "__main__":
    main()
