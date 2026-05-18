from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ANALYSIS_ROOT = Path(__file__).resolve().parents[2]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from plot_paths import (
    VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_PLOTS as PLOTS,
    ensure_plot_dir,
)
from result_paths import (
    VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_RESULTS as RESULTS,
    ensure_results_dir,
)


INPUT = RESULTS / "validation_positive_case_literature_design_space_correlation_significance.csv"
SUMMARY_OUTPUT = RESULTS / "validation_positive_case_literature_design_space_meta_summary.csv"
SUBGROUP_OUTPUT = RESULTS / "validation_positive_case_literature_design_space_meta_subgroups.csv"
FOREST_OUTPUT = PLOTS / "validation_positive_case_literature_design_space_meta_correlation.png"
OUTPUT_STEM_PREFIX = "validation_positive_case_literature_design_space"
PLOT_CONTEXT_LABEL = "Positive Case Design Space"

MODE_LABELS = {
    "reasoning": "single with explanation",
    "joint_reasoning": "joint with explanation",
}
VARIANT_LABELS = {
    "paper_only_narrative": "narrative",
    "paper_only_decision": "decision",
}


def configure_context(
    *,
    results_dir: Path | None = None,
    plots_dir: Path | None = None,
    output_stem_prefix: str = "validation_positive_case_literature_design_space",
    plot_context_label: str = "Positive Case Design Space",
) -> None:
    global RESULTS
    global PLOTS
    global INPUT
    global SUMMARY_OUTPUT
    global SUBGROUP_OUTPUT
    global FOREST_OUTPUT
    global OUTPUT_STEM_PREFIX
    global PLOT_CONTEXT_LABEL

    RESULTS = Path(results_dir) if results_dir is not None else RESULTS
    PLOTS = Path(plots_dir) if plots_dir is not None else PLOTS
    OUTPUT_STEM_PREFIX = output_stem_prefix
    PLOT_CONTEXT_LABEL = plot_context_label
    INPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_correlation_significance.csv"
    SUMMARY_OUTPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_meta_summary.csv"
    SUBGROUP_OUTPUT = RESULTS / f"{OUTPUT_STEM_PREFIX}_meta_subgroups.csv"
    FOREST_OUTPUT = PLOTS / f"{OUTPUT_STEM_PREFIX}_meta_correlation.png"


configure_context()


def _dersimonian_laird(df: pd.DataFrame, label: str) -> dict[str, object]:
    y = df["delta_correlation"].to_numpy(dtype=float)
    v = df["delta_correlation_boot_var"].to_numpy(dtype=float)
    k = len(df)
    if k == 0:
        return {
            "group": label,
            "k": 0,
            "pooled_fixed": float("nan"),
            "pooled_fixed_se": float("nan"),
            "pooled_random": float("nan"),
            "pooled_random_se": float("nan"),
            "ci_low": float("nan"),
            "ci_high": float("nan"),
            "tau2": float("nan"),
            "Q": float("nan"),
            "I2": float("nan"),
        }

    w = 1.0 / np.maximum(v, 1e-12)
    pooled_fixed = float(np.sum(w * y) / np.sum(w))
    pooled_fixed_se = float(math.sqrt(1.0 / np.sum(w)))
    q = float(np.sum(w * (y - pooled_fixed) ** 2))
    c = float(np.sum(w) - (np.sum(w**2) / np.sum(w)))
    tau2 = float(max((q - (k - 1)) / c, 0.0)) if k > 1 and c > 0 else 0.0
    w_re = 1.0 / np.maximum(v + tau2, 1e-12)
    pooled_random = float(np.sum(w_re * y) / np.sum(w_re))
    pooled_random_se = float(math.sqrt(1.0 / np.sum(w_re)))
    ci_low = pooled_random - 1.96 * pooled_random_se
    ci_high = pooled_random + 1.96 * pooled_random_se
    i2 = float(max((q - (k - 1)) / q, 0.0)) if k > 1 and q > 0 else 0.0
    return {
        "group": label,
        "k": k,
        "pooled_fixed": pooled_fixed,
        "pooled_fixed_se": pooled_fixed_se,
        "pooled_random": pooled_random,
        "pooled_random_se": pooled_random_se,
        "ci_low": float(ci_low),
        "ci_high": float(ci_high),
        "tau2": tau2,
        "Q": q,
        "I2": i2,
    }


