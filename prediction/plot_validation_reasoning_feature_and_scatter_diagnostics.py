from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_validation_interaction_alignment import (
    compute_enet_validation_permutation_importance,
    load_or_compute_enet_validation_shap,
    parse_variation,
)


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import VALIDATION_PLOTS as PLOTS, ensure_plot_dir
DATA = ROOT / "science-data_and_code" / "data" / "processed_data"

FEATURES = [
    "CONFIG_chat",
    "CONFIG_defaultContribProp",
    "CONFIG_allOrNothing",
    "CONFIG_numRounds",
    "CONFIG_showOtherSummaries",
    "CONFIG_rewardExists",
    "CONFIG_showNRounds",
    "CONFIG_MPCR",
    "CONFIG_punishmentCost",
    "CONFIG_showPunishmentId",
    "CONFIG_playerCount",
    "CONFIG_punishmentTech",
]

FEATURE_LABELS = {
    "CONFIG_chat": "Communication",
    "CONFIG_defaultContribProp": "Contribution Framing",
    "CONFIG_allOrNothing": "Contribution Type",
    "CONFIG_numRounds": "Game Length",
    "CONFIG_showOtherSummaries": "Peer Outcome Visibility",
    "CONFIG_rewardExists": "Reward",
    "CONFIG_showNRounds": "Horizon Knowledge",
    "CONFIG_MPCR": "Return Rate (MPCR)",
    "CONFIG_punishmentCost": "Peer Incentive Cost",
    "CONFIG_showPunishmentId": "Actor Anonymity",
    "CONFIG_playerCount": "Group Size",
    "CONFIG_punishmentTech": "Punishment Technology",
}

REASONING_CASES = [
    ("baseline_reasoning", "Baseline reasoning", "#4c78a8"),
    ("both_contrastive_reasoning", "Best augmented reasoning", "#59a14f"),
    ("both_ensemble_reasoning", "Degraded augmented reasoning", "#e15759"),
]

MODE_BASELINE = {
    "single": "baseline",
    "reasoning": "baseline_reasoning",
    "joint": "baseline_joint",
    "joint_reasoning": "baseline_joint_reasoning",
}


def compute_r2_from_rmse(rmse: float, val_df: pd.DataFrame) -> float:
    control = 100 * val_df["control_itt_efficiency"].to_numpy()
    treatment = 100 * val_df["treatment_itt_efficiency"].to_numpy()
    null_mse = float(np.mean((control - treatment) ** 2))
    return 1.0 - (rmse**2) / null_mse


def signed_effect(x: pd.Series, y: pd.Series) -> float:
    x = x.astype(float)
    y = y.astype(float)
    uniq = sorted(pd.unique(x))
    if set(uniq).issubset({0, 1}):
        g1 = y[x == 1]
        g0 = y[x == 0]
        if len(g1) == 0 or len(g0) == 0:
            return np.nan
        return float(g1.mean() - g0.mean())
    if len(x) < 2 or np.allclose(x.std(ddof=0), 0):
        return np.nan
    slope = np.polyfit(x, y, 1)[0]
    return float(slope * x.std(ddof=0))


def slope_through_origin(x: np.ndarray, y: np.ndarray) -> float:
    denom = float(np.sum(x**2))
    if denom == 0:
        return np.nan
    return float(np.sum(x * y) / denom)


def load_variant_effects(val_df: pd.DataFrame) -> pd.DataFrame:
    pred = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    q_cols = [c for c in pred.columns if c.startswith("Q")]
    control = 100 * val_df["control_itt_efficiency"].reset_index(drop=True)
    rows = []
    for _, row in pred.iterrows():
        temp = val_df.copy()
        temp["variation"] = row["variation"]
        temp["pred_effect"] = row[q_cols].astype(float).reset_index(drop=True).values - control.values
        input_group, family, mode = parse_variation(row["variation"])
        temp["input_group"] = input_group
        temp["family"] = family
        temp["mode"] = mode
        rows.append(temp)
    return pd.concat(rows, ignore_index=True)


