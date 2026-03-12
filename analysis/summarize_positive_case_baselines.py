#!/usr/bin/env python3
"""Summarize baseline-family variants from prediction_positive_case_variations_41."""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd


METRICS_FILE = "prediction_positive_case_variations_41_metrics.csv"
DELTA_FILE = "prediction_positive_case_variations_41_metrics_delta.csv"
OUTPUT_FILE = "prediction_positive_case_variations_baseline_comparison.csv"

BASELINE_VARIATIONS = [
    "baseline",
    "baseline_reasoning",
    "baseline_joint",
    "baseline_joint_reasoning",
]


def ci_verdict(better_direction: str, ci_low: float, ci_high: float) -> str:
    if math.isnan(ci_low) or math.isnan(ci_high):
        return "missing"
    if better_direction == "lower":
        if ci_high < 0:
            return "better"
        if ci_low > 0:
            return "worse"
        return "uncertain"
    if ci_low > 0:
        return "better"
    if ci_high < 0:
        return "worse"
    return "uncertain"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"

    metrics_df = pd.read_csv(results_dir / METRICS_FILE)
    delta_df = pd.read_csv(results_dir / DELTA_FILE)

    summary = metrics_df.merge(delta_df, on=["variation", "n"], how="inner")
    summary = summary[summary["variation"].isin(BASELINE_VARIATIONS)].copy()

    summary["rmse_ci_verdict"] = summary.apply(
        lambda row: ci_verdict("lower", row["delta_rmse_ci_low"], row["delta_rmse_ci_high"]),
        axis=1,
    )
    summary["correlation_ci_verdict"] = summary.apply(
        lambda row: ci_verdict(
            "higher", row["delta_correlation_ci_low"], row["delta_correlation_ci_high"]
        ),
        axis=1,
    )
    summary["directional_accuracy_ci_verdict"] = summary.apply(
        lambda row: ci_verdict(
            "higher",
            row["delta_directional_accuracy_ci_low"],
            row["delta_directional_accuracy_ci_high"],
        ),
        axis=1,
    )

    summary["rmse_rank"] = summary["rmse"].rank(method="min", ascending=True).astype(int)
    summary["correlation_rank"] = summary["correlation"].rank(
        method="min", ascending=False
    ).astype(int)
    summary["directional_accuracy_rank"] = summary["directional_accuracy"].rank(
        method="min", ascending=False
    ).astype(int)

    summary = summary.sort_values(
        by=["rmse_rank", "correlation_rank", "directional_accuracy_rank", "variation"]
    )

    output_path = results_dir / OUTPUT_FILE
    summary.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")
    print(summary[[
        "variation",
        "rmse",
        "correlation",
        "directional_accuracy",
        "delta_rmse",
        "delta_correlation",
        "delta_directional_accuracy",
        "rmse_ci_verdict",
        "correlation_ci_verdict",
        "directional_accuracy_ci_verdict",
    ]].to_string(index=False))


if __name__ == "__main__":
    main()