def build_meta_tables(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_rows = [_dersimonian_laird(df, "overall")]
    subgroup_rows: list[dict[str, object]] = []

    for mode, part in df.groupby("mode", observed=True):
        subgroup_rows.append(_dersimonian_laird(part, f"mode={mode}"))
    for variant, part in df.groupby("variant", observed=True):
        subgroup_rows.append(_dersimonian_laird(part, f"variant={variant}"))
    for (mode, variant), part in df.groupby(["mode", "variant"], observed=True):
        subgroup_rows.append(_dersimonian_laird(part, f"mode={mode};variant={variant}"))

    summary = pd.DataFrame(summary_rows)
    subgroups = pd.DataFrame(subgroup_rows)
    return summary, subgroups


def plot_forest(df: pd.DataFrame, summary: pd.DataFrame, subgroups: pd.DataFrame) -> None:
    df = df.copy()
    df["row_label"] = (
        df["model"].astype(str)
        + " | "
        + df["mode"].astype(str).map(MODE_LABELS)
        + " | "
        + df["variant"].astype(str).map(VARIANT_LABELS)
    )
    df["group_sort"] = df["mode"].map({"reasoning": 0, "joint_reasoning": 1})
    df = df.sort_values(["group_sort", "variant", "model"]).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(11.5, 0.55 * len(df) + 3.4), constrained_layout=False)
    y = np.arange(len(df))
    ax.axvline(0.0, color="0.6", linestyle="--", linewidth=1.0, zorder=0)
    ax.errorbar(
        df["delta_correlation"],
        y,
        xerr=[
            df["delta_correlation"] - df["delta_correlation_ci_low"],
            df["delta_correlation_ci_high"] - df["delta_correlation"],
        ],
        fmt="o",
        color="#2b8cbe",
        ecolor="#7aa6c2",
        elinewidth=1.3,
        capsize=2.5,
        markersize=5.5,
        zorder=2,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(df["row_label"], fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel("ΔCorrelation vs matched baseline")
    ax.set_title(f"{PLOT_CONTEXT_LABEL}: Meta-analytic Inputs for Correlation Gain")
    ax.grid(axis="x", alpha=0.18)

    overall = summary.iloc[0]
    subgroup_map = subgroups.set_index("group")
    pooled_lines = [
        ("overall", overall["pooled_random"], overall["ci_low"], overall["ci_high"]),
        (
            "single with explanation pooled",
            subgroup_map.loc["mode=reasoning", "pooled_random"],
            subgroup_map.loc["mode=reasoning", "ci_low"],
            subgroup_map.loc["mode=reasoning", "ci_high"],
        ),
        (
            "joint with explanation pooled",
            subgroup_map.loc["mode=joint_reasoning", "pooled_random"],
            subgroup_map.loc["mode=joint_reasoning", "ci_low"],
            subgroup_map.loc["mode=joint_reasoning", "ci_high"],
        ),
    ]
    text_y = len(df) + 0.4
    for idx, (label, center, lo, hi) in enumerate(pooled_lines):
        ypos = text_y + idx * 0.6
        ax.hlines(ypos, lo, hi, color="#d95f02", linewidth=3)
        ax.plot(center, ypos, marker="D", color="#d95f02", markersize=6)
        ax.text(hi + 0.01, ypos, f"{label}: {center:.3f} [{lo:.3f}, {hi:.3f}]", va="center", fontsize=8.5, color="0.25")

    ax.set_ylim(text_y + len(pooled_lines) * 0.6 + 0.5, -1)
    fig.text(
        0.5,
        0.01,
        "Random-effects meta-analysis using paired-bootstrap within-condition variance.",
        ha="center",
        fontsize=9,
        color="0.3",
    )
    fig.tight_layout(rect=[0.03, 0.03, 1, 0.98])
    fig.savefig(FOREST_OUTPUT, dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_results_dir(RESULTS)
    ensure_plot_dir(PLOTS)
    df = pd.read_csv(INPUT)
    summary, subgroups = build_meta_tables(df)
    summary.to_csv(SUMMARY_OUTPUT, index=False)
    subgroups.to_csv(SUBGROUP_OUTPUT, index=False)
    plot_forest(df, summary, subgroups)
    print(SUMMARY_OUTPUT)
    print(SUBGROUP_OUTPUT)
    print(FOREST_OUTPUT)


if __name__ == "__main__":
    main()
