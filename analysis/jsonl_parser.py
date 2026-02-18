import json
import re

import numpy as np
import pandas as pd


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


def jsonl_to_dataframe(jsonl_path, verbose: bool = False):
    """
    Converts a list of dictionaries (parsed from a jsonl file) to a DataFrame.
    
    Each dictionary is expected to have:
      - a 'custom_id' key of the form "DOI/QX", where "DOI" is the row id and "QX" (X in 1..20) is the column name.
      - an answer string in item['choices'][0]['message']['content'] that ends with a float value,
        typically formatted like "Final Answer: |||||0.80|||||", but with possible variations.
    
    Returns a DataFrame with DOI as the index and columns "Q1" to "Q20", where each cell is the extracted float.

    Include the value of log probability, get the mean, and then generate the output
    """
    # Create an empty dictionary to hold data. Each key will be a DOI.
    data = {}
    
    with open(jsonl_path, "r", encoding="utf-8") as jsonl_file:
        jsonl_list = [json.loads(line) for line in jsonl_file]  # Load each line as a dictionary

    for item in jsonl_list:
        custom_id = item.get('custom_id', '')
        # Expect custom_id to have two parts separated by '/'
        try:
            synthesis, question = custom_id.split('/')
        except ValueError:
            if verbose:
                print(f"Skipping item with invalid custom_id format: {custom_id}")
            continue

        body = item['response']['body']
        
        # Extract the answer text
        try:
            if body['object'] == 'chat.completion':
                answer_text = body['choices'][0]['message']['content']
            elif body['object'] == 'response':
                answer_text = body['output'][-1]['content'][0]['text']               
        except (IndexError, KeyError):
            if verbose:
                print(f"Skipping item due to missing answer content for: {custom_id}")
            continue
        
        # extract the answer text 
        try:
            if body['object'] == 'chat.completion':
                top_lp = body['choices'][0]['logprobs']['content'][0]['top_logprobs']
            elif body['object'] == 'response':
                top_lp = body['output'][-1]['content'][0]['logprobs'][0]['top_logprobs']
            else:
                top_lp = []
            mean = _mean_from_logprobs(top_lp)
        except Exception:
            mean = None

        if mean is None:
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
    
    # Ensure the DataFrame has exactly 20 columns (Q1 to Q20), even if some are missing.
    ordered_cols = [f"Q{i}" for i in range(1, 21)]
    df = df.reindex(columns=ordered_cols)
    
    return df
