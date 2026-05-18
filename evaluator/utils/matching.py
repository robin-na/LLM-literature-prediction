# This file contains all the matching rules that allow us to generate a draft comparision of the LLM and Human generated outputs

from __future__ import annotations

import json
from typing import Optional

from utils.helpers import is_empty_like

# CONFIG fields where the LLM often outputs 0/false when the paper omits the detail;
# human raters use N/A-style sentinels. Treat those as agreement for auto-matching only
# when comparing ground truth to the LLM (not for human-vs-human consensus).
_SET_LIST_FIELDS: frozenset[str] = frozenset({"DVs"})
_SET_DICT_FIELDS: frozenset[str] = frozenset({"DVs_Definitions"})

_NA_VS_INFERRED_FALSE_FIELDS: frozenset[str] = frozenset(
    {
        "CONFIG_showRewardId",
        "CONFIG_rewardExists",
        "CONFIG_rewardCost",
        "CONFIG_rewardTech",
        "CONFIG_showPunishmentId",
        "CONFIG_punishmentExists",
        "CONFIG_punishmentCost",
        "CONFIG_punishmentTech",
        "CONFIG_showNRounds",
        "CONFIG_chat",
    }
)


def normalize_val(value: str) -> str:
    return value.strip().lower().replace('"', "").replace("'", "")


def _both_nr_na_variants(h_n: str, l_n: str) -> bool:
    """Match 'N/R (explanation)' against 'N/R', 'N/A (note)' against 'N/A', etc."""
    for prefix in ("n/r", "n/a", "nr", "na"):
        if h_n.startswith(prefix) and l_n.startswith(prefix):
            return True
    return False


def _canonicalize_dv_list(items: list[str]) -> list[str]:
    """Map each DV name to its canonical form using the taxonomy (falls back to lowercase)."""
    from utils.dv_taxonomy import canonicalize, load_taxonomy
    taxonomy = load_taxonomy()
    return [canonicalize(x, taxonomy) for x in items]


def _jaccard_list_match(field_label: str, h_raw: str, l_raw: str) -> str | None:
    """DVs: canonicalize both lists via taxonomy, then Jaccard >= 0.7 → match."""
    if field_label not in _SET_LIST_FIELDS:
        return None

    def parse_list(s: str) -> list[str]:
        try:
            parsed = json.loads(s)
            if isinstance(parsed, list):
                return [x.strip() for x in parsed if isinstance(x, str) and x.strip()]
        except Exception:
            pass
        return [x.strip() for x in s.split(",") if x.strip()]

    h_items = parse_list(h_raw)
    l_items = parse_list(l_raw)
    if not h_items and not l_items:
        return "both_empty"

    h_canon = set(_canonicalize_dv_list(h_items))
    l_canon = set(_canonicalize_dv_list(l_items))

    union = len(h_canon | l_canon)
    jaccard = len(h_canon & l_canon) / union if union else 0.0
    return "match" if jaccard >= 0.7 else "mismatch"


def _jaccard_dict_keys_match(field_label: str, h_raw: str, l_raw: str) -> str | None:
    """DVs_Definitions: align definitions by canonical DV key, average embedding similarity >= 0.7 → match.

    Steps:
    1. Canonicalize both dicts' keys via the taxonomy.
    2. Find the intersection of canonical keys (DVs extracted by both sides).
    3. Batch-compute embedding cosine similarity for the aligned definition pairs.
    4. Average similarity across all aligned pairs >= 0.70 → match.
    5. If no canonical key overlap (taxonomy not yet built), fall back to all-vs-all average.
    """
    if field_label not in _SET_DICT_FIELDS:
        return None
    try:
        h_dict = json.loads(h_raw)
        l_dict = json.loads(l_raw)
    except Exception:
        return None
    if not isinstance(h_dict, dict) or not isinstance(l_dict, dict):
        return None

    from utils.definition_similarity import similarity_matrix
    from utils.dv_taxonomy import canonicalize, load_taxonomy

    taxonomy = load_taxonomy()
    h_canon = {canonicalize(k, taxonomy): str(v).strip() for k, v in h_dict.items() if str(v).strip()}
    l_canon = {canonicalize(k, taxonomy): str(v).strip() for k, v in l_dict.items() if str(v).strip()}

    if not h_canon and not l_canon:
        return "both_empty"
    if not h_canon or not l_canon:
        return "mismatch"

    common_keys = sorted(set(h_canon.keys()) & set(l_canon.keys()))

    if common_keys:
        # Batch-compute similarities for aligned (h_def, l_def) pairs.
        h_defs = [h_canon[k] for k in common_keys]
        l_defs = [l_canon[k] for k in common_keys]
        mat = similarity_matrix(h_defs, l_defs)
        # Diagonal mat[i][i] = similarity for the i-th aligned pair.
        sims = [mat[i][i] for i in range(len(common_keys))] if mat else []
    else:
        # No canonical key overlap — fall back to all-vs-all and take row-wise maxima.
        h_defs = list(h_canon.values())
        l_defs = list(l_canon.values())
        mat = similarity_matrix(h_defs, l_defs)
        sims = [max(row) for row in mat] if mat else []

    if not sims:
        return "mismatch"

    avg_sim = sum(sims) / len(sims)
    return "match" if avg_sim >= 0.70 else "mismatch"


