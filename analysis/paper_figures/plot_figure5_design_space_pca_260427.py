from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427" / "exploratory"
PLOTS_DIR = ROOT / "plots" / "paper" / "main_text_260427" / "exploratory"

LAB_ROWS_CSV = ROOT / "results" / "paper" / "lab_config_distributions_260427" / "combined_lab_extractions_broad_all_rows.csv"
BENCHMARK_CSVS = [
    ROOT / "input" / "pgg_CONFIGmerged_learn.csv",
    ROOT / "input" / "pgg_CONFIGmerged_validation.csv",
]

ROWS_CSV = RESULTS_DIR / "figure5_design_space_pca_projection_rows.csv"
DOC_MD = RESULTS_DIR / "figure5_design_space_pca_projection_documentation.md"
OUT_STEM = "figure5_design_space_pca_projection"

MISSING_MARKERS = {"", "N/R", "N/A", "NA", "NR"}
BOOL_TRUE = {"true", "1", "yes", "y"}
BOOL_FALSE = {"false", "0", "no", "n"}


@dataclass(frozen=True)
class ParameterSpec:
    name: str
    label: str
    kind: str
    columns: tuple[str, ...]


PARAMETER_SPECS = [
    ParameterSpec("CONFIG_playerCount", "Group size", "numeric", ("CONFIG_playerCount",)),
    ParameterSpec("CONFIG_numRounds", "Number of rounds", "numeric", ("CONFIG_numRounds",)),
    ParameterSpec("CONFIG_allOrNothing", "All-or-nothing", "binary", ("CONFIG_allOrNothing",)),
    ParameterSpec("CONFIG_defaultContribProp", "Default contribution", "binary", ("CONFIG_defaultContribProp",)),
    ParameterSpec("CONFIG_MPCR", "MPCR", "numeric", ("CONFIG_MPCR",)),
    ParameterSpec("CONFIG_chat", "Chat", "binary", ("CONFIG_chat",)),
    ParameterSpec("CONFIG_showOtherSummaries", "Show other summaries", "binary", ("CONFIG_showOtherSummaries",)),
    ParameterSpec("CONFIG_showAnyId", "Show punishment/reward ID", "merged_binary", ("CONFIG_showPunishmentId", "CONFIG_showRewardId")),
    ParameterSpec("CONFIG_showNRounds", "Show number of rounds", "binary", ("CONFIG_showNRounds",)),
    ParameterSpec("CONFIG_punishmentCost", "Punishment cost", "categorical", ("CONFIG_punishmentCost",)),
    ParameterSpec("CONFIG_punishmentTech", "Punishment technology", "numeric", ("CONFIG_punishmentTech",)),
    ParameterSpec("CONFIG_rewardExists", "Reward exists", "binary", ("CONFIG_rewardExists",)),
]


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.dpi": 300,
        }
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


def benchmark_bin_edges(benchmark: pd.DataFrame, spec: ParameterSpec) -> np.ndarray | None:
    values = pd.to_numeric(benchmark[spec.name], errors="coerce").dropna()
    if values.empty:
        return None
    if spec.kind == "categorical" or values.nunique() <= 6:
        return None
    edges = np.unique(np.quantile(values.to_numpy(dtype=float), [0.0, 0.25, 0.5, 0.75, 1.0]))
    if len(edges) < 3:
        return None
    edges = edges.astype(float)
    edges[0] -= 1e-9
    edges[-1] += 1e-9
    return edges


def load_lab_rows() -> pd.DataFrame:
    df = pd.read_csv(LAB_ROWS_CSV)
    df["CONFIG_showAnyId"] = merged_any_id_series(df)
    return df


def load_benchmark_rows() -> pd.DataFrame:
    df = pd.concat([pd.read_csv(path) for path in BENCHMARK_CSVS], ignore_index=True)
    df["CONFIG_showAnyId"] = np.maximum(df["CONFIG_showPunishmentId"].astype(int), df["CONFIG_showRewardId"].astype(int))
    return df


