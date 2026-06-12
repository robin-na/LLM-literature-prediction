from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from analyze_validation_interaction_alignment import parse_variation


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
DATA = ROOT / "science_data" / "data" / "processed_data"

VAL_PATH = DATA / "df_paired_val.csv"
PRED_PATH = RESULTS / "prediction_positive_case_variations_41.csv"
METRICS_PATH = RESULTS / "prediction_positive_case_variations_41_metrics.csv"

FEATURE_COLS = [
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
    "control_itt_efficiency",
]

INTERACTION_DEGREES = [
    ("chat_x_peer", ["CONFIG_chat", "CONFIG_showOtherSummaries"]),
    ("numrounds_x_chat", ["CONFIG_numRounds", "CONFIG_chat"]),
    ("numrounds_x_peer", ["CONFIG_numRounds", "CONFIG_showOtherSummaries"]),
    ("numrounds_x_chat_x_peer", ["CONFIG_numRounds", "CONFIG_chat", "CONFIG_showOtherSummaries"]),
    ("frame_x_peer", ["CONFIG_defaultContribProp", "CONFIG_showOtherSummaries"]),
    ("frame_x_type", ["CONFIG_defaultContribProp", "CONFIG_allOrNothing"]),
    ("peer_x_type", ["CONFIG_showOtherSummaries", "CONFIG_allOrNothing"]),
    ("frame_x_peer_x_type", ["CONFIG_defaultContribProp", "CONFIG_showOtherSummaries", "CONFIG_allOrNothing"]),
]

MODE_BASELINE = {
    "single": "baseline",
    "reasoning": "baseline_reasoning",
    "joint": "baseline_joint",
    "joint_reasoning": "baseline_joint_reasoning",
}


def ridge_pipeline() -> Pipeline:
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("ridge", RidgeCV(alphas=np.logspace(-4, 4, 100))),
        ]
    )