def to_html_class(classification: str) -> str:
    return classification.replace("_", "-")

# This function is the main function that classifies the match between the LLM and Human generated outputs
def classify_match(
    field_label: str,
    human_value: str,
    llm_value: str,
    human_exists: bool,
    llm_exists: bool,
    *,
    compare_human_to_llm: bool = True,
) -> str:
    if not human_exists or not llm_exists:
        return "missing_row"
    if is_empty_like(human_value) and is_empty_like(llm_value):
        return "both_empty"
    if not human_value or not llm_value:
        return "one_empty"

    h_n = normalize_val(human_value)
    l_n = normalize_val(llm_value)
    if h_n == l_n:
        return "match"

    if _lab_or_field_exception(field_label, h_n, l_n):
        return "match"

    if _both_nr_na_variants(h_n, l_n):
        return "match"

    list_result = _jaccard_list_match(field_label, human_value, llm_value)
    if list_result is not None:
        return list_result
    dict_result = _jaccard_dict_keys_match(field_label, human_value, llm_value)
    if dict_result is not None:
        return dict_result

    numeric = _numeric_classification(human_value, llm_value)
    if numeric:
        return numeric

    if _boolean_equivalent(h_n, l_n):
        return "match"

    if compare_human_to_llm and _na_human_vs_llm_inferred_false(field_label, human_value, llm_value, l_n):
        return "match"
    if compare_human_to_llm and _na_llm_vs_human_false(field_label, human_value, llm_value, h_n):
        return "match"

    return "mismatch"

# It makes sure that when the value inputed by the human for Lab_Or_filed experiment is 0, True for the LLM, it understands that the both mean : "this is a lab exp"
def _lab_or_field_exception(field_label: str, human_norm: str, llm_norm: str) -> bool:
    if field_label != "Lab / Experiment":
        return False
    if human_norm not in {"0", "0.0"}:
        return False
    return llm_norm in {"true", "1", "yes"}

# Matches numerically close values, with a tolerance of 0.001 or 5%
def _numeric_classification(human_value: str, llm_value: str) -> Optional[str]:
    try:
        hf = float(human_value)
        lf = float(llm_value)
    except ValueError:
        return None

    if abs(hf - lf) < 0.001:
        return "match"
    if abs(hf - lf) / max(abs(hf), abs(lf), 1e-9) < 0.05:
        return "close"
    return None

# General Boolean matching rule
def _boolean_equivalent(human_norm: str, llm_norm: str) -> bool:
    true_vals = {"true", "1", "yes", "1.0"}
    false_vals = {"false", "0", "no", "0.0"}
    return (human_norm in true_vals and llm_norm in true_vals) or (
        human_norm in false_vals and llm_norm in false_vals
    )


def _llm_inferred_absence_sentinel(llm_value: str, llm_norm: str) -> bool:
    """Values the LLM often emits when the paper does not state the feature (numeric/boolean zero)."""
    if llm_norm in {"0", "false", "no", "0.0"}:
        return True
    try:
        return float((llm_value or "").strip()) == 0.0
    except ValueError:
        return False


def _na_human_vs_llm_inferred_false(
    field_label: str,
    human_value: str,
    llm_value: str,
    llm_norm: str,
) -> bool:
    if field_label not in _NA_VS_INFERRED_FALSE_FIELDS:
        return False
    if not is_empty_like(human_value):
        return False
    if is_empty_like(llm_value):
        return False
    return _llm_inferred_absence_sentinel(llm_value, llm_norm)


def _na_llm_vs_human_false(
    field_label: str,
    human_value: str,
    llm_value: str,
    h_n: str,
) -> bool:
    """LLM outputs N/A (strict non-inference) but human coded an explicit 0/false."""
    if field_label not in _NA_VS_INFERRED_FALSE_FIELDS:
        return False
    if is_empty_like(human_value):
        return False
    if not is_empty_like(llm_value):
        return False
    false_vals = {"0", "false", "no", "0.0"}
    if h_n in false_vals:
        return True
    try:
        return float(human_value.strip()) == 0.0
    except ValueError:
        return False

