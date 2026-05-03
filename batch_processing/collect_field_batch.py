"""
Collect a completed field-specific batch and replace column(s) in an existing xlsx.

The field extractor returns {"experiments": [{condition}, ...]} with one entry per
condition. Since CONFIG_allOrNothing and most CONFIG fields are constant within a paper,
we take the first condition's value and apply it to every row for that paper.

Usage:
    python batch_processing/collect_field_batch.py \
        --batch-id batch_69f666611ce88190aac9741b68a91e1e \
        --field CONFIG_allOrNothing \
        --xlsx batch_processing/output_xlsx/simple_batch_810papers.xlsx \
        --output-xlsx batch_processing/output_xlsx/simple_batch_810papers.xlsx
"""
from __future__ import annotations
import argparse, json, os, re, sys
from pathlib import Path
import pandas as pd

_ILLEGAL_XML_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

from extract_papers_app import _extract_output_text
from agentic_workflow import make_openai_client


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--batch-id", required=True)
    p.add_argument("--field", required=True, help="e.g. CONFIG_allOrNothing")
    p.add_argument("--xlsx", required=True, help="Existing xlsx to update")
    p.add_argument("--output-xlsx", required=True, help="Where to write the updated xlsx")
    p.add_argument("--save-jsonl", help="Optional path to save raw batch output JSONL")
    return p.parse_args()


def fetch_batch_output(batch_id: str) -> str:
    client = make_openai_client()
    batch = client.batches.retrieve(batch_id)
    print(f"Batch status: {batch.status}")
    if batch.status != "completed":
        print("Batch is not completed yet. Try again later.", file=sys.stderr)
        sys.exit(1)
    return client.files.content(batch.output_file_id).text


def extract_field_per_paper(raw_content: str, field: str) -> dict[str, dict]:
    """
    Returns {custom_id: {field: val, field_reason: ..., field_confidence: ...}}.
    Takes the first condition's values when a paper has multiple conditions.
    """
    reason_key = f"{field}_reason"
    conf_key = f"{field}_confidence"
    fallback = {field: "N/R", reason_key: "", conf_key: 0}

    out: dict[str, dict] = {}
    for line in raw_content.splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        custom_id = rec.get("custom_id", "")
        text = _extract_output_text(rec.get("response", {}).get("body", {}))
        if not text:
            print(f"Warning: no text output for {custom_id}", file=sys.stderr)
            out[custom_id] = fallback
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            print(f"Warning: JSON parse error for {custom_id}", file=sys.stderr)
            out[custom_id] = fallback
            continue

        experiments = data.get("experiments", [])
        row = experiments[0] if experiments else data
        out[custom_id] = {
            field: row.get(field, "N/R"),
            reason_key: row.get(reason_key, ""),
            conf_key: row.get(conf_key, 0),
        }
    return out


def main():
    args = parse_args()
    field = args.field
    reason_col = f"{field}_reason"
    conf_col = f"{field}_confidence"

    print(f"Fetching batch {args.batch_id}...")
    raw_content = fetch_batch_output(args.batch_id)
    print(f"  {raw_content.count(chr(10))} lines received.")

    if args.save_jsonl:
        path = Path(args.save_jsonl)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(raw_content, encoding="utf-8")
        print(f"  Raw output saved to {args.save_jsonl}")

    field_data = extract_field_per_paper(raw_content, field)
    print(f"  {len(field_data)} papers parsed.")

    df = pd.read_excel(args.xlsx)

    print(f"\nOld {field} distribution:")
    print(df[field].value_counts(dropna=False).to_string())

    # Single pass: look up all three columns per custom_id at once
    updates = df["custom_id"].map(field_data)
    df[field] = updates.map(lambda d: d[field] if isinstance(d, dict) else None)
    df[reason_col] = updates.map(lambda d: d[reason_col] if isinstance(d, dict) else "")
    df[conf_col] = updates.map(lambda d: d[conf_col] if isinstance(d, dict) else 0)

    print(f"\nNew {field} distribution:")
    print(df[field].value_counts(dropna=False).to_string())

    # Strip control characters that openpyxl rejects from XML
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(
        lambda col: col.map(lambda v: _ILLEGAL_XML_CHARS.sub("", v) if isinstance(v, str) else v)
    )

    with pd.ExcelWriter(args.output_xlsx, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="extractions", index=False)
    print(f"\nUpdated xlsx written to {args.output_xlsx}")


if __name__ == "__main__":
    main()
