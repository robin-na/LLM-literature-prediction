"""
Run Claude (Sonnet 4.6) extraction on the 25-paper out-of-sample test set,
matching the 34-column schema used by human_out_of_sample.csv.

Usage:
    python benchmarks/test_set_eval/extract_claude.py

Outputs:
    evaluator/inputs/llm/claude_out_of_sample.csv
    benchmarks/test_set_eval/raw_claude_responses.json  (per-paper raw JSON)
"""
from __future__ import annotations

import asyncio
import csv
import json
import os
import re
import sys
from pathlib import Path

import anthropic
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
HUMAN_CSV = REPO_ROOT / "evaluator" / "inputs" / "human" / "human_out_of_sample.csv"
PAPERS_DIR = REPO_ROOT / "PGG_papers" / "papers"
OUT_CSV = REPO_ROOT / "evaluator" / "inputs" / "llm" / "claude_out_of_sample.csv"
RAW_JSON = Path(__file__).parent / "raw_claude_responses.json"
WOS_CSV = REPO_ROOT / "PGG_papers" / "WoS_251031_eligible.csv"

MODEL = "claude-sonnet-4-6"
MAX_CONCURRENT = 5  # Tier-1 rate limits
MAX_TOKENS = 4096


def load_dotenv() -> None:
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


SCHEMA_COLUMNS = [
    "Filename", "Title of the Paper", "Topic", "Experiment Name",
    "Controled_Or_Observational", "Granularity",
    "Independent Variables", "Dependent Variables", "Dependent Variables Definitions",
    "Empirical", "Lab_Or_Field", "Simulation", "Analytical", "Review",
    "CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_allOrNothing",
    "CONFIG_defaultContribProp", "CONFIG_MPCR",
    "CONFIG_chat", "CONFIG_showOtherSummaries",
    "CONFIG_showPunishmentId", "CONFIG_showRewardId", "CONFIG_showNRounds",
    "CONFIG_punishmentExists", "CONFIG_punishmentCost", "CONFIG_punishmentTech",
    "CONFIG_rewardExists", "CONFIG_rewardCost", "CONFIG_rewardTech",
    "DV_contributionRate", "DV_efficiencyReported", "DV_efficiency", "Misc",
]

SYSTEM_PROMPT = """You are extracting structured experimental parameters from PGG (public-goods-game) papers.

Return ONE JSON object per paper with a "conditions" array. Each condition object covers ONE between-subjects treatment arm. Within-subjects manipulations stay inside one condition (note them in Misc).

Field rules:
- Empirical: "1" = involves human participants; "0" = pure theory/simulation/analytical.
- If Empirical = "0", set Lab_Or_Field and every CONFIG_* field to "N/A".
- Controled_Or_Observational: "1" = controlled experiment with manipulation; "0" = observational; "N/A" if non-empirical. (Note the single-`l` typo — keep it.)
- Lab_Or_Field: "1" = field experiment; "0" = lab or online.
- Simulation, Analytical, Review: "1" if the paper IS that type; "0" otherwise (mutually exclusive in practice).
- CONFIG_playerCount, CONFIG_numRounds, CONFIG_endowment, CONFIG_MPCR: integer or float as string. Use "N/R" if reported numerically but value is unstated; "N/A" if concept doesn't apply.
- CONFIG_allOrNothing: "1" = continuous contributions; "0" = binary (counterintuitive — note this!).
- CONFIG_defaultContribProp: "0" = opt-in (private default), "1" = opt-out (public default).
- CONFIG_chat: "1" = explicitly enabled; "0" = explicitly disabled; "N/A" if not mentioned (silence → N/A, not 0).
- CONFIG_showOtherSummaries: "1" if individual payoffs visible to others; "0" otherwise.
- CONFIG_showNRounds: "1" only if round counter explicitly displayed during play. "N/A" otherwise (do NOT infer from fixed rounds).
- CONFIG_punishmentExists, CONFIG_rewardExists: "1" / "0" / "N/A". Silence → "N/A".
- CONFIG_punishmentCost / Tech: cost = coins spent per unit; tech = target loss per coin spent. "N/A" if no mechanism; "N/R" if exists but rate not stated.
- CONFIG_showPunishmentId / showRewardId: "1" = identity revealed; "0" = anonymous; "N/A" = no mechanism.
- Independent Variables, Dependent Variables: INTEGER COUNTS (as strings). E.g. "2", "3". "N/A" if non-empirical.
- DV_contributionRate, DV_efficiencyReported, DV_efficiency: free text. Often "N/A".
- Topic: a 1-2 sentence summary of what THIS condition is testing.
- Experiment Name: short label like "Punishment treatment - Study 1".
- Misc: edge cases, payoff equations, within-subjects manipulations, anything notable.

Return ONLY the JSON object — no prose, no markdown fences."""


