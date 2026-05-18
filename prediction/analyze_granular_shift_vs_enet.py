from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import shap
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
from plot_paths import GRANULAR_PLOTS as PLOTS, ensure_plot_dir
DATA = ROOT / "science_data" / "data" / "processed_data"
HPO = ROOT / "science_data" / "data" / "hpo_model_configs.json"

MODES = ["single", "reasoning", "joint", "joint_reasoning"]
INPUT_GROUPS = ["both", "paper_only", "data_only"]
FEATURES = [
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_showNRounds",
    "CONFIG_MPCR",
    "CONFIG_allOrNothing",
    "CONFIG_chat",
    "CONFIG_defaultContribProp",
    "CONFIG_rewardExists",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
]

FEATURE_LABELS = {
    "CONFIG_playerCount": "Group Size",
    "CONFIG_numRounds": "Game Length",
    "CONFIG_showNRounds": "Horizon Knowledge",
    "CONFIG_MPCR": "Return Rate (MPCR)",
    "CONFIG_allOrNothing": "Contribution Type",
    "CONFIG_chat": "Communication",
    "CONFIG_defaultContribProp": "Contribution Framing",
    "CONFIG_rewardExists": "Reward",
    "CONFIG_showOtherSummaries": "Peer Outcome Visibility",
    "CONFIG_showPunishmentId": "Actor Anonymity",
    "CONFIG_punishmentCost": "Peer Incentive Cost",
    "CONFIG_punishmentTech": "Punishment Technology",
}

CATEGORY_MAP = {
    "Group Size": "Game Structure",
    "Game Length": "Game Structure",
    "Horizon Knowledge": "Game Structure",
    "Return Rate (MPCR)": "Game Structure",
    "Contribution Type": "Contribution Structure",
    "Contribution Framing": "Contribution Structure",
    "Communication": "Social Information",
    "Peer Outcome Visibility": "Social Information",
    "Actor Anonymity": "Social Information",
    "Reward": "Incentive Mechanisms",
    "Peer Incentive Cost": "Incentive Mechanisms",
    "Punishment Technology": "Incentive Mechanisms",
}

CATEGORY_COLORS = {
    "Game Structure": "#2166AC",
    "Contribution Structure": "#92C5DE",
    "Social Information": "#D6604D",
    "Incentive Mechanisms": "#F4A582",
}


def parse_variation(variation: str) -> tuple[str, str, str]:
    if variation == "baseline":
        return "baseline", "baseline", "single"
    if variation == "baseline_reasoning":
        return "baseline", "baseline", "reasoning"
    if variation == "baseline_joint":
        return "baseline", "baseline", "joint"
    if variation == "baseline_joint_reasoning":
        return "baseline", "baseline", "joint_reasoning"

    mode = "single"
    stem = variation
    for suffix, parsed in [
        ("_joint_reasoning", "joint_reasoning"),
        ("_reasoning", "reasoning"),
        ("_joint", "joint"),
    ]:
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            mode = parsed
            break

    for input_group in INPUT_GROUPS:
        prefix = f"{input_group}_"
        if stem.startswith(prefix):
            family = stem[len(prefix) :]
            return input_group, family, mode
    raise ValueError(f"Unrecognized variation format: {variation}")


def family_order(input_group: str) -> list[str]:
    if input_group == "both":
        return [
            "contrastive",
            "ensemble",
            "freeform",
            "quantitative",
            "refined",
            "rules",
            "structured",
            "uncertainty",
        ]
    return ["freeform", "quantitative", "structured"]


def null_mse(df: pd.DataFrame) -> float:
    return ((100 * df["treatment_itt_efficiency"] - 100 * df["control_itt_efficiency"]) ** 2).mean()


def r2_from_rmse(rmse: float, baseline_mse: float) -> float:
    return 1.0 - (rmse ** 2) / baseline_mse


def load_metrics_with_delta_r2(path: Path, wave: str, baseline_mse: float) -> pd.DataFrame:
    df = pd.read_csv(path).copy()
    meta = df["variation"].apply(parse_variation)
    df["input_group"] = meta.str[0]
    df["family"] = meta.str[1]
    df["mode"] = meta.str[2]
    df["wave"] = wave
    df["r2"] = df["rmse"].map(lambda x: r2_from_rmse(float(x), baseline_mse))

    baseline_map = {
        mode: df.loc[(df["input_group"] == "baseline") & (df["mode"] == mode), "r2"].iloc[0]
        for mode in MODES
    }
    df["baseline_r2_matched"] = df["mode"].map(baseline_map)
    df["delta_r2_vs_matched_baseline"] = df["r2"] - df["baseline_r2_matched"]
    return df


