from __future__ import annotations

from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO_ROOT / "results"
PRED_PATH = RESULTS_DIR / "prediction_positive_case_variations_41.csv"
VALIDATION_DF = REPO_ROOT / "input" / "pgg_CONFIGmerged_validation.csv"

BINARY_FEATURES = [
    "CONFIG_chat",
    "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp",
    "CONFIG_rewardExists",
    "CONFIG_showNRounds",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
]

CONTINUOUS_FEATURES = [
    "control_pct",
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_MPCR",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
    "CONFIG_rewardTech",
]


def parse_variation_name(name: str) -> tuple[str, str]:
    if name.endswith("_joint_reasoning"):
        return name[: -len("_joint_reasoning")], "joint_reasoning"
    if name.endswith("_joint"):
        return name[: -len("_joint")], "joint"
    if name.endswith("_reasoning"):
        return name[: -len("_reasoning")], "reasoning"
    return name, "single"


def input_group_for_family(family: str) -> str:
    if family == "baseline":
        return "baseline"
    if family.startswith("both_"):
        return "both"
    if family.startswith("paper_only_"):
        return "paper_only"
    if family.startswith("data_only_"):
        return "data_only"
    return "other"


def build_effect_frame() -> tuple[pd.DataFrame, pd.DataFrame]:
    pred = pd.read_csv(PRED_PATH, index_col=0)
    df = pd.read_csv(VALIDATION_DF).reset_index(drop=True)
    labels = [f"Q{i}" for i in range(1, len(df) + 1)]
    control = df["efficiency_np"] * 100
    treatment = df["efficiency_p"] * 100

    config_df = pd.DataFrame(
        {
            "label": labels,
            "CONFIG_configId": df["CONFIG_configId"].astype(int),
            "control_pct": control,
            "true_treatment_pct": treatment,
            "true_effect_pct": treatment - control,
        }
    )
    for feature in BINARY_FEATURES:
        config_df[feature] = df[feature].astype(int)
    for feature in [
        "CONFIG_playerCount",
        "CONFIG_numRounds",
        "CONFIG_MPCR",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_rewardTech",
    ]:
        config_df[feature] = df[feature].astype(float)

    variation_meta = []
    for variation in pred.index:
        family, mode = parse_variation_name(variation)
        variation_meta.append(
            {
                "variation": variation,
                "family": family,
                "mode": mode,
                "input_group": input_group_for_family(family),
            }
        )
        pred_vals = pd.to_numeric(pred.loc[variation], errors="coerce").reindex(labels).to_numpy(float)
        config_df[f"{variation}_pred"] = pred_vals
        config_df[f"{variation}_effect"] = pred_vals - control.to_numpy(float)

    meta_df = pd.DataFrame(variation_meta)
    return config_df, meta_df


