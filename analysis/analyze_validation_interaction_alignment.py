from __future__ import annotations

import json
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PLOTS = ROOT / "plots"
DATA = ROOT / "science-data_and_code" / "data" / "processed_data"
HPO = ROOT / "science-data_and_code" / "data" / "hpo_model_configs.json"

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
    for input_group in ["both", "paper_only", "data_only"]:
        prefix = f"{input_group}_"
        if stem.startswith(prefix):
            return input_group, stem[len(prefix) :], mode
    raise ValueError(f"Unrecognized variation: {variation}")


def load_or_compute_enet_validation_shap(force: bool = False) -> pd.DataFrame:
    cache_path = RESULTS / "cache_enet_validation_shap_values.csv"
    if cache_path.exists() and not force:
        return pd.read_csv(cache_path)

    learn = pd.read_csv(DATA / "df_paired_learn.csv")
    val = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    cfg = json.load(open(HPO))
    elastic_cfg = cfg["ELASTIC"]

    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("interactions", PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)),
            (
                "estimator",
                ElasticNet(
                    alpha=elastic_cfg["alpha"],
                    l1_ratio=elastic_cfg["l1_ratio"],
                    random_state=elastic_cfg["random_seed"],
                ),
            ),
        ]
    )
    pipe.fit(learn[FEATURE_COLS], learn["treatment_itt_efficiency"])

    background_data = learn[FEATURE_COLS].astype(float).values
    masker = shap.maskers.Independent(background_data)

    def model_wrapper(x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        x_df = pd.DataFrame(x, columns=FEATURE_COLS)
        return pipe.predict(x_df)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        explainer = shap.Explainer(model=model_wrapper, masker=masker, feature_names=FEATURE_COLS)
        shap_values = explainer(val[FEATURE_COLS].astype(float).values)

    out = val[FEATURE_COLS].copy()
    out["q_idx"] = np.arange(1, len(out) + 1)
    out["enet_prediction"] = pipe.predict(val[FEATURE_COLS])
    for feature in FEATURE_COLS:
        out[f"shap_{feature}"] = shap_values[:, feature].values
    out.to_csv(cache_path, index=False)
    return out


def compute_enet_validation_permutation_importance(force: bool = False) -> pd.DataFrame:
    cache_path = RESULTS / "cache_enet_validation_permutation_importance.csv"
    if cache_path.exists() and not force:
        return pd.read_csv(cache_path)

    learn = pd.read_csv(DATA / "df_paired_learn.csv")
    val = pd.read_csv(DATA / "df_paired_val.csv")
    cfg = json.load(open(HPO))
    elastic_cfg = cfg["ELASTIC"]
    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("interactions", PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)),
            (
                "estimator",
                ElasticNet(
                    alpha=elastic_cfg["alpha"],
                    l1_ratio=elastic_cfg["l1_ratio"],
                    random_state=elastic_cfg["random_seed"],
                ),
            ),
        ]
    )
    pipe.fit(learn[FEATURE_COLS], learn["treatment_itt_efficiency"])
    baseline = np.sqrt(np.mean((pipe.predict(val[FEATURE_COLS]) * 100 - val["treatment_itt_efficiency"] * 100) ** 2))

    rows = []
    for feature in FEATURE_COLS:
        shuffled_perf = []
        for seed in range(30):
            temp = val.copy()
            temp[feature] = np.random.RandomState(seed=seed).permutation(temp[feature].values)
            rmse = np.sqrt(np.mean((pipe.predict(temp[FEATURE_COLS]) * 100 - val["treatment_itt_efficiency"] * 100) ** 2))
            shuffled_perf.append(rmse)
        rows.append(
            {
                "feature": feature,
                "baseline_rmse": baseline,
                "permuted_rmse_mean": float(np.mean(shuffled_perf)),
                "pct_increase_in_error": 100 * (np.mean(shuffled_perf) - baseline) / baseline,
            }
        )
    out = pd.DataFrame(rows)
    out.to_csv(cache_path, index=False)
    return out