def load_prediction_table(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path).rename(columns={"Unnamed: 0": "variation"}).copy()
    meta = df["variation"].apply(parse_variation)
    df["input_group"] = meta.str[0]
    df["family"] = meta.str[1]
    df["mode"] = meta.str[2]
    return df


def compute_feature_correlations_from_predictions(
    pred_df: pd.DataFrame, config_df: pd.DataFrame, label_prefix: str
) -> pd.DataFrame:
    label_cols = [c for c in pred_df.columns if c.startswith(label_prefix)]
    control = 100 * config_df["control_itt_efficiency"].to_numpy()

    rows = []
    for _, row in pred_df.iterrows():
        values = row[label_cols].astype(float).to_numpy()
        effect = values - control
        for feature in FEATURES:
            feat = config_df[feature].astype(float).to_numpy()
            corr = np.corrcoef(feat, effect)[0, 1]
            rows.append(
                {
                    "variation": row["variation"],
                    "input_group": row["input_group"],
                    "family": row["family"],
                    "mode": row["mode"],
                    "feature": feature,
                    "predicted_effect_feature_corr": corr,
                }
            )
    return pd.DataFrame(rows)


def compute_shift_vs_matched_baseline(corr_df: pd.DataFrame, wave: str) -> pd.DataFrame:
    baseline = (
        corr_df.loc[corr_df["input_group"] == "baseline", ["mode", "feature", "predicted_effect_feature_corr"]]
        .rename(columns={"predicted_effect_feature_corr": "baseline_feature_corr"})
        .copy()
    )
    aug = corr_df.loc[corr_df["input_group"] != "baseline"].copy()
    out = aug.merge(baseline, on=["mode", "feature"], how="left")
    out["feature_corr_shift_vs_matched_baseline"] = (
        out["predicted_effect_feature_corr"] - out["baseline_feature_corr"]
    )
    out["wave"] = wave
    return out