def build_feature_targets() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    shap_df = load_or_compute_enet_validation_shap().copy()
    imp_df = compute_enet_validation_permutation_importance().copy()
    llm_df = load_variant_effects(val_df)
    metrics = pd.read_csv(RESULTS / "prediction_positive_case_variations_41_metrics.csv")

    target_rows = []
    for feature in FEATURES:
        target_rows.append(
            {
                "feature": feature,
                "feature_label": FEATURE_LABELS[feature],
                "target_signed_effect": signed_effect(val_df[feature], 100 * shap_df[f"shap_{feature}"]),
                "enet_pct_increase_rmse": float(
                    imp_df.loc[imp_df["feature"] == feature, "pct_increase_in_error"].iloc[0]
                ),
            }
        )
    target_df = pd.DataFrame(target_rows).sort_values("enet_pct_increase_rmse", ascending=False).reset_index(drop=True)

    case_rows = []
    for variation, _, _ in REASONING_CASES:
        sub = llm_df[llm_df["variation"] == variation].copy()
        row = {"variation": variation}
        for feature in FEATURES:
            row[feature] = signed_effect(sub[feature], sub["pred_effect"])
        case_rows.append(row)
    case_df = pd.DataFrame(case_rows)

    metrics_rows = []
    for variation, label, _ in REASONING_CASES:
        metric_row = metrics.loc[metrics["variation"] == variation].iloc[0]
        metrics_rows.append(
            {
                "variation": variation,
                "label": label,
                "rmse": float(metric_row["rmse"]),
                "correlation": float(metric_row["correlation"]),
                "directional_accuracy": float(metric_row["directional_accuracy"]),
                "r2": compute_r2_from_rmse(float(metric_row["rmse"]), val_df),
            }
        )
    metrics_df = pd.DataFrame(metrics_rows)
    return target_df, case_df, metrics_df


def plot_reasoning_feature_figure(target_df: pd.DataFrame, case_df: pd.DataFrame, metrics_df: pd.DataFrame) -> None:
    order = target_df["feature"].tolist()
    labels = target_df["feature_label"].tolist()
    y = np.arange(len(order))

    fig, axes = plt.subplots(1, 3, figsize=(19, 10.5), sharey=True, constrained_layout=True)
    ax_imp, ax_best, ax_bad = axes

    ax_imp.barh(y, target_df["enet_pct_increase_rmse"], color="#9c755f", alpha=0.85)
    ax_imp.set_title("A. Validation E-net importance", fontsize=14)
    ax_imp.set_xlabel("% increase in RMSE when permuted", fontsize=12)
    ax_imp.set_yticks(y, labels, fontsize=12)
    ax_imp.invert_yaxis()
    ax_imp.grid(axis="x", alpha=0.2)

    target_map = target_df.set_index("feature")["target_signed_effect"]

    def draw_compare(ax, comparison_variation: str, title: str, color: str) -> None:
        baseline_map = case_df.loc[case_df["variation"] == "baseline_reasoning"].iloc[0].to_dict()
        comp_map = case_df.loc[case_df["variation"] == comparison_variation].iloc[0].to_dict()
        target_vals = np.array([target_map[f] for f in order], dtype=float)
        baseline_vals = np.array([baseline_map[f] for f in order], dtype=float)
        comp_vals = np.array([comp_map[f] for f in order], dtype=float)
        for yi, b, c in zip(y, baseline_vals, comp_vals):
            ax.plot([b, c], [yi, yi], color="#c7c7c7", linewidth=2, zorder=1)
        ax.scatter(target_vals, y, color="#111111", marker="|", s=550, linewidths=2.8, label="E-net target", zorder=3)
        ax.scatter(baseline_vals, y, color="#4c78a8", s=70, label="Baseline reasoning", zorder=4)
        ax.scatter(comp_vals, y, color=color, s=70, label=title, zorder=4)
        ax.axvline(0, color="#999999", linewidth=1)
        ax.set_title(title, fontsize=14)
        ax.set_xlabel("Signed standardized effect", fontsize=12)
        ax.grid(axis="x", alpha=0.2)

    draw_compare(ax_best, "both_contrastive_reasoning", "B. Best augmented reasoning", "#59a14f")
    draw_compare(ax_bad, "both_ensemble_reasoning", "C. Degraded augmented reasoning", "#e15759")
    ax_best.legend(frameon=False, fontsize=11, loc="lower right")

    metric_lines = [
        f"{row.label}: RMSE {row.rmse:.2f}, corr {row.correlation:.3f}, DA {row.directional_accuracy:.2f}, R^2 {row.r2:.3f}"
        for row in metrics_df.itertuples(index=False)
    ]
    fig.suptitle(
        "Validation feature comparison in reasoning mode",
        fontsize=18,
        y=1.02,
    )
    fig.text(0.5, 0.01, " | ".join(metric_lines), ha="center", fontsize=11, color="#444444")
    fig.savefig(PLOTS / "validation_reasoning_feature_comparison.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_reasoning_feature_comparison.pdf", bbox_inches="tight")


