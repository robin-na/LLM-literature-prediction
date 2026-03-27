from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


RAW_PAPERS_DIR = Path("paper_collection/papers_markdown")
CLEAN_PAPERS_DIR = Path("paper_collection/papers_markdown_cleaned")
DEFAULT_SUMMARY_CSV = Path("paper_collection/papers_markdown_cleaned_summary.csv")
DEFAULT_SUMMARY_JSON = Path("paper_collection/papers_markdown_cleaned_summary.json")
DEFAULT_METADATA_CSV = Path("paper_collection/WoS_251031_fileInfo.csv")

MIN_TRAILING_CUT_CHARS = 8_000
MIN_TRAILING_CUT_FRACTION = 0.20
MIN_APPENDIX_CUT_FRACTION = 0.55

TITLE_HEADING_RE = re.compile(r"^#\s+.+", re.MULTILINE)
ANY_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)", re.MULTILINE)
DISCUSSION_HEADING_RE = re.compile(
    r"^##\s+(?:\d+\s+)?(?:Discussion|Conclusion|Conclusions|Concluding Remarks|General Discussion|Summary)\b",
    re.IGNORECASE | re.MULTILINE,
)
ABSTRACT_RE = re.compile(r"^####?\s+Abstract\b|^Abstract\b", re.IGNORECASE | re.MULTILINE)
ARTICLE_SEPARATOR_RE = re.compile(r"^##\s+ARTICLES\b", re.IGNORECASE | re.MULTILINE)
TRAILING_SECTION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "commentary",
        re.compile(r"^#\s+Open Peer Commentary\b", re.IGNORECASE | re.MULTILINE),
    ),
    (
        "author_response",
        re.compile(r"^##\s+Authors?' Response\b", re.IGNORECASE | re.MULTILINE),
    ),
    (
        "correction",
        re.compile(r"^##\s+Correction to\b", re.IGNORECASE | re.MULTILINE),
    ),
    (
        "correction",
        re.compile(r"^#\s+Correction to\b", re.IGNORECASE | re.MULTILINE),
    ),
    (
        "references",
        re.compile(r"^###?\s+References\b", re.IGNORECASE | re.MULTILINE),
    ),
]
APPENDIX_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "appendix",
        re.compile(r"^###?\s+Appendix\b", re.IGNORECASE | re.MULTILINE),
    ),
    (
        "appendix_letter",
        re.compile(r"^##\s+[A-Z](?:\b|\.)", re.MULTILINE),
    ),
]


@dataclass
class CutDecision:
    char_index: int
    line_number: int
    reason: str
    marker: str


@dataclass
class TitleMatch:
    char_index: int
    line_number: int
    heading_level: int
    heading_text: str
    match_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a cleaned markdown corpus for literature extraction by trimming "
            "leading pre-title spillover and removing trailing references, "
            "commentary bundles, and corrections with safeguards."
        )
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=RAW_PAPERS_DIR,
        help="Directory containing raw markdown papers.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=CLEAN_PAPERS_DIR,
        help="Directory for cleaned markdown papers.",
    )
    parser.add_argument(
        "--summary-csv",
        type=Path,
        default=DEFAULT_SUMMARY_CSV,
        help="CSV path for the cleaning summary.",
    )
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=DEFAULT_SUMMARY_JSON,
        help="JSON path for aggregate cleaning stats.",
    )
    parser.add_argument(
        "--metadata-csv",
        type=Path,
        default=DEFAULT_METADATA_CSV,
        help="CSV with DOI/custom_id and article-title metadata for title-aware cleaning.",
    )
    parser.add_argument(
        "--strip-appendices",
        action="store_true",
        help=(
            "Also trim late appendix sections. Off by default so appendices are "
            "preserved unless explicitly requested."
        ),
    )
    return parser.parse_args()


def _line_number_at(text: str, char_index: int) -> int:
    return text.count("\n", 0, char_index) + 1