def plot_granular_performance_heatmap(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(14.5, 8.5), constrained_layout=True)
    vmin, vmax = -0.22, 0.10
    for row_idx, wave in enumerate(["validation", "learning"]):
        for col_idx, input_group in enumerate(INPUT_GROUPS):
            ax = axes[row_idx, col_idx]
            part = df.loc[(df["wave"] == wave) & (df["input_group"] == input_group)].copy()
            order = family_order(input_group)
            part["family"] = pd.Categorical(part["family"], categories=order, ordered=True)
            pivot = part.pivot(index="family", columns="mode", values="delta_r2_vs_matched_baseline")
            pivot = pivot.reindex(index=order, columns=MODES)
            sns.heatmap(
                pivot,
                ax=ax,
                cmap="RdBu_r",
                center=0,
                vmin=vmin,
                vmax=vmax,
                annot=True,
                fmt=".02f",
                linewidths=0.5,
                cbar=(row_idx == 0 and col_idx == 2),
                cbar_kws={"label": "ΔR² vs matched baseline"},
            )
            ax.set_title(f"{wave.title()} | {input_group}")
            ax.set_xlabel("")
            ax.set_ylabel("")
    fig.suptitle("Granular Performance: exact writing families instead of family-averaged blocks", fontsize=16)
    fig.savefig(PLOTS / "granular_performance_delta_r2_heatmap.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "granular_performance_delta_r2_heatmap.pdf", bbox_inches="tight")


def plot_chat_shift_heatmap(shift_df: pd.DataFrame) -> None:
    chat = shift_df.loc[shift_df["feature"] == "CONFIG_chat"].copy()
    fig, axes = plt.subplots(2, 3, figsize=(14.5, 8.5), constrained_layout=True)
    vmin, vmax = -0.40, 0.40
    for row_idx, wave in enumerate(["validation", "learning"]):
        for col_idx, input_group in enumerate(INPUT_GROUPS):
            ax = axes[row_idx, col_idx]
            part = chat.loc[(chat["wave"] == wave) & (chat["input_group"] == input_group)].copy()
            order = family_order(input_group)
            part["family"] = pd.Categorical(part["family"], categories=order, ordered=True)
            pivot = part.pivot(index="family", columns="mode", values="feature_corr_shift_vs_matched_baseline")
            pivot = pivot.reindex(index=order, columns=MODES)
            sns.heatmap(
                pivot,
                ax=ax,
                cmap="PuOr",
                center=0,
                vmin=vmin,
                vmax=vmax,
                annot=True,
                fmt=".02f",
                linewidths=0.5,
                cbar=(row_idx == 0 and col_idx == 2),
                cbar_kws={"label": "Δ corr(feature, predicted effect)"},
            )
            ax.set_title(f"{wave.title()} | {input_group}")
            ax.set_xlabel("")
            ax.set_ylabel("")
    fig.suptitle("Granular Communication Shift: augmentation often pushes 'chat' upward, but not uniformly", fontsize=16)
    fig.savefig(PLOTS / "granular_chat_shift_heatmap.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "granular_chat_shift_heatmap.pdf", bbox_inches="tight")


def plot_chat_shift_vs_performance(shift_df: pd.DataFrame, perf_df: pd.DataFrame) -> None:
    chat = shift_df.loc[shift_df["feature"] == "CONFIG_chat"].copy()
    merged = chat.merge(
        perf_df[["variation", "wave", "delta_r2_vs_matched_baseline", "input_group", "mode"]],
        on=["variation", "wave", "input_group", "mode"],
        how="left",
    )
    palette = {"both": "#1f77b4", "paper_only": "#ff7f0e", "data_only": "#2ca02c"}
    markers = {"single": "o", "reasoning": "s", "joint": "^", "joint_reasoning": "D"}
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4), sharey=True, constrained_layout=True)
    for ax, wave in zip(axes, ["validation", "learning"]):
        part = merged.loc[merged["wave"] == wave].copy()
        for mode, marker in markers.items():
            sub = part.loc[part["mode"] == mode]
            for input_group, color in palette.items():
                sub2 = sub.loc[sub["input_group"] == input_group]
                ax.scatter(
                    sub2["feature_corr_shift_vs_matched_baseline"],
                    sub2["delta_r2_vs_matched_baseline"],
                    color=color,
                    marker=marker,
                    alpha=0.85,
                    s=55,
                    edgecolor="white",
                    linewidth=0.4,
                )
        ax.axhline(0, color="#777777", linestyle="--", linewidth=1)
        ax.axvline(0, color="#777777", linestyle="--", linewidth=1)
        ax.set_title(wave.title())
        ax.set_xlabel("Chat shift vs matched baseline")
        ax.grid(alpha=0.2)
    axes[0].set_ylabel("ΔR² vs matched baseline")
    fig.suptitle("Communication shift is real, but stronger shifts do not guarantee better performance", fontsize=16)
    fig.savefig(PLOTS / "chat_shift_vs_delta_r2.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "chat_shift_vs_delta_r2.pdf", bbox_inches="tight")


def fit_enet_and_importances() -> pd.DataFrame:
    cfg = json.load(open(HPO))
    learn = pd.read_csv(DATA / "df_paired_learn.csv")
    val = pd.read_csv(DATA / "df_paired_val.csv")

    feature_cols = FEATURES + ["control_itt_efficiency"]
    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("interactions", PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)),
            (
                "estimator",
                ElasticNet(
                    alpha=cfg["ELASTIC"]["alpha"],
                    l1_ratio=cfg["ELASTIC"]["l1_ratio"],
                    random_state=cfg["ELASTIC"]["random_seed"],
                ),
            ),
        ]
    )
    pipe.fit(learn[feature_cols], learn["treatment_itt_efficiency"])
    baseline_rmse = np.sqrt(mean_squared_error(pipe.predict(val[feature_cols]) * 100, val["treatment_itt_efficiency"] * 100))

    imp_rows = []
    for feature in feature_cols:
        shuffled = []
        for shuffle_iteration in range(30):
            df_shuffle = val.copy()
            df_shuffle[feature] = np.random.RandomState(seed=shuffle_iteration).permutation(df_shuffle[feature].values)
            rmse = np.sqrt(mean_squared_error(pipe.predict(df_shuffle[feature_cols]) * 100, val["treatment_itt_efficiency"] * 100))
            shuffled.append(rmse)
        pct_increase = 100 * (np.mean(shuffled) - baseline_rmse) / baseline_rmse
        imp_rows.append({"feature": feature, "enet_pct_increase_rmse": pct_increase})
    imp_df = pd.DataFrame(imp_rows)

    background_data = learn[feature_cols].astype(float).values
    masker = shap.maskers.Independent(background_data)

    def model_wrapper(x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        return pipe.predict(x)

    explainer = shap.Explainer(model=model_wrapper, masker=masker, feature_names=feature_cols)
    shap_values = explainer(learn[feature_cols].astype(float).values)

    shap_rows = []
    for feature in FEATURES:
        vals = shap_values[:, feature].values
        data = shap_values[:, feature].data.astype(float)
        direction = np.corrcoef(data, vals)[0, 1]
        shap_rows.append(
            {
                "feature": feature,
                "enet_mean_abs_shap": float(np.mean(np.abs(vals))),
                "enet_shap_direction": float(direction),
            }
        )
    shap_df = pd.DataFrame(shap_rows)
    out = imp_df.merge(shap_df, on="feature", how="left")
    return out.loc[out["feature"].isin(FEATURES)].copy()


def plot_llm_shift_vs_enet(feature_shift_df: pd.DataFrame, enet_df: pd.DataFrame) -> None:
    agg = (
        feature_shift_df.groupby(["wave", "feature"])["feature_corr_shift_vs_matched_baseline"]
        .agg(mean_shift="mean", mean_abs_shift=lambda x: np.mean(np.abs(x)))
        .reset_index()
    )
    plot_df = agg.merge(enet_df, on="feature", how="left")
    plot_df["feature_label"] = plot_df["feature"].map(FEATURE_LABELS)
    plot_df["category"] = plot_df["feature_label"].map(CATEGORY_MAP)
    plot_df["sign_aligned"] = np.sign(plot_df["mean_shift"]) == np.sign(plot_df["enet_shap_direction"])

    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.6), sharey=True, constrained_layout=True)
    for ax, wave in zip(axes, ["validation", "learning"]):
        part = plot_df.loc[plot_df["wave"] == wave].copy()
        for _, row in part.iterrows():
            color = CATEGORY_COLORS[row["category"]]
            edge = "black" if not row["sign_aligned"] else "white"
            ax.scatter(
                row["enet_pct_increase_rmse"],
                row["mean_abs_shift"],
                color=color,
                s=110,
                edgecolor=edge,
                linewidth=0.9,
                alpha=0.9,
            )
            ax.text(
                row["enet_pct_increase_rmse"] + 0.6,
                row["mean_abs_shift"] + 0.003,
                row["feature_label"],
                fontsize=8,
            )
        ax.set_title(wave.title())
        ax.set_xlabel("E-net permutation importance\n(% increase in validation RMSE)")
        ax.grid(alpha=0.2)
    axes[0].set_ylabel("Mean absolute LLM shift vs matched baseline\nin corr(feature, predicted effect)")
    fig.suptitle("Do augmented LLMs move most on the features that matter most in the data?", fontsize=16)

    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", label=cat, markerfacecolor=color, markersize=9)
        for cat, color in CATEGORY_COLORS.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], marker="o", color="black", label="Sign mismatch vs SHAP", markerfacecolor="white", markersize=9)
    )
    axes[1].legend(handles=legend_handles, loc="lower right", frameon=False, fontsize=8)

    fig.savefig(PLOTS / "llm_shift_vs_enet_importance.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "llm_shift_vs_enet_importance.pdf", bbox_inches="tight")
    plot_df.to_csv(RESULTS / "llm_shift_vs_enet_importance_table.csv", index=False)


def main() -> None:
    df_val = pd.read_csv(DATA / "df_paired_val.csv")
    df_learn = pd.read_csv(DATA / "df_paired_learn.csv").sort_values("CONFIG_configId").reset_index(drop=True)
    val_null_mse = null_mse(df_val)
    learn_null_mse = null_mse(df_learn)

    val_perf = load_metrics_with_delta_r2(
        RESULTS / "prediction_positive_case_variations_41_metrics.csv",
        wave="validation",
        baseline_mse=val_null_mse,
    )
    learn_perf = load_metrics_with_delta_r2(
        RESULTS / "prediction_crosswave_variations_41_learning_with_baselines_metrics.csv",
        wave="learning",
        baseline_mse=learn_null_mse,
    )
    perf = pd.concat([val_perf.loc[val_perf["input_group"] != "baseline"], learn_perf.loc[learn_perf["input_group"] != "baseline"]], ignore_index=True)
    perf.to_csv(RESULTS / "granular_performance_delta_r2_table.csv", index=False)
    plot_granular_performance_heatmap(perf)

    val_pred = load_prediction_table(RESULTS / "prediction_positive_case_variations_41.csv")
    learn_pred_aug = load_prediction_table(RESULTS / "prediction_crosswave_variations_41_learning.csv")
    learn_pred_base = load_prediction_table(RESULTS / "prediction_learning_wave_elicitation_41.csv")
    learn_pred = pd.concat([learn_pred_base, learn_pred_aug], ignore_index=True)

    val_corr = compute_feature_correlations_from_predictions(val_pred, df_val.reset_index(drop=True), "Q")
    learn_corr = compute_feature_correlations_from_predictions(learn_pred, df_learn, "L")

    val_shift = compute_shift_vs_matched_baseline(val_corr, "validation")
    learn_shift = compute_shift_vs_matched_baseline(learn_corr, "learning")
    feature_shift = pd.concat([val_shift, learn_shift], ignore_index=True)
    feature_shift.to_csv(RESULTS / "feature_corr_shift_vs_matched_baseline_by_variant.csv", index=False)

    plot_chat_shift_heatmap(feature_shift)
    plot_chat_shift_vs_performance(feature_shift, perf)

    enet_df = fit_enet_and_importances()
    enet_df["feature_label"] = enet_df["feature"].map(FEATURE_LABELS)
    enet_df.to_csv(RESULTS / "enet_feature_importance_and_shap_summary.csv", index=False)
    plot_llm_shift_vs_enet(feature_shift, enet_df)


if __name__ == "__main__":
    main()
