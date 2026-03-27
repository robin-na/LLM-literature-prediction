from __future__ import annotations

import json
from collections.abc import Iterable, Sequence
from pathlib import Path

import pandas as pd


def load_collection_map(
    mapping_path: Path,
    *,
    max_collections: int | None = None,
) -> list[tuple[str, list[int]]]:
    raw = json.loads(mapping_path.read_text(encoding="utf-8"))
    items: list[tuple[str, list[int]]] = []
    for label, raw_indices in raw.items():
        indices = [int(idx) for idx in raw_indices if str(idx).isdigit() and int(idx) >= 0]
        if indices:
            items.append((str(label), indices))
    if max_collections is not None:
        items = items[: max(0, max_collections)]
    return items


def build_collection_file_id_map(
    eligible_csv: Path,
    collection_items: Sequence[tuple[str, list[int]]],
    *,
    file_id_column: str = "file_id",
) -> dict[str, list[str]]:
    df = pd.read_csv(eligible_csv)
    if file_id_column not in df.columns:
        raise KeyError(f"{eligible_csv} is missing required column '{file_id_column}'")

    file_id_map: dict[str, list[str]] = {}
    max_index = len(df) - 1
    for label, indices in collection_items:
        bad = [idx for idx in indices if idx > max_index]
        if bad:
            raise IndexError(
                f"Collection '{label}' references row(s) beyond {eligible_csv}: {bad[:5]}"
            )
        file_ids = [
            str(file_id)
            for file_id in df.iloc[indices][file_id_column].tolist()
            if pd.notna(file_id) and str(file_id).strip()
        ]
        if not file_ids:
            raise ValueError(f"Collection '{label}' has no usable file ids in {eligible_csv}")
        file_id_map[label] = file_ids
    return file_id_map


def chunk_items(items: Sequence[str], chunk_size: int) -> list[list[str]]:
    if chunk_size <= 0:
        return [list(items)]
    return [list(items[i : i + chunk_size]) for i in range(0, len(items), chunk_size)]


def write_jsonl(path: Path, records: Iterable[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def extract_openai_batch_output_text(item: dict) -> str | None:
    body = ((item.get("response") or {}).get("body")) or {}
    if not isinstance(body, dict):
        return None

    if body.get("object") == "chat.completion":
        choices = body.get("choices") or []
        if not choices:
            return None
        return (
            ((choices[0].get("message") or {}).get("content"))
            if isinstance(choices[0], dict)
            else None
        )

    if body.get("object") == "response":
        output = body.get("output") or []
        for item_output in output:
            if item_output.get("type") != "message":
                continue
            for content in item_output.get("content") or []:
                text = content.get("text")
                if text:
                    return text
        output_text = body.get("output_text")
        if output_text:
            return str(output_text)

    return None
