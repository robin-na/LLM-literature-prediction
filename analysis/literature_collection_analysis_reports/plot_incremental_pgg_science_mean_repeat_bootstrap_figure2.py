from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

from analyze_validation_incremental_pgg_science_repeat30 import (
    CONDITION_COLORS,
    CONDITION_LABELS,
    CONDITION_ORDER,
    PLOTS_DIR,
    RESULTS_DIR,
)


REPEAT_ROWS_CSV = RESULTS_DIR / "incremental_pgg_science_repeat_rows.csv"
SUMMARY_CSV = RESULTS_DIR / "incremental_pgg_science_mean_repeat_bootstrap_figure2_summary.csv"
PLOT_ROWS_CSV = RESULTS_DIR / "incremental_pgg_science_mean_repeat_bootstrap_figure2_plot_rows.csv"
REPEAT_DETAIL_CSV = RESULTS_DIR / "incremental_pgg_science_mean_repeat_bootstrap_figure2_repeat_detail.csv"
OUTPUT_STEM = "incremental_pgg_science_mean_repeat_bootstrap_figure2"
N_BOOT = 50000
BASE_SEED = 20260408


def bootstrap_mean_ci(values: np.ndarray, *, n_boot: int, seed: int) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return {
            "n_repeats": 0,
            "mean": float("nan"),
            "sd": float("nan"),
            "se": float("nan"),
            "ci95_low": float("nan"),
            "ci95_high": float("nan"),
            "ci99_low": float("nan"),
            "ci99_high": float("nan"),
        }
    if arr.size == 1:
        value = float(arr[0])
        return {
            "n_repeats": 1,
            "mean": value,
            "sd": float("nan"),
            "se": float("nan"),
            "ci95_low": value,
            "ci95_high": value,
            "ci99_low": value,
            "ci99_high": value,
        }

    rng = np.random.default_rng(seed)
    idx = rng.integers(0, arr.size, size=(n_boot, arr.size))
    boot_means = arr[idx].mean(axis=1)
    return {
        "n_repeats": int(arr.size),
        "mean": float(arr.mean()),
        "sd": float(arr.std(ddof=1)),
        "se": float(arr.std(ddof=1) / np.sqrt(arr.size)),
        "ci95_low": float(np.quantile(boot_means, 0.025)),
        "ci95_high": float(np.quantile(boot_means, 0.975)),
        "ci99_low": float(np.quantile(boot_means, 0.005)),
        "ci99_high": float(np.quantile(boot_means, 0.995)),
    }


def build_plot_rows() -> tuple[pd.DataFrame, pd.DataFrame]:
    repeat_rows = pd.read_csv(REPEAT_ROWS_CSV)
    repeat_detail = repeat_rows.loc[:, ["model", "condition", "repeat", "correlation"]].copy()

    rows: list[dict[str, object]] = []
    for idx, ((model, condition), part) in enumerate(repeat_detail.groupby(["model", "condition"], sort=False)):
        summary = bootstrap_mean_ci(
            part["correlation"].to_numpy(dtype=float),
            n_boot=N_BOOT,
            seed=BASE_SEED + idx,
        )
        rows.append(
            {
                "model": model,
                "condition": condition,
                "correlation": summary["mean"],
                "repeat_sd": summary["sd"],
                "repeat_se": summary["se"],
                "ci_low": summary["ci95_low"],
                "ci_high": summary["ci95_high"],
                "ci99_low": summary["ci99_low"],
                "ci99_high": summary["ci99_high"],
                "n_repeats": summary["n_repeats"],
            }
        )

    plot_df = pd.DataFrame(rows)
    baseline_order = (
        plot_df.loc[plot_df["condition"] == "baseline", ["model", "correlation"]]
        .sort_values("correlation", ascending=False)["model"]
        .tolist()
    )
    plot_df["model"] = pd.Categorical(plot_df["model"], categories=baseline_order, ordered=True)
    plot_df["condition"] = pd.Categorical(plot_df["condition"], categories=CONDITION_ORDER, ordered=True)
    plot_df = plot_df.sort_values(["model", "condition"]).reset_index(drop=True)

    repeat_detail["model"] = pd.Categorical(repeat_detail["model"], categories=baseline_order, ordered=True)
    repeat_detail["condition"] = pd.Categorical(repeat_detail["condition"], categories=CONDITION_ORDER, ordered=True)
    repeat_detail = repeat_detail.sort_values(["model", "condition", "repeat"]).reset_index(drop=True)
    return plot_df, repeat_detail