USER_TEMPLATE = """Extract structured parameters for paper: {paper_id}

Title (from metadata): {title}

Schema for each condition (return as JSON, all values are strings):
{{
  "conditions": [
    {{
      "Topic": "...",
      "Experiment Name": "...",
      "Controled_Or_Observational": "0|1|N/A",
      "Independent Variables": "<integer count or N/A>",
      "Dependent Variables": "<integer count or N/A>",
      "Dependent Variables Definitions": "...",
      "Empirical": "0|1",
      "Lab_Or_Field": "0|1|N/A",
      "Simulation": "0|1",
      "Analytical": "0|1",
      "Review": "0|1",
      "CONFIG_playerCount": "...",
      "CONFIG_numRounds": "...",
      "CONFIG_allOrNothing": "0|1|N/A",
      "CONFIG_defaultContribProp": "0|1|N/A",
      "CONFIG_MPCR": "...",
      "CONFIG_chat": "0|1|N/A",
      "CONFIG_showOtherSummaries": "0|1|N/A",
      "CONFIG_showPunishmentId": "0|1|N/A",
      "CONFIG_showRewardId": "0|1|N/A",
      "CONFIG_showNRounds": "1|N/A",
      "CONFIG_punishmentExists": "0|1|N/A",
      "CONFIG_punishmentCost": "...",
      "CONFIG_punishmentTech": "...",
      "CONFIG_rewardExists": "0|1|N/A",
      "CONFIG_rewardCost": "...",
      "CONFIG_rewardTech": "...",
      "DV_contributionRate": "...",
      "DV_efficiencyReported": "...",
      "DV_efficiency": "...",
      "Misc": "..."
    }}
    // ...one object per between-subjects condition
  ]
}}

Paper Markdown:
---
{paper_md}
---"""


JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def parse_response(text: str) -> dict:
    """Tolerant JSON extraction from model output."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = JSON_RE.search(text)
        if not m:
            raise
        return json.loads(m.group(0))


async def extract_one(
    client: anthropic.AsyncAnthropic,
    sem: asyncio.Semaphore,
    paper_id: str,
    title: str,
    paper_md: str,
) -> tuple[str, dict | None, str | None]:
    user_msg = USER_TEMPLATE.format(paper_id=paper_id, title=title, paper_md=paper_md)
    async with sem:
        try:
            resp = await client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            text = "".join(b.text for b in resp.content if b.type == "text")
            return paper_id, parse_response(text), None
        except Exception as e:
            return paper_id, None, f"{type(e).__name__}: {e}"


def load_titles() -> dict[str, str]:
    if not WOS_CSV.exists():
        return {}
    titles = {}
    with open(WOS_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            cid = r.get("custom_id", "").removesuffix(".md")
            if cid:
                titles[cid] = r.get("Article Title", "")
    return titles


async def main() -> None:
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    paper_ids = sorted({r["Filename"] for _, r in pd.read_csv(HUMAN_CSV).iterrows()})
    titles = load_titles()

    # Load paper Markdowns
    jobs = []
    for pid in paper_ids:
        md_path = PAPERS_DIR / f"{pid}.md"
        if not md_path.exists():
            print(f"  ⚠ missing markdown: {pid}", file=sys.stderr)
            continue
        md = md_path.read_text(encoding="utf-8")
        # Cap to avoid context overflow on monster papers
        if len(md) > 120_000:
            md = md[:120_000] + "\n\n[...truncated for length...]"
        jobs.append((pid, titles.get(pid, ""), md))

    print(f"Extracting from {len(jobs)} papers with {MODEL} (concurrent={MAX_CONCURRENT})...")

    client = anthropic.AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    sem = asyncio.Semaphore(MAX_CONCURRENT)
    tasks = [extract_one(client, sem, pid, title, md) for pid, title, md in jobs]

    results: dict[str, dict] = {}
    errors: dict[str, str] = {}
    for coro in asyncio.as_completed(tasks):
        pid, data, err = await coro
        if err:
            errors[pid] = err
            print(f"  ✗ {pid}: {err}", file=sys.stderr)
        else:
            results[pid] = data
            n_cond = len(data.get("conditions", []))
            print(f"  ✓ {pid} ({n_cond} cond)")

    # Save raw responses for inspection
    RAW_JSON.write_text(json.dumps({"results": results, "errors": errors}, indent=2))

    # Flatten to CSV
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for pid in paper_ids:
        data = results.get(pid)
        if not data:
            continue
        title = titles.get(pid, "")
        for i, cond in enumerate(data.get("conditions", [])):
            row = {c: "" for c in SCHEMA_COLUMNS}
            row["Filename"] = pid
            row["Title of the Paper"] = title
            row["Granularity"] = f"Condition {i}"
            for k in SCHEMA_COLUMNS:
                if k in cond:
                    row[k] = cond[k]
            rows.append(row)

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SCHEMA_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print(f"\nWrote {len(rows)} rows from {len(results)} papers → {OUT_CSV}")
    if errors:
        print(f"  {len(errors)} paper(s) failed; see {RAW_JSON}")


if __name__ == "__main__":
    asyncio.run(main())
