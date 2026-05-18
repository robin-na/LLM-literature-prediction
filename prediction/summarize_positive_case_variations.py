#!/usr/bin/env python3
"""Summarize positive-case variation performance against the baseline."""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd


DELTA_FILE = "prediction_positive_case_variations_41_metrics_delta.csv"
METRICS_FILE = "prediction_positive_case_variations_41_metrics.csv"
OUTPUT_FILE = "prediction_positive_case_variations_ranked_summary.csv"


def parse_variation_name(name: str) -> tuple[str, str]:
    if name.endswith("_joint_reasoning"):
        return name[: -len("_joint_reasoning")], "joint_reasoning"
    if name.endswith("_joint"):
        return name[: -len("_joint")], "joint"
    if name.endswith("_reasoning"):
        return name[: -len("_reasoning")], "reasoning"
    return name, "single"


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

    delta_df = pd.read_csv(results_dir / DELTA_FILE)
    metrics_df = pd.read_csv(results_dir / METRICS_FILE)

    summary = delta_df.merge(metrics_df, on=["variation", "n"], how="left", suffixes=("_delta", ""))
    summary = summary[~summary["variation"].str.startswith("baseline")].copy()

    family_mode = summary["variation"].map(parse_variation_name)
    summary["family"] = family_mode.map(lambda item: item[0])
    summary["mode"] = family_mode.map(lambda item: item[1])

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

    summary["point_improve_count"] = (
        (summary["delta_rmse"] < 0).astype(int)
        + (summary["delta_correlation"] > 0).astype(int)
        + (summary["delta_directional_accuracy"] > 0).astype(int)
    )
    summary["ci_improve_count"] = (
        (summary["rmse_ci_verdict"] == "better").astype(int)
        + (summary["correlation_ci_verdict"] == "better").astype(int)
        + (summary["directional_accuracy_ci_verdict"] == "better").astype(int)
    )

    summary["rmse_rank"] = summary["delta_rmse"].rank(method="min", ascending=True).astype(int)
    summary["correlation_rank"] = (
        summary["delta_correlation"].rank(method="min", ascending=False).astype(int)
    )
    summary["directional_accuracy_rank"] = (
        summary["delta_directional_accuracy"].rank(method="min", ascending=False).astype(int)
    )
    summary["overall_rank_mean"] = (
        summary["rmse_rank"]
        + summary["correlation_rank"]
        + summary["directional_accuracy_rank"]
    ) / 3.0
    summary["overall_rank"] = summary["overall_rank_mean"].rank(method="min").astype(int)

    ordered_columns = [
        "overall_rank",
        "overall_rank_mean",
        "variation",
        "family",
        "mode",
        "n",
        "rmse",
        "delta_rmse",
        "delta_rmse_ci_low",
        "delta_rmse_ci_high",
        "rmse_rank",
        "rmse_ci_verdict",
        "correlation",
        "delta_correlation",
        "delta_correlation_ci_low",
        "delta_correlation_ci_high",
        "correlation_rank",
        "correlation_ci_verdict",
        "directional_accuracy",
        "delta_directional_accuracy",
        "delta_directional_accuracy_ci_low",
        "delta_directional_accuracy_ci_high",
        "directional_accuracy_rank",
        "directional_accuracy_ci_verdict",
        "point_improve_count",
        "ci_improve_count",
    ]

    summary = summary.sort_values(
        by=[
            "overall_rank_mean",
            "delta_rmse",
            "delta_correlation",
            "delta_directional_accuracy",
        ],
        ascending=[True, True, False, False],
    )
    output_path = results_dir / OUTPUT_FILE
    summary.to_csv(output_path, index=False, columns=ordered_columns)

    print(f"Saved: {output_path}")
    print(f"Rows summarized: {len(summary)}")
    print("Top 5 variants by overall rank:")
    for _, row in summary.head(5).iterrows():
        print(
            f"{row['overall_rank']}: {row['variation']} | "
            f"delta_rmse={row['delta_rmse']:.3f} | "
            f"delta_corr={row['delta_correlation']:.3f} | "
            f"delta_da={row['delta_directional_accuracy']:.3f}"
        )


if __name__ == "__main__":
    main()
