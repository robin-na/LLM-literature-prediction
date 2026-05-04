from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    from scipy.stats import pearsonr
except Exception:  # pragma: no cover - fallback if scipy is unavailable
    pearsonr = None


WORKBOOKS = [
    ROOT / "batch_processing" / "output_csv" / "simple_batch_197papers.xlsx",
    ROOT / "batch_processing" / "output_csv" / "simple_batch_810papers.xlsx",
]
BROAD_ALL_INDEX = ROOT / "literature" / "output" / "paper_analysis_reports" / "broad_all" / "report_index.csv"
INTEGRATIVE_CSV = ROOT / "science-data_and_code" / "data" / "processed_data" / "df_analysis_learn.csv"
IMPORTANCE_CSV = ROOT / "plots" / "lab_config_distributions_260421" / "parameter_analysis_mentions_variation_vs_predictive_importance.csv"

ANALYSIS_RESULTS_DIR = ROOT / "results" / "paper" / "lab_config_distributions_260427"
PARAM_PLOTS_DIR = ROOT / "plots" / "lab_config_distributions_260427"
BATCH_PLOTS_DIR = ROOT / "batch_processing" / "plots" / "lab_config_distributions_260427"
MAIN_TEXT_RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"

MISSING_MARKERS = {"", "N/R", "N/A", "NA", "NR"}
BOOL_TRUE = {"true", "1", "yes", "y"}
BOOL_FALSE = {"false", "0", "no", "n"}

ALL_CONFIG_COLS = [
    "CONFIG_playerCount",
    "CONFIG_numRounds",
    "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp",
    "CONFIG_MPCR",
    "CONFIG_chat",
    "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId",
    "CONFIG_showRewardId",
    "CONFIG_showNRounds",
    "CONFIG_punishmentExists",
    "CONFIG_punishmentCost",
    "CONFIG_punishmentTech",
    "CONFIG_rewardExists",
    "CONFIG_endowment",
]

COMPARE_CONFIG_COLS = [col for col in ALL_CONFIG_COLS if col != "CONFIG_endowment"]

LABELS = {
    "CONFIG_playerCount": "Group size",
    "CONFIG_numRounds": "Number of rounds",
    "CONFIG_allOrNothing": "All-or-nothing",
    "CONFIG_defaultContribProp": "Default contribution",
    "CONFIG_MPCR": "MPCR",
    "CONFIG_chat": "Chat",
    "CONFIG_showOtherSummaries": "Show other summaries",
    "CONFIG_showPunishmentId": "Show punishment ID",
    "CONFIG_showRewardId": "Show reward ID",
    "CONFIG_showNRounds": "Show number of rounds",
    "CONFIG_punishmentExists": "Punishment exists",
    "CONFIG_punishmentCost": "Punishment cost",
    "CONFIG_punishmentTech": "Punishment technology",
    "CONFIG_rewardExists": "Reward exists",
    "CONFIG_rewardCost": "Reward cost",
    "CONFIG_rewardTech": "Reward technology",
    "CONFIG_endowment": "Endowment",
    "CONFIG_showAnyId": "Show punishment/reward ID",
}

PREDICTIVE_CATEGORIES = {
    "Game Structure": "#5DA5DA",
    "Contribution Structure": "#60BD68",
    "Social Information": "#F15854",
    "Incentive Mechanisms": "#B276B2",
}


@dataclass(frozen=True)
class ParameterSpec:
    name: str
    label: str
    kind: str
    columns: tuple[str, ...]


DESIGN_PARAMETER_SPECS = [
    ParameterSpec("CONFIG_playerCount", "Group size", "atomic", ("CONFIG_playerCount",)),
    ParameterSpec("CONFIG_numRounds", "Number of rounds", "atomic", ("CONFIG_numRounds",)),
    ParameterSpec("CONFIG_rewardExists", "Reward exists", "atomic", ("CONFIG_rewardExists",)),
    ParameterSpec("CONFIG_punishmentTech", "Punishment technology", "atomic", ("CONFIG_punishmentTech",)),
    ParameterSpec("CONFIG_punishmentCost", "Punishment cost", "atomic", ("CONFIG_punishmentCost",)),
    ParameterSpec("CONFIG_chat", "Chat", "atomic", ("CONFIG_chat",)),
    ParameterSpec("CONFIG_allOrNothing", "All-or-nothing", "atomic", ("CONFIG_allOrNothing",)),
    ParameterSpec("CONFIG_MPCR", "MPCR", "atomic", ("CONFIG_MPCR",)),
    ParameterSpec("CONFIG_showOtherSummaries", "Show other summaries", "atomic", ("CONFIG_showOtherSummaries",)),
    ParameterSpec("CONFIG_defaultContribProp", "Default contribution", "atomic", ("CONFIG_defaultContribProp",)),
    ParameterSpec("CONFIG_showAnyId", "Show punishment/reward ID", "merged_any_id", ("CONFIG_showPunishmentId", "CONFIG_showRewardId")),
    ParameterSpec("CONFIG_showNRounds", "Show number of rounds", "atomic", ("CONFIG_showNRounds",)),
]


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "figure.dpi": 120,
            "savefig.dpi": 300,
        }
    )