def build_scatter_tables(target_df: pd.DataFrame, case_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    feature_meta = target_df.set_index("feature")
    llm_df = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    metrics = pd.read_csv(RESULTS / "prediction_positive_case_variations_41_metrics.csv")
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    null_mse = float(np.mean(((100 * val_df["control_itt_efficiency"]) - (100 * val_df["treatment_itt_efficiency"])) ** 2))

    def get_mode_name(variation: str) -> str:
        return parse_variation(variation)[2]

    case_map = case_df.set_index("variation")
    point_rows = []
    variant_rows = []
    for variation in llm_df["variation"]:
        input_group, family, mode = parse_variation(variation)
        if input_group == "baseline":
            continue
        baseline_var = MODE_BASELINE[mode]
        var_effects = case_map.loc[variation] if variation in case_map.index else None
        base_effects = case_map.loc[baseline_var] if baseline_var in case_map.index else None
        if var_effects is None or base_effects is None:
            # compute on demand for non-reasoning variants
            row = llm_df.loc[llm_df["variation"] == variation].iloc[0]
            q_cols = [c for c in llm_df.columns if c.startswith("Q")]
            control = 100 * val_df["control_itt_efficiency"].reset_index(drop=True)
            temp = val_df.copy()
            temp["pred_effect"] = row[q_cols].astype(float).reset_index(drop=True).values - control.values
            temp_base = llm_df.loc[llm_df["variation"] == baseline_var].iloc[0]
            temp2 = val_df.copy()
            temp2["pred_effect"] = temp_base[q_cols].astype(float).reset_index(drop=True).values - control.values
            var_series = {f: signed_effect(temp[f], temp["pred_effect"]) for f in FEATURES}
            base_series = {f: signed_effect(temp2[f], temp2["pred_effect"]) for f in FEATURES}
        else:
            var_series = {f: float(var_effects[f]) for f in FEATURES}
            base_series = {f: float(base_effects[f]) for f in FEATURES}

        metric_row = metrics.loc[metrics["variation"] == variation].iloc[0]
        base_rmse = float(metrics.loc[metrics["variation"] == baseline_var, "rmse"].iloc[0])
        delta_r2 = (1 - float(metric_row["rmse"]) ** 2 / null_mse) - (1 - base_rmse**2 / null_mse)

        shifts = []
        corrections = []
        weight_sum = 0.0
        weighted_abs_shift = 0.0
        for feature in FEATURES:
            needed_correction = float(feature_meta.loc[feature, "target_signed_effect"] - base_series[feature])
            actual_shift = float(var_series[feature] - base_series[feature])
            importance = max(float(feature_meta.loc[feature, "enet_pct_increase_rmse"]), 0.0)
            point_rows.append(
                {
                    "variation": variation,
                    "input_group": input_group,
                    "family": family,
                    "mode": mode,
                    "feature": feature,
                    "feature_label": FEATURE_LABELS[feature],
                    "needed_correction": needed_correction,
                    "actual_shift": actual_shift,
                    "importance": importance,
                    "delta_r2_vs_matched_baseline": delta_r2,
                }
            )
            shifts.append(actual_shift)
            corrections.append(needed_correction)
            weight_sum += importance
            weighted_abs_shift += abs(actual_shift) * importance

        shifts_arr = np.array(shifts, dtype=float)
        corrections_arr = np.array(corrections, dtype=float)
        corr = float(np.corrcoef(shifts_arr, corrections_arr)[0, 1]) if np.std(shifts_arr) > 0 and np.std(corrections_arr) > 0 else np.nan
        slope0 = slope_through_origin(corrections_arr, shifts_arr)
        variant_rows.append(
            {
                "variation": variation,
                "input_group": input_group,
                "family": family,
                "mode": mode,
                "delta_r2_vs_matched_baseline": delta_r2,
                "shift_alignment_corr": corr,
                "calibration_slope": slope0,
                "weighted_abs_shift": weighted_abs_shift / weight_sum if weight_sum > 0 else np.nan,
            }
        )

    return pd.DataFrame(point_rows), pd.DataFrame(variant_rows)


def plot_scatter_dashboard(point_df: pd.DataFrame, variant_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(16, 13), constrained_layout=True)
    ax_all, ax_align, ax_cal, ax_shift = axes.ravel()

    # Panel A: all feature-variant points
    sc = ax_all.scatter(
        point_df["needed_correction"],
        point_df["actual_shift"],
        s=18 + 8 * np.sqrt(point_df["importance"].clip(lower=0)),
        c=point_df["delta_r2_vs_matched_baseline"],
        cmap="coolwarm",
        alpha=0.55,
        edgecolor="none",
    )
    lim = np.nanmax(np.abs(np.r_[point_df["needed_correction"].values, point_df["actual_shift"].values]))
    ax_all.plot([-lim, lim], [-lim, lim], color="#444444", linestyle="--", linewidth=1.5)
    ax_all.axhline(0, color="#999999", linewidth=1)
    ax_all.axvline(0, color="#999999", linewidth=1)
    ax_all.set_title("A. Feature-level shifts after augmentation")
    ax_all.set_xlabel("Needed correction from matched baseline to E-net target")
    ax_all.set_ylabel("Actual shift after augmentation vs matched baseline")
    ax_all.grid(alpha=0.2)
    cbar = fig.colorbar(sc, ax=ax_all, shrink=0.85)
    cbar.set_label("ΔR² vs matched baseline")

    # Panel B: alignment correlation vs performance
    colors = {"both": "#1f77b4", "paper_only": "#ff7f0e", "data_only": "#2ca02c"}
    markers = {"single": "o", "reasoning": "s", "joint": "^", "joint_reasoning": "D"}
    for mode, marker in markers.items():
        for input_group, color in colors.items():
            sub = variant_df[(variant_df["mode"] == mode) & (variant_df["input_group"] == input_group)]
            ax_align.scatter(
                sub["shift_alignment_corr"],
                sub["delta_r2_vs_matched_baseline"],
                color=color,
                marker=marker,
                s=58,
                alpha=0.8,
            )
    ax_align.axhline(0, color="#999999", linewidth=1)
    ax_align.axvline(0, color="#999999", linewidth=1)
    ax_align.set_title("B. Does moving in the right feature directions help?")
    ax_align.set_xlabel("Correlation(actual shift, needed correction)")
    ax_align.set_ylabel("ΔR² vs matched baseline")
    ax_align.grid(alpha=0.2)

    # Panel C: calibration slope vs performance
    for mode, marker in markers.items():
        for input_group, color in colors.items():
            sub = variant_df[(variant_df["mode"] == mode) & (variant_df["input_group"] == input_group)]
            ax_cal.scatter(
                sub["calibration_slope"],
                sub["delta_r2_vs_matched_baseline"],
                color=color,
                marker=marker,
                s=58,
                alpha=0.8,
            )
    ax_cal.axhline(0, color="#999999", linewidth=1)
    ax_cal.axvline(1, color="#444444", linestyle="--", linewidth=1.5)
    ax_cal.set_title("C. Numerical calibration of the update")
    ax_cal.set_xlabel("Slope(actual shift ~ needed correction, origin-fixed)")
    ax_cal.set_ylabel("ΔR² vs matched baseline")
    ax_cal.grid(alpha=0.2)

    # Panel D: total shift magnitude vs performance
    for mode, marker in markers.items():
        for input_group, color in colors.items():
            sub = variant_df[(variant_df["mode"] == mode) & (variant_df["input_group"] == input_group)]
            ax_shift.scatter(
                sub["weighted_abs_shift"],
                sub["delta_r2_vs_matched_baseline"],
                color=color,
                marker=marker,
                s=58,
                alpha=0.8,
            )
    ax_shift.axhline(0, color="#999999", linewidth=1)
    ax_shift.set_title("D. Do bigger updates just create confusion?")
    ax_shift.set_xlabel("Importance-weighted total absolute shift")
    ax_shift.set_ylabel("ΔR² vs matched baseline")
    ax_shift.grid(alpha=0.2)

    legend_handles = [
        plt.Line2D([0], [0], color="#1f77b4", marker="o", linestyle="", label="both"),
        plt.Line2D([0], [0], color="#ff7f0e", marker="o", linestyle="", label="paper_only"),
        plt.Line2D([0], [0], color="#2ca02c", marker="o", linestyle="", label="data_only"),
        plt.Line2D([0], [0], color="#555555", marker="o", linestyle="", label="single"),
        plt.Line2D([0], [0], color="#555555", marker="s", linestyle="", label="reasoning"),
        plt.Line2D([0], [0], color="#555555", marker="^", linestyle="", label="joint"),
        plt.Line2D([0], [0], color="#555555", marker="D", linestyle="", label="joint+reasoning"),
    ]
    fig.legend(handles=legend_handles, frameon=False, ncol=7, loc="upper center", bbox_to_anchor=(0.5, 1.01))
    fig.suptitle("Validation augmentation diagnostics against the E-net interpretability target", fontsize=17, y=1.03)
    fig.savefig(PLOTS / "validation_shift_vs_interpretability_scatter.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_shift_vs_interpretability_scatter.pdf", bbox_inches="tight")


def summarize_feature_gap_change(point_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    temp = point_df.copy()
    temp["gap_change"] = temp["needed_correction"].abs() - (temp["needed_correction"] - temp["actual_shift"]).abs()
    for feature_label, sub in temp.groupby("feature_label"):
        rows.append(
            {
                "feature_label": feature_label,
                "corr_gap_change_vs_delta_r2": sub["gap_change"].corr(sub["delta_r2_vs_matched_baseline"]),
                "corr_actual_shift_vs_delta_r2": sub["actual_shift"].corr(sub["delta_r2_vs_matched_baseline"]),
                "mean_gap_change": sub["gap_change"].mean(),
                "mean_abs_needed_correction": sub["needed_correction"].abs().mean(),
                "importance": sub["importance"].iloc[0],
            }
        )
    return pd.DataFrame(rows).sort_values("corr_gap_change_vs_delta_r2", ascending=False)


def main() -> None:
    target_df, case_df, metrics_df = build_feature_targets()
    target_df.to_csv(RESULTS / "validation_reasoning_feature_target_table.csv", index=False)
    metrics_df.to_csv(RESULTS / "validation_reasoning_feature_metrics.csv", index=False)
    plot_reasoning_feature_figure(target_df, case_df, metrics_df)

    point_df, variant_df = build_scatter_tables(target_df, case_df)
    point_df.to_csv(RESULTS / "validation_shift_vs_interpretability_points.csv", index=False)
    variant_df.to_csv(RESULTS / "validation_shift_vs_interpretability_variants.csv", index=False)
    summarize_feature_gap_change(point_df).to_csv(RESULTS / "validation_feature_gapchange_vs_delta_r2.csv", index=False)
    plot_scatter_dashboard(point_df, variant_df)


if __name__ == "__main__":
    main()
