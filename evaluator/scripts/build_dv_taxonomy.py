"""
Build (or refresh) the DV canonical taxonomy.

Collects every unique DV name from the human CSV and LLM xlsx, sends them to
GPT-4.1 in a single call, and writes the resulting {raw_name: canonical_name}
mapping to utils/dv_taxonomy.json.

Run via:
    python3 main.py build-dv-taxonomy
"""
from __future__ import annotations

import json
import os

import pandas as pd

from utils.dv_taxonomy import TAXONOMY_PATH
from utils.paths import HUMAN_DATASET_CSV, LLM_DATASET_CSV


SYSTEM_PROMPT = (
    "You are building a canonical dependent-variable (DV) taxonomy for "
    "Public Goods Game experiments. You will receive a JSON array of DV names "
    "collected from human annotators (written as plain English phrases) and from "
    "an LLM extractor (written as short snake_case identifiers). "
    "Your task: for each name, assign one canonical snake_case identifier that "
    "captures the underlying construct. Names that measure the same thing must "
    "map to the same canonical name. Names that measure genuinely different things "
    "must map to different canonical names. "
    "Return only a valid JSON object: {\"raw_name\": \"canonical_name\", ...}. "
    "No commentary, no markdown, only the JSON object."
)


def _collect_dv_names() -> list[str]:
    names: set[str] = set()

    human = pd.read_csv(HUMAN_DATASET_CSV)
    if "Dependent Variables" in human.columns:
        for val in human["Dependent Variables"].dropna():
            try:
                items = json.loads(str(val))
                if isinstance(items, list):
                    names.update(x.strip() for x in items if isinstance(x, str) and x.strip())
            except Exception:
                pass

    llm = pd.read_excel(LLM_DATASET_CSV)
    if "DVs" in llm.columns:
        for val in llm["DVs"].dropna():
            try:
                items = json.loads(str(val))
                if isinstance(items, list):
                    names.update(x.strip() for x in items if isinstance(x, str) and x.strip())
            except Exception:
                pass

    return sorted(names)


def build_taxonomy(model: str = "gpt-4.1") -> dict[str, str]:
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set.")
    client = OpenAI(api_key=api_key)

    names = _collect_dv_names()
    if not names:
        raise ValueError("No DV names found in either dataset.")

    print(f"Found {len(names)} unique DV names. Calling {model}...")
    for n in names:
        print(f"  - {n}")

    user_prompt = (
        "Here are all unique DV names collected from the datasets:\n"
        + json.dumps(names, ensure_ascii=False, indent=2)
        + "\n\nReturn the canonical mapping JSON."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )

    raw = response.choices[0].message.content or "{}"
    taxonomy: dict[str, str] = json.loads(raw)

    # Validate: every input name should appear as a key
    missing = [n for n in names if n not in taxonomy and n.lower() not in taxonomy]
    if missing:
        print(f"Warning: {len(missing)} names not returned by model — keeping as-is:")
        for m in missing:
            print(f"  {m}")
            taxonomy[m] = m.lower().replace(" ", "_").replace("-", "_")

    TAXONOMY_PATH.parent.mkdir(parents=True, exist_ok=True)
    TAXONOMY_PATH.write_text(json.dumps(taxonomy, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nTaxonomy saved to: {TAXONOMY_PATH}")
    print(f"Total mappings: {len(taxonomy)}")
    return taxonomy


def print_taxonomy(taxonomy: dict[str, str]) -> None:
    canonical_groups: dict[str, list[str]] = {}
    for raw, canon in sorted(taxonomy.items()):
        canonical_groups.setdefault(canon, []).append(raw)
    print("\nCanonical taxonomy:")
    for canon, raws in sorted(canonical_groups.items()):
        print(f"  {canon}")
        for r in raws:
            print(f"    <- {r!r}")