def loocv_predict(model, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    loo = LeaveOneOut()
    preds = np.empty_like(y, dtype=float)
    for train_idx, test_idx in loo.split(X):
        fitted = clone(model)
        fitted.fit(X[train_idx], y[train_idx])
        preds[test_idx] = fitted.predict(X[test_idx]).reshape(-1)
    return preds


def add_interactions(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for name, cols in INTERACTION_DEGREES:
        prod = np.ones(len(out), dtype=float)
        for col in cols:
            prod = prod * out[col].astype(float).to_numpy()
        out[name] = prod
    return out


def compute_r2_from_rmse(rmse: float, y_true: np.ndarray, y_control: np.ndarray) -> float:
    null_mse = float(np.mean((y_true - y_control) ** 2))
    return 1.0 - (rmse**2) / null_mse


def load_core_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    val_df = (
        pd.read_csv(VAL_PATH)
        .sort_values("CONFIG_configId")
        .reset_index(drop=True)
    )
    pred_df = pd.read_csv(PRED_PATH).rename(columns={"Unnamed: 0": "variation"})
    metrics_df = pd.read_csv(METRICS_PATH)
    return val_df, pred_df, metrics_df


def build_prediction_table(val_df: pd.DataFrame, pred_df: pd.DataFrame, metrics_df: pd.DataFrame) -> pd.DataFrame:
    q_cols = [c for c in pred_df.columns if c.startswith("Q")]
    y_true = 100 * val_df["treatment_itt_efficiency"].to_numpy()
    y_control = 100 * val_df["control_itt_efficiency"].to_numpy()
    y_enet = 100 * val_df["elastic_prereg_pred"].to_numpy()

    baseline_r2_by_mode = {}
    for baseline_var in MODE_BASELINE.values():
        baseline_rmse = float(metrics_df.loc[metrics_df["variation"] == baseline_var, "rmse"].iloc[0])
        baseline_r2_by_mode[parse_variation(baseline_var)[2]] = compute_r2_from_rmse(baseline_rmse, y_true, y_control)

    rows = []
    for _, row in pred_df.iterrows():
        variation = row["variation"]
        input_group, family, mode = parse_variation(variation)
        y_pred = row[q_cols].astype(float).to_numpy()
        effect_true = y_true - y_control
        effect_pred = y_pred - y_control
        effect_enet = y_enet - y_control
        metric_row = metrics_df.loc[metrics_df["variation"] == variation].iloc[0]
        baseline_var = MODE_BASELINE[mode]
        baseline_pred = pred_df.loc[pred_df["variation"] == baseline_var, q_cols].iloc[0].astype(float).to_numpy()
        baseline_effect = baseline_pred - y_control
        rmse = float(metric_row["rmse"])
        rows.append(
            {
                "variation": variation,
                "input_group": input_group,
                "family": family,
                "mode": mode,
                "baseline_variation": baseline_var,
                "y_pred": y_pred,
                "effect_pred": effect_pred,
                "baseline_effect": baseline_effect,
                "rmse": rmse,
                "correlation": float(metric_row["correlation"]),
                "directional_accuracy": float(metric_row["directional_accuracy"]),
                "r2": compute_r2_from_rmse(rmse, y_true, y_control),
                "baseline_r2_matched": baseline_r2_by_mode[mode],
                "delta_r2_vs_matched_baseline": compute_r2_from_rmse(rmse, y_true, y_control) - baseline_r2_by_mode[mode],
            }
        )

    out = pd.DataFrame(rows)
    out.attrs["y_true"] = y_true
    out.attrs["y_control"] = y_control
    out.attrs["y_enet"] = y_enet
    out.attrs["effect_true"] = effect_true
    out.attrs["effect_enet"] = effect_enet
    return out


def compute_ewoa(pred_table: pd.DataFrame, epsilon: float = 0.5) -> tuple[pd.DataFrame, pd.DataFrame]:
    y_enet = pred_table.attrs["y_enet"]
    config_rows = []
    variant_rows = []
    for row in pred_table.itertuples(index=False):
        needed = y_enet - row.baseline_effect - pred_table.attrs["y_control"]
        # needed correction in treatment-prediction space
        needed = y_enet - (row.baseline_effect + pred_table.attrs["y_control"])
        actual = row.y_pred - (row.baseline_effect + pred_table.attrs["y_control"])
        denom = needed
        valid = np.abs(denom) >= epsilon
        ewoa = np.full_like(actual, np.nan, dtype=float)
        ewoa[valid] = actual[valid] / denom[valid]
        for idx, (n, a, e, v) in enumerate(zip(denom, actual, ewoa, valid), start=1):
            config_rows.append(
                {
                    "variation": row.variation,
                    "input_group": row.input_group,
                    "family": row.family,
                    "mode": row.mode,
                    "baseline_variation": row.baseline_variation,
                    "q_idx": idx,
                    "needed_correction": float(n),
                    "actual_update": float(a),
                    "ewoa": float(e) if v else np.nan,
                    "valid_ewoa": bool(v),
                }
            )
        valid_ewoa = ewoa[valid]
        variant_rows.append(
            {
                "variation": row.variation,
                "input_group": row.input_group,
                "family": row.family,
                "mode": row.mode,
                "baseline_variation": row.baseline_variation,
                "mean_ewoa": float(np.nanmean(valid_ewoa)) if valid_ewoa.size else np.nan,
                "median_ewoa": float(np.nanmedian(valid_ewoa)) if valid_ewoa.size else np.nan,
                "pct_ewoa_gt_0": float(np.mean(valid_ewoa > 0)) if valid_ewoa.size else np.nan,
                "pct_ewoa_gt_1": float(np.mean(valid_ewoa > 1)) if valid_ewoa.size else np.nan,
                "pct_ewoa_lt_0": float(np.mean(valid_ewoa < 0)) if valid_ewoa.size else np.nan,
                "mean_abs_update": float(np.mean(np.abs(actual))),
                "mean_abs_needed_correction": float(np.mean(np.abs(denom))),
                "valid_ewoa_n": int(valid.sum()),
            }
        )
    return pd.DataFrame(config_rows), pd.DataFrame(variant_rows)


def compute_error_decomposition(pred_table: pd.DataFrame) -> pd.DataFrame:
    y_true = pred_table.attrs["y_true"]
    y_enet = pred_table.attrs["y_enet"]
    rows = []
    enet_mse = float(mean_squared_error(y_true, y_enet))
    for row in pred_table.itertuples(index=False):
        mse = float(mean_squared_error(y_true, row.y_pred))
        extraction_gap = float(mean_squared_error(y_enet, row.y_pred))
        cross_term = float(2 * np.mean((y_true - y_enet) * (y_enet - row.y_pred)))
        rows.append(
            {
                "variation": row.variation,
                "input_group": row.input_group,
                "family": row.family,
                "mode": row.mode,
                "baseline_variation": row.baseline_variation,
                "mse_total": mse,
                "rmse_total": float(np.sqrt(mse)),
                "mse_enet": enet_mse,
                "extraction_gap": extraction_gap,
                "cross_term": cross_term,
                "reconstruction_error": mse - (enet_mse + extraction_gap + cross_term),
                "pct_total_from_extraction_gap": extraction_gap / mse if mse > 0 else np.nan,
            }
        )
    out = pd.DataFrame(rows)
    baseline_gap = out.loc[:, ["variation", "extraction_gap"]].rename(
        columns={"variation": "baseline_variation", "extraction_gap": "baseline_extraction_gap"}
    )
    out = out.merge(baseline_gap, on="baseline_variation", how="left")
    out["delta_extraction_gap_vs_matched_baseline"] = out["extraction_gap"] - out["baseline_extraction_gap"]
    return out


def compute_monotonicity(pred_table: pd.DataFrame) -> pd.DataFrame:
    effect_true = pred_table.attrs["effect_true"]
    effect_enet = pred_table.attrs["effect_enet"]
    var_true = float(np.var(effect_true, ddof=0))
    sign_true = np.sign(effect_true)
    rows = []
    for row in pred_table.itertuples(index=False):
        effect_pred = row.effect_pred
        rows.append(
            {
                "variation": row.variation,
                "input_group": row.input_group,
                "family": row.family,
                "mode": row.mode,
                "baseline_variation": row.baseline_variation,
                "effect_mean": float(np.mean(effect_pred)),
                "effect_sd": float(np.std(effect_pred, ddof=0)),
                "effect_var": float(np.var(effect_pred, ddof=0)),
                "variance_ratio_vs_true": float(np.var(effect_pred, ddof=0) / var_true) if var_true > 0 else np.nan,
                "sign_accuracy_vs_true": float(np.mean(np.sign(effect_pred) == sign_true)),
                "sign_accuracy_vs_enet": float(np.mean(np.sign(effect_pred) == np.sign(effect_enet))),
                "effect_corr_vs_true": float(np.corrcoef(effect_pred, effect_true)[0, 1]),
                "effect_corr_vs_enet": float(np.corrcoef(effect_pred, effect_enet)[0, 1]),
                "predicted_positive_share": float(np.mean(effect_pred > 0)),
                "predicted_negative_share": float(np.mean(effect_pred < 0)),
            }
        )
    out = pd.DataFrame(rows)
    baseline_cols = [
        "baseline_variation",
        "variance_ratio_vs_true",
        "sign_accuracy_vs_true",
        "effect_corr_vs_true",
        "predicted_positive_share",
    ]
    baseline = out.loc[:, ["variation", "variance_ratio_vs_true", "sign_accuracy_vs_true", "effect_corr_vs_true", "predicted_positive_share"]].rename(
        columns={
            "variation": "baseline_variation",
            "variance_ratio_vs_true": "baseline_variance_ratio_vs_true",
            "sign_accuracy_vs_true": "baseline_sign_accuracy_vs_true",
            "effect_corr_vs_true": "baseline_effect_corr_vs_true",
            "predicted_positive_share": "baseline_predicted_positive_share",
        }
    )
    out = out.merge(baseline, on="baseline_variation", how="left")
    out["delta_sign_accuracy_vs_matched_baseline"] = out["sign_accuracy_vs_true"] - out["baseline_sign_accuracy_vs_true"]
    out["delta_effect_corr_vs_matched_baseline"] = out["effect_corr_vs_true"] - out["baseline_effect_corr_vs_true"]
    out["delta_variance_ratio_vs_matched_baseline"] = out["variance_ratio_vs_true"] - out["baseline_variance_ratio_vs_true"]
    return out


def compute_interaction_blindness(pred_table: pd.DataFrame, val_df: pd.DataFrame) -> pd.DataFrame:
    design_df = add_interactions(val_df[FEATURE_COLS[:-1]].copy())
    X_main = val_df[FEATURE_COLS].astype(float).to_numpy()
    interaction_cols = [name for name, _ in INTERACTION_DEGREES]
    X_full = pd.concat([val_df[FEATURE_COLS].astype(float), design_df[interaction_cols].astype(float)], axis=1).to_numpy()

    targets = {
        "true_effect": pred_table.attrs["effect_true"],
        "enet_effect": pred_table.attrs["effect_enet"],
    }
    for row in pred_table.itertuples(index=False):
        targets[row.variation] = row.effect_pred

    rows = []
    for name, y in targets.items():
        main_pred = loocv_predict(ridge_pipeline(), X_main, y)
        full_pred = loocv_predict(ridge_pipeline(), X_full, y)
        sst = float(np.sum((y - np.mean(y)) ** 2))
        main_sse = float(np.sum((y - main_pred) ** 2))
        full_sse = float(np.sum((y - full_pred) ** 2))
        main_r2 = 1.0 - main_sse / sst if sst > 0 else np.nan
        full_r2 = 1.0 - full_sse / sst if sst > 0 else np.nan
        rows.append(
            {
                "variation": name,
                "main_effect_cv_r2": main_r2,
                "main_plus_interactions_cv_r2": full_r2,
                "interaction_gain_cv_r2": full_r2 - main_r2,
                "main_effect_rmse": float(np.sqrt(mean_squared_error(y, main_pred))),
                "main_plus_interactions_rmse": float(np.sqrt(mean_squared_error(y, full_pred))),
            }
        )
    out = pd.DataFrame(rows)
    meta = pred_table.loc[:, ["variation", "input_group", "family", "mode", "baseline_variation"]]
    out = out.merge(meta, on="variation", how="left")
    baseline = out.loc[:, ["variation", "interaction_gain_cv_r2"]].rename(
        columns={"variation": "baseline_variation", "interaction_gain_cv_r2": "baseline_interaction_gain_cv_r2"}
    )
    out = out.merge(baseline, on="baseline_variation", how="left")
    out["delta_interaction_gain_vs_matched_baseline"] = out["interaction_gain_cv_r2"] - out["baseline_interaction_gain_cv_r2"]
    return out


def compute_calibration_decomposition(pred_table: pd.DataFrame, val_df: pd.DataFrame) -> pd.DataFrame:
    y_true = pred_table.attrs["y_true"]
    y_enet = pred_table.attrs["y_enet"]
    X = val_df[FEATURE_COLS].astype(float).to_numpy()
    config_only_pred = loocv_predict(ridge_pipeline(), X, y_true)
    config_only_mse = float(mean_squared_error(y_true, config_only_pred))
    enet_mse = float(mean_squared_error(y_true, y_enet))

    rows = []
    for row in pred_table.itertuples(index=False):
        raw_mse = float(mean_squared_error(y_true, row.y_pred))
        raw_rmse = float(np.sqrt(raw_mse))
        X_uni = row.y_pred.reshape(-1, 1)
        uni_pred = loocv_predict(LinearRegression(), X_uni, y_true)
        uni_mse = float(mean_squared_error(y_true, uni_pred))
        X_plus = np.column_stack([X, row.y_pred])
        plus_pred = loocv_predict(ridge_pipeline(), X_plus, y_true)
        plus_mse = float(mean_squared_error(y_true, plus_pred))

        rows.append(
            {
                "variation": row.variation,
                "input_group": row.input_group,
                "family": row.family,
                "mode": row.mode,
                "baseline_variation": row.baseline_variation,
                "raw_mse": raw_mse,
                "raw_rmse": raw_rmse,
                "univariate_calibrated_mse": uni_mse,
                "univariate_calibrated_rmse": float(np.sqrt(uni_mse)),
                "config_only_mse": config_only_mse,
                "config_only_rmse": float(np.sqrt(config_only_mse)),
                "config_plus_prediction_mse": plus_mse,
                "config_plus_prediction_rmse": float(np.sqrt(plus_mse)),
                "enet_mse": enet_mse,
                "enet_rmse": float(np.sqrt(enet_mse)),
                "univariate_calibration_gain_mse": raw_mse - uni_mse,
                "config_plus_incremental_gain_mse": config_only_mse - plus_mse,
                "benchmark_gap_after_univariate": uni_mse - enet_mse,
                "benchmark_gap_after_config_plus": plus_mse - enet_mse,
            }
        )
    return pd.DataFrame(rows)


def add_variant_overview(
    pred_table: pd.DataFrame,
    ewoa_summary: pd.DataFrame,
    error_decomp: pd.DataFrame,
    monotonicity: pd.DataFrame,
    interaction_df: pd.DataFrame,
    calibration_df: pd.DataFrame,
) -> pd.DataFrame:
    base = pred_table.loc[:, ["variation", "input_group", "family", "mode", "baseline_variation", "rmse", "correlation", "directional_accuracy", "r2", "baseline_r2_matched", "delta_r2_vs_matched_baseline"]]
    out = (
        base.merge(ewoa_summary, on=["variation", "input_group", "family", "mode", "baseline_variation"], how="left")
        .merge(
            error_decomp[
                [
                    "variation",
                    "mse_total",
                    "extraction_gap",
                    "delta_extraction_gap_vs_matched_baseline",
                    "pct_total_from_extraction_gap",
                ]
            ],
            on="variation",
            how="left",
        )
        .merge(
            monotonicity[
                [
                    "variation",
                    "effect_mean",
                    "variance_ratio_vs_true",
                    "sign_accuracy_vs_true",
                    "effect_corr_vs_true",
                    "delta_sign_accuracy_vs_matched_baseline",
                    "delta_effect_corr_vs_matched_baseline",
                ]
            ],
            on="variation",
            how="left",
        )
        .merge(
            interaction_df[
                [
                    "variation",
                    "main_effect_cv_r2",
                    "main_plus_interactions_cv_r2",
                    "interaction_gain_cv_r2",
                    "delta_interaction_gain_vs_matched_baseline",
                ]
            ],
            on="variation",
            how="left",
        )
        .merge(
            calibration_df[
                [
                    "variation",
                    "univariate_calibration_gain_mse",
                    "config_plus_incremental_gain_mse",
                    "benchmark_gap_after_univariate",
                    "benchmark_gap_after_config_plus",
                ]
            ],
            on="variation",
            how="left",
        )
    )
    return out


def add_group_summaries(overview: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    aug = overview.loc[overview["input_group"] != "baseline"].copy()
    by_mode_input = (
        aug.groupby(["input_group", "mode"], as_index=False)
        .agg(
            n_variants=("variation", "size"),
            mean_delta_r2=("delta_r2_vs_matched_baseline", "mean"),
            mean_ewoa=("mean_ewoa", "mean"),
            mean_extraction_gap_delta=("delta_extraction_gap_vs_matched_baseline", "mean"),
            mean_sign_acc_delta=("delta_sign_accuracy_vs_matched_baseline", "mean"),
            mean_effect_corr=("effect_corr_vs_true", "mean"),
            mean_interaction_gain_delta=("delta_interaction_gain_vs_matched_baseline", "mean"),
            mean_calibration_gain=("univariate_calibration_gain_mse", "mean"),
            mean_config_plus_incremental_gain=("config_plus_incremental_gain_mse", "mean"),
        )
    )
    by_family = (
        aug.groupby(["input_group", "family", "mode"], as_index=False)
        .agg(
            mean_r2=("r2", "mean"),
            mean_ewoa=("mean_ewoa", "mean"),
            mean_delta_extraction_gap=("delta_extraction_gap_vs_matched_baseline", "mean"),
            mean_sign_accuracy=("sign_accuracy_vs_true", "mean"),
            mean_effect_corr=("effect_corr_vs_true", "mean"),
            mean_interaction_gain=("interaction_gain_cv_r2", "mean"),
            mean_calibration_gain=("univariate_calibration_gain_mse", "mean"),
            mean_config_plus_incremental_gain=("config_plus_incremental_gain_mse", "mean"),
        )
    )
    return by_mode_input, by_family


def main() -> None:
    val_df, pred_df, metrics_df = load_core_data()
    pred_table = build_prediction_table(val_df, pred_df, metrics_df)

    ewoa_cfg, ewoa_variant = compute_ewoa(pred_table)
    error_decomp = compute_error_decomposition(pred_table)
    monotonicity = compute_monotonicity(pred_table)
    interaction_df = compute_interaction_blindness(pred_table, val_df)
    calibration_df = compute_calibration_decomposition(pred_table, val_df)
    overview = add_variant_overview(
        pred_table=pred_table,
        ewoa_summary=ewoa_variant,
        error_decomp=error_decomp,
        monotonicity=monotonicity,
        interaction_df=interaction_df,
        calibration_df=calibration_df,
    )
    group_mode_input, group_family = add_group_summaries(overview)

    ewoa_cfg.to_csv(RESULTS / "validation_matched_ewoa_by_config.csv", index=False)
    ewoa_variant.to_csv(RESULTS / "validation_matched_ewoa_by_variant.csv", index=False)
    error_decomp.to_csv(RESULTS / "validation_extraction_gap_decomposition.csv", index=False)
    monotonicity.to_csv(RESULTS / "validation_monotonicity_heterogeneity.csv", index=False)
    interaction_df.to_csv(RESULTS / "validation_interaction_blindness_summary.csv", index=False)
    calibration_df.to_csv(RESULTS / "validation_calibration_structure_decomposition.csv", index=False)
    overview.to_csv(RESULTS / "validation_high_priority_variant_overview.csv", index=False)
    group_mode_input.to_csv(RESULTS / "validation_high_priority_group_mode_input_summary.csv", index=False)
    group_family.to_csv(RESULTS / "validation_high_priority_family_summary.csv", index=False)


if __name__ == "__main__":
    main()
