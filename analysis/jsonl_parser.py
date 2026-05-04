import json
import re

import numpy as np
import pandas as pd


def _extract_prediction_from_reasoning_text(text: str | None) -> float | None:
    if not text:
        return None

    candidate = text.strip()
    patterns = [
        r"(?:predicted|prediction|predicted efficiency|overall predicted efficiency|bringing it to|leading to|to about|around|approximately)\D{0,20}(-?\d+(?:\.\d+)?)\s*%",
        r"=\s*(-?\d+(?:\.\d+)?)\s*%",
        r"(-?\d+(?:\.\d+)?)\s*%\s*$",
        r"(?:predicted|prediction|predicted efficiency|overall predicted efficiency|bringing it to|leading to|to about|around|approximately)\D{0,20}(-?\d+(?:\.\d+)?)\s*$",
        r"(-?\d+(?:\.\d+)?)\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, candidate, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return None
    return None


def _extract_prediction_from_json_text(text: str | None) -> float | None:
    """
    Try to parse model output as JSON and read a numeric `prediction` field.
    Returns None when parsing fails or when `prediction` is missing/non-numeric.
    """
    if not text:
        return None

    def _to_prediction(parsed_obj) -> float | None:
        if not isinstance(parsed_obj, dict):
            return None
        value = parsed_obj.get("prediction")
        if isinstance(value, (int, float)) and not np.isnan(value):
            return float(value)
        if isinstance(value, str):
            numeric = _extract_numeric(value)
            if not np.isnan(numeric):
                return float(numeric)
        reasoning_value = parsed_obj.get("reasoning")
        if isinstance(reasoning_value, str):
            numeric = _extract_prediction_from_reasoning_text(reasoning_value)
            if numeric is not None:
                return float(numeric)
        return None

    candidate = text.strip()

    # Case 1: the whole content is valid JSON.
    try:
        pred = _to_prediction(json.loads(candidate))
        if pred is not None:
            return pred
    except (json.JSONDecodeError, TypeError):
        pass

    # Case 2: JSON wrapped in markdown fences.
    fence_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", candidate, re.DOTALL)
    if fence_match:
        try:
            pred = _to_prediction(json.loads(fence_match.group(1)))
            if pred is not None:
                return pred
        except (json.JSONDecodeError, TypeError):
            pass

    # Case 3: object-like substring.
    start = candidate.find("{")
    end = candidate.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            pred = _to_prediction(json.loads(candidate[start : end + 1]))
            if pred is not None:
                return pred
        except (json.JSONDecodeError, TypeError):
            pass

    # Case 4: key-based extraction when JSON is malformed/truncated.
    key_match = re.search(r'"prediction"\s*:\s*(-?\d+(?:\.\d+)?)', candidate)
    if key_match:
        return float(key_match.group(1))

    reasoning_pred = _extract_prediction_from_reasoning_text(candidate)
    if reasoning_pred is not None:
        return reasoning_pred

    return None


def _extract_joint_predictions_from_json_text(text: str | None) -> dict[str, float] | None:
    """
    Parse joint outputs like:
    {"Q1": 71, "Q2": 64}
    or
    {"Q1": {"reasoning": "...", "prediction": 71}, ...}
    and the analogous L1/L2/... forms.
    """
    if not text:
        return None

    def _to_joint_predictions(parsed_obj) -> dict[str, float] | None:
        if not isinstance(parsed_obj, dict):
            return None

        preds: dict[str, float] = {}
        for key, value in parsed_obj.items():
            if not isinstance(key, str) or not re.fullmatch(r"[QL]\d+", key):
                continue

            if isinstance(value, dict):
                pred_value = value.get("prediction")
            else:
                pred_value = value

            if isinstance(pred_value, (int, float)) and not np.isnan(pred_value):
                preds[key] = float(pred_value)
                continue
            if isinstance(pred_value, str):
                numeric = _extract_numeric(pred_value)
                if not np.isnan(numeric):
                    preds[key] = float(numeric)

        return preds or None

    candidate = text.strip()

    # Gemini occasionally emits doubled quotes around a JSON key, e.g.
    # ""prediction"": 85. Normalize that mild corruption before parsing.
    candidate = re.sub(r'""([A-Za-z][A-Za-z0-9_]*)""(?=\s*:)', r'"\1"', candidate)
    # Claude occasionally emits a stray ">" after the prediction key,
    # e.g. "prediction">87. Normalize that mild corruption too.
    candidate = re.sub(r'"prediction"\s*>\s*(-?\d+(?:\.\d+)?)', r'"prediction": \1', candidate)
    candidate = re.sub(r'"prediction"\s*=\s*(-?\d+(?:\.\d+)?)', r'"prediction": \1', candidate)

    try:
        preds = _to_joint_predictions(json.loads(candidate))
        if preds is not None:
            return preds
    except (json.JSONDecodeError, TypeError):
        pass

    fence_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", candidate, re.DOTALL)
    if fence_match:
        try:
            preds = _to_joint_predictions(json.loads(fence_match.group(1)))
            if preds is not None:
                return preds
        except (json.JSONDecodeError, TypeError):
            pass

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            preds = _to_joint_predictions(json.loads(candidate[start : end + 1]))
            if preds is not None:
                return preds
        except (json.JSONDecodeError, TypeError):
            pass

    # Case 4: recover per-question predictions from mildly malformed joint JSON
    # by scanning one Q/L block at a time. This also handles cases where Gemini
    # drops one intermediate question label but still emits the corresponding
    # prediction block before the next labeled question.
    key_matches = list(re.finditer(r'"([QL]\d+)"\s*:\s*\{', candidate))
    if key_matches:
        preds: dict[str, float] = {}
        pred_pattern = re.compile(
            r'"prediction"\s*[:=]\s*[^-0-9]{0,32}?(-?\d+(?:\.\d+)?)'
        )
        for idx, match in enumerate(key_matches):
            question = match.group(1)
            block_start = match.start()
            block_end = key_matches[idx + 1].start() if idx + 1 < len(key_matches) else len(candidate)
            block = candidate[block_start:block_end]

            expected_questions = [question]
            if idx + 1 < len(key_matches):
                next_question = key_matches[idx + 1].group(1)
                if question[0] == next_question[0]:
                    current_idx = int(question[1:])
                    next_idx = int(next_question[1:])
                    if next_idx > current_idx + 1:
                        expected_questions.extend(
                            f"{question[0]}{missing_idx}"
                            for missing_idx in range(current_idx + 1, next_idx)
                        )

            pred_matches = list(pred_pattern.finditer(block))
            if not pred_matches:
                pred_matches = list(
                    re.finditer(r'"prediction"\s*>\s*[^-0-9]{0,32}?(-?\d+(?:\.\d+)?)', block)
                )

            for expected_question, pred_match in zip(expected_questions, pred_matches):
                preds[expected_question] = float(pred_match.group(1))
        if preds:
            return preds

    return None


def _extract_numeric(text: str | None) -> float:
    if not text:
        return float("nan")
    cleaned = text.replace(",", " ")
    matches = re.findall(r"-?\d+(?:\.\d+)?", cleaned)
    if not matches:
        return float("nan")
    try:
        return float(matches[-1])
    except ValueError:
        return float("nan")


def _mean_from_logprobs(top_logprobs) -> float | None:
    entries = []
    for entry in top_logprobs:
        token = entry.get("token")
        if token is None:
            continue
        token = token.strip()
        if token.isdigit():
            entries.append([int(token), np.exp(entry["logprob"])])
    if not entries:
        return None
    probs = np.array(entries).T
    probs_norm = probs[1] / probs[1].sum()
    return float(probs[0] @ probs_norm)


def _parse_custom_id(custom_id: str) -> tuple[str, str] | None:
    """
    Support both:
    - OpenAI style: "<variation>/Q1" or "<variation>/L1"
    - Claude style: "<variation>_Q1" or "<variation>_L1"
    """
    match = re.match(r"^(.*)[/_]([QL]\d+)$", custom_id)
    if not match:
        return None
    return match.group(1), match.group(2)


def _normalize_joint_row_id(custom_id: str) -> str:
    match = re.match(r"^(?:validation|learning)/(.*)$", custom_id)
    if match:
        return match.group(1)
    return custom_id


def _sort_question_labels(labels: list[str]) -> list[str]:
    def _key(label: str) -> tuple[str, int | str]:
        match = re.match(r"^([A-Z]+)(\d+)$", str(label))
        if not match:
            return (str(label), str(label))
        return (match.group(1), int(match.group(2)))

    return sorted(labels, key=_key)


def _extract_openai_answer_and_logprobs(body: dict) -> tuple[str | None, list]:
    answer_text = None
    top_logprobs = []

    if body.get("object") == "chat.completion":
        choice = body.get("choices", [{}])[0]
        answer_text = choice.get("message", {}).get("content")
        choice_logprobs = choice.get("logprobs") or {}
        content_logprobs = choice_logprobs.get("content") or []
        if content_logprobs:
            top_logprobs = content_logprobs[0].get("top_logprobs", []) or []
    elif body.get("object") == "response":
        output = body.get("output") or []
        if output:
            content = output[-1].get("content") or []
            if content:
                answer_text = content[0].get("text")
                logprobs = content[0].get("logprobs") or []
                if logprobs:
                    top_logprobs = logprobs[0].get("top_logprobs", []) or []

    return answer_text, top_logprobs


def _extract_claude_answer_text(item: dict) -> str | None:
    result = item.get("result", {})
    if result.get("type") != "succeeded":
        return None

    message = result.get("message", {})
    content = message.get("content") or []
    text_chunks = [
        part.get("text", "")
        for part in content
        if isinstance(part, dict) and part.get("type") == "text"
    ]
    joined = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    return joined if joined else None


def _extract_gemini_answer_text(item: dict) -> str | None:
    response = item.get("response", {})
    if not isinstance(response, dict):
        return None

    candidates = response.get("candidates") or []
    if not candidates:
        return None

    first = candidates[0] if isinstance(candidates[0], dict) else {}
    content = first.get("content") or {}
    if not isinstance(content, dict):
        return None

    parts = content.get("parts") or []
    text_chunks = [
        part.get("text", "")
        for part in parts
        if isinstance(part, dict) and isinstance(part.get("text"), str)
    ]
    joined = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    return joined if joined else None


def _looks_like_reasoning_payload(text: str | None) -> bool:
    if not text:
        return False
    lower = text.lower()
    return "reasoning" in lower and (
        '"prediction"' in lower or "```json" in lower or "{" in lower
    )


def jsonl_to_dataframe(jsonl_path, verbose: bool = False, platform: str = "auto"):
    """
    Converts a list of dictionaries (parsed from a jsonl file) to a DataFrame.
    
    Each dictionary is expected to have:
      - a 'custom_id' key of the form "DOI/QX", where "DOI" is the row id and "QX" (X in 1..20) is the column name.
      - an answer string in item['choices'][0]['message']['content'] that ends with a float value,
        typically formatted like "Final Answer: |||||0.80|||||", but with possible variations.
    
    Returns a DataFrame with DOI as the index and columns "Q1" to "Q20", where each cell is the extracted float.

    Include the value of log probability, get the mean, and then generate the output
    """
    if platform not in {"auto", "openai", "claude", "gemini"}:
        raise ValueError("platform must be one of: auto, openai, claude, gemini")

    # Create an empty dictionary to hold data. Each key will be a row id.
    data = {}
    
    with open(jsonl_path, "r", encoding="utf-8") as jsonl_file:
        jsonl_list = [json.loads(line) for line in jsonl_file]  # Load each line as a dictionary

    for item in jsonl_list:
        custom_id = item.get("custom_id") or item.get("key", "")

        item_platform = platform
        if item_platform == "auto":
            if "result" in item:
                item_platform = "claude"
            elif isinstance(item.get("response"), dict) and "candidates" in item.get("response", {}):
                item_platform = "gemini"
            else:
                item_platform = "openai"

        answer_text = None
        mean = None

        if item_platform == "openai":
            body = item.get("response", {}).get("body", {})
            answer_text, top_lp = _extract_openai_answer_and_logprobs(body)
            if top_lp:
                try:
                    mean = _mean_from_logprobs(top_lp)
                except Exception:
                    mean = None
        elif item_platform == "claude":
            answer_text = _extract_claude_answer_text(item)
        elif item_platform == "gemini":
            answer_text = _extract_gemini_answer_text(item)

        if answer_text is None:
            if verbose:
                print(f"Skipping item due to missing answer content for: {custom_id}")
            continue

        parsed_custom_id = _parse_custom_id(custom_id)
        if parsed_custom_id is None:
            joint_preds = _extract_joint_predictions_from_json_text(answer_text)
            if joint_preds is None:
                if verbose:
                    print(f"Skipping item with invalid custom_id format: {custom_id}")
                continue
            row_id = _normalize_joint_row_id(custom_id)
            if row_id not in data:
                data[row_id] = {}
            data[row_id].update(joint_preds)
            continue

        synthesis, question = parsed_custom_id

        if mean is None:
            json_pred = _extract_prediction_from_json_text(answer_text)
            if json_pred is not None:
                mean = json_pred
            else:
                # For reasoning payloads, avoid treating random in-text numbers as predictions.
                if _looks_like_reasoning_payload(answer_text):
                    mean = np.nan
                else:
                    mean = _extract_numeric(answer_text)
            if np.isnan(mean) and verbose:
                print(f"error: {custom_id}")
        
        # Insert the float into our data dictionary.
        if synthesis not in data:
            data[synthesis] = {}
        data[synthesis][question] = mean#ans_float

    # Create a DataFrame with DOI as the index.
    df = pd.DataFrame.from_dict(data, orient='index')

    # some values may use percentage. divide by 100 if that is the case
    #df = df.map(lambda x: x/100 if x > 2 else x)
    
    labels = [col for col in df.columns if isinstance(col, str)]
    prefixes = {
        match.group(1)
        for col in labels
        if (match := re.match(r"^([A-Z]+)(\d+)$", col))
    }
    if len(prefixes) == 1:
        prefix = next(iter(prefixes))
        nums = [
            int(match.group(2))
            for col in labels
            if (match := re.match(rf"^({re.escape(prefix)})(\d+)$", col))
        ]
        if nums:
            ordered_cols = [f"{prefix}{i}" for i in range(1, max(nums) + 1)]
            df = df.reindex(columns=ordered_cols)
        else:
            df = df.reindex(columns=_sort_question_labels(labels))
    else:
        df = df.reindex(columns=_sort_question_labels(labels))

    return df
