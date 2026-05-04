from __future__ import annotations

import csv
import json
import math
import re
import statistics
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = ROOT / "results" / "paper" / "main_text_figures_260427"

WORKBOOKS = [
    ROOT / "batch_processing" / "output_csv" / "simple_batch_197papers.xlsx",
    ROOT / "batch_processing" / "output_csv" / "simple_batch_810papers.xlsx",
]
CORPUS_SOURCE_IDS_CSV = ROOT / "results" / "validation" / "literature_analysis_report_sources_overview" / "single_paper_overview_dataset.csv"

FIGURE5_REPORTED_COUNT_CSV = RESULTS_DIR / "figure5_reported_parameter_count_rows.csv"
FIGURE5_VARIATION_IMPORTANCE_CSV = RESULTS_DIR / "figure5_variation_vs_importance_rows.csv"
FIGURE5_VALUE_DISTRIBUTION_CSV = RESULTS_DIR / "figure5_value_distribution_rows.csv"
FIGURE5_EVENNESS_CSV = RESULTS_DIR / "figure5_value_evenness_vs_benchmark_rows.csv"

OUT_KEY_VALUES = RESULTS_DIR / "figure5_main_text_key_values.csv"
OUT_DOC = RESULTS_DIR / "figure5_main_text_results_documentation.md"
OUT_LABEL_COUNTS = RESULTS_DIR / "figure5_workbook_iv_dv_label_counts.csv"
OUT_HARMONIZATION_ROWS = RESULTS_DIR / "figure5_workbook_iv_dv_harmonization_rows.csv"
OUT_HARMONIZATION_SUMMARY = RESULTS_DIR / "figure5_workbook_iv_dv_harmonization_summary.csv"
OUT_FAMILY_SUMMARY = RESULTS_DIR / "figure5_workbook_iv_dv_family_summary.csv"
OUT_CONCEPT_COVERAGE = RESULTS_DIR / "figure5_workbook_concept_coverage.csv"

NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
BOOL_TRUE = {"true", "1", "1.0", "yes", "y"}
WRAPPER_PREFIXES = [
    "individual_",
    "group_",
    "self_reported_",
    "average_",
    "mean_",
    "total_",
    "net_",
    "expected_",
    "perceived_",
    "reported_",
    "received_",
    "aggregate_",
    "overall_",
    "collective_",
    "public_",
    "private_",
    "within_group_",
]
FAMILY_STOPWORDS = {"of", "the", "and", "to", "for", "with", "others", "other"}
FAMILY_TOKEN_IGNORE = {"gt", "lt", "eq", "ge", "le", "ac", "ai", "di", "fe"}
FAMILY_PRIORITY = [
    "contribution",
    "cooperation",
    "punishment",
    "reward",
    "payoff",
    "efficiency",
    "trust",
    "fairness",
    "anger",
    "belief",
    "expectation",
    "harvest",
    "extraction",
    "investment",
    "allocation",
    "offer",
    "return",
    "compliance",
    "rejection",
    "acceptance",
    "theft",
    "income",
    "emotion",
    "choice",
    "effort",
    "production",
    "vote",
    "report",
    "conviction",
    "bribe",
    "retaliation",
    "surplus",
    "waste",
    "satisfaction",
]
FAMILY_ALIASES = {
    "earnings": "payoff",
    "profit": "payoff",
    "payoffs": "payoff",
    "welfare": "efficiency",
    "cooperation": "contribution",
    "contributions": "contribution",
    "cooperate": "contribution",
    "punishment_assigned": "punishment",
    "punishment_received": "punishment",
    "punishment_given": "punishment",
    "reward_assigned": "reward",
    "reward_received": "reward",
}
FAMILY_TOKEN_ALIASES = {
    "beliefs": "belief",
    "belief": "belief",
    "returned": "return",
    "returns": "return",
    "sending": "transfer",
    "sent": "transfer",
    "transferred": "transfer",
    "earnings": "payoff",
    "profits": "payoff",
    "payoffs": "payoff",
    "choices": "choice",
}

OUTCOME_CONCEPT_PATTERNS = {
    "contribution": [r"contribution"],
    "punishment_behavior": [r"punish", r"sanction", r"counterpunish", r"antisocial_punish"],
    "cooperation": [r"cooperation"],
    "earnings_payoff": [r"earning", r"payoff", r"profit", r"income"],
    "efficiency_welfare": [r"efficiency", r"welfare"],
}


def col_ref_to_index(ref: str) -> int:
    letters = "".join(ch for ch in ref if ch.isalpha()).upper()
    index = 0
    for ch in letters:
        index = index * 26 + (ord(ch) - ord("A") + 1)
    return index - 1