def build_projection_inputs(lab: pd.DataFrame, benchmark: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, list[str]]]:
    level_map: dict[str, list[str]] = {}
    edge_map: dict[str, np.ndarray] = {}
    fill_map: dict[str, str] = {}

    for spec in PARAMETER_SPECS:
        if spec.kind == "binary":
            level_map[spec.name] = ["No", "Yes"]
            fill_map[spec.name] = "Yes" if binaryish_series(benchmark[spec.name]).mean() >= 0.5 else "No"
            continue
        if spec.kind == "merged_binary":
            level_map[spec.name] = ["No", "Yes"]
            fill_map[spec.name] = "Yes" if pd.to_numeric(benchmark[spec.name], errors="coerce").mean() >= 0.5 else "No"
            continue

        edges = benchmark_bin_edges(benchmark, spec)
        if edges is None:
            values = pd.to_numeric(benchmark[spec.name], errors="coerce").dropna()
            level_map[spec.name] = [f"{int(v)}" if float(v).is_integer() else f"{v:g}" for v in sorted(values.unique().tolist())]
            fill_map[spec.name] = values.mode().iloc[0]
        else:
            edge_map[spec.name] = edges
            bins = pd.cut(pd.to_numeric(benchmark[spec.name], errors="coerce"), bins=edges, include_lowest=True).astype(str)
            levels = []
            for value in bins:
                if value not in levels:
                    levels.append(value)
            level_map[spec.name] = levels
            fill_map[spec.name] = bins.mode().iloc[0]

    def to_categorical(df: pd.DataFrame) -> pd.DataFrame:
        out = pd.DataFrame(index=df.index)
        for spec in PARAMETER_SPECS:
            if spec.kind == "binary":
                s = binaryish_series(df[spec.columns[0]])
                out[spec.name] = s.map({0.0: "No", 1.0: "Yes"}).fillna(fill_map[spec.name])
                continue
            if spec.kind == "merged_binary":
                s = pd.to_numeric(df[spec.name], errors="coerce")
                out[spec.name] = s.map({0.0: "No", 1.0: "Yes"}).fillna(fill_map[spec.name])
                continue

            numeric = pd.to_numeric(df[spec.columns[0]], errors="coerce")
            if spec.name in edge_map:
                cats = pd.cut(numeric, bins=edge_map[spec.name], include_lowest=True).astype(str)
                out[spec.name] = cats.where(numeric.notna(), np.nan).fillna(fill_map[spec.name])
            else:
                out[spec.name] = numeric.map(
                    lambda x: (
                        f"{int(x)}" if pd.notna(x) and float(x).is_integer() else (f"{x:g}" if pd.notna(x) else np.nan)
                    )
                ).fillna(str(fill_map[spec.name]) if not isinstance(fill_map[spec.name], str) else fill_map[spec.name])
        return out

    lab_present_counts = pd.Series(0, index=lab.index, dtype=int)
    for spec in PARAMETER_SPECS:
        if spec.kind == "merged_binary":
            present = ~(missing_mask(lab[spec.columns[0]], include_neg1=True) & missing_mask(lab[spec.columns[1]], include_neg1=True))
        else:
            present = ~missing_mask(lab[spec.columns[0]], include_neg1=True)
        lab_present_counts += present.astype(int)
    lab = lab.assign(n_reported_design_parameters=lab_present_counts)
    lab = lab.loc[lab["n_reported_design_parameters"] >= 8].copy().reset_index(drop=True)

    bench_cat = to_categorical(benchmark)
    lab_cat = to_categorical(lab)
    return lab, bench_cat, lab_cat, level_map


def one_hot_matrix(cat_df: pd.DataFrame, level_map: dict[str, list[str]]) -> tuple[np.ndarray, list[str]]:
    columns: list[np.ndarray] = []
    feature_names: list[str] = []
    for spec in PARAMETER_SPECS:
        for level in level_map[spec.name]:
            feature_names.append(f"{spec.name}={level}")
            columns.append((cat_df[spec.name] == level).astype(float).to_numpy())
    matrix = np.column_stack(columns)
    return matrix, feature_names


def save_projection_rows(bench_raw: pd.DataFrame, bench_cat: pd.DataFrame, lab_raw: pd.DataFrame, lab_cat: pd.DataFrame, bench_proj: np.ndarray, lab_proj: np.ndarray) -> None:
    bench_rows = pd.DataFrame(
        {
            "dataset": "Benchmark",
            "pc1": bench_proj[:, 0],
            "pc2": bench_proj[:, 1],
            "n_reported_design_parameters": len(PARAMETER_SPECS),
        }
    )
    lab_rows = pd.DataFrame(
        {
            "dataset": "Literature",
            "pc1": lab_proj[:, 0],
            "pc2": lab_proj[:, 1],
            "n_reported_design_parameters": lab_raw["n_reported_design_parameters"].to_numpy(),
        }
    )
    out = pd.concat([bench_rows, lab_rows], ignore_index=True)
    out.to_csv(ROWS_CSV, index=False)


def panel_title(ax: plt.Axes, letter: str, title: str) -> None:
    ax.set_title(rf"$\bf{{{letter}}}$  {title}", loc="left", pad=8)


def draw_density_panel(ax: plt.Axes, points: np.ndarray, xedges: np.ndarray, yedges: np.ndarray, title: str, vmax: float, cmap: str):
    counts, _, _ = np.histogram2d(points[:, 0], points[:, 1], bins=[xedges, yedges])
    pct = counts / counts.sum() * 100.0
    im = ax.imshow(
        pct.T,
        origin="lower",
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
        aspect="auto",
        cmap=cmap,
        vmin=0.0,
        vmax=vmax,
    )
    ax.set_title(title, fontsize=10, pad=4)
    ax.grid(False)
    return im