def ensure_dirs() -> None:
    for path in [ANALYSIS_RESULTS_DIR, PARAM_PLOTS_DIR, BATCH_PLOTS_DIR, MAIN_TEXT_RESULTS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def is_true_mask(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False)
    lowered = series.astype(str).str.strip().str.lower()
    num = pd.to_numeric(series, errors="coerce")
    return lowered.isin(BOOL_TRUE) | num.eq(1)


def missing_mask(series: pd.Series, include_neg1: bool = False) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.isna()

    s_str = series.astype(str).str.strip()
    miss = series.isna() | s_str.eq("") | s_str.str.upper().isin(MISSING_MARKERS)
    num = pd.to_numeric(series, errors="coerce")
    if include_neg1:
        miss = miss | num.eq(-1)
    return miss


def cleaned_series(series: pd.Series, include_neg1: bool = False) -> pd.Series:
    keep = ~missing_mask(series, include_neg1=include_neg1)
    s = series.loc[keep]
    if pd.api.types.is_bool_dtype(s):
        return s.astype(int)

    lowered = s.astype(str).str.strip().str.lower()
    boolish = lowered.map({**{k: 1 for k in BOOL_TRUE}, **{k: 0 for k in BOOL_FALSE}})
    if len(boolish) > 0 and boolish.notna().mean() >= 0.8:
        return boolish.dropna().astype(int)

    numeric = pd.to_numeric(s, errors="coerce")
    if len(numeric) > 0 and numeric.notna().mean() >= 0.8:
        return numeric.dropna()
    return s.astype(str).str.strip()


def binaryish_series(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.astype(float)
    s = series.astype(str).str.strip().str.lower()
    out = pd.Series(np.nan, index=series.index, dtype=float)
    out.loc[s.isin(BOOL_TRUE)] = 1.0
    out.loc[s.isin(BOOL_FALSE)] = 0.0
    num = pd.to_numeric(series, errors="coerce")
    out.loc[num.isin([0, 1])] = num.loc[num.isin([0, 1])]
    return out


def merged_any_id_series(df: pd.DataFrame) -> pd.Series:
    a = binaryish_series(df["CONFIG_showPunishmentId"])
    b = binaryish_series(df["CONFIG_showRewardId"])
    present = a.notna() | b.notna()
    merged = pd.Series(np.nan, index=df.index, dtype=float)
    merged.loc[present] = np.maximum(a.fillna(0), b.fillna(0)).loc[present]
    return merged


def parameter_present_mask(df: pd.DataFrame, spec: ParameterSpec) -> pd.Series:
    if spec.kind == "atomic":
        return ~missing_mask(df[spec.columns[0]], include_neg1=True)
    if spec.kind == "merged_any_id":
        return ~(missing_mask(df[spec.columns[0]], include_neg1=True) & missing_mask(df[spec.columns[1]], include_neg1=True))
    raise ValueError(f"Unsupported parameter kind: {spec.kind}")


def parameter_value_series(df: pd.DataFrame, spec: ParameterSpec) -> pd.Series:
    if spec.kind == "atomic":
        return cleaned_series(df[spec.columns[0]], include_neg1=True)
    if spec.kind == "merged_any_id":
        return merged_any_id_series(df).dropna()
    raise ValueError(f"Unsupported parameter kind: {spec.kind}")


def is_binary(series: pd.Series) -> bool:
    vals = pd.Series(series).dropna().unique().tolist()
    return set(vals).issubset({0, 1, True, False})


def evenness_metric(series: pd.Series) -> float:
    s = pd.Series(series).dropna()
    if len(s) == 0:
        return 0.0
    p = s.value_counts(normalize=True)
    if len(p) <= 1:
        return 0.0
    entropy = -(p * np.log2(p)).sum()
    return float(entropy / np.log2(len(p)))


def entropy_metric_from_bins(series: pd.Series, bins: np.ndarray) -> float:
    s = pd.to_numeric(pd.Series(series), errors="coerce").dropna()
    if len(s) == 0:
        return 0.0
    counts, _ = np.histogram(s, bins=bins)
    if counts.sum() == 0:
        return 0.0
    p = counts[counts > 0] / counts.sum()
    if len(p) <= 1:
        return 0.0
    entropy = -(p * np.log2(p)).sum()
    return float(entropy / np.log2(len(p)))


def load_combined_extractions() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    broad_all = pd.read_csv(BROAD_ALL_INDEX, usecols=["custom_id"])
    broad_all_ids = set(broad_all["custom_id"].dropna().astype(str))

    summaries: list[dict[str, object]] = []
    filtered_frames: list[pd.DataFrame] = []
    all_frames: list[pd.DataFrame] = []
    for workbook in WORKBOOKS:
        df = pd.read_excel(workbook, sheet_name="extractions")
        df["custom_id"] = df["custom_id"].astype(str)
        df["source_workbook"] = workbook.name
        all_frames.append(df)

        in_scope = df["custom_id"].isin(broad_all_ids)
        summaries.append(
            {
                "source_workbook": workbook.name,
                "rows_total": int(len(df)),
                "rows_in_broad_all": int(in_scope.sum()),
                "rows_dropped_outside_broad_all": int((~in_scope).sum()),
                "papers_total": int(df["custom_id"].nunique()),
                "papers_in_broad_all": int(df.loc[in_scope, "custom_id"].nunique()),
                "papers_dropped_outside_broad_all": int(df.loc[~in_scope, "custom_id"].nunique()),
            }
        )
        filtered_frames.append(df.loc[in_scope].copy())

    combined_all = pd.concat(all_frames, ignore_index=True, sort=False)
    combined = pd.concat(filtered_frames, ignore_index=True, sort=False)
    combined = combined.sort_values(["custom_id", "source_workbook"]).reset_index(drop=True)
    lab = combined.loc[is_true_mask(combined["METHOD_lab"])].copy().reset_index(drop=True)

    summary_df = pd.DataFrame(summaries)
    overall_row = {
        "source_workbook": "combined",
        "rows_total": int(len(combined_all)),
        "rows_in_broad_all": int(len(combined)),
        "rows_dropped_outside_broad_all": int(len(combined_all) - len(combined)),
        "papers_total": int(combined_all["custom_id"].nunique()),
        "papers_in_broad_all": int(combined["custom_id"].nunique()),
        "papers_dropped_outside_broad_all": int(combined_all["custom_id"].nunique() - combined["custom_id"].nunique()),
    }
    summary_df = pd.concat([summary_df, pd.DataFrame([overall_row])], ignore_index=True)
    return combined_all, combined, lab, summary_df


def save_combined_tables(combined_all: pd.DataFrame, combined: pd.DataFrame, lab: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    combined_all.to_csv(ANALYSIS_RESULTS_DIR / "combined_extractions_all_rows.csv", index=False)
    combined.to_csv(ANALYSIS_RESULTS_DIR / "combined_extractions_broad_all_rows.csv", index=False)
    lab.to_csv(ANALYSIS_RESULTS_DIR / "combined_lab_extractions_broad_all_rows.csv", index=False)
    summary_df.to_csv(ANALYSIS_RESULTS_DIR / "combined_extractions_broad_all_summary.csv", index=False)


def plot_single_distribution(series: pd.Series, label: str, out_path: Path) -> None:
    s = cleaned_series(series, include_neg1=True)
    if len(s) == 0:
        return

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    if is_binary(s) or pd.Series(s).nunique() <= 10:
        counts = pd.Series(s).value_counts().sort_index()
        ax.bar(counts.index.astype(str), counts.values, color="#4c78a8", edgecolor="white")
        ax.set_ylabel("Number of experiments")
    else:
        vals = pd.to_numeric(s, errors="coerce").dropna()
        ax.hist(vals, bins=15, color="#4c78a8", edgecolor="white")
        ax.set_ylabel("Number of experiments")
    ax.set_xlabel(label)
    ax.set_title(f"{label} distribution")
    plt.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)


def make_batch_config_distributions(lab: pd.DataFrame) -> None:
    for col in ALL_CONFIG_COLS:
        plot_single_distribution(lab[col], LABELS[col], BATCH_PLOTS_DIR / f"lab_{col}_distribution.png")


def make_reported_count_histogram(lab: pd.DataFrame) -> pd.DataFrame:
    counts = pd.Series(0, index=lab.index, dtype=int)
    for spec in DESIGN_PARAMETER_SPECS:
        counts += parameter_present_mask(lab, spec).astype(int)

    total_params = len(DESIGN_PARAMETER_SPECS)
    value_counts = counts.value_counts().sort_index().reindex(range(0, total_params + 1), fill_value=0)
    rows = pd.DataFrame(
        {
            "n_design_parameters_reported": value_counts.index.astype(int),
            "n_experiments": value_counts.values.astype(int),
        }
    )
    rows.to_csv(ANALYSIS_RESULTS_DIR / "parameter_analysis_config_specified_counts.csv", index=False)

    cmap = plt.cm.YlGnBu
    colors = [cmap(i / max(1, total_params)) for i in value_counts.index]

    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.bar(value_counts.index.values, value_counts.values, color=colors, edgecolor="white")
    ax.set_xlabel(f"Number of design parameters reported/inferred (out of {total_params})")
    ax.set_ylabel("Number of experiments")
    fully_reported = (counts == total_params).mean() * 100
    more_than_half_missing = (counts < (total_params / 2)).mean() * 100
    ax.legend(
        [
            f"Fully reported ({total_params} of {total_params}): {fully_reported:.1f}%",
            f"More than half missing: {more_than_half_missing:.1f}%",
        ],
        loc="upper left",
        frameon=True,
    )
    ax.set_xticks(value_counts.index.values)
    ax.set_xlim(-0.5, total_params + 0.5)
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_config_specified_counts.{ext}", bbox_inches="tight")
    plt.close(fig)
    return rows


def make_dv_availability_figure(lab: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        ("Outcome variables listed", "DVs"),
        ("Outcome variables defined", "DVs_Definitions"),
        ("Efficiency outcome flagged", "DV_efficiencyReported"),
    ]
    rows = []
    for label, col in metrics:
        available = (~missing_mask(lab[col], include_neg1=True)).mean() * 100
        rows.append({"metric": label, "percent_available": available, "percent_missing": 100 - available})
    out = pd.DataFrame(rows)
    out.to_csv(ANALYSIS_RESULTS_DIR / "parameter_analysis_missing_dv_values_available_schema.csv", index=False)

    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    y = np.arange(len(out))
    ax.barh(y, out["percent_available"], color="#4c78a8", label="Available")
    ax.barh(y, out["percent_missing"], left=out["percent_available"], color="#d9dde5", label="Missing")
    ax.set_yticks(y)
    ax.set_yticklabels(out["metric"])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("% of experiments")
    ax.set_title("Outcome-variable reporting availability (lab experiments)")
    ax.legend(frameon=False, loc="lower right")
    for idx, row in out.iterrows():
        ax.text(min(row["percent_available"] + 1.5, 96), idx, f"{row['percent_available']:.1f}%", va="center", ha="left", fontsize=9)
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_missing_dv_values_available_schema.{ext}", bbox_inches="tight")
    plt.close(fig)
    return out


def make_integrative_comparison_figure(lab: pd.DataFrame) -> None:
    intg = pd.read_csv(INTEGRATIVE_CSV)
    n_cols = 4
    n_rows = int(np.ceil(len(COMPARE_CONFIG_COLS) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 3.6 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(COMPARE_CONFIG_COLS):
        ax = axes[i]
        s_int_raw = cleaned_series(intg[col], include_neg1=True)
        s_lit_raw = cleaned_series(lab[col], include_neg1=True)
        if len(s_int_raw) == 0:
            ax.set_visible(False)
            continue

        use_evenness = is_binary(s_int_raw) or pd.Series(s_int_raw).nunique() <= 5
        if is_binary(s_int_raw):
            s_int = pd.to_numeric(s_int_raw, errors="coerce").dropna().astype(int)
            s_lit = pd.to_numeric(s_lit_raw, errors="coerce").dropna().astype(int)
            categories = [0, 1]
            s_int = s_int[s_int.isin(categories)]
            s_lit = s_lit[s_lit.isin(categories)]
            int_counts = s_int.value_counts(normalize=True).reindex(categories, fill_value=0)
            lit_counts = s_lit.value_counts(normalize=True).reindex(categories, fill_value=0)
            ax.bar(categories, int_counts.values, width=0.6, alpha=0.55, color="#1f77b4")
            ax.bar(categories, lit_counts.values, width=0.6, alpha=0.55, color="#ff7f0e")
            ax.set_xticks(categories)
            ax.set_xticklabels(["False", "True"])
            ax.set_ylim(0, max(int_counts.max(), lit_counts.max()) * 1.15 + 1e-9)
            m_int = evenness_metric(s_int)
            m_lit = evenness_metric(s_lit)
            metric_name = "Evenness"
        elif use_evenness:
            s_int = pd.to_numeric(s_int_raw, errors="coerce").dropna()
            s_lit = pd.to_numeric(s_lit_raw, errors="coerce").dropna()
            categories = sorted(s_int.unique())
            s_lit = s_lit[s_lit.isin(categories)]
            int_counts = s_int.value_counts(normalize=True).reindex(categories, fill_value=0)
            lit_counts = s_lit.value_counts(normalize=True).reindex(categories, fill_value=0)
            ax.bar(categories, int_counts.values, width=0.6, alpha=0.55, color="#1f77b4")
            ax.bar(categories, lit_counts.values, width=0.6, alpha=0.55, color="#ff7f0e")
            ax.set_xticks(categories)
            ax.set_ylim(0, max(int_counts.max(), lit_counts.max()) * 1.15 + 1e-9)
            m_int = evenness_metric(s_int)
            m_lit = evenness_metric(s_lit)
            metric_name = "Evenness"
        else:
            s_int = pd.to_numeric(s_int_raw, errors="coerce").dropna()
            s_lit = pd.to_numeric(s_lit_raw, errors="coerce").dropna()
            if len(s_int) == 0:
                ax.set_visible(False)
                continue
            min_i, max_i = s_int.min(), s_int.max()
            s_lit = s_lit[(s_lit >= min_i) & (s_lit <= max_i)]
            if min_i == max_i:
                ax.axvline(min_i, color="#1f77b4", linewidth=2)
                if len(s_lit) > 0:
                    ax.axvline(s_lit.median(), color="#ff7f0e", linewidth=2)
                bins = np.linspace(min_i - 0.5, max_i + 0.5, 2)
            else:
                bins = np.linspace(min_i, max_i, 15)
                ax.hist(s_int, bins=bins, density=True, alpha=0.55, color="#1f77b4")
                ax.hist(s_lit, bins=bins, density=True, alpha=0.55, color="#ff7f0e")
                ax.set_xlim(min_i, max_i)
            m_int = entropy_metric_from_bins(s_int, bins)
            m_lit = entropy_metric_from_bins(s_lit, bins)
            metric_name = "Entropy"

        ax.set_title(LABELS[col])
        ax.set_ylabel("Density")
        ax.legend(
            [
                f"Integrative {metric_name}: {m_int:.2f}",
                f"Literature {metric_name}: {m_lit:.2f}",
            ],
            fontsize=7,
            frameon=True,
            loc="upper right",
        )

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.legend(["integrative experiments", "literature experiments"], loc="upper center", bbox_to_anchor=(0.5, 0.965), ncol=2, frameon=True)
    fig.suptitle("Design parameter distributions: literature vs. integrative experiments", y=0.995)
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_config_distributions_literature_vs_integrative.{ext}", bbox_inches="tight")
    plt.close(fig)


def compute_heatmap_tables(lab: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    player = pd.to_numeric(cleaned_series(lab["CONFIG_playerCount"], include_neg1=True), errors="coerce")
    rounds = pd.to_numeric(cleaned_series(lab["CONFIG_numRounds"], include_neg1=True), errors="coerce")
    df_heat = pd.DataFrame({"playerCount": player, "numRounds": rounds}).dropna()
    df_heat = df_heat[(df_heat["playerCount"] >= 2) & (df_heat["numRounds"] >= 1)]

    group_bins = [2, 3, 4, 5, 6, 7, 11, 16, np.inf]
    group_labels = ["2", "3", "4", "5", "6", "7-10", "11-15", ">15"]
    round_bins = [1, 2, 6, 11, 16, 21, 31, 51, np.inf]
    round_labels = ["1", "2-5", "6-10", "11-15", "16-20", "21-30", "31-50", ">50"]

    df_heat["group_bin"] = pd.cut(df_heat["playerCount"], bins=group_bins, labels=group_labels, right=False)
    df_heat["round_bin"] = pd.cut(df_heat["numRounds"], bins=round_bins, labels=round_labels, right=False)
    df_heat = df_heat.dropna(subset=["group_bin", "round_bin"])

    counts = pd.crosstab(df_heat["round_bin"], df_heat["group_bin"]).reindex(index=round_labels, columns=group_labels, fill_value=0)
    percent = counts / counts.values.sum() * 100.0
    return counts, percent


def make_heatmap_figure(counts: pd.DataFrame, percent: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 6.6))
    vmax = float(np.nanmax(percent.values))
    im = ax.imshow(percent.values, cmap="Blues", origin="lower", vmin=0.0, vmax=vmax)
    ax.set_xticks(range(len(percent.columns)))
    ax.set_xticklabels(list(percent.columns))
    ax.set_yticks(range(len(percent.index)))
    ax.set_yticklabels(list(percent.index))
    ax.set_xlabel("Group size")
    ax.set_ylabel("Number of rounds")
    ax.set_title("Confounded variations across design parameters")
    for i in range(percent.shape[0]):
        for j in range(percent.shape[1]):
            val = float(percent.values[i, j])
            if val <= 0:
                continue
            color = "white" if val >= 0.45 * vmax else "#1f2933"
            ax.text(j, i, f"{val:.1f}", ha="center", va="center", fontsize=8, color=color)
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("% of experiments")
    ax.text(0.98, 0.98, f"n={int(counts.values.sum())} experiments", transform=ax.transAxes, ha="right", va="top", fontsize=9, color="#444444")
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_group_size_by_rounds_heatmap.{ext}", bbox_inches="tight")
    plt.close(fig)
    counts.to_csv(ANALYSIS_RESULTS_DIR / "parameter_analysis_group_size_by_rounds_heatmap_counts.csv")
    percent.to_csv(ANALYSIS_RESULTS_DIR / "parameter_analysis_group_size_by_rounds_heatmap_percent.csv")


def pearson_r_and_p(x: pd.Series, y: pd.Series) -> tuple[float, float]:
    x = pd.to_numeric(pd.Series(x), errors="coerce")
    y = pd.to_numeric(pd.Series(y), errors="coerce")
    mask = x.notna() & y.notna()
    x = x.loc[mask]
    y = y.loc[mask]
    if len(x) < 3:
        return float("nan"), float("nan")
    if pearsonr is not None:
        r, p = pearsonr(x.to_numpy(dtype=float), y.to_numpy(dtype=float))
        return float(r), float(p)
    return float(np.corrcoef(x, y)[0, 1]), float("nan")


def build_design_parameter_tables(lab: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    papers = []
    param_summary: list[dict[str, object]] = []
    varied_paper_ids: dict[str, list[str]] = {spec.name: [] for spec in DESIGN_PARAMETER_SPECS}
    any_reported_by_param: dict[str, int] = {spec.name: 0 for spec in DESIGN_PARAMETER_SPECS}
    varied_by_param: dict[str, int] = {spec.name: 0 for spec in DESIGN_PARAMETER_SPECS}

    grouped = list(lab.groupby("custom_id", sort=True))
    n_papers_total = len(grouped)
    for custom_id, paper_df in grouped:
        n_reported_all = 0
        n_varied = 0
        for spec in DESIGN_PARAMETER_SPECS:
            present = parameter_present_mask(paper_df, spec)
            any_reported = bool(present.any())
            all_reported = bool(present.all())
            values = parameter_value_series(paper_df, spec)
            varied = bool(pd.Series(values).nunique(dropna=True) > 1)
            if any_reported:
                any_reported_by_param[spec.name] += 1
            if varied:
                varied_by_param[spec.name] += 1
                varied_paper_ids[spec.name].append(custom_id)
            if all_reported:
                n_reported_all += 1
            if varied:
                n_varied += 1
        papers.append(
            {
                "custom_id": custom_id,
                "n_lab_rows": int(len(paper_df)),
                "n_reported_params": n_reported_all,
                "n_varied_params": n_varied,
            }
        )

    paper_df = pd.DataFrame(papers).sort_values(["n_varied_params", "n_lab_rows", "custom_id"], ascending=[False, False, True]).reset_index(drop=True)
    dist_df = (
        pd.DataFrame({"n_design_parameters": range(len(DESIGN_PARAMETER_SPECS) + 1)})
        .merge(paper_df["n_reported_params"].value_counts().rename("n_papers_mentioned"), left_on="n_design_parameters", right_index=True, how="left")
        .merge(paper_df["n_varied_params"].value_counts().rename("n_papers_varied"), left_on="n_design_parameters", right_index=True, how="left")
        .fillna(0)
    )
    dist_df[["n_papers_mentioned", "n_papers_varied"]] = dist_df[["n_papers_mentioned", "n_papers_varied"]].astype(int)

    for spec in DESIGN_PARAMETER_SPECS:
        param_summary.append(
            {
                "parameter": spec.name,
                "label": spec.label,
                "n_papers_mentioned": any_reported_by_param[spec.name],
                "percent_papers_mentioned": any_reported_by_param[spec.name] / n_papers_total * 100.0,
                "n_papers_varied": varied_by_param[spec.name],
                "percent_papers_varied": varied_by_param[spec.name] / n_papers_total * 100.0,
                "n_papers_total": n_papers_total,
                "paper_ids": ";".join(varied_paper_ids[spec.name]),
            }
        )
    param_df = pd.DataFrame(param_summary).sort_values(
        ["percent_papers_varied", "percent_papers_mentioned", "label"],
        ascending=[False, False, True],
    ).reset_index(drop=True)
    return paper_df, dist_df, param_df


def make_varied_counts_plot(paper_df: pd.DataFrame) -> None:
    paper_df.to_csv(ANALYSIS_RESULTS_DIR / "parameter_analysis_config_varied_counts_by_paper_rows.csv", index=False)
    hist = paper_df["n_varied_params"].value_counts().sort_index().reindex(range(len(DESIGN_PARAMETER_SPECS) + 1), fill_value=0)
    fig, ax = plt.subplots(figsize=(8.2, 4.5))
    ax.bar(hist.index, hist.values, color="#f58518", edgecolor="white")
    ax.set_xlabel("Number of design parameters varied")
    ax.set_ylabel("Number of papers")
    ax.set_title("Most papers vary few design parameters")
    ax.set_xticks(hist.index)
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_config_varied_counts_by_paper.{ext}", bbox_inches="tight")
    plt.close(fig)
    paper_df[["custom_id", "n_lab_rows", "n_varied_params"]].to_csv(PARAM_PLOTS_DIR / "parameter_analysis_config_varied_counts_by_paper.csv", index=False)


def make_varied_percent_plot(param_df: pd.DataFrame) -> None:
    out = param_df[["parameter", "label", "n_papers_varied", "n_papers_total", "percent_papers_varied", "paper_ids"]].copy()
    out.to_csv(PARAM_PLOTS_DIR / "parameter_analysis_config_varied_percent_by_parameter.csv", index=False)

    plot_df = out.sort_values(["percent_papers_varied", "percent_papers_mentioned" if "percent_papers_mentioned" in out.columns else "label"], ascending=[False, False]).copy()
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    y = np.arange(len(plot_df))
    ax.barh(y, plot_df["percent_papers_varied"], color="#f58518", edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(plot_df["label"])
    ax.invert_yaxis()
    ax.set_xlabel("% of papers")
    ax.set_title("Design parameters rarely vary across papers")
    for idx, row in enumerate(plot_df.itertuples()):
        ax.text(row.percent_papers_varied + 0.6, idx, f"{row.percent_papers_varied:.1f}%", va="center", ha="left", fontsize=8)
    plt.tight_layout()
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_config_varied_percent_by_parameter.{ext}", bbox_inches="tight")
    plt.close(fig)


def make_predictive_importance_plot(param_df: pd.DataFrame) -> None:
    mapping = pd.read_csv(IMPORTANCE_CSV)
    keep_cols = ["parameter", "label", "short_label", "category", "importance_feature", "predictive_importance_pct_rmse", "plotted"]
    mapping = mapping[keep_cols].drop_duplicates("parameter")
    mapping = mapping.loc[mapping["parameter"].isin(param_df["parameter"])].copy()
    merged = mapping.merge(
        param_df[["parameter", "n_papers_mentioned", "percent_papers_mentioned", "n_papers_varied", "percent_papers_varied", "n_papers_total"]],
        on="parameter",
        how="left",
    )
    merged.to_csv(PARAM_PLOTS_DIR / "parameter_analysis_mentions_variation_vs_predictive_importance.csv", index=False)

    plot_df = merged.loc[merged["plotted"].fillna(False)].copy()
    if plot_df.empty:
        return

    fig, axes = plt.subplots(1, 2, figsize=(15.6, 7.2), sharex=False)
    panels = [
        ("Reported vs. Importance", "percent_papers_mentioned", "% of papers reporting parameter"),
        ("Explicit Variation vs. Importance", "percent_papers_varied", "% of papers varying parameter"),
    ]
    for ax, (title, y_col, y_label) in zip(axes, panels):
        x = plot_df["predictive_importance_pct_rmse"]
        y = plot_df[y_col]
        r, p = pearson_r_and_p(x, y)
        ax.axvline(x.mean(), color="#b8b8b8", linestyle=(0, (5, 4)), linewidth=1.2, zorder=1)
        ax.axhline(y.mean(), color="#b8b8b8", linestyle=(0, (5, 4)), linewidth=1.2, zorder=1)
        for row in plot_df.itertuples():
            color = PREDICTIVE_CATEGORIES.get(row.category, "#4c78a8")
            ax.scatter(row.predictive_importance_pct_rmse, getattr(row, y_col), s=850, color=color, edgecolor="#444444", linewidth=2.4, alpha=0.9, zorder=3)
            ax.text(
                row.predictive_importance_pct_rmse + 0.7,
                getattr(row, y_col) + 0.3,
                row.short_label,
                fontsize=8.5,
                fontweight="bold",
                color="black",
                bbox={"facecolor": "white", "edgecolor": color, "boxstyle": "round,pad=0.25", "linewidth": 1.2},
                zorder=4,
            )
        p_text = f"{p:.3f}" if np.isfinite(p) else "n/a"
        ax.set_title(f"{title}\nr = {r:.2f}, p = {p_text}", fontsize=16, fontweight="bold", pad=14)
        ax.set_xlabel("Predictive importance (% change in RMSE when shuffled)", fontsize=13, fontweight="bold")
        ax.set_ylabel(y_label, fontsize=13, fontweight="bold")
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35)

    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="", markersize=14, markerfacecolor=color, markeredgecolor="#444444", markeredgewidth=1.5, label=label)
        for label, color in PREDICTIVE_CATEGORIES.items()
    ]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.02), ncol=4, frameon=False, fontsize=11)
    fig.text(
        0.5,
        -0.09,
        f"E-net permutation importance from Abdullah Fig. 4; plotted 12 design parameters. n = {int(plot_df['n_papers_total'].iloc[0])} lab papers.",
        ha="center",
        va="center",
        fontsize=10,
        color="#555555",
    )
    plt.tight_layout(rect=[0, 0.06, 1, 1])
    for ext in ["png", "pdf"]:
        fig.savefig(PARAM_PLOTS_DIR / f"parameter_analysis_mentions_variation_vs_predictive_importance.{ext}", bbox_inches="tight")
    plt.close(fig)


def save_figure4_inputs(paper_df: pd.DataFrame, dist_df: pd.DataFrame, param_df: pd.DataFrame, counts: pd.DataFrame, percent: pd.DataFrame, summary_df: pd.DataFrame, lab: pd.DataFrame) -> None:
    MAIN_TEXT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    param_df[["parameter", "label", "n_papers_mentioned", "percent_papers_mentioned", "n_papers_varied", "percent_papers_varied", "n_papers_total"]].to_csv(
        MAIN_TEXT_RESULTS_DIR / "figure4_design_parameter_mention_variation_rows.csv",
        index=False,
    )
    dist_df.to_csv(MAIN_TEXT_RESULTS_DIR / "figure4_design_parameter_count_distribution_rows.csv", index=False)
    paper_df.to_csv(MAIN_TEXT_RESULTS_DIR / "figure4_design_parameter_count_by_paper_rows.csv", index=False)
    counts.to_csv(MAIN_TEXT_RESULTS_DIR / "figure4_group_size_rounds_heatmap_counts.csv")
    percent.to_csv(MAIN_TEXT_RESULTS_DIR / "figure4_group_size_rounds_heatmap_percent.csv")

    dropped_papers = int(summary_df.loc[summary_df["source_workbook"] == "combined", "papers_dropped_outside_broad_all"].iloc[0])
    dropped_rows = int(summary_df.loc[summary_df["source_workbook"] == "combined", "rows_dropped_outside_broad_all"].iloc[0])
    doc_lines = [
        "# Figure 5: Empirical Design Limitations",
        "",
        "This file documents the intermediate extraction outputs prepared from the workbook merge step.",
        "The final `260427` Figure 5 panel definitions are written by `analysis/paper_figures/plot_figure5_main_text_260427.py` after it combines these tables with the benchmark design files.",
        "",
        "Inputs:",
        "- `batch_processing/output_csv/simple_batch_197papers.xlsx`",
        "- `batch_processing/output_csv/simple_batch_810papers.xlsx`",
        f"- filtered to the `broad_all` main-analysis inventory in `literature/output/paper_analysis_reports/broad_all/report_index.csv` (`2,011` papers); dropped `{dropped_papers}` out-of-scope papers and `{dropped_rows}` rows.",
        "",
        f"Rows included after filtering: `{len(lab)}` lab-condition rows grouped by `custom_id` (`{lab['custom_id'].nunique()}` papers).",
        "",
        "Intermediate tables saved here:",
        "- `figure4_design_parameter_mention_variation_rows.csv`",
        "- `figure4_design_parameter_count_distribution_rows.csv`",
        "- `figure4_design_parameter_count_by_paper_rows.csv`",
        "- `figure4_group_size_rounds_heatmap_counts.csv`",
        "- `figure4_group_size_rounds_heatmap_percent.csv`",
        "",
        f"The group-size/round-count heatmap intermediate uses `{int(counts.values.sum())}` rows with numeric group size >= 2 and number of rounds >= 1.",
        "",
    ]
    (MAIN_TEXT_RESULTS_DIR / "figure5_empirical_design_limitations_documentation.md").write_text("\n".join(doc_lines))


def main() -> None:
    set_style()
    ensure_dirs()
    combined_all, combined, lab, summary_df = load_combined_extractions()
    save_combined_tables(combined_all, combined, lab, summary_df)

    make_batch_config_distributions(lab)
    make_reported_count_histogram(lab)
    make_dv_availability_figure(lab)
    make_integrative_comparison_figure(lab)

    heat_counts, heat_percent = compute_heatmap_tables(lab)
    make_heatmap_figure(heat_counts, heat_percent)

    paper_df, dist_df, param_df = build_design_parameter_tables(lab)
    make_varied_counts_plot(paper_df)
    make_varied_percent_plot(param_df)
    make_predictive_importance_plot(param_df)
    save_figure4_inputs(paper_df, dist_df, param_df, heat_counts, heat_percent, summary_df, lab)

    print("Saved analysis to:")
    print(f"  {ANALYSIS_RESULTS_DIR}")
    print(f"  {PARAM_PLOTS_DIR}")
    print(f"  {BATCH_PLOTS_DIR}")
    print(f"  {MAIN_TEXT_RESULTS_DIR}")


if __name__ == "__main__":
    main()