def parse_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    path = "xl/sharedStrings.xml"
    if path not in zf.namelist():
        return []
    root = ET.fromstring(zf.read(path))
    values: list[str] = []
    for si in root.findall("a:si", NS):
        text_parts = [node.text or "" for node in si.findall(".//a:t", NS)]
        values.append("".join(text_parts))
    return values


def cell_text(cell: ET.Element, shared_strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        text_parts = [node.text or "" for node in cell.findall(".//a:t", NS)]
        return "".join(text_parts)

    v = cell.find("a:v", NS)
    if v is None or v.text is None:
        return ""

    raw = v.text
    if cell_type == "s":
        try:
            return shared_strings[int(raw)]
        except Exception:
            return raw
    return raw


def read_xlsx_rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as zf:
        shared_strings = parse_shared_strings(zf)
        sheet_root = ET.fromstring(zf.read("xl/worksheets/sheet1.xml"))

    sheet_data = sheet_root.find("a:sheetData", NS)
    if sheet_data is None:
        return []

    header: list[str] | None = None
    records: list[dict[str, str]] = []
    for row in sheet_data.findall("a:row", NS):
        row_map: dict[int, str] = {}
        for cell in row.findall("a:c", NS):
            ref = cell.attrib.get("r", "")
            if not ref:
                continue
            row_map[col_ref_to_index(ref)] = cell_text(cell, shared_strings)
        if not row_map:
            continue

        if header is None:
            max_idx = max(row_map)
            header = [(row_map.get(i, "") or "").strip() for i in range(max_idx + 1)]
            continue

        assert header is not None
        record: dict[str, str] = {}
        for idx, key in enumerate(header):
            if not key:
                continue
            record[key] = row_map.get(idx, "")
        if any(str(value).strip() for value in record.values()):
            records.append(record)
    return records


def load_workbook_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for workbook in WORKBOOKS:
        for row in read_xlsx_rows(workbook):
            row["source_workbook"] = workbook.name
            rows.append(row)
    return rows


def is_true(value: object) -> bool:
    if value is None:
        return False
    text = str(value).strip().lower()
    if text in BOOL_TRUE:
        return True
    try:
        return float(text) == 1.0
    except Exception:
        return False


def to_float(value: object) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_json_list(value: object) -> list[str]:
    if value is None:
        return []
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return []
    if isinstance(parsed, list):
        return [str(item).strip() for item in parsed if str(item).strip()]
    if isinstance(parsed, str) and parsed.strip():
        return [parsed.strip()]
    return []


def conservative_label(label: str) -> str:
    text = label.lower().strip()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text


def family_label(label: str) -> str:
    text = conservative_label(label)
    changed = True
    while changed:
        changed = False
        for prefix in WRAPPER_PREFIXES:
            if text.startswith(prefix):
                text = text[len(prefix) :]
                changed = True
    text = FAMILY_ALIASES.get(text, text)
    tokens = []
    for token in text.split("_"):
        if not token or token in FAMILY_STOPWORDS or token in FAMILY_TOKEN_IGNORE or token.isdigit():
            continue
        token = FAMILY_TOKEN_ALIASES.get(token, token)
        tokens.append(token)
    for priority in FAMILY_PRIORITY:
        if priority in tokens or text == priority:
            return priority
    if not tokens:
        return text
    return tokens[-1]


def has_regex_match(labels: set[str], patterns: list[str]) -> bool:
    joined = " || ".join(sorted(labels)).lower()
    return any(re.search(pattern, joined) for pattern in patterns)


def load_corpus_ids() -> set[str]:
    with CORPUS_SOURCE_IDS_CSV.open() as f:
        reader = csv.DictReader(f)
        return {row["source_id"].strip() for row in reader if row.get("source_id")}


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open() as f:
        return list(csv.DictReader(f))


def percent(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return float("nan")
    return numerator / denominator * 100.0


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    return statistics.median(values)


def format_pct(value: float, digits: int = 1) -> str:
    return f"{value:.{digits}f}%"


def format_num(value: float, digits: int = 1) -> str:
    return f"{value:.{digits}f}"


def main() -> None:
    corpus_ids = load_corpus_ids()
    workbook_rows_all = load_workbook_rows()
    workbook_rows = [row for row in workbook_rows_all if row.get("custom_id", "").strip() in corpus_ids]

    workbook_paper_ids = {row["custom_id"].strip() for row in workbook_rows}
    empirical_papers_strict = {
        row["custom_id"].strip()
        for row in workbook_rows
        if is_true(row.get("METHOD_empirical"))
    }
    lab_papers = {
        row["custom_id"].strip()
        for row in workbook_rows
        if is_true(row.get("METHOD_lab"))
    }
    empirical_papers = empirical_papers_strict | lab_papers
    lab_rows = [row for row in workbook_rows if is_true(row.get("METHOD_lab"))]

    iv_count_values = [value for row in lab_rows if (value := to_float(row.get("number_IVs"))) is not None]
    dv_count_values = [value for row in lab_rows if (value := to_float(row.get("number_DVs"))) is not None]

    iv_label_counter: Counter[str] = Counter()
    dv_label_counter: Counter[str] = Counter()
    paper_iv_labels: defaultdict[str, set[str]] = defaultdict(set)
    paper_dv_labels: defaultdict[str, set[str]] = defaultdict(set)
    for row in lab_rows:
        ivs = parse_json_list(row.get("IVs"))
        dvs = parse_json_list(row.get("DVs"))
        iv_label_counter.update(ivs)
        dv_label_counter.update(dvs)
        custom_id = row["custom_id"].strip()
        paper_iv_labels[custom_id].update(ivs)
        paper_dv_labels[custom_id].update(dvs)

    label_count_rows: list[dict[str, object]] = []
    for kind, counter in [("IV", iv_label_counter), ("DV", dv_label_counter)]:
        for rank, (label, count) in enumerate(counter.most_common(), start=1):
            label_count_rows.append(
                {
                    "kind": kind,
                    "rank": rank,
                    "label": label,
                    "count": count,
                }
            )
    with OUT_LABEL_COUNTS.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["kind", "rank", "label", "count"])
        writer.writeheader()
        writer.writerows(label_count_rows)

    harmonization_rows: list[dict[str, object]] = []
    harmonization_summary: list[dict[str, object]] = []
    family_summary_rows: list[dict[str, object]] = []
    for kind, counter in [("IV", iv_label_counter), ("DV", dv_label_counter)]:
        conservative_groups: defaultdict[str, list[str]] = defaultdict(list)
        family_groups: defaultdict[str, list[str]] = defaultdict(list)
        family_counts: Counter[str] = Counter()
        for raw_label, count in counter.items():
            conservative = conservative_label(raw_label)
            family = family_label(raw_label)
            harmonization_rows.append(
                {
                    "kind": kind,
                    "raw_label": raw_label,
                    "raw_count": count,
                    "conservative_label": conservative,
                    "family_label": family,
                }
            )
            conservative_groups[conservative].append(raw_label)
            family_groups[family].append(raw_label)
            family_counts[family] += count
        for family, labels in family_groups.items():
            unique_labels = sorted(set(labels))
            family_summary_rows.append(
                {
                    "kind": kind,
                    "family_label": family,
                    "n_unique_raw_labels": len(unique_labels),
                    "total_mentions": family_counts[family],
                    "example_raw_labels": "; ".join(unique_labels[:12]),
                }
            )
        harmonization_summary.extend(
            [
                {
                    "kind": kind,
                    "scheme": "raw",
                    "n_unique_labels": len(counter),
                    "notes": "Exact raw labels from workbook JSON lists.",
                },
                {
                    "kind": kind,
                    "scheme": "conservative",
                    "n_unique_labels": len(conservative_groups),
                    "notes": "Lowercasing plus punctuation/separator normalization only.",
                },
                {
                    "kind": kind,
                    "scheme": "family",
                    "n_unique_labels": len(family_groups),
                    "notes": "Broader exploratory family heuristic: strips wrappers such as individual/group/net and maps common payoff/cooperation/punishment variants to shared concept labels.",
                },
            ]
        )
    with OUT_HARMONIZATION_ROWS.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["kind", "raw_label", "raw_count", "conservative_label", "family_label"],
        )
        writer.writeheader()
        writer.writerows(sorted(harmonization_rows, key=lambda row: (row["kind"], row["family_label"], row["conservative_label"], row["raw_label"])))
    with OUT_HARMONIZATION_SUMMARY.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["kind", "scheme", "n_unique_labels", "notes"])
        writer.writeheader()
        writer.writerows(harmonization_summary)
    with OUT_FAMILY_SUMMARY.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["kind", "family_label", "n_unique_raw_labels", "total_mentions", "example_raw_labels"],
        )
        writer.writeheader()
        writer.writerows(
            sorted(
                family_summary_rows,
                key=lambda row: (row["kind"], -int(row["total_mentions"]), row["family_label"]),
            )
        )

    reported_rows = read_csv_rows(FIGURE5_REPORTED_COUNT_CSV)
    importance_rows = read_csv_rows(FIGURE5_VARIATION_IMPORTANCE_CSV)
    distribution_rows = read_csv_rows(FIGURE5_VALUE_DISTRIBUTION_CSV)
    evenness_rows = read_csv_rows(FIGURE5_EVENNESS_CSV)

    concept_coverage_rows: list[dict[str, object]] = []
    for row in importance_rows:
        concept_coverage_rows.append(
            {
                "concept_type": "benchmark_parameter",
                "concept_name": row["label"],
                "n_papers": int(row["n_papers_mentioned"]),
                "percent_papers": float(row["percent_papers_mentioned"]),
                "notes": "Paper-level mention/reporting count from canonical Figure 5 parameter table.",
            }
        )
    for concept_name, patterns in OUTCOME_CONCEPT_PATTERNS.items():
        n_papers = sum(1 for labels in paper_dv_labels.values() if has_regex_match(labels, patterns))
        concept_coverage_rows.append(
            {
                "concept_type": "outcome_family",
                "concept_name": concept_name,
                "n_papers": n_papers,
                "percent_papers": percent(n_papers, len(paper_dv_labels)),
                "notes": "Paper-level workbook DV coverage using a simple regex family match over the union of DV labels within each lab paper.",
            }
        )
    with OUT_CONCEPT_COVERAGE.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["concept_type", "concept_name", "n_papers", "percent_papers", "notes"],
        )
        writer.writeheader()
        writer.writerows(concept_coverage_rows)

    n_lab_experiments = int(reported_rows[0]["n_experiments_total"])
    n_design_parameters = int(reported_rows[0]["n_design_parameters_total"])
    counts_by_reported = {
        int(row["n_design_parameters_reported"]): int(row["n_experiments"])
        for row in reported_rows
    }
    params_reported_values: list[int] = []
    for n_reported, n_experiments in counts_by_reported.items():
        params_reported_values.extend([n_reported] * n_experiments)

    n_7_or_fewer = sum(n for k, n in counts_by_reported.items() if k <= 7)
    n_all_params = counts_by_reported[n_design_parameters]

    varied_pairs = [
        (row["label"], float(row["percent_papers_varied"]), int(row["n_papers_varied"]))
        for row in importance_rows
    ]
    importance_pairs = [
        (row["label"], float(row["predictive_importance_pct_rmse"]), int(row["n_papers_varied"]), float(row["percent_papers_varied"]))
        for row in importance_rows
    ]
    varied_pairs.sort(key=lambda x: (-x[1], x[0]))
    importance_pairs.sort(key=lambda x: (-x[1], x[0]))

    x_vals = [float(row["predictive_importance_pct_rmse"]) for row in importance_rows]
    y_vals = [float(row["percent_papers_varied"]) for row in importance_rows]
    x_mean = sum(x_vals) / len(x_vals)
    y_mean = sum(y_vals) / len(y_vals)
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_vals, y_vals))
    den_x = math.sqrt(sum((x - x_mean) ** 2 for x in x_vals))
    den_y = math.sqrt(sum((y - y_mean) ** 2 for y in y_vals))
    pearson_r = num / (den_x * den_y)

    mean_literature_evenness = mean([float(row["literature_evenness"]) for row in evenness_rows])
    mean_benchmark_evenness = mean([float(row["benchmark_evenness"]) for row in evenness_rows])

    modal_rows = {}
    for row in distribution_rows:
        param = row["parameter"]
        current = modal_rows.get(param)
        if current is None or float(row["share"]) > float(current["share"]):
            modal_rows[param] = row
    most_concentrated = sorted(
        (
            row["parameter"],
            row["bin_label_display"],
            float(row["percent"]),
        )
        for row in modal_rows.values()
    )
    most_concentrated.sort(key=lambda x: (-x[2], x[0]))

    key_values = [
        {
            "section": "corpus",
            "value_name": "n_corpus_papers",
            "value": len(corpus_ids),
            "notes": "Unique source_id values in the 2,011-paper main-text corpus.",
        },
        {
            "section": "corpus",
            "value_name": "n_corpus_papers_with_workbook_rows",
            "value": len(workbook_paper_ids),
            "notes": "Corpus papers with at least one extraction-workbook row.",
        },
        {
            "section": "corpus",
            "value_name": "n_corpus_papers_missing_from_workbook",
            "value": len(corpus_ids - workbook_paper_ids),
            "notes": "Corpus papers with no extraction-workbook row in the two workbook files.",
        },
        {
            "section": "corpus",
            "value_name": "n_empirical_papers_workbook_strict",
            "value": len(empirical_papers_strict),
            "notes": "Strict workbook-based empirical-paper count: a paper is empirical if any workbook row is marked METHOD_empirical.",
        },
        {
            "section": "corpus",
            "value_name": "n_empirical_papers_workbook_inclusive",
            "value": len(empirical_papers),
            "notes": "Inclusive workbook-based empirical-paper count: a paper is empirical if any workbook row is marked METHOD_empirical or METHOD_lab.",
        },
        {
            "section": "corpus",
            "value_name": "n_lab_papers_workbook",
            "value": len(lab_papers),
            "notes": "Workbook-based lab-paper count: a paper includes lab experiments if any workbook row is marked METHOD_lab.",
        },
        {
            "section": "corpus",
            "value_name": "share_lab_within_empirical_pct_workbook",
            "value": percent(len(lab_papers), len(empirical_papers)),
            "notes": "Percent of inclusive workbook-based empirical papers that include at least one lab row.",
        },
        {
            "section": "causal_density",
            "value_name": "n_lab_experiment_rows_workbook",
            "value": len(lab_rows),
            "notes": "Workbook rows marked METHOD_lab within the 2,011-paper corpus.",
        },
        {
            "section": "causal_density",
            "value_name": "n_lab_rows_with_nonmissing_iv_count",
            "value": len(iv_count_values),
            "notes": "Lab rows with a numeric number_IVs value in the workbook.",
        },
        {
            "section": "causal_density",
            "value_name": "mean_number_IVs",
            "value": mean(iv_count_values),
            "notes": "Mean number_IVs across lab rows with nonmissing IV counts.",
        },
        {
            "section": "causal_density",
            "value_name": "median_number_IVs",
            "value": median(iv_count_values),
            "notes": "Median number_IVs across lab rows with nonmissing IV counts.",
        },
        {
            "section": "causal_density",
            "value_name": "n_lab_rows_with_nonmissing_dv_count",
            "value": len(dv_count_values),
            "notes": "Lab rows with a numeric number_DVs value in the workbook.",
        },
        {
            "section": "causal_density",
            "value_name": "mean_number_DVs",
            "value": mean(dv_count_values),
            "notes": "Mean number_DVs across lab rows with nonmissing DV counts.",
        },
        {
            "section": "causal_density",
            "value_name": "median_number_DVs",
            "value": median(dv_count_values),
            "notes": "Median number_DVs across lab rows with nonmissing DV counts.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_iv_labels",
            "value": len(iv_label_counter),
            "notes": "Unique IV labels parsed from workbook IVs JSON lists across lab rows.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_dv_labels",
            "value": len(dv_label_counter),
            "notes": "Unique DV labels parsed from workbook DVs JSON lists across lab rows.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_iv_labels_conservative_harmonized",
            "value": len({conservative_label(label) for label in iv_label_counter}),
            "notes": "IV labels after conservative lexical harmonization only.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_dv_labels_conservative_harmonized",
            "value": len({conservative_label(label) for label in dv_label_counter}),
            "notes": "DV labels after conservative lexical harmonization only.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_iv_labels_family_harmonized",
            "value": len({family_label(label) for label in iv_label_counter}),
            "notes": "IV labels after broader exploratory family-level harmonization.",
        },
        {
            "section": "causal_density",
            "value_name": "n_unique_dv_labels_family_harmonized",
            "value": len({family_label(label) for label in dv_label_counter}),
            "notes": "DV labels after broader exploratory family-level harmonization.",
        },
        {
            "section": "panel_a",
            "value_name": "n_lab_experiments",
            "value": n_lab_experiments,
            "notes": "Filtered lab-experiment rows used in Figure 5 Panel A.",
        },
        {
            "section": "panel_a",
            "value_name": "n_design_parameters",
            "value": n_design_parameters,
            "notes": "Number of benchmark-comparable design parameters in Figure 5.",
        },
        {
            "section": "panel_a",
            "value_name": "mean_parameters_reported",
            "value": mean(params_reported_values),
            "notes": "Mean number of the 12 displayed design parameters reported per lab experiment.",
        },
        {
            "section": "panel_a",
            "value_name": "median_parameters_reported",
            "value": median(params_reported_values),
            "notes": "Median number of the 12 displayed design parameters reported per lab experiment.",
        },
        {
            "section": "panel_a",
            "value_name": "n_experiments_reporting_7_or_fewer",
            "value": n_7_or_fewer,
            "notes": "Lab experiments reporting 7 or fewer of the 12 displayed parameters.",
        },
        {
            "section": "panel_a",
            "value_name": "share_experiments_reporting_7_or_fewer_pct",
            "value": percent(n_7_or_fewer, n_lab_experiments),
            "notes": "Percent of lab experiments reporting 7 or fewer of the 12 displayed parameters.",
        },
        {
            "section": "panel_a",
            "value_name": "n_experiments_reporting_all_parameters",
            "value": n_all_params,
            "notes": "Lab experiments reporting all 12 displayed parameters.",
        },
        {
            "section": "panel_a",
            "value_name": "share_experiments_reporting_all_parameters_pct",
            "value": percent(n_all_params, n_lab_experiments),
            "notes": "Percent of lab experiments reporting all 12 displayed parameters.",
        },
        {
            "section": "panel_b",
            "value_name": "n_lab_papers_panel_b",
            "value": int(importance_rows[0]["n_papers_total"]),
            "notes": "Lab papers used in the parameter-variation analysis.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_group_size",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_playerCount"),
            "notes": "Lab papers that reported group size in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_contribution_type",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_allOrNothing"),
            "notes": "Lab papers that reported contribution type in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_game_length",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_numRounds"),
            "notes": "Lab papers that reported game length in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_contribution_framing",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_defaultContribProp"),
            "notes": "Lab papers that reported contribution framing in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_punishment_cost",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_punishmentCost"),
            "notes": "Lab papers that reported punishment cost in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_punishment_technology",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_punishmentTech"),
            "notes": "Lab papers that reported punishment technology in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_reward",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_rewardExists"),
            "notes": "Lab papers that reported reward availability in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_reporting_communication",
            "value": next(int(row["n_papers_mentioned"]) for row in importance_rows if row["parameter"] == "CONFIG_chat"),
            "notes": "Lab papers that reported communication in the canonical Figure 5 parameter table.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_with_contribution_outcomes",
            "value": next(int(row["n_papers"]) for row in concept_coverage_rows if row["concept_name"] == "contribution"),
            "notes": "Lab papers with at least one contribution-related DV label.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_with_punishment_outcomes",
            "value": next(int(row["n_papers"]) for row in concept_coverage_rows if row["concept_name"] == "punishment_behavior"),
            "notes": "Lab papers with at least one punishment-related DV label.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_with_cooperation_outcomes",
            "value": next(int(row["n_papers"]) for row in concept_coverage_rows if row["concept_name"] == "cooperation"),
            "notes": "Lab papers with at least one cooperation-related DV label.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_with_earnings_payoff_outcomes",
            "value": next(int(row["n_papers"]) for row in concept_coverage_rows if row["concept_name"] == "earnings_payoff"),
            "notes": "Lab papers with at least one earnings/payoff/profit/income DV label.",
        },
        {
            "section": "coverage",
            "value_name": "n_papers_with_efficiency_outcomes",
            "value": next(int(row["n_papers"]) for row in concept_coverage_rows if row["concept_name"] == "efficiency_welfare"),
            "notes": "Lab papers with at least one efficiency/welfare DV label.",
        },
        {
            "section": "panel_b",
            "value_name": "pearson_r_variation_vs_importance",
            "value": pearson_r,
            "notes": "Pearson r between percent of lab papers varying a parameter and benchmark predictive importance.",
        },
        {
            "section": "panel_b",
            "value_name": "p_value_variation_vs_importance",
            "value": 0.693,
            "notes": "P value shown in the canonical Figure 5 documentation for the same correlation.",
        },
        {
            "section": "panel_c",
            "value_name": "mean_literature_evenness",
            "value": mean_literature_evenness,
            "notes": "Mean normalized evenness across the 12 displayed parameters in the literature.",
        },
        {
            "section": "panel_c",
            "value_name": "mean_benchmark_evenness",
            "value": mean_benchmark_evenness,
            "notes": "Mean normalized evenness across the same parameters in the benchmark experiments.",
        },
    ]

    with OUT_KEY_VALUES.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["section", "value_name", "value", "notes"])
        writer.writeheader()
        writer.writerows(key_values)

    top_iv_text = ", ".join(f"{label} ({count})" for label, count in iv_label_counter.most_common(10))
    top_dv_text = ", ".join(f"{label} ({count})" for label, count in dv_label_counter.most_common(10))
    varied_text = ", ".join(f"{label} ({format_pct(pct)}; n={n})" for label, pct, n in varied_pairs[:3])
    importance_text = ", ".join(
        f"{label} ({format_num(importance, 1)}% error increase when shuffled; varied in {format_pct(pct)} of papers)"
        for label, importance, _n, pct in importance_pairs[:3]
    )
    concentrated_text = ", ".join(
        f"{row['label']}={row['bin_label_display']} ({format_num(float(row['percent']), 1)}%)"
        for row in [modal_rows[param] for param, _bin, _pct in most_concentrated[:6]]
    )

    doc_lines = [
        "# figure5_main_text_results",
        "",
        "## Purpose",
        "Main-text numerical summary for the Figure 5 results section in `main_text_260427`.",
        "",
        "## Source files",
        "- Main-text corpus IDs: `results/validation/literature_analysis_report_sources_overview/single_paper_overview_dataset.csv`",
        "- Extraction workbooks: `batch_processing/output_csv/simple_batch_197papers.xlsx`, `batch_processing/output_csv/simple_batch_810papers.xlsx`",
        "- Panel A rows: `results/paper/main_text_figures_260427/figure5_reported_parameter_count_rows.csv`",
        "- Panel B rows: `results/paper/main_text_figures_260427/figure5_variation_vs_importance_rows.csv`",
        "- Panel C rows: `results/paper/main_text_figures_260427/figure5_value_distribution_rows.csv`",
        "- Evenness comparison: `results/paper/main_text_figures_260427/figure5_value_evenness_vs_benchmark_rows.csv`",
        "- This summary script treats those Figure 5 row tables as canonical for the displayed 12-parameter comparison. In manuscript prose, describe the `14 -> 12` reduction as excluding reward cost and reward technology because they are only defined when reward exists.",
        "",
        "## Workbook methodology",
        f"- The main-text corpus contains `{len(corpus_ids):,}` unique papers.",
        f"- `{len(workbook_paper_ids):,}` of those papers appear in the extraction workbooks; `{len(corpus_ids - workbook_paper_ids):,}` corpus papers have no workbook row.",
        "- A paper counts as empirical if **any** workbook row for that `custom_id` is marked `METHOD_empirical`.",
        "- A paper counts as including lab experiments if **any** workbook row for that `custom_id` is marked `METHOD_lab`.",
        f"- Two papers are marked `METHOD_lab` without also being marked `METHOD_empirical`, so for the paper-level denominator we treat `METHOD_lab` as sufficient evidence of empirical status.",
        f"- Under that inclusive rule, the workbook-based empirical denominator is `{len(empirical_papers):,}` papers, and `{len(lab_papers):,}` of them (`{format_pct(percent(len(lab_papers), len(empirical_papers)))}`) include at least one lab row.",
        f"- The lab-row subset used for the causal-density opener contains `{len(lab_rows):,}` rows marked `METHOD_lab` in the workbooks.",
        "",
        "## Key manuscript values",
        "",
        "### Corpus composition",
        f"- Strict workbook-based empirical papers (`METHOD_empirical`): `{len(empirical_papers_strict):,}`",
        f"- Inclusive workbook-based empirical papers (`METHOD_empirical` or `METHOD_lab`): `{len(empirical_papers):,}`",
        f"- Workbook-based lab papers in that corpus: `{len(lab_papers):,}`",
        f"- Share of inclusive empirical papers that include at least one lab row: `{format_pct(percent(len(lab_papers), len(empirical_papers)))}`",
        "",
        "### Causal density from the workbook",
        f"- Lab rows: `{len(lab_rows):,}`",
        f"- Mean `number_IVs`: `{format_num(mean(iv_count_values))}` (median `{int(median(iv_count_values))}`; `{len(iv_count_values):,}` rows with nonmissing IV counts)",
        f"- Mean `number_DVs`: `{format_num(mean(dv_count_values))}` (median `{int(median(dv_count_values))}`; `{len(dv_count_values):,}` rows with nonmissing DV counts)",
        f"- Unique IV labels across lab rows: `{len(iv_label_counter):,}`",
        f"- Unique DV labels across lab rows: `{len(dv_label_counter):,}`",
        f"- After conservative lexical harmonization, these counts are `{len({conservative_label(label) for label in iv_label_counter}):,}` IV labels and `{len({conservative_label(label) for label in dv_label_counter}):,}` DV labels.",
        f"- Under a broader exploratory family heuristic, they drop to `{len({family_label(label) for label in iv_label_counter}):,}` IV families and `{len({family_label(label) for label in dv_label_counter}):,}` DV families.",
        f"- Most common IV labels: {top_iv_text}",
        f"- Most common DV labels: {top_dv_text}",
        "",
        "### Benchmark-parameter coverage in the aggregate",
        f"- Group size reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_playerCount')}` of `756` lab papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_playerCount'))}`)",
        f"- Contribution type reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_allOrNothing')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_allOrNothing'))}`)",
        f"- Game length reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_numRounds')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_numRounds'))}`)",
        f"- Contribution framing reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_defaultContribProp')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_defaultContribProp'))}`)",
        f"- Punishment cost reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_punishmentCost')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_punishmentCost'))}`)",
        f"- Punishment technology reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_punishmentTech')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_punishmentTech'))}`)",
        f"- Communication reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_chat')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_chat'))}`)",
        f"- Reward reported in `{next(int(row['n_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_rewardExists')}` papers (`{format_pct(next(float(row['percent_papers_mentioned']) for row in importance_rows if row['parameter'] == 'CONFIG_rewardExists'))}`)",
        "",
        "### Outcome coverage in the aggregate",
        f"- Contribution-related outcomes appear in `{next(int(row['n_papers']) for row in concept_coverage_rows if row['concept_name'] == 'contribution')}` of `756` lab papers (`{format_pct(next(float(row['percent_papers']) for row in concept_coverage_rows if row['concept_name'] == 'contribution'))}`)",
        f"- Punishment-related outcomes appear in `{next(int(row['n_papers']) for row in concept_coverage_rows if row['concept_name'] == 'punishment_behavior')}` papers (`{format_pct(next(float(row['percent_papers']) for row in concept_coverage_rows if row['concept_name'] == 'punishment_behavior'))}`)",
        f"- Earnings/payoff outcomes appear in `{next(int(row['n_papers']) for row in concept_coverage_rows if row['concept_name'] == 'earnings_payoff')}` papers (`{format_pct(next(float(row['percent_papers']) for row in concept_coverage_rows if row['concept_name'] == 'earnings_payoff'))}`)",
        f"- Cooperation outcomes appear in `{next(int(row['n_papers']) for row in concept_coverage_rows if row['concept_name'] == 'cooperation')}` papers (`{format_pct(next(float(row['percent_papers']) for row in concept_coverage_rows if row['concept_name'] == 'cooperation'))}`)",
        f"- Efficiency/welfare outcomes appear in `{next(int(row['n_papers']) for row in concept_coverage_rows if row['concept_name'] == 'efficiency_welfare')}` papers (`{format_pct(next(float(row['percent_papers']) for row in concept_coverage_rows if row['concept_name'] == 'efficiency_welfare'))}`)",
        "",
        "### Panel A: parameter reporting",
        f"- Lab-experiment rows: `{n_lab_experiments:,}`",
        f"- Displayed benchmark-comparable parameters: `{n_design_parameters}`",
        f"- Mean parameters reported per experiment: `{format_num(mean(params_reported_values))}`",
        f"- Median parameters reported per experiment: `{int(median(params_reported_values))}`",
        f"- Experiments reporting 7 or fewer parameters: `{n_7_or_fewer:,}` (`{format_pct(percent(n_7_or_fewer, n_lab_experiments))}`)",
        f"- Experiments reporting all `{n_design_parameters}` parameters: `{n_all_params:,}` (`{format_pct(percent(n_all_params, n_lab_experiments))}`)",
        "",
        "### Panel B: variation versus benchmark importance",
        f"- Lab papers: `{int(importance_rows[0]['n_papers_total']):,}`",
        f"- Pearson `r = {pearson_r:.3f}`, `p = 0.693`",
        f"- Most frequently varied parameters: {varied_text}",
        f"- Most predictive benchmark parameters: {importance_text}",
        "- The benchmark importance values are the canonical Figure 5 values: percent increase in prediction error when the parameter is shuffled in the benchmark model.",
        "",
        "### Panel C: concentration in a narrow subset of settings",
        f"- Mean literature evenness across the 12 displayed parameters: `{format_num(mean_literature_evenness, 3)}`",
        f"- Mean benchmark evenness across the same parameters: `{format_num(mean_benchmark_evenness, 3)}`",
        f"- Most concentrated modal values: {concentrated_text}",
        "",
        "## Interpretation notes",
        "- The workbook-based method supports the claim that most empirical papers in the main-text corpus include lab experiments. Under the inclusive workbook rule (`METHOD_empirical` or `METHOD_lab`), the denominator is `940`, not the evidence-card count of `947`.",
        "- The causal-density opener can be grounded in the workbook itself: typical lab rows already involve multiple independent variables and multiple dependent variables, and the label vocabulary is very large.",
        f"- The raw `{len(iv_label_counter):,}` / `{len(dv_label_counter):,}` counts are exact-label counts, not hand-harmonized concept counts. Conservative lexical harmonization changes almost nothing (`{len({conservative_label(label) for label in iv_label_counter}):,}` IVs, `{len({conservative_label(label) for label in dv_label_counter}):,}` DVs), while a broader exploratory family heuristic still leaves hundreds of families (`{len({family_label(label) for label in iv_label_counter}):,}` IV, `{len({family_label(label) for label in dv_label_counter}):,}` DV).",
        "- Figure 5 is therefore not just about sparsity. The literature contains many experiments, many manipulated factors, and many outcomes, yet it remains misaligned with the benchmark because relevant parameters are underreported, the wrong parameters are varied most often, and observed values cluster in narrow regions of the design space.",
        "",
        "## Output tables",
        "- `figure5_main_text_key_values.csv`",
        "- `figure5_workbook_iv_dv_label_counts.csv`",
        "- `figure5_workbook_iv_dv_harmonization_rows.csv`",
        "- `figure5_workbook_iv_dv_harmonization_summary.csv`",
        "- `figure5_workbook_iv_dv_family_summary.csv`",
        "- `figure5_workbook_concept_coverage.csv`",
    ]
    OUT_DOC.write_text("\n".join(doc_lines))

    print(f"Wrote {OUT_KEY_VALUES}")
    print(f"Wrote {OUT_DOC}")
    print(f"Wrote {OUT_LABEL_COUNTS}")


if __name__ == "__main__":
    main()
