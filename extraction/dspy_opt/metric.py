from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "evaluator"))

from utils.columns import COLUMN_MAP  # noqa: E402
from utils.matching import classify_match  # noqa: E402
from utils.row_alignment import align_rows  # noqa: E402

PGG_CONFIG_FIELDS: list[str] = [
    "CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_showNRounds",
    "CONFIG_allOrNothing", "CONFIG_defaultContribProp", "CONFIG_MPCR",
    "CONFIG_chat", "CONFIG_showOtherSummaries", "CONFIG_showPunishmentId",
    "CONFIG_punishmentExists", "CONFIG_punishmentCost", "CONFIG_punishmentTech",
]


def _parse_extraction(raw: str) -> list[dict] | None:
    s = (raw or "").strip()
    candidates: list[str] = []
    if s.startswith("```"):
        nl = s.find("\n")
        if nl != -1:
            inner = s[nl + 1:]
            last_fence = inner.rfind("```")
            candidates.append(inner[:last_fence].strip() if last_fence > 0 else inner.strip())
    first, last = s.find("{"), s.rfind("}")
    if first != -1 and last > first:
        candidates.append(s[first:last + 1])
    candidates.append(s)
    for c in candidates:
        try:
            obj = json.loads(c)
            if isinstance(obj, dict) and isinstance(obj.get("experiments"), list):
                return obj["experiments"]
        except json.JSONDecodeError:
            continue
    return None


def _llm_row_from_experiment(exp: dict) -> dict:
    row = {k: ("" if v is None else str(v)) for k, v in exp.items()}
    row.setdefault("data_id", "")
    row["v"] = row.get("data_id", "")
    return row


def _score_field(cls: str) -> float | None:
    if cls in ("match", "close"):
        return 1.0
    if cls in ("mismatch", "missing_row"):
        return 0.0
    return None  # both_empty / one_empty → excluded


def score_extraction(human_rows: list[dict], experiments: list[dict],
                     fields: list[str] | None = None) -> float:
    """Mean field accuracy across all aligned (condition × field) pairs."""
    fields = fields or list(COLUMN_MAP.keys())
    llm_rows = [_llm_row_from_experiment(e) for e in experiments]
    pairs = align_rows(human_rows, llm_rows, column_map=COLUMN_MAP)

    scores: list[float] = []
    for h, l in pairs:
        for fn in fields:
            human_col, llm_col = COLUMN_MAP[fn]
            h_val = str((h or {}).get(human_col, "")) if h else ""
            l_val = str((l or {}).get(llm_col, "")) if l else ""
            cls = classify_match(
                field_label=fn,
                human_value=h_val,
                llm_value=l_val,
                human_exists=h is not None,
                llm_exists=l is not None,
                compare_human_to_llm=True,
            )
            s = _score_field(cls)
            if s is not None:
                scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


def dspy_metric(example, pred, trace=None) -> float:
    experiments = _parse_extraction(getattr(pred, "extraction_json", "") or "")
    if experiments is None:
        return 0.0
    return score_extraction(example.human_rows, experiments)


def dspy_metric_pgg_only(example, pred, trace=None) -> float:
    """Variant that scores only the 12 PGG CONFIG fields (excludes method + DV fields)."""
    experiments = _parse_extraction(getattr(pred, "extraction_json", "") or "")
    if experiments is None:
        return 0.0
    return score_extraction(example.human_rows, experiments, fields=PGG_CONFIG_FIELDS)
