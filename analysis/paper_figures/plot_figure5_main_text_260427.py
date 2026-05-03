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
except Exception:  # pragma: no cover
    pearsonr = None


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427"

LAB_ROWS_CSV = ROOT / "results" / "paper" / "lab_config_distributions_260427" / "combined_lab_extractions_broad_all_rows.csv"
IMPORTANCE_CSV = ROOT / "plots" / "lab_config_distributions_260427" / "parameter_analysis_mentions_variation_vs_predictive_importance.csv"
BENCHMARK_CSVS = [
    ROOT / "input" / "pgg_CONFIGmerged_learn.csv",
    ROOT / "input" / "pgg_CONFIGmerged_validation.csv",
]

REPORTED_COUNT_ROWS_CSV = RESULTS_DIR / "figure5_reported_parameter_count_rows.csv"
IMPORTANCE_ROWS_CSV = RESULTS_DIR / "figure5_variation_vs_importance_rows.csv"
DISTRIBUTION_ROWS_CSV = RESULTS_DIR / "figure5_value_distribution_rows.csv"
DOC_MD = RESULTS_DIR / "figure5_empirical_design_limitations_documentation.md"
OUT_STEM = "figure5_empirical_design_limitations"

MISSING_MARKERS = {"", "N/R", "N/A", "NA", "NR"}
BOOL_TRUE = {"true", "1", "yes", "y"}
BOOL_FALSE = {"false", "0", "no", "n"}

BLUE = "#4c78a8"
ORANGE = "#f58518"
GRID = "#e8ebef"
TEXT = "#222222"


@dataclass(frozen=True)
class ParameterSpec:
    name: str
    label: str
    short_label: str
    value_kind: str
    columns: tuple[str, ...]


PARAMETER_SPECS = [
    ParameterSpec("CONFIG_playerCount", "Group size", "Group size", "numeric", ("CONFIG_playerCount",)),
    ParameterSpec("CONFIG_numRounds", "Number of rounds", "Rounds", "numeric", ("CONFIG_numRounds",)),
    ParameterSpec("CONFIG_allOrNothing", "All-or-nothing", "All-or-nothing", "binary", ("CONFIG_allOrNothing",)),
    ParameterSpec("CONFIG_defaultContribProp", "Default contribution", "Default contrib.", "binary", ("CONFIG_defaultContribProp",)),
    ParameterSpec("CONFIG_MPCR", "MPCR", "MPCR", "numeric", ("CONFIG_MPCR",)),
    ParameterSpec("CONFIG_chat", "Chat", "Chat", "binary", ("CONFIG_chat",)),
    ParameterSpec("CONFIG_showOtherSummaries", "Show other summaries", "Peer summaries", "binary", ("CONFIG_showOtherSummaries",)),
    ParameterSpec("CONFIG_showAnyId", "Show punishment/reward ID", "ID shown", "merged_binary", ("CONFIG_showPunishmentId", "CONFIG_showRewardId")),
    ParameterSpec("CONFIG_showNRounds", "Show number of rounds", "Rounds shown", "binary", ("CONFIG_showNRounds",)),
    ParameterSpec("CONFIG_punishmentCost", "Punishment cost", "Punish. cost", "categorical", ("CONFIG_punishmentCost",)),
    ParameterSpec("CONFIG_punishmentTech", "Punishment technology", "Punish. tech.", "numeric", ("CONFIG_punishmentTech",)),
    ParameterSpec("CONFIG_rewardExists", "Reward exists", "Reward exists", "binary", ("CONFIG_rewardExists",)),
]

PANEL_B_TEXT_POSITIONS = {
    "CONFIG_playerCount": {"x": 0.95, "y": 10.15, "ha": "left"},
    "CONFIG_numRounds": {"x": 10.8, "y": 10.55, "ha": "left"},
    "CONFIG_punishmentTech": {"x": 0.9, "y": 6.0, "ha": "left"},
    "CONFIG_punishmentCost": {"x": 1.0, "y": 6.8, "ha": "left"},
    "CONFIG_rewardExists": {"x": 6.6, "y": 5.55, "ha": "left"},
    "CONFIG_chat": {"x": 58.9, "y": 4.0, "ha": "right"},
    "CONFIG_MPCR": {"x": 1.25, "y": 3.45, "ha": "left"},
    "CONFIG_showAnyId": {"x": 0.95, "y": 2.2, "ha": "left"},
    "CONFIG_allOrNothing": {"x": 12.9, "y": 1.95, "ha": "left"},
    "CONFIG_showOtherSummaries": {"x": 5.7, "y": 1.00, "ha": "left"},
    "CONFIG_defaultContribProp": {"x": 22.5, "y": 0.65, "ha": "left"},
    "CONFIG_showNRounds": {"x": 0.95, "y": 0.10, "ha": "left"},
}

