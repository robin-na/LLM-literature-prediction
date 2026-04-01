from __future__ import annotations

import argparse
import csv
import json
import re
from itertools import combinations, product
from pathlib import Path

import pandas as pd


DEFAULT_COMBINED_CSV = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/combined.csv"
)
DEFAULT_METADATA_CSV = Path("paper_collection/WoS_251031_fileInfo.csv")
DEFAULT_JCR_XLSX = Path("paper_collection/2024-2025JCRlist.xlsx")
DEFAULT_OUTPUT_DIR = Path(
    "literature/output/evidence_cards/literature_evidence_cards_cleaned/collection_metadata_sets"
)
ALWAYS_EXCLUDED_IDS = {"PGG_MS_202502"}

DIMENSION_ORDER = ["type", "citation", "jcr", "year", "discipline"]

DIMENSION_SPECS = {
    "type": {
        "column": "type_filter",
        "label": "type",
        "values": ["empirical", "theoretical"],
    },
    "citation": {
        "column": "citation_quartile",
        "label": "citation",
        "values": ["Q1_lowest", "Q2", "Q3", "Q4_highest"],
    },
    "jcr": {
        "column": "jcr_quartile",
        "label": "jcr",
        "values": ["Q1", "Q2", "Q3", "Q4"],
    },
    "year": {
        "column": "year_quartile",
        "label": "year",
        "values": ["Q1_oldest", "Q2", "Q3", "Q4_newest"],
    },
    "discipline": {
        "column": "discipline_coarse",
        "label": "discipline",
        "values": [
            "economics",
            "psych_social",
            "bio_evo",
            "math_phys_cs",
            "multidisciplinary",
            "other",
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build metadata-based literature collection sets using up to N simultaneous "
            "filters across paper type, citation quartile, JCR quartile, publication "
            "year quartile, and coarse discipline."
        )
    )
    parser.add_argument(
        "--combined-csv",
        type=Path,
        default=DEFAULT_COMBINED_CSV,
        help="Combined evidence-card CSV from parse_evidence_card_batch_output.py",
    )
    parser.add_argument(
        "--metadata-csv",
        type=Path,
        default=DEFAULT_METADATA_CSV,
        help="Paper metadata CSV exported from Web of Science.",
    )
    parser.add_argument(
        "--jcr-xlsx",
        type=Path,
        default=DEFAULT_JCR_XLSX,
        help="JCR workbook used to map ISSN/eISSN to JIF and quartile.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for the enriched catalog and generated collection-set CSVs.",
    )
    parser.add_argument(
        "--max-filters",
        type=int,
        default=3,
        help="Maximum number of simultaneous filters to combine.",
    )
    parser.add_argument(
        "--min-papers",
        type=int,
        default=2,
        help="Minimum collection size to keep. Use 2 to drop only one-paper collections.",
    )
    parser.add_argument(
        "--exclude-custom-ids",
        nargs="*",
        default=[],
        help="Optional custom_id values to exclude from the catalog before building sets.",
    )
    return parser.parse_args()


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize_custom_id(value: object) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    return text.removesuffix(".md")


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def quartile_rank_from_category(value: object) -> int | None:
    match = re.search(r"\|(Q[1-4])\|", str(value or ""))
    if not match:
        return None
    return int(match.group(1)[1:])


def extract_jcr_quartile(value: object) -> str | None:
    match = re.search(r"\|(Q[1-4])\|", str(value or ""))
    if not match:
        return None
    return match.group(1)


def nearest_quartile_split_values(series: pd.Series) -> list[float]:
    counts = series.dropna().value_counts().sort_index()
    if counts.empty:
        raise ValueError("Cannot compute quartile splits for an empty series.")

    total = int(counts.sum())
    cumulative = counts.cumsum()
    split_values: list[float] = []
    previous_value = None

    for fraction in (0.25, 0.50, 0.75):
        target = total * fraction
        candidates = cumulative.index
        if previous_value is not None:
            candidates = candidates[candidates > previous_value]
        if len(candidates) == 0:
            break
        distances = (cumulative.loc[candidates] - target).abs()
        split_value = float(distances.idxmin())
        split_values.append(split_value)
        previous_value = split_value

    if len(split_values) != 3:
        raise ValueError(
            "Expected three quartile split values, but could not determine them from the series."
        )
    return split_values


def assign_ordered_quartile(
    value: object,
    *,
    split_values: list[float],
    labels: list[str],
) -> str | None:
    if pd.isna(value):
        return None
    numeric = float(value)
    for threshold, label in zip(split_values, labels[:-1], strict=True):
        if numeric <= threshold:
            return label
    return labels[-1]


def classify_disciplines(
    *,
    wos_categories: object,
) -> str:
    category_parts = [
        part.strip()
        for part in str(wos_categories or "").split(";")
        if part and part.strip()
    ]

    labels: list[str] = []

    def add_label(label: str) -> None:
        if label not in labels:
            labels.append(label)

    for category in category_parts:
        category_lower = category.lower()

        # Treat the WoS top-level journal bucket literally. This avoids
        # misclassifying values like "Psychology, Multidisciplinary" as the
        # same thing as Nature/Science/PNAS-style journals.
        if category_lower == "multidisciplinary sciences":
            add_label("multidisciplinary")
            continue

        if "economics" in category_lower or category_lower == "business, finance":
            add_label("economics")

        if any(
            keyword in category_lower
            for keyword in [
                "psychology",
                "behavioral sciences",
                "sociology",
                "social sciences",
                "management",
                "business",
                "anthropology",
                "political science",
                "international relations",
                "ethics",
                "development studies",
                "area studies",
            ]
        ):
            add_label("psych_social")

        if any(
            keyword in category_lower
            for keyword in [
                "biology",
                "ecology",
                "evolutionary",
                "neurosciences",
                "genetics",
                "zoology",
                "ornithology",
                "biodiversity conservation",
            ]
        ):
            add_label("bio_evo")

        if any(
            keyword in category_lower
            for keyword in [
                "physics",
                "mathematics",
                "mathematical",
                "statistics",
                "computer science",
                "automation & control systems",
                "operations research",
            ]
        ):
            add_label("math_phys_cs")

    if not labels:
        labels.append("other")
    return ";".join(labels)


def collection_filter_mask(
    catalog: pd.DataFrame,
    *,
    dimension_name: str,
    value: str,
) -> pd.Series:
    spec = DIMENSION_SPECS[dimension_name]
    if dimension_name != "discipline":
        return catalog[spec["column"]] == value

    return catalog[spec["column"]].fillna("").map(
        lambda item: value in [part for part in str(item).split(";") if part]
    )


def build_catalog(
    *,
    combined_csv: Path,
    metadata_csv: Path,
    jcr_xlsx: Path,
    excluded_ids: set[str],
) -> tuple[pd.DataFrame, dict[str, object]]:
    combined = pd.read_csv(
        combined_csv,
        usecols=[
            "custom_id",
            "paper_type_primary",
        ],
    ).copy()
    combined["custom_id"] = combined["custom_id"].map(normalize_custom_id)
    combined = combined[combined["custom_id"] != ""].copy()

    metadata = pd.read_csv(
        metadata_csv,
        usecols=[
            "custom_id",
            "Article Title",
            "Source Title",
            "Publication Year",
            "Times Cited, All Databases",
            "ISSN",
            "eISSN",
            "WoS Categories",
            "Research Areas",
        ],
    ).copy()
    metadata["custom_id"] = metadata["custom_id"].map(normalize_custom_id)
    metadata = metadata[metadata["custom_id"] != ""].copy()
    metadata = metadata.drop_duplicates("custom_id", keep="first").copy()

    catalog = combined.merge(metadata, on="custom_id", how="left", validate="one_to_one")
    if excluded_ids:
        catalog = catalog[~catalog["custom_id"].isin(excluded_ids)].copy()

    jcr = pd.read_excel(
        jcr_xlsx,
        usecols=["Name", "ISSN", "EISSN", "JIF", "Category"],
    ).copy()
    for column in ["ISSN", "eISSN"]:
        catalog[column] = catalog[column].fillna("").astype(str).str.strip()
    for column in ["ISSN", "EISSN"]:
        jcr[column] = jcr[column].fillna("").astype(str).str.strip()

    jcr_by_issn = jcr[jcr["ISSN"] != ""].drop_duplicates("ISSN")
    jcr_by_eissn = jcr[jcr["EISSN"] != ""].drop_duplicates("EISSN")

    catalog = catalog.merge(
        jcr_by_issn[["ISSN", "Name", "JIF", "Category"]],
        on="ISSN",
        how="left",
    )
    catalog = catalog.merge(
        jcr_by_eissn[["EISSN", "Name", "JIF", "Category"]],
        left_on="eISSN",
        right_on="EISSN",
        how="left",
        suffixes=("_issn", "_eissn"),
    )

    catalog["jcr_journal_name"] = catalog["Name_issn"].combine_first(catalog["Name_eissn"])
    catalog["jif_value"] = catalog["JIF_issn"].combine_first(catalog["JIF_eissn"])
    catalog["jcr_category_raw"] = catalog["Category_issn"].combine_first(
        catalog["Category_eissn"]
    )
    catalog["jcr_quartile"] = catalog["jcr_category_raw"].map(extract_jcr_quartile)

    catalog["type_filter"] = catalog["paper_type_primary"].map(
        {
            "empirical": "empirical",
            "theory": "theoretical",
        }
    )

    year_splits = nearest_quartile_split_values(catalog["Publication Year"])
    citation_splits = nearest_quartile_split_values(catalog["Times Cited, All Databases"])

    year_labels = ["Q1_oldest", "Q2", "Q3", "Q4_newest"]
    citation_labels = ["Q1_lowest", "Q2", "Q3", "Q4_highest"]

    catalog["year_quartile"] = catalog["Publication Year"].map(
        lambda value: assign_ordered_quartile(
            value,
            split_values=year_splits,
            labels=year_labels,
        )
    )
    catalog["citation_quartile"] = catalog["Times Cited, All Databases"].map(
        lambda value: assign_ordered_quartile(
            value,
            split_values=citation_splits,
            labels=citation_labels,
        )
    )
    catalog["discipline_coarse"] = catalog.apply(
        lambda row: classify_disciplines(
            wos_categories=row.get("WoS Categories"),
        ),
        axis=1,
    )

    summary = {
        "n_papers": int(len(catalog)),
        "n_wos_matches": int(catalog["Publication Year"].notna().sum()),
        "n_jcr_matches": int(catalog["jcr_quartile"].notna().sum()),
        "citation_source_column": "Times Cited, All Databases",
        "discipline_source_column": "WoS Categories",
        "year_split_upper_bounds": year_splits,
        "citation_split_upper_bounds": citation_splits,
        "year_bucket_counts": {
            label: int((catalog["year_quartile"] == label).sum()) for label in year_labels
        },
        "citation_bucket_counts": {
            label: int((catalog["citation_quartile"] == label).sum())
            for label in citation_labels
        },
    }
    return catalog, summary


def write_set_csv(path: Path, custom_ids: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"custom_id": custom_ids}).to_csv(path, index=False)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sets_dir = args.output_dir / "sets"
    sets_dir.mkdir(parents=True, exist_ok=True)

    excluded_ids = ALWAYS_EXCLUDED_IDS | {
        normalize_custom_id(value) for value in args.exclude_custom_ids
    }
    catalog, catalog_summary = build_catalog(
        combined_csv=args.combined_csv,
        metadata_csv=args.metadata_csv,
        jcr_xlsx=args.jcr_xlsx,
        excluded_ids=excluded_ids,
    )

    catalog_columns = [
        "custom_id",
        "paper_type_primary",
        "type_filter",
        "Article Title",
        "Source Title",
        "Publication Year",
        "year_quartile",
        "Times Cited, All Databases",
        "citation_quartile",
        "ISSN",
        "eISSN",
        "jif_value",
        "jcr_quartile",
        "jcr_category_raw",
        "WoS Categories",
        "Research Areas",
        "discipline_coarse",
    ]
    catalog_path = args.output_dir / "collection_metadata_catalog.csv"
    catalog[catalog_columns].sort_values("custom_id").to_csv(catalog_path, index=False)
    print(catalog_path)

    summary_rows: list[dict[str, object]] = []
    kept_by_n_filters = {n: 0 for n in range(1, args.max_filters + 1)}
    nonempty_by_n_filters = {n: 0 for n in range(1, args.max_filters + 1)}
    dropped_too_small_by_n_filters = {n: 0 for n in range(1, args.max_filters + 1)}
    theoretical_by_n_filters = {n: 0 for n in range(1, args.max_filters + 1)}

    for n_filters in range(1, args.max_filters + 1):
        for dimension_names in combinations(DIMENSION_ORDER, n_filters):
            theoretical_count = 1
            for dimension_name in dimension_names:
                theoretical_count *= len(DIMENSION_SPECS[dimension_name]["values"])
            theoretical_by_n_filters[n_filters] += theoretical_count

            value_lists = [DIMENSION_SPECS[name]["values"] for name in dimension_names]
            for values in product(*value_lists):
                mask = pd.Series(True, index=catalog.index)
                filter_parts: list[str] = []
                row: dict[str, object] = {
                    "n_filters": n_filters,
                    "count": 0,
                }

                slug_parts: list[str] = []
                filters_json: dict[str, str] = {}
                for dimension_name in DIMENSION_ORDER:
                    row[f"{dimension_name}_value"] = ""

                for dimension_name, value in zip(dimension_names, values, strict=True):
                    spec = DIMENSION_SPECS[dimension_name]
                    mask &= collection_filter_mask(
                        catalog,
                        dimension_name=dimension_name,
                        value=value,
                    )
                    filter_parts.append(f"{spec['label']}={value}")
                    row[f"{dimension_name}_value"] = value
                    filters_json[dimension_name] = value
                    slug_parts.append(f"{dimension_name}_{slugify(value)}")

                custom_ids = sorted(catalog.loc[mask, "custom_id"].tolist())
                count = len(custom_ids)
                if count == 0:
                    continue

                nonempty_by_n_filters[n_filters] += 1
                if count < args.min_papers:
                    dropped_too_small_by_n_filters[n_filters] += 1
                    continue

                collection_id = "__".join(slug_parts)
                set_path = sets_dir / f"{collection_id}.csv"
                write_set_csv(set_path, custom_ids)

                kept_by_n_filters[n_filters] += 1
                row.update(
                    {
                        "collection_id": collection_id,
                        "filter_label": " | ".join(filter_parts),
                        "filters_json": json.dumps(filters_json, sort_keys=True),
                        "count": count,
                        "set_path": str(set_path),
                    }
                )
                summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows).sort_values(
        ["n_filters", "collection_id"], kind="mergesort"
    )
    summary_path = args.output_dir / "collection_metadata_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    print(summary_path)

    meta = {
        "max_filters": args.max_filters,
        "min_papers": args.min_papers,
        "excluded_ids": sorted(excluded_ids),
        "catalog_summary": catalog_summary,
        "theoretical_by_n_filters": theoretical_by_n_filters,
        "nonempty_by_n_filters": nonempty_by_n_filters,
        "kept_by_n_filters": kept_by_n_filters,
        "dropped_too_small_by_n_filters": dropped_too_small_by_n_filters,
        "n_collections_kept": int(len(summary_df)),
    }
    summary_json_path = args.output_dir / "collection_metadata_summary.json"
    summary_json_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(summary_json_path)


if __name__ == "__main__":
    main()
