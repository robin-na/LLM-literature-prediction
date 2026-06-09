from __future__ import annotations

import json
from pathlib import Path

TAXONOMY_PATH: Path = Path(__file__).resolve().parent / "dv_taxonomy.json"


def load_taxonomy() -> dict[str, str]:
    """Return {raw_dv_name: canonical_dv_name}. Empty dict if file not yet built."""
    if not TAXONOMY_PATH.exists():
        return {}
    try:
        return json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def canonicalize(name: str, taxonomy: dict[str, str]) -> str:
    """Map a raw DV name to its canonical form, falling back to the original."""
    key = name.strip()
    return taxonomy.get(key, taxonomy.get(key.lower(), key.lower()))