PANEL_C_LABELS = {
    "CONFIG_defaultContribProp": "Contribution framing",
    "CONFIG_showOtherSummaries": "Peer outcome visibility",
    "CONFIG_showAnyId": "Actor anonymity",
    "CONFIG_showNRounds": "Horizon knowledge",
    "CONFIG_punishmentCost": "Peer incentive cost",
    "CONFIG_punishmentTech": "Punishment technology",
    "CONFIG_rewardExists": "Reward",
    "CONFIG_allOrNothing": "Contribution type",
    "CONFIG_chat": "Communication",
    "CONFIG_numRounds": "Game length",
    "CONFIG_playerCount": "Group size",
}


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 8.2,
            "ytick.labelsize": 8.6,
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.dpi": 300,
        }
    )


def panel_title(ax: plt.Axes, letter: str, title: str) -> None:
    ax.set_title(rf"$\bf{{{letter}}}$  {title}", loc="left", pad=8)


def annotate_sample_size(ax: plt.Axes, text: str, x: float = 0.995, y: float = 0.98) -> None:
    ax.text(
        x,
        y,
        text,
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8.2,
        color="#555555",
    )


def missing_mask(series: pd.Series, include_neg1: bool = False) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.isna()
    s_str = series.astype(str).str.strip()
    miss = series.isna() | s_str.eq("") | s_str.str.upper().isin(MISSING_MARKERS)
    num = pd.to_numeric(series, errors="coerce")
    if include_neg1:
        miss = miss | num.eq(-1)
    return miss


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
    if spec.value_kind == "merged_binary":
        return ~(missing_mask(df[spec.columns[0]], include_neg1=True) & missing_mask(df[spec.columns[1]], include_neg1=True))
    return ~missing_mask(df[spec.columns[0]], include_neg1=True)


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


def load_lab_rows() -> pd.DataFrame:
    df = pd.read_csv(LAB_ROWS_CSV)
    df["CONFIG_showAnyId"] = merged_any_id_series(df)
    return df


def load_benchmark_rows() -> pd.DataFrame:
    df = pd.concat([pd.read_csv(path) for path in BENCHMARK_CSVS], ignore_index=True)
    df["CONFIG_showAnyId"] = np.maximum(df["CONFIG_showPunishmentId"].astype(int), df["CONFIG_showRewardId"].astype(int))
    return df


def build_reported_count_rows(lab: pd.DataFrame) -> pd.DataFrame:
    reported_counts = pd.Series(0, index=lab.index, dtype=int)
    for spec in PARAMETER_SPECS:
        reported_counts += parameter_present_mask(lab, spec).astype(int)

    total_params = len(PARAMETER_SPECS)
    value_counts = reported_counts.value_counts().sort_index().reindex(range(total_params + 1), fill_value=0)
    out = pd.DataFrame(
        {
            "n_design_parameters_reported": value_counts.index.astype(int),
            "n_experiments": value_counts.values.astype(int),
            "percent_experiments": value_counts.values / len(lab) * 100.0,
            "n_experiments_total": int(len(lab)),
            "n_design_parameters_total": total_params,
        }
    )
    out.to_csv(REPORTED_COUNT_ROWS_CSV, index=False)
    return out


def build_importance_rows() -> pd.DataFrame:
    df = pd.read_csv(IMPORTANCE_CSV)
    df = df.loc[df["plotted"].fillna(False)].copy()
    df = df.sort_values(["percent_papers_varied", "predictive_importance_pct_rmse"], ascending=[False, False]).reset_index(drop=True)
    df.to_csv(IMPORTANCE_ROWS_CSV, index=False)
    return df