def plot_figure2_style(plot_df: pd.DataFrame, repeat_detail: pd.DataFrame, *, output_stem: str) -> None:
    sns.set_theme(style="white")
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.0, 7.9))
    model_order = plot_df["model"].cat.categories.tolist()
    y_positions = np.arange(len(model_order))
    offsets = {"baseline": -0.25, "science_gpt41": 0.0, "science_gpt51": 0.25}

    for condition in CONDITION_ORDER:
        part = (
            plot_df.loc[plot_df["condition"] == condition]
            .set_index("model")
            .reindex(model_order)
            .reset_index()
        )
        y = y_positions + offsets[condition]
        ax.barh(
            y,
            part["correlation"].to_numpy(dtype=float),
            color=CONDITION_COLORS[condition],
            edgecolor="#4b5563",
            linewidth=0.8,
            height=0.22,
            zorder=2,
            label=CONDITION_LABELS[condition],
        )
        xerr = np.vstack(
            [
                part["correlation"].to_numpy(dtype=float) - part["ci_low"].to_numpy(dtype=float),
                part["ci_high"].to_numpy(dtype=float) - part["correlation"].to_numpy(dtype=float),
            ]
        )
        ax.errorbar(
            part["correlation"].to_numpy(dtype=float),
            y,
            xerr=xerr,
            fmt="none",
            ecolor=(17 / 255, 24 / 255, 39 / 255, 0.28),
            elinewidth=0.9,
            capsize=2.5,
            zorder=3,
        )

        for idx, model in enumerate(model_order):
            repeats = repeat_detail.loc[
                (repeat_detail["model"] == model) & (repeat_detail["condition"] == condition),
                "correlation",
            ].to_numpy(dtype=float)
            if repeats.size == 0:
                continue
            jitter = np.linspace(-0.08, 0.08, repeats.size) if repeats.size > 1 else np.array([0.0])
            ax.scatter(
                repeats,
                np.full(repeats.size, y_positions[idx] + offsets[condition]) + jitter,
                s=10,
                color="#111827",
                alpha=0.25,
                linewidths=0.0,
                zorder=4,
            )

    ax.set_xlim(0.0, 1.0)
    ax.set_xticks(np.arange(0.0, 1.01, 0.1))
    ax.set_xlabel("Mean correlation with true treatment outcome across 30 repeats")
    ax.set_yticks(y_positions, model_order)
    ax.invert_yaxis()
    ax.grid(False)

    legend_items = [
        Line2D([0], [0], color=CONDITION_COLORS["baseline"], linewidth=8, label=CONDITION_LABELS["baseline"]),
        Line2D([0], [0], color=CONDITION_COLORS["science_gpt41"], linewidth=8, label=CONDITION_LABELS["science_gpt41"]),
        Line2D([0], [0], color=CONDITION_COLORS["science_gpt51"], linewidth=8, label=CONDITION_LABELS["science_gpt51"]),
    ]
    ax.legend(
        handles=legend_items,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=2,
        columnspacing=1.2,
        handlelength=2.4,
        borderaxespad=0.0,
    )
    fig.text(
        0.99,
        0.02,
        "Bars show the mean of the 30 run-level correlations; whiskers show the bootstrap 95% CI for that mean.",
        ha="right",
        va="bottom",
        fontsize=9.4,
        color="#4b5563",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOTS_DIR / f"{output_stem}.png", dpi=240, bbox_inches="tight")
    fig.savefig(PLOTS_DIR / f"{output_stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    plot_df, repeat_detail = build_plot_rows()
    plot_df.to_csv(SUMMARY_CSV, index=False)
    plot_df.to_csv(PLOT_ROWS_CSV, index=False)
    repeat_detail.to_csv(REPEAT_DETAIL_CSV, index=False)
    plot_figure2_style(plot_df, repeat_detail, output_stem=OUTPUT_STEM)


if __name__ == "__main__":
    main()
