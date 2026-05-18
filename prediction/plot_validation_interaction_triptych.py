from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_validation_interaction_alignment import load_or_compute_enet_validation_shap


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir
DATA = ROOT / "science-data_and_code" / "data" / "processed_data"


def fit_line(x: pd.Series, y: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    x = x.astype(float)
    y = y.astype(float)
    if len(x) < 2 or np.allclose(x.std(ddof=0), 0):
        xs = np.sort(x.unique())
        return xs, np.repeat(y.mean(), len(xs))
    xs = np.linspace(float(x.min()), float(x.max()), 50)
    slope, intercept = np.polyfit(x, y, 1)
    ys = intercept + slope * xs
    return xs, ys


def load_best_variant() -> tuple[str, str, float, float]:
    perf = pd.read_csv(RESULTS / "granular_performance_delta_r2_table.csv")
    val = perf[(perf["wave"] == "validation") & (perf["input_group"] != "baseline")].copy()
    best = val.sort_values("delta_r2_vs_matched_baseline", ascending=False).iloc[0]
    baseline_map = {
        "single": "baseline",
        "reasoning": "baseline_reasoning",
        "joint": "baseline_joint",
        "joint_reasoning": "baseline_joint_reasoning",
    }
    return (
        best["variation"],
        baseline_map[best["mode"]],
        float(best["delta_r2_vs_matched_baseline"]),
        float(best["r2"]),
    )


def load_llm_effects(val_df: pd.DataFrame) -> pd.DataFrame:
    pred = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    q_cols = [c for c in pred.columns if c.startswith("Q")]
    control = 100 * val_df["control_itt_efficiency"].reset_index(drop=True)
    rows = []
    for _, row in pred.iterrows():
        effect = row[q_cols].astype(float).reset_index(drop=True) - control
        temp = val_df.copy()
        temp["variation"] = row["variation"]
        temp["pred_effect"] = effect.values
        temp["q_idx"] = np.arange(1, len(temp) + 1)
        rows.append(temp)
    return pd.concat(rows, ignore_index=True)


def plot_game_length_panel(ax, source_df: pd.DataFrame, y_col: str, chat: int, source_color: str, source_label: str) -> None:
    peer_specs = [
        (0, "Peer outcomes hidden", "s", "-"),
        (1, "Peer outcomes visible", "o", "--"),
    ]
    for peer, label, marker, linestyle in peer_specs:
        sub = source_df[
            (source_df["CONFIG_chat"] == chat) & (source_df["CONFIG_showOtherSummaries"] == peer)
        ].copy()
        if sub.empty:
            continue
        ax.scatter(
            sub["CONFIG_numRounds"],
            sub[y_col],
            color=source_color,
            marker=marker,
            s=28,
            alpha=0.35,
        )
        xs, ys = fit_line(sub["CONFIG_numRounds"], sub[y_col])
        ax.plot(xs, ys, color=source_color, linestyle=linestyle, linewidth=2.0, label=label if source_label is None else f"{source_label} | {label}")
    ax.axhline(0, color="#c7c7c7", linewidth=1)
    ax.grid(alpha=0.18)


def framing_means(source_df: pd.DataFrame, y_col: str, peer: int, all_or_nothing: int) -> pd.DataFrame:
    sub = source_df[
        (source_df["CONFIG_showOtherSummaries"] == peer) & (source_df["CONFIG_allOrNothing"] == all_or_nothing)
    ].copy()
    out = (
        sub.groupby("CONFIG_defaultContribProp", as_index=False)[y_col]
        .mean()
        .sort_values("CONFIG_defaultContribProp")
    )
    out["frame_label"] = out["CONFIG_defaultContribProp"].map({0: "Opt-in", 1: "Opt-out"})
    out["frame_x"] = out["CONFIG_defaultContribProp"].map({0: 0, 1: 1})
    return out


def plot_framing_panel(ax, source_df: pd.DataFrame, y_col: str, peer: int, source_color: str, source_label: str) -> None:
    contrib_specs = [
        (0, "Variable contribution", "D", "-."),
        (1, "All-or-nothing contribution", "v", ":"),
    ]
    for all_or_nothing, label, marker, linestyle in contrib_specs:
        means = framing_means(source_df, y_col, peer, all_or_nothing)
        if means.empty:
            continue
        ax.plot(
            means["frame_x"],
            means[y_col],
            color=source_color,
            linestyle=linestyle,
            marker=marker,
            linewidth=2.0,
            markersize=7,
            label=label if source_label is None else f"{source_label} | {label}",
        )
    ax.axhline(0, color="#c7c7c7", linewidth=1)
    ax.set_xticks([0, 1], ["Opt-in", "Opt-out"])
    ax.grid(alpha=0.18)


def build_source_frames(best_variant: str, baseline_variant: str) -> dict[str, tuple[pd.DataFrame, str, str]]:
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    shap_df = load_or_compute_enet_validation_shap().copy()
    llm_df = load_llm_effects(val_df)
    metrics = pd.read_csv(RESULTS / "prediction_positive_case_variations_41_metrics.csv")
    control = 100 * val_df["control_itt_efficiency"].to_numpy()
    treatment = 100 * val_df["treatment_itt_efficiency"].to_numpy()
    null_mse = float(np.mean((control - treatment) ** 2))

    def lookup_r2(variation: str) -> float:
        rmse = float(metrics.loc[metrics["variation"] == variation, "rmse"].iloc[0])
        return 1.0 - (rmse**2) / null_mse

    baseline_r2 = lookup_r2(baseline_variant)
    best_r2 = lookup_r2(best_variant)

    return {
        "E-net target": (
            shap_df,
            "shap",
            "Learning-trained E-net target\n(validation SHAP)",
        ),
        baseline_variant: (
            llm_df[llm_df["variation"] == baseline_variant].copy(),
            "pred_effect",
            f"No augmentation\n{baseline_variant}, R^2={baseline_r2:.3f}",
        ),
        best_variant: (
            llm_df[llm_df["variation"] == best_variant].copy(),
            "pred_effect",
            f"Best augmented\n{best_variant}, R^2={best_r2:.3f}",
        ),
    }


def main() -> None:
    best_variant, baseline_variant, best_delta_r2, _ = load_best_variant()
    alignment = pd.read_csv(RESULTS / "validation_interaction_alignment_vs_baseline.csv")
    selected_row = alignment.loc[alignment["variation"] == best_variant].iloc[0]

    sources = build_source_frames(best_variant, baseline_variant)
    fig, axes = plt.subplots(4, 3, figsize=(15.5, 15.8), constrained_layout=True)

    colors = {
        "E-net target": "#111111",
        baseline_variant: "#4c78a8",
        best_variant: "#e45756",
    }

    row_titles = [
        "A. Communication disabled: game-length interaction",
        "B. Communication enabled: game-length interaction",
        "C. Peer outcomes hidden: contribution-framing interaction",
        "D. Peer outcomes visible: contribution-framing interaction",
    ]

    for col_idx, (source_key, (df, y_kind, col_title)) in enumerate(sources.items()):
        axes[0, col_idx].set_title(col_title, fontsize=12)
        y_col_num = "shap_CONFIG_numRounds" if y_kind == "shap" else "pred_effect"
        y_col_frame = "shap_CONFIG_defaultContribProp" if y_kind == "shap" else "pred_effect"

        plot_game_length_panel(axes[0, col_idx], df, y_col_num, chat=0, source_color=colors[source_key], source_label=None)
        plot_game_length_panel(axes[1, col_idx], df, y_col_num, chat=1, source_color=colors[source_key], source_label=None)
        plot_framing_panel(axes[2, col_idx], df, y_col_frame, peer=0, source_color=colors[source_key], source_label=None)
        plot_framing_panel(axes[3, col_idx], df, y_col_frame, peer=1, source_color=colors[source_key], source_label=None)

    for row_idx, title in enumerate(row_titles):
        axes[row_idx, 0].set_ylabel(title, fontsize=11)

    for col_idx in range(3):
        axes[0, col_idx].set_xlabel("Game Length")
        axes[1, col_idx].set_xlabel("Game Length")
        axes[2, col_idx].set_xlabel("Contribution Framing")
        axes[3, col_idx].set_xlabel("Contribution Framing")

    legend_lines = [
        plt.Line2D([0], [0], color="#555555", linestyle="-", marker="s", label="Peer outcomes hidden"),
        plt.Line2D([0], [0], color="#555555", linestyle="--", marker="o", label="Peer outcomes visible"),
        plt.Line2D([0], [0], color="#555555", linestyle="-.", marker="D", label="Variable contribution"),
        plt.Line2D([0], [0], color="#555555", linestyle=":", marker="v", label="All-or-nothing contribution"),
    ]
    fig.legend(handles=legend_lines, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.01))

    fig.suptitle(
        "Validation Figure-5 comparison: E-net target vs no augmentation vs best augmented variant",
        fontsize=16,
        y=1.03,
    )
    fig.text(
        0.5,
        0.01,
        (
            f"Best augmented variant chosen by validation ΔR²: {best_variant} "
            f"(ΔR² vs matched baseline = {best_delta_r2:+.3f}). "
            f"For this variant, game-length interaction alignment improves slightly "
            f"({selected_row['delta_numrounds_alignment_corr_vs_baseline']:+.3f}) "
            f"but contribution-framing alignment worsens materially "
            f"({selected_row['delta_framing_alignment_corr_vs_baseline']:+.3f}). "
            "Validation lacks the hidden + all-or-nothing + opt-in framing cell, so those line segments are incomplete."
        ),
        ha="center",
        va="bottom",
        fontsize=9.5,
        color="#444444",
    )

    png_path = PLOTS / "validation_interaction_best_augmented_vs_baseline_vs_enet.png"
    pdf_path = PLOTS / "validation_interaction_best_augmented_vs_baseline_vs_enet.pdf"
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")

    summary = pd.DataFrame(
        [
            {
                "best_augmented_variant": best_variant,
                "matched_baseline_variant": baseline_variant,
                "best_augmented_delta_r2_vs_matched_baseline": best_delta_r2,
                "delta_numrounds_alignment_corr_vs_baseline": selected_row["delta_numrounds_alignment_corr_vs_baseline"],
                "delta_framing_alignment_corr_vs_baseline": selected_row["delta_framing_alignment_corr_vs_baseline"],
                "combined_alignment_corr_vs_baseline": selected_row["combined_alignment_corr_vs_baseline"],
            }
        ]
    )
    summary.to_csv(RESULTS / "validation_interaction_best_augmented_summary.csv", index=False)


if __name__ == "__main__":
    main()