def normalize_title(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.casefold()
    return "".join(ch for ch in text if ch.isalnum())


def load_expected_titles(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    title_map: dict[str, str] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            title = (row.get("Article Title") or "").strip()
            if not title:
                continue

            custom_id = (row.get("custom_id") or "").strip()
            if custom_id:
                title_map[Path(custom_id).stem] = title

            doi = (row.get("DOI") or "").strip()
            if doi:
                title_map[doi.replace("/", "_")] = title
    return title_map


def find_expected_title_match(text: str, expected_title: str) -> TitleMatch | None:
    expected_norm = normalize_title(expected_title)
    if not expected_norm:
        return None

    matches: list[tuple[int, re.Match[str], str]] = []
    for match in ANY_HEADING_RE.finditer(text):
        heading_text = match.group(2).strip()
        heading_norm = normalize_title(heading_text)
        if not heading_norm:
            continue
        if heading_norm == expected_norm or heading_norm in expected_norm or expected_norm in heading_norm:
            matches.append((match.start(), match, heading_text))

    if not matches:
        return None

    chosen_index = 0
    while chosen_index + 1 < len(matches):
        current_start = matches[chosen_index][0]
        next_start = matches[chosen_index + 1][0]
        if next_start - current_start > 3_000:
            break
        chosen_index += 1

    start, match, heading_text = matches[chosen_index]
    return TitleMatch(
        char_index=start,
        line_number=_line_number_at(text, start),
        heading_level=len(match.group(1)),
        heading_text=heading_text,
        match_count=len(matches),
    )


def trim_leading_to_title(
    text: str,
    *,
    expected_title: str | None,
) -> tuple[str, dict[str, object]]:
    title_match = find_expected_title_match(text, expected_title) if expected_title else None
    if title_match is not None:
        if title_match.char_index == 0:
            return text, {
                "expected_title": expected_title or "",
                "title_match_found": True,
                "title_match_count": title_match.match_count,
                "title_match_heading_level": title_match.heading_level,
                "title_match_heading_text": title_match.heading_text,
                "title_match_char_index": title_match.char_index,
                "leading_trimmed": False,
                "leading_trim_chars": 0,
                "leading_trim_lines": 0,
                "leading_trim_reason": "",
            }

        trimmed = text[title_match.char_index :]
        return trimmed, {
            "expected_title": expected_title or "",
            "title_match_found": True,
            "title_match_count": title_match.match_count,
            "title_match_heading_level": title_match.heading_level,
            "title_match_heading_text": title_match.heading_text,
            "title_match_char_index": title_match.char_index,
            "leading_trimmed": True,
            "leading_trim_chars": title_match.char_index,
            "leading_trim_lines": title_match.line_number - 1,
            "leading_trim_reason": "trimmed_to_expected_title_heading",
        }

    match = TITLE_HEADING_RE.search(text)
    if match is None or match.start() == 0:
        return text, {
            "expected_title": expected_title or "",
            "title_match_found": False,
            "title_match_count": 0,
            "title_match_heading_level": 0,
            "title_match_heading_text": "",
            "title_match_char_index": -1,
            "leading_trimmed": False,
            "leading_trim_chars": 0,
            "leading_trim_lines": 0,
            "leading_trim_reason": "",
        }

    trimmed = text[match.start() :]
    return trimmed, {
        "expected_title": expected_title or "",
        "title_match_found": False,
        "title_match_count": 0,
        "title_match_heading_level": 0,
        "title_match_heading_text": "",
        "title_match_char_index": -1,
        "leading_trimmed": True,
        "leading_trim_chars": match.start(),
        "leading_trim_lines": _line_number_at(text, match.start()) - 1,
        "leading_trim_reason": "trimmed_to_first_h1_title",
    }


def _valid_cut(match_start: int, text_len: int, *, min_fraction: float) -> bool:
    return match_start >= MIN_TRAILING_CUT_CHARS and (match_start / max(text_len, 1)) >= min_fraction


def find_next_article_start(text: str, *, expected_title: str | None) -> CutDecision | None:
    expected_norm = normalize_title(expected_title or "")
    if not expected_norm:
        return None

    for match in ANY_HEADING_RE.finditer(text):
        if len(match.group(1)) != 1:
            continue
        heading_text = match.group(2).strip()
        heading_norm = normalize_title(heading_text)
        if not heading_norm or heading_norm == expected_norm:
            continue
        lookahead = text[match.start() : min(len(text), match.start() + 2_500)]
        if ABSTRACT_RE.search(lookahead) is None:
            continue
        if not _valid_cut(match.start(), len(text), min_fraction=MIN_TRAILING_CUT_FRACTION):
            continue
        cut_start = match.start()
        separator_window_start = max(0, cut_start - 5_000)
        separator_matches = list(ARTICLE_SEPARATOR_RE.finditer(text, separator_window_start, cut_start))
        if separator_matches:
            cut_start = separator_matches[-1].start()
        return CutDecision(
            char_index=cut_start,
            line_number=_line_number_at(text, cut_start),
            reason="next_article",
            marker=match.group(0).strip(),
        )
    return None


def find_trailing_cut(
    text: str,
    *,
    strip_appendices: bool,
    expected_title: str | None,
) -> CutDecision | None:
    text_len = len(text)
    candidates: list[CutDecision] = []

    for reason, pattern in TRAILING_SECTION_PATTERNS:
        for match in pattern.finditer(text):
            if not _valid_cut(match.start(), text_len, min_fraction=0.0):
                continue
            marker = match.group(0).strip()
            candidates.append(
                CutDecision(
                    char_index=match.start(),
                    line_number=_line_number_at(text, match.start()),
                    reason=reason,
                    marker=marker,
                )
            )
            break

    next_article = find_next_article_start(text, expected_title=expected_title)
    if next_article is not None:
        candidates.append(next_article)

    if strip_appendices:
        discussion_match = DISCUSSION_HEADING_RE.search(text)
        has_discussion = discussion_match is not None
        for reason, pattern in APPENDIX_PATTERNS:
            for match in pattern.finditer(text):
                if not _valid_cut(match.start(), text_len, min_fraction=MIN_APPENDIX_CUT_FRACTION):
                    continue
                if has_discussion and discussion_match is not None and match.start() <= discussion_match.start():
                    continue
                marker = match.group(0).strip()
                candidates.append(
                    CutDecision(
                        char_index=match.start(),
                        line_number=_line_number_at(text, match.start()),
                        reason=reason,
                        marker=marker,
                    )
                )
                break

    if not candidates:
        return None
    return min(candidates, key=lambda item: item.char_index)


def clean_text(
    text: str,
    *,
    strip_appendices: bool,
    expected_title: str | None,
) -> tuple[str, dict[str, object]]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    original_len = len(text)
    trimmed, lead_meta = trim_leading_to_title(text, expected_title=expected_title)
    trailing = find_trailing_cut(
        trimmed,
        strip_appendices=strip_appendices,
        expected_title=expected_title,
    )

    if trailing is None:
        cleaned = trimmed.rstrip() + "\n"
        trail_meta = {
            "trailing_cut": False,
            "trailing_cut_reason": "",
            "trailing_cut_marker": "",
            "trailing_cut_line": 0,
            "trailing_cut_chars": 0,
        }
    else:
        cleaned = trimmed[: trailing.char_index].rstrip() + "\n"
        trail_meta = {
            "trailing_cut": True,
            "trailing_cut_reason": trailing.reason,
            "trailing_cut_marker": trailing.marker,
            "trailing_cut_line": trailing.line_number,
            "trailing_cut_chars": len(trimmed) - trailing.char_index,
        }

    cleaned_len = len(cleaned)
    meta = {
        **lead_meta,
        **trail_meta,
        "strip_appendices": strip_appendices,
        "original_chars": original_len,
        "cleaned_chars": cleaned_len,
        "chars_removed_total": original_len - cleaned_len,
        "chars_removed_fraction": (
            float(original_len - cleaned_len) / original_len if original_len else 0.0
        ),
    }
    return cleaned, meta


def write_summary_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "paper_id",
        "source_path",
        "output_path",
        "leading_trimmed",
        "leading_trim_chars",
        "leading_trim_lines",
        "leading_trim_reason",
        "trailing_cut",
        "trailing_cut_reason",
        "trailing_cut_marker",
        "trailing_cut_line",
        "trailing_cut_chars",
        "expected_title",
        "title_match_found",
        "title_match_count",
        "title_match_heading_level",
        "title_match_heading_text",
        "title_match_char_index",
        "strip_appendices",
        "original_chars",
        "cleaned_chars",
        "chars_removed_total",
        "chars_removed_fraction",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_aggregate_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    n_rows = len(rows)
    trailing_rows = [row for row in rows if row["trailing_cut"]]
    leading_rows = [row for row in rows if row["leading_trimmed"]]

    reason_counts: dict[str, int] = {}
    for row in trailing_rows:
        reason = str(row["trailing_cut_reason"])
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    largest_reductions = sorted(
        rows,
        key=lambda row: int(row["chars_removed_total"]),
        reverse=True,
    )[:20]

    return {
        "n_files": n_rows,
        "n_leading_trimmed": len(leading_rows),
        "n_trailing_cut": len(trailing_rows),
        "trailing_cut_reason_counts": reason_counts,
        "total_original_chars": int(sum(int(row["original_chars"]) for row in rows)),
        "total_cleaned_chars": int(sum(int(row["cleaned_chars"]) for row in rows)),
        "total_chars_removed": int(sum(int(row["chars_removed_total"]) for row in rows)),
        "largest_reductions": largest_reductions,
    }


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    expected_titles = load_expected_titles(args.metadata_csv)

    rows: list[dict[str, object]] = []
    for source_path in sorted(args.source_dir.glob("*.md")):
        output_path = args.output_dir / source_path.name
        raw_text = source_path.read_text(encoding="utf-8")
        expected_title = expected_titles.get(source_path.stem)
        cleaned_text, meta = clean_text(
            raw_text,
            strip_appendices=args.strip_appendices,
            expected_title=expected_title,
        )
        output_path.write_text(cleaned_text, encoding="utf-8")
        rows.append(
            {
                "paper_id": source_path.stem,
                "source_path": str(source_path),
                "output_path": str(output_path),
                **meta,
            }
        )

    write_summary_csv(args.summary_csv, rows)
    aggregate = build_aggregate_summary(rows)
    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(
        json.dumps(aggregate, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote cleaned markdown files to {args.output_dir}")
    print(f"Wrote cleaning summary CSV to {args.summary_csv}")
    print(f"Wrote cleaning summary JSON to {args.summary_json}")
    if args.strip_appendices:
        print("Appendix trimming was enabled.")
    else:
        print("Appendix trimming was disabled.")


if __name__ == "__main__":
    main()