def binary_contrasts(config_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, meta in meta_df.iterrows():
        variation = meta["variation"]
        for feature in BINARY_FEATURES:
            low = config_df[config_df[feature] == 0]
            high = config_df[config_df[feature] == 1]
            row = {
                "feature": feature,
                **meta.to_dict(),
                "n_level0": len(low),
                "n_level1": len(high),
                "true_mean_effect_diff_1_minus_0": float(
                    high["true_effect_pct"].mean() - low["true_effect_pct"].mean()
                ),
                "true_positive_share_diff_1_minus_0": float(
                    (high["true_effect_pct"] > 0).mean() - (low["true_effect_pct"] > 0).mean()
                ),
                "mean_effect_level0": float(low[f"{variation}_effect"].mean()),
                "mean_effect_level1": float(high[f"{variation}_effect"].mean()),
                "mean_effect_diff_1_minus_0": float(
                    high[f"{variation}_effect"].mean() - low[f"{variation}_effect"].mean()
                ),
                "positive_share_level0": float((low[f"{variation}_effect"] > 0).mean()),
                "positive_share_level1": float((high[f"{variation}_effect"] > 0).mean()),
                "positive_share_diff_1_minus_0": float(
                    (high[f"{variation}_effect"] > 0).mean()
                    - (low[f"{variation}_effect"] > 0).mean()
                ),
            }
            rows.append(row)
    return pd.DataFrame(rows)


def binary_consistency(binary_df: pd.DataFrame) -> pd.DataFrame:
    def summarize(group: pd.DataFrame, label: str, value: str) -> dict[str, object]:
        diffs = group["mean_effect_diff_1_minus_0"]
        return {
            "scope": label,
            "scope_value": value,
            "feature": group["feature"].iloc[0],
            "n_variants": len(group),
            "n_up": int((diffs > 0).sum()),
            "n_down": int((diffs < 0).sum()),
            "n_zero": int((diffs == 0).sum()),
            "mean_diff": float(diffs.mean()),
            "median_diff": float(diffs.median()),
            "consistent_direction": (
                "up"
                if (diffs > 0).all()
                else "down"
                if (diffs < 0).all()
                else "mixed"
            ),
        }

    rows: list[dict[str, object]] = []
    for feature, feature_df in binary_df.groupby("feature"):
        rows.append(summarize(feature_df, "all_variants", "all"))
        for mode, mode_df in feature_df.groupby("mode"):
            rows.append(summarize(mode_df, "mode", mode))
        for input_group, group_df in feature_df.groupby("input_group"):
            rows.append(summarize(group_df, "input_group", input_group))
    return pd.DataFrame(rows)


def continuous_correlations(config_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, meta in meta_df.iterrows():
        variation = meta["variation"]
        for feature in CONTINUOUS_FEATURES:
            rows.append(
                {
                    "feature": feature,
                    **meta.to_dict(),
                    "true_effect_corr": float(
                        config_df[feature].corr(config_df["true_effect_pct"])
                    ),
                    "predicted_effect_corr": float(
                        config_df[feature].corr(config_df[f"{variation}_effect"])
                    ),
                }
            )
    return pd.DataFrame(rows)


def continuous_consistency(cont_df: pd.DataFrame) -> pd.DataFrame:
    def summarize(group: pd.DataFrame, label: str, value: str) -> dict[str, object]:
        vals = group["predicted_effect_corr"]
        return {
            "scope": label,
            "scope_value": value,
            "feature": group["feature"].iloc[0],
            "n_variants": len(group),
            "n_positive": int((vals > 0).sum()),
            "n_negative": int((vals < 0).sum()),
            "mean_corr": float(vals.mean()),
            "median_corr": float(vals.median()),
            "consistent_direction": (
                "positive"
                if (vals > 0).all()
                else "negative"
                if (vals < 0).all()
                else "mixed"
            ),
        }

    rows: list[dict[str, object]] = []
    for feature, feature_df in cont_df.groupby("feature"):
        rows.append(summarize(feature_df, "all_variants", "all"))
        for mode, mode_df in feature_df.groupby("mode"):
            rows.append(summarize(mode_df, "mode", mode))
        for input_group, group_df in feature_df.groupby("input_group"):
            rows.append(summarize(group_df, "input_group", input_group))
    return pd.DataFrame(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    config_df, meta_df = build_effect_frame()

    config_df.to_csv(RESULTS_DIR / "validation_config_effect_patterns_all_variants.csv", index=False)
    meta_df.to_csv(RESULTS_DIR / "validation_variant_metadata.csv", index=False)

    binary_df = binary_contrasts(config_df, meta_df)
    binary_df.to_csv(
        RESULTS_DIR / "validation_config_binary_feature_contrasts_by_variant.csv",
        index=False,
    )

    binary_consistency(binary_df).to_csv(
        RESULTS_DIR / "validation_config_binary_feature_consistency.csv",
        index=False,
    )

    cont_df = continuous_correlations(config_df, meta_df)
    cont_df.to_csv(
        RESULTS_DIR / "validation_config_continuous_feature_correlations_by_variant.csv",
        index=False,
    )

    continuous_consistency(cont_df).to_csv(
        RESULTS_DIR / "validation_config_continuous_feature_consistency.csv",
        index=False,
    )

    print("Wrote validation_config_effect_patterns_all_variants.csv")
    print("Wrote validation_variant_metadata.csv")
    print("Wrote validation_config_binary_feature_contrasts_by_variant.csv")
    print("Wrote validation_config_binary_feature_consistency.csv")
    print("Wrote validation_config_continuous_feature_correlations_by_variant.csv")
    print("Wrote validation_config_continuous_feature_consistency.csv")


if __name__ == "__main__":
    main()
