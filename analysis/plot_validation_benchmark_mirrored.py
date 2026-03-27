from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir

NULL_MSE = 50.847465
CANONICAL_BASELINE_RMSE = 6.704339
CANONICAL_BASELINE_CORR = 0.641394
CANONICAL_BASELINE_DA = 0.65


def r2_from_rmse(rmse: float) -> float:
    return 1.0 - (rmse ** 2) / NULL_MSE


def load_table() -> pd.DataFrame:
    baseline_comp = pd.read_csv(
        RESULTS / "prediction_positive_case_variations_baseline_comparison.csv"
    )
    nano = pd.read_csv(RESULTS / "prediction_crosswave_variations_41nano_validation_metrics.csv")

    rows = [
        {
            "label": "GPT-4.1 baseline",
            "model": "GPT-4.1",
            "variation": "baseline",
            "rmse": CANONICAL_BASELINE_RMSE,
            "correlation": CANONICAL_BASELINE_CORR,
            "directional_accuracy": CANONICAL_BASELINE_DA,
            "r2": r2_from_rmse(CANONICAL_BASELINE_RMSE),
        }
    ]
    keep = ["baseline_reasoning", "baseline_joint", "baseline_joint_reasoning"]
    for variation in keep:
        row = baseline_comp.loc[baseline_comp["variation"] == variation].iloc[0]
        rows.append(
            {
                "label": f"GPT-4.1 {variation}",
                "model": "GPT-4.1",
                "variation": variation,
                "rmse": float(row["rmse"]),
                "correlation": float(row["correlation"]),
                "directional_accuracy": float(row["directional_accuracy"]),
                "r2": r2_from_rmse(float(row["rmse"])),
            }
        )

    for variation in [
        "baseline",
        "baseline_reasoning",
        "baseline_joint",
        "baseline_joint_reasoning",
    ]:
        row = nano.loc[nano["variation"] == variation].iloc[0]
        rows.append(
            {
                "label": f"GPT-4.1-nano {variation}",
                "model": "GPT-4.1-nano",
                "variation": variation,
                "rmse": float(row["rmse"]),
                "correlation": float(row["correlation"]),
                "directional_accuracy": float(row["directional_accuracy"]),
                "r2": r2_from_rmse(float(row["rmse"])),
            }
        )
    order = [
        "GPT-4.1 baseline",
        "GPT-4.1 baseline_reasoning",
        "GPT-4.1 baseline_joint",
        "GPT-4.1 baseline_joint_reasoning",
        "GPT-4.1-nano baseline",
        "GPT-4.1-nano baseline_reasoning",
        "GPT-4.1-nano baseline_joint",
        "GPT-4.1-nano baseline_joint_reasoning",
    ]
    return pd.DataFrame(rows).set_index("label").loc[order].reset_index()


def main() -> None:
    df = load_table()
    df.to_csv(RESULTS / "validation_benchmark_mirrored_table.csv", index=False)

    colors = {"GPT-4.1": "#1f77b4", "GPT-4.1-nano": "#ff7f0e"}
    metrics = [
        ("rmse", "RMSE", "lower is better"),
        ("r2", r"$R^2$", "higher is better"),
        ("correlation", "Correlation", "higher is better"),
        ("directional_accuracy", "Directional Accuracy", "higher is better"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(13.5, 8.4), sharey=True)
    axes = axes.flatten()
    y = list(range(len(df)))[::-1]

    for ax, (col, title, subtitle) in zip(axes, metrics):
        for idx, (_, row) in enumerate(df.iterrows()):
            ypos = y[idx]
            ax.barh(ypos, row[col], color=colors[row["model"]], height=0.68)
            value = row[col]
            ha = "left" if value >= 0 else "right"
            x = value + 0.01 if value >= 0 else value - 0.01
            fmt = "{:.3f}" if col != "rmse" else "{:.2f}"
            ax.text(x, ypos, fmt.format(value), va="center", ha=ha, fontsize=8.5)
        ax.set_title(f"{title}\n({subtitle})", fontsize=12)
        ax.grid(axis="x", alpha=0.25)
        if col == "rmse":
            ax.set_xlim(5.0, 10.8)
        elif col == "r2":
            ax.set_xlim(-1.1, 0.45)
            ax.axvline(0, color="#777777", linestyle="--", linewidth=1)
        elif col == "correlation":
            ax.set_xlim(0.0, 0.85)
        else:
            ax.set_xlim(0.3, 0.75)
        ax.set_yticks(y, df["label"])

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=colors[model], label=model)
        for model in ["GPT-4.1", "GPT-4.1-nano"]
    ]
    fig.legend(handles=legend_handles, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.985))
    fig.suptitle(
        "Validation Benchmark Before Augmentation",
        fontsize=18,
        y=0.995,
    )
    fig.text(
        0.5,
        0.01,
        r"$R^2$ uses the control-equals-treatment null on the validation wave.",
        ha="center",
        fontsize=10,
        color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))

    fig.savefig(PLOTS / "validation_benchmark_mirrored.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_benchmark_mirrored.pdf", bbox_inches="tight")


if __name__ == "__main__":
    main()