def slope(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 2 or np.allclose(np.std(x), 0):
        return np.nan
    return float(np.polyfit(x, y, 1)[0])


def target_numrounds_vector(shap_df: pd.DataFrame) -> pd.Series:
    rows = []
    for chat in [0, 1]:
        for peer in [0, 1]:
            sub = shap_df[(shap_df["CONFIG_chat"] == chat) & (shap_df["CONFIG_showOtherSummaries"] == peer)]
            rows.append(
                {
                    "cell": f"chat={chat}|peer={peer}",
                    "value": slope(sub["CONFIG_numRounds"].to_numpy(), sub["shap_CONFIG_numRounds"].to_numpy()),
                }
            )
    return pd.DataFrame(rows).set_index("cell")["value"]


def target_framing_vector(shap_df: pd.DataFrame) -> pd.Series:
    rows = []
    for peer in [0, 1]:
        for cont in [0, 1]:
            sub = shap_df[
                (shap_df["CONFIG_showOtherSummaries"] == peer) & (shap_df["CONFIG_allOrNothing"] == cont)
            ]
            opt_in = sub.loc[sub["CONFIG_defaultContribProp"] == 0, "shap_CONFIG_defaultContribProp"]
            opt_out = sub.loc[sub["CONFIG_defaultContribProp"] == 1, "shap_CONFIG_defaultContribProp"]
            value = np.nan
            if len(opt_in) > 0 and len(opt_out) > 0:
                value = float(opt_out.mean() - opt_in.mean())
            rows.append({"cell": f"peer={peer}|allornothing={cont}", "value": value})
    return pd.DataFrame(rows).set_index("cell")["value"]


def variant_numrounds_vector(effect: pd.Series, val_df: pd.DataFrame) -> pd.Series:
    rows = []
    temp = val_df.copy()
    temp["pred_effect"] = effect.values
    for chat in [0, 1]:
        for peer in [0, 1]:
            sub = temp[(temp["CONFIG_chat"] == chat) & (temp["CONFIG_showOtherSummaries"] == peer)]
            rows.append(
                {
                    "cell": f"chat={chat}|peer={peer}",
                    "value": slope(sub["CONFIG_numRounds"].to_numpy(), sub["pred_effect"].to_numpy()),
                }
            )
    return pd.DataFrame(rows).set_index("cell")["value"]


def variant_framing_vector(effect: pd.Series, val_df: pd.DataFrame) -> pd.Series:
    rows = []
    temp = val_df.copy()
    temp["pred_effect"] = effect.values
    for peer in [0, 1]:
        for cont in [0, 1]:
            sub = temp[(temp["CONFIG_showOtherSummaries"] == peer) & (temp["CONFIG_allOrNothing"] == cont)]
            opt_in = sub.loc[sub["CONFIG_defaultContribProp"] == 0, "pred_effect"]
            opt_out = sub.loc[sub["CONFIG_defaultContribProp"] == 1, "pred_effect"]
            value = np.nan
            if len(opt_in) > 0 and len(opt_out) > 0:
                value = float(opt_out.mean() - opt_in.mean())
            rows.append({"cell": f"peer={peer}|allornothing={cont}", "value": value})
    return pd.DataFrame(rows).set_index("cell")["value"]


def safe_corr(a: pd.Series, b: pd.Series) -> float:
    mask = a.notna() & b.notna()
    if mask.sum() < 2:
        return np.nan
    return float(np.corrcoef(a[mask], b[mask])[0, 1])


def safe_rmse(a: pd.Series, b: pd.Series) -> float:
    mask = a.notna() & b.notna()
    if mask.sum() == 0:
        return np.nan
    return float(np.sqrt(np.mean((a[mask] - b[mask]) ** 2)))


def compute_variant_interaction_alignment() -> pd.DataFrame:
    shap_df = load_or_compute_enet_validation_shap()
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    pred_df = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    perf_df = pd.read_csv(RESULTS / "granular_performance_delta_r2_table.csv")
    perf_df = perf_df.loc[perf_df["wave"] == "validation", ["variation", "delta_r2_vs_matched_baseline", "input_group", "family", "mode"]]

    target_num = target_numrounds_vector(shap_df)
    target_frame = target_framing_vector(shap_df)

    control = 100 * val_df["control_itt_efficiency"]
    q_cols = [c for c in pred_df.columns if c.startswith("Q")]

    rows = []
    for _, row in pred_df.iterrows():
        input_group, family, mode = parse_variation(row["variation"])
        effect = row[q_cols].astype(float).reset_index(drop=True) - control.reset_index(drop=True)
        vec_num = variant_numrounds_vector(effect, val_df)
        vec_frame = variant_framing_vector(effect, val_df)
        rows.append(
            {
                "variation": row["variation"],
                "input_group": input_group,
                "family": family,
                "mode": mode,
                "numrounds_alignment_corr": safe_corr(vec_num, target_num),
                "numrounds_alignment_rmse": safe_rmse(vec_num, target_num),
                "framing_alignment_corr": safe_corr(vec_frame, target_frame),
                "framing_alignment_rmse": safe_rmse(vec_frame, target_frame),
            }
        )
    out = pd.DataFrame(rows).merge(perf_df, on=["variation", "input_group", "family", "mode"], how="left")
    return out


def add_vs_baseline(alignment_df: pd.DataFrame) -> pd.DataFrame:
    baseline = (
        alignment_df.loc[alignment_df["input_group"] == "baseline", ["mode", "numrounds_alignment_corr", "numrounds_alignment_rmse", "framing_alignment_corr", "framing_alignment_rmse"]]
        .rename(
            columns={
                "numrounds_alignment_corr": "baseline_numrounds_alignment_corr",
                "numrounds_alignment_rmse": "baseline_numrounds_alignment_rmse",
                "framing_alignment_corr": "baseline_framing_alignment_corr",
                "framing_alignment_rmse": "baseline_framing_alignment_rmse",
            }
        )
    )
    aug = alignment_df.loc[alignment_df["input_group"] != "baseline"].copy()
    out = aug.merge(baseline, on="mode", how="left")
    out["delta_numrounds_alignment_corr_vs_baseline"] = out["numrounds_alignment_corr"] - out["baseline_numrounds_alignment_corr"]
    out["delta_framing_alignment_corr_vs_baseline"] = out["framing_alignment_corr"] - out["baseline_framing_alignment_corr"]
    out["delta_numrounds_alignment_rmse_vs_baseline"] = out["baseline_numrounds_alignment_rmse"] - out["numrounds_alignment_rmse"]
    out["delta_framing_alignment_rmse_vs_baseline"] = out["baseline_framing_alignment_rmse"] - out["framing_alignment_rmse"]
    out["combined_alignment_corr_vs_baseline"] = out[
        ["delta_numrounds_alignment_corr_vs_baseline", "delta_framing_alignment_corr_vs_baseline"]
    ].mean(axis=1)
    out["combined_alignment_rmse_vs_baseline"] = out[
        ["delta_numrounds_alignment_rmse_vs_baseline", "delta_framing_alignment_rmse_vs_baseline"]
    ].mean(axis=1)
    return out


def plot_alignment_scatter(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.3), sharey=True, constrained_layout=True)
    specs = [
        ("delta_numrounds_alignment_corr_vs_baseline", "Game Length interaction\nalignment change vs baseline"),
        ("delta_framing_alignment_corr_vs_baseline", "Contribution Framing interaction\nalignment change vs baseline"),
        ("combined_alignment_corr_vs_baseline", "Combined interaction\nalignment change vs baseline"),
    ]
    colors = {"both": "#1f77b4", "paper_only": "#ff7f0e", "data_only": "#2ca02c"}
    markers = {"single": "o", "reasoning": "s", "joint": "^", "joint_reasoning": "D"}

    for ax, (col, title) in zip(axes, specs):
        for mode, marker in markers.items():
            for input_group, color in colors.items():
                sub = df[(df["mode"] == mode) & (df["input_group"] == input_group)]
                ax.scatter(
                    sub[col],
                    sub["delta_r2_vs_matched_baseline"],
                    color=color,
                    marker=marker,
                    s=58,
                    alpha=0.85,
                    edgecolor="white",
                    linewidth=0.4,
                )
        ax.axhline(0, color="#777777", linestyle="--", linewidth=1)
        ax.axvline(0, color="#777777", linestyle="--", linewidth=1)
        ax.set_title(title)
        ax.set_xlabel("Closer to E-net Figure-5 pattern")
        ax.grid(alpha=0.2)
    axes[0].set_ylabel("ΔR² vs matched baseline")
    fig.suptitle(
        "Validation interaction alignment: do variants that move closer to the E-net interaction pattern perform better?",
        fontsize=16,
    )
    fig.text(
        0.5,
        0.01,
        "Framing comparison uses only the observed validation cells; one Figure-5 cell is absent in the validation design set.",
        ha="center",
        fontsize=9,
        color="#555555",
    )
    fig.savefig(PLOTS / "validation_interaction_alignment_vs_delta_r2.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_interaction_alignment_vs_delta_r2.pdf", bbox_inches="tight")