def benchmark_bin_edges(benchmark: pd.DataFrame, spec: ParameterSpec) -> np.ndarray | None:
    if spec.name == "CONFIG_MPCR":
        return np.array([-1e-9, 0.2, 0.4, 0.6, 0.800000001], dtype=float)
    values = pd.to_numeric(benchmark[spec.name], errors="coerce").dropna()
    if values.empty:
        return None
    if spec.value_kind == "categorical" or values.nunique() <= 6:
        return None
    edges = np.unique(np.quantile(values.to_numpy(dtype=float), [0.0, 0.25, 0.5, 0.75, 1.0]))
    if len(edges) < 3:
        return None
    edges = edges.astype(float)
    edges[0] -= 1e-9
    edges[-1] += 1e-9
    return edges


def format_numeric_value(value: float) -> str:
    if float(value).is_integer():
        return f"{int(value)}"
    return f"{float(value):.2f}".rstrip("0").rstrip(".")


def format_interval_labels(edges: np.ndarray) -> list[str]:
    labels: list[str] = []
    clean_edges = edges.astype(float).copy()
    clean_edges[0] += 1e-9
    clean_edges[-1] -= 1e-9
    for left, right in zip(clean_edges[:-1], clean_edges[1:]):
        labels.append(f"{format_numeric_value(left)}-{format_numeric_value(right)}")
    return labels


def benchmark_level_labels(benchmark: pd.DataFrame, spec: ParameterSpec) -> list[str]:
    if spec.value_kind in {"binary", "merged_binary"}:
        return ["Yes", "No"]

    edges = benchmark_bin_edges(benchmark, spec)
    if edges is not None:
        return format_interval_labels(edges)

    benchmark_values = pd.to_numeric(benchmark[spec.name], errors="coerce").dropna()
    if spec.name == "CONFIG_punishmentCost":
        levels = [format_numeric_value(v) for v in sorted(benchmark_values.unique().tolist())]
        return levels + ["Other"]

    return [format_numeric_value(v) for v in sorted(benchmark_values.unique().tolist())]


def categorical_parameter_frame(df: pd.DataFrame, benchmark: pd.DataFrame) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    for spec in PARAMETER_SPECS:
        if spec.value_kind in {"binary", "merged_binary"}:
            raw = df[spec.name] if spec.name == "CONFIG_showAnyId" else df[spec.columns[0]]
            binary = pd.to_numeric(raw, errors="coerce") if spec.name == "CONFIG_showAnyId" else binaryish_series(raw)
            mapped = pd.Series(np.nan, index=df.index, dtype=object)
            mapped.loc[binary.eq(0)] = "No"
            mapped.loc[binary.eq(1)] = "Yes"
            out[spec.name] = mapped
            continue

        numeric = pd.to_numeric(df[spec.columns[0]], errors="coerce")
        edges = benchmark_bin_edges(benchmark, spec)
        if edges is None:
            if spec.name == "CONFIG_punishmentCost":
                benchmark_levels = set(benchmark_level_labels(benchmark, spec)[:-1])
                mapped = numeric.map(
                    lambda x: (
                        format_numeric_value(x)
                        if pd.notna(x) and format_numeric_value(x) in benchmark_levels
                        else ("Other" if pd.notna(x) else np.nan)
                    )
                )
            else:
                mapped = numeric.map(lambda x: format_numeric_value(x) if pd.notna(x) else np.nan)
        else:
            labels = format_interval_labels(edges)
            mapped = pd.cut(numeric, bins=edges, include_lowest=True, labels=labels).astype(object)
            mapped = mapped.where(numeric.notna(), np.nan)
        out[spec.name] = mapped.astype(object)
    return out


