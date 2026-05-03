from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


RESULTS_DIR = ROOT / "results" / "validation" / "literature_incremental_pgg_science_repeat30"
PLOTS_DIR = ROOT / "plots" / "validation" / "literature_incremental_pgg_science_repeat30"
CURVE_CSV = RESULTS_DIR / "incremental_pgg_science_ensemble_size_curve.csv"

CONDITION_ORDER = ["baseline", "science_gpt41", "science_gpt51"]
CONDITION_LABELS = {
    "baseline": "No augmentation",
    "science_gpt41": "PGG Science report (GPT-4.1)",
    "science_gpt51": "PGG Science report (GPT-5.1)",
}
KEY_K = [1, 3, 5, 10, 15, 20, 30]


def load_curve() -> pd.DataFrame:
    df = pd.read_csv(CURVE_CSV)
    df["condition"] = pd.Categorical(df["condition"], categories=CONDITION_ORDER, ordered=True)
    df["corr_interval80_width"] = df["p90"] - df["p10"]
    df["corr_interval90_width"] = df["p95"] - df["p05"]
    return df.sort_values(["condition", "model", "k_runs"]).reset_index(drop=True)


def summarize_by_k(curve: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for (condition, k_runs), part in curve.groupby(["condition", "k_runs"], observed=True):
        rows.append(
            {
                "condition": condition,
                "k_runs": int(k_runs),
                "n_model_conditions": int(len(part)),
                "median_sampling_sd": float(part["sd"].median()),
                "mean_sampling_sd": float(part["sd"].mean()),
                "max_sampling_sd": float(part["sd"].max()),
                "median_corr_interval80_width": float(part["corr_interval80_width"].median()),
                "mean_corr_interval80_width": float(part["corr_interval80_width"].mean()),
                "max_corr_interval80_width": float(part["corr_interval80_width"].max()),
                "median_corr_interval90_width": float(part["corr_interval90_width"].median()),
                "mean_corr_interval90_width": float(part["corr_interval90_width"].mean()),
                "max_corr_interval90_width": float(part["corr_interval90_width"].max()),
                "median_mean_abs_gap_to_ensemble30": float(part["mean_abs_gap_to_ensemble30"].median()),
                "mean_mean_abs_gap_to_ensemble30": float(part["mean_abs_gap_to_ensemble30"].mean()),
                "max_mean_abs_gap_to_ensemble30": float(part["mean_abs_gap_to_ensemble30"].max()),
            }
        )
    out = pd.DataFrame(rows)
    out["condition"] = pd.Categorical(out["condition"], categories=CONDITION_ORDER, ordered=True)
    return out.sort_values(["condition", "k_runs"]).reset_index(drop=True)


def summarize_key_k(curve: pd.DataFrame) -> pd.DataFrame:
    sub = curve.loc[curve["k_runs"].isin(KEY_K)].copy()
    sub = sub.loc[
        :,
        [
            "model",
            "condition",
            "k_runs",
            "mean",
            "sd",
            "p05",
            "p95",
            "corr_interval90_width",
            "ensemble30_correlation",
            "mean_abs_gap_to_ensemble30",
            "p90_abs_gap_to_ensemble30",
            "p95_abs_gap_to_ensemble30",
        ],
    ]
    sub["condition"] = pd.Categorical(sub["condition"], categories=CONDITION_ORDER, ordered=True)
    return sub.sort_values(["condition", "model", "k_runs"]).reset_index(drop=True)


def plot_uncertainty_vs_k(summary_by_k: pd.DataFrame) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.6), sharex=True)
    plot_specs = [
        ("median_sampling_sd", "Median sampling SD"),
        ("median_corr_interval90_width", "Median 90% interval width"),
        ("median_mean_abs_gap_to_ensemble30", "Median mean abs gap to 30-run ensemble"),
    ]
    colors = {"baseline": "#9ca3af", "science_gpt41": "#2563eb", "science_gpt51": "#f28e2b"}

    for ax, (metric, title) in zip(axes, plot_specs):
        for condition in CONDITION_ORDER:
            sub = summary_by_k.loc[summary_by_k["condition"] == condition].copy()
            ax.plot(
                sub["k_runs"],
                sub[metric],
                color=colors[condition],
                linewidth=2.0,
                label=CONDITION_LABELS[condition],
            )
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Number of runs averaged")
        ax.grid(False)

    axes[0].set_ylabel("Uncertainty")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.03))
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_sampling_uncertainty_vs_k.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / "incremental_pgg_science_sampling_uncertainty_vs_k.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    curve = load_curve()
    summary_by_k = summarize_by_k(curve)
    key_k = summarize_key_k(curve)
    summary_by_k.to_csv(RESULTS_DIR / "incremental_pgg_science_sampling_uncertainty_by_k.csv", index=False)
    key_k.to_csv(RESULTS_DIR / "incremental_pgg_science_sampling_uncertainty_key_k.csv", index=False)
    plot_uncertainty_vs_k(summary_by_k)


if __name__ == "__main__":
    main()