def plot_interaction_targets_example(df: pd.DataFrame) -> None:
    shap_df = load_or_compute_enet_validation_shap()
    val_df = pd.read_csv(DATA / "df_paired_val.csv").reset_index(drop=True)
    pred_df = pd.read_csv(RESULTS / "prediction_positive_case_variations_41.csv").rename(columns={"Unnamed: 0": "variation"})
    control = 100 * val_df["control_itt_efficiency"]
    q_cols = [c for c in pred_df.columns if c.startswith("Q")]

    best = df.sort_values("delta_r2_vs_matched_baseline", ascending=False).iloc[0]["variation"]
    baseline = "baseline_joint_reasoning"
    selected = [baseline, best]

    fig, axes = plt.subplots(2, 2, figsize=(12.8, 9.0), constrained_layout=True)
    colors = {"E-net target": "#111111", baseline: "#4c78a8", best: "#e45756"}

    # NumRounds interaction lines
    for col_idx, chat in enumerate([0, 1]):
        ax = axes[0, col_idx]
        for peer, label in [(0, "Peer outcomes hidden"), (1, "Peer outcomes visible")]:
            sub = shap_df[(shap_df["CONFIG_chat"] == chat) & (shap_df["CONFIG_showOtherSummaries"] == peer)]
            ax.scatter(sub["CONFIG_numRounds"], sub["shap_CONFIG_numRounds"], color="#666666" if peer == 0 else "#b07aa1", alpha=0.45, s=30)
            xs = np.sort(sub["CONFIG_numRounds"].unique())
            slope_val = slope(sub["CONFIG_numRounds"].to_numpy(), sub["shap_CONFIG_numRounds"].to_numpy())
            intercept = sub["shap_CONFIG_numRounds"].mean() - slope_val * sub["CONFIG_numRounds"].mean()
            ax.plot(xs, intercept + slope_val * xs, color="#111111", linewidth=2, linestyle="--", label=f"E-net target | peer={peer}")

            for variant in selected:
                effect = pred_df.loc[pred_df["variation"] == variant, q_cols].iloc[0].astype(float).reset_index(drop=True) - control.reset_index(drop=True)
                temp = val_df.copy()
                temp["pred_effect"] = effect.values
                part = temp[(temp["CONFIG_chat"] == chat) & (temp["CONFIG_showOtherSummaries"] == peer)]
                sl = slope(part["CONFIG_numRounds"].to_numpy(), part["pred_effect"].to_numpy())
                intercept_llm = part["pred_effect"].mean() - sl * part["CONFIG_numRounds"].mean()
                ax.plot(xs, intercept_llm + sl * xs, color=colors[variant], linewidth=2, alpha=0.85, label=f"{variant} | peer={peer}")
        ax.set_title(f"Validation game-length effect | chat={chat}")
        ax.set_xlabel("Game Length")
        ax.set_ylabel("Effect / SHAP scale")
        ax.grid(alpha=0.2)

    # Framing deltas
    target_frame = target_framing_vector(shap_df)
    categories = list(target_frame.index)
    x = np.arange(len(categories))
    width = 0.22
    axes[1, 0].bar(x - width, target_frame.values, width=width, color="#111111", label="E-net target")
    axes[1, 1].axis("off")
    for idx, variant in enumerate(selected):
        effect = pred_df.loc[pred_df["variation"] == variant, q_cols].iloc[0].astype(float).reset_index(drop=True) - control.reset_index(drop=True)
        vec = variant_framing_vector(effect, val_df)
        axes[1, 0].bar(x + idx * width, vec.values, width=width, color=colors[variant], label=variant)
    axes[1, 0].set_xticks(x, categories, rotation=25, ha="right")
    axes[1, 0].set_title("Validation contribution-framing effect\n(opt-out minus opt-in)")
    axes[1, 0].axhline(0, color="#777777", linewidth=1)
    axes[1, 0].legend(frameon=False, fontsize=8)
    axes[1, 0].grid(axis="y", alpha=0.2)

    note = (
        f"Example best validation variant: {best}\n"
        "The E-net target is computed on validation inputs using the learning-trained manuscript model.\n"
        "One framing cell is absent in validation, so that bar is omitted."
    )
    axes[1, 1].text(0.02, 0.7, note, fontsize=11, va="top")
    fig.suptitle("Validation interaction targets vs LLM examples", fontsize=16)
    fig.savefig(PLOTS / "validation_interaction_targets_examples.png", dpi=220, bbox_inches="tight")
    fig.savefig(PLOTS / "validation_interaction_targets_examples.pdf", bbox_inches="tight")


def main() -> None:
    load_or_compute_enet_validation_shap()
    compute_enet_validation_permutation_importance()
    alignment = compute_variant_interaction_alignment()
    alignment.to_csv(RESULTS / "validation_interaction_alignment_by_variant.csv", index=False)
    aug = add_vs_baseline(alignment)
    aug.to_csv(RESULTS / "validation_interaction_alignment_vs_baseline.csv", index=False)
    plot_alignment_scatter(aug)
    plot_interaction_targets_example(aug)


if __name__ == "__main__":
    main()