def build_distribution_rows(lab: pd.DataFrame, benchmark: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    lab_cat = categorical_parameter_frame(lab, benchmark)

    rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for spec in PARAMETER_SPECS:
        benchmark_levels = benchmark_level_labels(benchmark, spec)
        levels = benchmark_levels.copy()
        if not levels:
            continue

        counts = pd.Series(lab_cat[spec.name]).dropna().astype(str).value_counts().reindex(pd.Index(levels), fill_value=0)
        n_nonmissing = int(counts.sum())
        shares = counts / n_nonmissing if n_nonmissing else counts.astype(float)
        modal_share = float(shares.max()) if n_nonmissing else 0.0
        summaries.append(
            {
                "parameter": spec.name,
                "label": spec.label,
                "short_label": spec.short_label,
                "modal_share": modal_share,
                "n_nonmissing": n_nonmissing,
                "n_levels": len(levels),
            }
        )

        for bin_order, level in enumerate(levels):
            rows.append(
                {
                    "parameter": spec.name,
                    "label": spec.label,
                    "short_label": spec.short_label,
                    "bin_order": bin_order,
                    "bin_label": str(level),
                    "bin_label_display": str(level),
                    "count": int(counts.loc[level]),
                    "share": float(shares.loc[level]) if n_nonmissing else 0.0,
                    "percent": float(shares.loc[level] * 100.0) if n_nonmissing else 0.0,
                    "n_nonmissing": n_nonmissing,
                    "modal_share": modal_share,
                }
            )

    dist_rows = pd.DataFrame(rows)
    dist_rows["bin_label_display"] = dist_rows["bin_label"]
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_defaultContribProp", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_defaultContribProp", "bin_label"]
        .map({"Yes": "opt out", "No": "opt in"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_defaultContribProp", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_allOrNothing", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_allOrNothing", "bin_label"]
        .map({"Yes": "all-or-nothing", "No": "variable"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_allOrNothing", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_chat", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_chat", "bin_label"]
        .map({"Yes": "enabled", "No": "disabled"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_chat", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_showOtherSummaries", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_showOtherSummaries", "bin_label"]
        .map({"Yes": "visible", "No": "hidden"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_showOtherSummaries", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_showAnyId", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_showAnyId", "bin_label"]
        .map({"Yes": "revealed", "No": "hidden"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_showAnyId", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_showNRounds", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_showNRounds", "bin_label"]
        .map({"Yes": "known", "No": "unknown"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_showNRounds", "bin_label"])
    )
    dist_rows.loc[dist_rows["parameter"] == "CONFIG_rewardExists", "bin_label_display"] = (
        dist_rows.loc[dist_rows["parameter"] == "CONFIG_rewardExists", "bin_label"]
        .map({"Yes": "enabled", "No": "disabled"})
        .fillna(dist_rows.loc[dist_rows["parameter"] == "CONFIG_rewardExists", "bin_label"])
    )
    summary_rows = (
        pd.DataFrame(summaries)
        .sort_values(["modal_share", "n_nonmissing", "label"], ascending=[False, False, True])
        .reset_index(drop=True)
    )
    parameter_order = summary_rows["parameter"].tolist()
    order_map = {parameter: i for i, parameter in enumerate(parameter_order)}
    dist_rows["parameter_order"] = dist_rows["parameter"].map(order_map)
    dist_rows = dist_rows.sort_values(["parameter_order", "bin_order"]).reset_index(drop=True)
    dist_rows.to_csv(DISTRIBUTION_ROWS_CSV, index=False)
    return dist_rows, summary_rows


def draw_panel_a(ax: plt.Axes, reported_count_rows: pd.DataFrame) -> None:
    x = reported_count_rows["n_design_parameters_reported"]
    y = reported_count_rows["n_experiments"]
    total_params = int(reported_count_rows["n_design_parameters_total"].iloc[0])
    cmap = plt.cm.YlGnBu
    colors = [cmap(i / max(1, total_params)) for i in x]

    ax.bar(x, y, color=colors, edgecolor="white")
    ax.set_xlim(-0.5, total_params + 0.5)
    ax.set_xticks(x)
    ax.set_xlabel("Number of design parameters reported")
    ax.set_ylabel("Number of experiments")
    panel_title(ax, "A", "Underreported design parameter values")
    annotate_sample_size(ax, f"n={int(reported_count_rows['n_experiments_total'].iloc[0]):,} lab experiments")
    ax.axvline(total_params / 2, color="#b8b8b8", linestyle=(0, (4, 4)), linewidth=1.0, zorder=0)
    ax.grid(axis="y", color=GRID, linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)


def draw_panel_b(ax: plt.Axes, importance_rows: pd.DataFrame) -> None:
    x = importance_rows["predictive_importance_pct_rmse"].astype(float)
    y = importance_rows["percent_papers_varied"].astype(float)
    r, p = pearson_r_and_p(x, y)
    n_papers = int(importance_rows["n_papers_total"].iloc[0])

    ax.set_xlim(min(-3.5, float(x.min()) - 1.5), float(x.max()) + 5.0)
    ax.set_ylim(-0.2, max(11.7, float(y.max()) + 1.5))

    ax.scatter(x, y, s=150, color=ORANGE, edgecolor="#444444", linewidth=1.5, alpha=0.92, zorder=3)
    if len(importance_rows) >= 2:
        coeffs = np.polyfit(x, y, 1)
        x_line = np.linspace(float(x.min()) - 1.0, float(x.max()) + 1.0, 100)
        y_line = coeffs[0] * x_line + coeffs[1]
        ax.plot(x_line, y_line, color="#7f7f7f", linewidth=1.6, linestyle=(0, (4, 3)), zorder=2)

    for row in importance_rows.itertuples():
        pos = PANEL_B_TEXT_POSITIONS.get(row.parameter, {"x": row.predictive_importance_pct_rmse + 0.9, "y": row.percent_papers_varied + 0.2, "ha": "left"})
        ax.text(
            pos["x"],
            pos["y"],
            PANEL_C_LABELS.get(row.parameter, row.short_label),
            ha=pos["ha"],
            fontsize=7.0,
            color=TEXT,
            bbox={"facecolor": "white", "edgecolor": "#d5d9de", "boxstyle": "round,pad=0.20", "linewidth": 0.8},
            zorder=4,
        )

    p_text = f"{p:.3f}" if np.isfinite(p) else "n/a"
    panel_title(ax, "B", "Frequently varied parameters are not the most predictive")
    ax.text(0.02, 0.98, f"r = {r:.2f}, p = {p_text}, n = {n_papers} papers", transform=ax.transAxes, ha="left", va="top", fontsize=8.4, color="#555555")
    ax.set_xlabel("Predictive importance\n(% increase in prediction error when shuffled)")
    ax.set_ylabel("% of papers varying parameter")
    ax.grid(True, color=GRID, linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)


def draw_panel_c(fig: plt.Figure, parent_spec, dist_rows: pd.DataFrame, summary_rows: pd.DataFrame, n_lab: int) -> None:
    outer = parent_spec.subgridspec(4, 4, height_ratios=[0.10, 1.0, 1.0, 1.0], hspace=0.46, wspace=0.30)

    title_ax = fig.add_subplot(outer[0, :])
    title_ax.set_frame_on(False)
    title_ax.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    title_ax.text(0.0, 0.36, r"$\bf{C}$  Reported values are concentrated in a narrow subset of settings", transform=title_ax.transAxes, ha="left", va="center", fontsize=11, color=TEXT)

    parameter_order = summary_rows["parameter"].tolist()
    cmap = plt.cm.YlOrRd
    axes: list[plt.Axes] = []

    for idx, parameter in enumerate(parameter_order):
        ax = fig.add_subplot(outer[1 + idx // 4, idx % 4])
        axes.append(ax)
        param_rows = dist_rows.loc[dist_rows["parameter"] == parameter].sort_values("bin_order").reset_index(drop=True)
        values = param_rows["share"].to_numpy(dtype=float)[None, :]
        im = ax.imshow(values, cmap=cmap, vmin=0.0, vmax=1.0, aspect="auto")

        ax.set_title(
            f"{PANEL_C_LABELS.get(parameter, param_rows['short_label'].iloc[0])} (n={int(param_rows['n_nonmissing'].iloc[0]):,})",
            fontsize=7.9,
            pad=4,
        )
        ax.set_yticks([])
        ax.set_xlim(-0.5, len(param_rows) - 0.5)
        ax.set_xticks(range(len(param_rows)))
        ax.set_xticklabels(param_rows["bin_label_display"])
        ax.tick_params(axis="x", length=0, pad=1, labelsize=6.8)
        ax.set_ylim(0.5, -0.5)

        for col, row in enumerate(param_rows.itertuples()):
            text_color = "white" if row.share >= 0.55 else TEXT
            ax.text(
                col,
                0,
                f"{row.percent:.0f}",
                ha="center",
                va="center",
                fontsize=7.7,
                color=text_color,
                fontweight="bold" if row.share >= 0.35 else None,
            )

        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(0.8)
            spine.set_edgecolor("#c8ced6")

    cbar = fig.colorbar(im, ax=axes, fraction=0.018, pad=0.012)
    cbar.set_label("% of reported experiments", fontsize=8.6)
    cbar.set_ticks([0.0, 0.25, 0.5, 0.75, 1.0])
    cbar.set_ticklabels(["0", "25", "50", "75", "100"])
    cbar.ax.tick_params(labelsize=8)


def write_documentation(reported_count_rows: pd.DataFrame, importance_rows: pd.DataFrame, dist_rows: pd.DataFrame, summary_rows: pd.DataFrame, n_lab: int) -> None:
    r, p = pearson_r_and_p(importance_rows["predictive_importance_pct_rmse"], importance_rows["percent_papers_varied"])
    lines = [
        "# Figure 5: Empirical Design Limitations",
        "",
        "Inputs:",
        "- `results/paper/lab_config_distributions_260427/combined_lab_extractions_broad_all_rows.csv`",
        "- `plots/lab_config_distributions_260427/parameter_analysis_mentions_variation_vs_predictive_importance.csv`",
        "- `input/pgg_CONFIGmerged_learn.csv`",
        "- `input/pgg_CONFIGmerged_validation.csv`",
        "",
        f"Panel A uses `{n_lab}` filtered lab-experiment rows and the 12-parameter design set to count how many design parameters are reported in each extracted experiment.",
        f"Panel B uses `{int(importance_rows['n_papers_total'].iloc[0])}` lab papers and 12 design parameters that have benchmark permutation-importance values. Pearson correlation between predictive importance and cross-paper variation is `r = {r:.3f}`, `p = {p:.3f}`." if np.isfinite(p) else f"Panel B uses `{int(importance_rows['n_papers_total'].iloc[0])}` lab papers and 12 design parameters that have benchmark permutation-importance values.",
        f"Panel C shows literature-only value concentration across the same 12 design parameters. Each mini-heatmap uses the share of reported experiments in each observed value or benchmark-defined bin, on a 0-100% color scale.",
        "",
        "Outputs:",
        f"- `{REPORTED_COUNT_ROWS_CSV.relative_to(ROOT)}`",
        f"- `{IMPORTANCE_ROWS_CSV.relative_to(ROOT)}`",
        f"- `{DISTRIBUTION_ROWS_CSV.relative_to(ROOT)}`",
        "",
        "Notes:",
        "- ID-visibility merges punishment-ID and reward-ID visibility into one design parameter.",
        "- Punishment-existence, reward cost, reward technology, and endowment are excluded from the 12-parameter set.",
        "- For Panel C, continuous parameters use benchmark-defined quartile bins to keep the value ranges readable and comparable.",
        "- Parameters are ordered by modal share, so the most concentrated distributions appear first.",
    ]
    DOC_MD.write_text("\n".join(lines))


def draw_figure() -> None:
    set_style()
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    lab = load_lab_rows()
    benchmark = load_benchmark_rows()

    reported_count_rows = build_reported_count_rows(lab)
    importance_rows = build_importance_rows()
    dist_rows, summary_rows = build_distribution_rows(lab, benchmark)

    fig = plt.figure(figsize=(11.6, 9.0))
    gs = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.18, 1.0],
        height_ratios=[0.95, 1.15],
        left=0.16,
        right=0.98,
        bottom=0.08,
        top=0.94,
        wspace=0.22,
        hspace=0.23,
    )

    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    draw_panel_a(ax_a, reported_count_rows)
    draw_panel_b(ax_b, importance_rows)
    draw_panel_c(fig, gs[1, :], dist_rows, summary_rows, n_lab=len(lab))

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{OUT_STEM}.{ext}", bbox_inches="tight")
    plt.close(fig)

    write_documentation(reported_count_rows, importance_rows, dist_rows, summary_rows, n_lab=len(lab))
    print(PLOTS_DIR / f"{OUT_STEM}.png")


if __name__ == "__main__":
    draw_figure()