def draw_figure(bench_proj: np.ndarray, lab_proj: np.ndarray, explained: np.ndarray, n_lab_rows: int, n_lab_papers: int) -> None:
    set_style()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    combined = np.vstack([bench_proj, lab_proj])
    xedges = np.linspace(combined[:, 0].min() - 0.15, combined[:, 0].max() + 0.15, 13)
    yedges = np.linspace(combined[:, 1].min() - 0.15, combined[:, 1].max() + 0.15, 13)

    bench_counts, _, _ = np.histogram2d(bench_proj[:, 0], bench_proj[:, 1], bins=[xedges, yedges])
    lab_counts, _, _ = np.histogram2d(lab_proj[:, 0], lab_proj[:, 1], bins=[xedges, yedges])
    vmax = max((bench_counts / bench_counts.sum() * 100.0).max(), (lab_counts / lab_counts.sum() * 100.0).max())

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.1), sharex=True, sharey=True)
    fig.subplots_adjust(left=0.09, right=0.88, top=0.88, bottom=0.12, wspace=0.08)
    im = draw_density_panel(axes[0], bench_proj, xedges, yedges, "Benchmark", vmax=vmax, cmap="YlOrRd")
    draw_density_panel(axes[1], lab_proj, xedges, yedges, "Literature", vmax=vmax, cmap="YlOrRd")

    fig.suptitle("Exploratory: Benchmark-fitted PCA projection of the design space", x=0.10, y=0.96, ha="left", fontsize=12, fontweight="bold")
    fig.text(
        0.10,
        0.92,
        "Literature rows with >=8/12 reported parameters; remaining missing values are filled only for projection.",
        ha="left",
        va="center",
        fontsize=8.0,
        color="#555555",
    )
    fig.text(
        0.98,
        0.92,
        f"Benchmark n=170; Literature n={n_lab_rows} rows from {n_lab_papers} papers",
        ha="right",
        va="center",
        fontsize=8.0,
        color="#555555",
    )

    for ax in axes:
        ax.set_xlabel(f"PC1 ({explained[0] * 100:.1f}%)")
        ax.set_ylabel(f"PC2 ({explained[1] * 100:.1f}%)")

    cbar = fig.colorbar(im, ax=axes, fraction=0.035, pad=0.02)
    cbar.set_label("% of dataset in cell", fontsize=9)
    cbar.ax.tick_params(labelsize=8)

    for ext in ["png", "pdf"]:
        fig.savefig(PLOTS_DIR / f"{OUT_STEM}.{ext}", bbox_inches="tight")
    plt.close(fig)


def write_documentation(explained: np.ndarray, n_lab_rows: int, n_lab_papers: int) -> None:
    lines = [
        "# Exploratory Figure: Design-Space PCA Projection",
        "",
        "Purpose:",
        "- Explore whether a benchmark-fitted 2D projection shows broader coverage of the benchmark design space than the literature extraction set.",
        "",
        "Inputs:",
        "- `results/paper/lab_config_distributions_260427/combined_lab_extractions_broad_all_rows.csv`",
        "- `input/pgg_CONFIGmerged_learn.csv`",
        "- `input/pgg_CONFIGmerged_validation.csv`",
        "",
        "Method:",
        "- Use the same 12 design parameters as the current Figure 5.",
        "- Convert all parameters into benchmark-supported bins or levels before encoding.",
        "- Fit PCA on the benchmark one-hot design matrix only.",
        f"- Keep literature rows that report at least 8 of 12 design parameters (`n = {n_lab_rows}` rows from `{n_lab_papers}` papers).",
        "- Fill the remaining missing literature values with benchmark modal bins only for projection into the benchmark PCA basis.",
        "",
        f"Explained variance: PC1 = `{explained[0] * 100:.2f}%`, PC2 = `{explained[1] * 100:.2f}%`.",
        "",
        "Outputs:",
        f"- `{ROWS_CSV.relative_to(ROOT)}`",
        f"- `{PLOTS_DIR.joinpath(OUT_STEM + '.png').relative_to(ROOT)}`",
    ]
    DOC_MD.write_text("\n".join(lines))


def main() -> None:
    lab = load_lab_rows()
    benchmark = load_benchmark_rows()
    lab_filtered, bench_cat, lab_cat, level_map = build_projection_inputs(lab, benchmark)

    X_bench, _ = one_hot_matrix(bench_cat, level_map)
    X_lab, _ = one_hot_matrix(lab_cat, level_map)

    pca = PCA(n_components=2)
    bench_proj = pca.fit_transform(X_bench)
    lab_proj = pca.transform(X_lab)

    save_projection_rows(benchmark, bench_cat, lab_filtered, lab_cat, bench_proj, lab_proj)
    draw_figure(bench_proj, lab_proj, pca.explained_variance_ratio_, n_lab_rows=len(lab_filtered), n_lab_papers=lab_filtered["custom_id"].nunique())
    write_documentation(pca.explained_variance_ratio_, n_lab_rows=len(lab_filtered), n_lab_papers=lab_filtered["custom_id"].nunique())
    print(PLOTS_DIR / f"{OUT_STEM}.png")


if __name__ == "__main__":
    main()
