from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import LEARNING_PLOTS as PLOTS, ensure_plot_dir
LEARN_PATH = ROOT / "science_data" / "data" / "processed_data" / "df_paired_learn.csv"


def r2_from_rmse(rmse: float, null_mse: float) -> float:
    return 1.0 - (rmse ** 2) / null_mse


def load_table() -> pd.DataFrame:
    learn = pd.read_csv(LEARN_PATH)
    null_mse = ((100 * learn["treatment_itt_efficiency"] - 100 * learn["control_itt_efficiency"]) ** 2).mean()

    gpt41 = pd.read_csv(RESULTS / "prediction_learning_wave_elicitation_41_metrics.csv")
    nano = pd.read_csv(RESULTS / "prediction_crosswave_variations_41nano_learning_metrics.csv")

    keep = ["baseline", "baseline_reasoning", "baseline_joint", "baseline_joint_reasoning"]
    rows = []
    for source_df, model in [(gpt41, "GPT-4.1"), (nano, "GPT-4.1-nano")]:
        part = source_df.loc[source_df["variation"].isin(keep)].copy()
        for _, row in part.iterrows():
            rows.append(
                {
                    "label": f"{model} {row['variation']}",
                    "model": model,
                    "variation": row["variation"],
                    "rmse": float(row["rmse"]),
                    "correlation": float(row["correlation"]),
                    "directional_accuracy": float(row["directional_accuracy"]),
                    "r2": r2_from_rmse(float(row["rmse"]), null_mse),
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
    df.to_csv(RESULTS / "learning_r2_benchmark_table.csv", index=False)

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
            ax.set_xlim(13.0, 18.8)
        elif col == "r2":
            ax.set_xlim(-0.5, 0.15)
            ax.axvline(0, color="#777777", linestyle="--", linewidth=1)
        elif col == "correlation":
            ax.set_xlim(0.0, 0.45)
        else:
            ax.set_xlim(0.4, 0.7)
        ax.set_yticks(y, df["label"])

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=colors[model], label=model)
        for model in ["GPT-4.1", "GPT-4.1-nano"]
    ]
    fig.legend(handles=legend_handles, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.985))
    fig.suptitle(
        "Learning-Wave Benchmark Before Augmentation",
        fontsize=18,
        y=0.995,
    )
    fig.text(
        0.5,
        0.01,
        r"$R^2$ uses the control-equals-treatment null on the learning wave.",
        ha="center",
        fontsize=10,
        color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))

    fig.savefig(PLOTS / "learning_r2_benchmark.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "learning_r2_benchmark.pdf", bbox_inches="tight")


if __name__ == "__main__":
    main()
