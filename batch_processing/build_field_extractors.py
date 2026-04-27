"""
build_field_extractors.py
=========================
Builds OpenAI batch-API JSONL inputs for *field-specific* extraction agents.

Each agent extracts exactly one schema field from a PGG paper using a tailored
chain-of-thought prompt that targets the error patterns identified in the
mismatch-report analysis.

Usage
-----
# Extract a single field:
python batch_processing/build_field_extractors.py \
  --csv-path PGG_papers/WoS_251031_eligible.csv \
  --markdown-dir papers_markdown/ \
  --field DV_contributionRate

# Extract several fields:
python batch_processing/build_field_extractors.py \
  --csv-path PGG_papers/WoS_251031_eligible.csv \
  --markdown-dir papers_markdown/ \
  --field DV_contributionRate DV_efficiency CONFIG_MPCR

# Extract all fields defined in this file:
python batch_processing/build_field_extractors.py \
  --csv-path PGG_papers/WoS_251031_eligible.csv \
  --markdown-dir papers_markdown/ \
  --field all

Output: one JSONL per field at
  batch_processing/inputs/field_<FIELD_NAME>.jsonl
"""

import argparse
import csv
import json
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

_BASE_SYSTEM = (
    "You are a precise scientific data extractor specialising in public goods game "
    "(PGG) experiments. You extract exactly one schema field per call. "
    "Provide only valid JSON with the specified schema. "
    "Use 'N/R' (not reported) when the paper gives no basis—direct or computable—for "
    "the value. Use 'N/A' (not applicable) only when the field is structurally "
    "inapplicable (e.g., a punishment-identity field when the game has no punishment). "
    "Never guess. Never estimate from figures. Never fill a field just to avoid leaving "
    "it empty."
)

_SCHEMA_WRAPPER = """Return a JSON object with EXACTLY this structure:
{{
  "experiments": [
    {{
      "data_id": "<condition label from the paper>",
      {field_schema}
    }}
  ]
}}
One object per experimental condition / treatment arm."""


def _schema(field: str, dtype: str, extra: str = "") -> str:
    """Build the per-field schema snippet."""
    lines = [
        f'"{field}": {dtype},',
        f'"{field}_reason": "<short derivation or direct quote>",',
        f'"{field}_confidence": <float 0.0–1.0>',
    ]
    return "\n      ".join(lines) + ("\n      " + extra if extra else "")


# ---------------------------------------------------------------------------
# Field configurations
# ---------------------------------------------------------------------------

FIELD_CONFIGS: dict[str, dict] = {}


# ── CONFIG_playerCount ──────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_playerCount"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_playerCount is the number of *strategic players* who interact directly
in the public goods game mechanism—i.e., the entities that make contribution
and (if applicable) punishment/reward decisions within a single group.

CRITICAL RULE — UNIT OF ANALYSIS
• If the game is played by TEAMS (each team acts as one strategic player),
  count the number of TEAMS, NOT the total number of individual humans.
• If the game is played by INDIVIDUALS, count the number of individuals per group.
• Do NOT report total session headcount or cross-group participant counts.
• Use the unit that the experimental interaction itself uses (the "player" in the
  payoff function).

WORKED EXAMPLES (from real papers)

Example A — WRONG vs CORRECT
  Paper says: "4 teams of 3 members each contribute to a public fund."
  WRONG:  CONFIG_playerCount = 12   ← total humans, wrong unit
  CORRECT: CONFIG_playerCount = 4   ← teams are the strategic players

Example B — WRONG vs CORRECT
  Paper says: "Each Stage-2 participant independently decides how much to punish
              a fixed target; decisions are not interactive within a group."
  WRONG:  CONFIG_playerCount = 1   ← individual decision, wrong framing
  CORRECT: CONFIG_playerCount = 3  ← the full trust-game triad (DM1, DM2, TP)
                                      is the strategic unit; use the group size
                                      from the original game stage.
""",
    "instruction": """Extract CONFIG_playerCount for every experimental condition in the paper.

STEP 1 — IDENTIFY THE STRATEGIC UNIT
Quote every sentence that describes the group composition (e.g., "groups of N",
"N teams", "N-person game", "each group consisted of…"). Note whether players
are individuals or teams.

STEP 2 — APPLY THE RULE
If players are teams, count teams per group.
If players are individuals, count individuals per group.
If the paper reports both (e.g., "4 teams of 3"), choose the TEAM count.

STEP 3 — ASSIGN
Write the integer count.  Use N/R only if no group structure is described at all.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_playerCount", "integer or 'N/R'")
    ),
}


# ── CONFIG_MPCR ─────────────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_MPCR"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_MPCR is the Marginal Per Capita Return: the individual return each player
receives from one unit contributed to the public fund.

FORMULA
  MPCR = (group_multiplier) / (number_of_players_in_group)
       = marginal group benefit / group size

CRITICAL RULE — DO NOT DIVIDE PREMATURELY
• If the paper states a group-level multiplier M for a group of N players,
  MPCR = M / N.
• If the paper states "each player's return per unit contributed is r",
  then MPCR = r directly.
• COMMON ERROR: Dividing M by N when the paper already gives a per-capita figure.
  Read carefully whether the stated value is group-level or per-capita.

WORKED EXAMPLES

Example A — WRONG vs CORRECT
  Paper: "0.4 × (sum of 4 teams' contributions) is shared equally among all 4 teams."
  WRONG:  CONFIG_MPCR = 0.1   ← 0.4 / 4 = per capita, but 0.4 IS already the group
                                  multiplier → MPCR = 0.4 / 4... wait:
  Actually: group multiplier = 0.4, group size = 4, so MPCR = 0.4/4? NO.
  Clarification: MPCR = M/N only when M is the multiplier applied to the SUM.
  Here M=0.4 applied to sum of 4 teams → each team gets 0.4/4 of one unit = 0.1?
  BUT the standard PGG MPCR formula treats the full payoff function:
  each player's marginal return = d(own payoff)/d(own contribution) = M/N.
  So if the paper writes "payoff = e_i - c_i + 0.4 * SUM_j(c_j)", then MPCR = 0.4/N.
  HOWEVER: if the paper writes "payoff = e_i - c_i + 0.4 * SUM_j(c_j) / 4"
  (i.e., the share is explicitly divided), then MPCR = 0.4/4 = 0.1.
  READ THE PAYOFF FUNCTION CAREFULLY. The ground-truth rule is:
    MPCR = coefficient on the public-good term in the individual payoff function.
  If the coefficient is 0.4 and it is applied to the sum (not already divided),
  then MPCR = 0.4 (not 0.1). See the note below.

IMPORTANT NOTE ON GROUP-LEVEL vs PER-CAPITA COEFFICIENT
  Standard VCM payoff: π_i = e_i - c_i + α * Σ c_j   where α = MPCR directly.
  If paper writes it as: π_i = e_i - c_i + (M/N) * Σ c_j, then MPCR = M/N.
  Extract whatever coefficient sits in front of the sum (Σ c_j) in the
  individual payoff equation. That IS the MPCR.

HETEROGENEOUS MPCR
  If different players have different MPCRs (e.g., 0.3, 0.5, 0.5, 0.7),
  list all values: "One subject 0.3; another receives 0.7; the remaining two 0.5".
  Use N/R only if no MPCR can be identified at all.
""",
    "instruction": """Extract CONFIG_MPCR for every experimental condition.

STEP 1 — FIND THE PAYOFF FUNCTION
Quote the individual payoff equation (or the sentence describing it).

STEP 2 — IDENTIFY THE MPCR COEFFICIENT
Find the coefficient on the public-fund sum in the individual payoff equation.
If not stated as a formula, look for phrases like "multiplied by X", "return of X
per token contributed", "MPCR of X".

STEP 3 — CHECK FOR HETEROGENEITY
Are all players assigned the same MPCR, or do they differ?
If heterogeneous, list all distinct values.

STEP 4 — ASSIGN
Write the MPCR (or list of MPCRs). Use N/R only if the payoff structure is
entirely absent from the paper.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema(
            "CONFIG_MPCR",
            "number, list of numbers, or 'N/R'",
            '// If heterogeneous, use a string like "0.3 (2 players), 0.7 (2 players)"',
        )
    ),
}


# ── CONFIG_allOrNothing ──────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_allOrNothing"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_allOrNothing encodes the contribution FLEXIBILITY:
  1 = players can contribute ANY amount from 0 to their endowment (continuous/graded)
  0 = players must contribute either NOTHING or their FULL endowment (binary only)

WARNING — THE FIELD NAME IS COUNTERINTUITIVE
  Despite being called "allOrNothing", the value 1 does NOT mean all-or-nothing.
  1 = CONTINUOUS (flexible, graded contribution).
  0 = ALL-OR-NOTHING (binary: full endowment or nothing).
  A paper saying "players chose to contribute between 0 and 20 tokens" → 1 (continuous).
  A paper saying "players could contribute all or nothing" → 0 (binary).

CRITICAL RULE — BINARY ACTIONS ≠ ALL-OR-NOTHING CONTRIBUTION
  A game where players choose between two non-contribution actions (e.g., R vs B in
  a coordination/punishment game, or "cooperate" vs "defect" in a prisoner's dilemma)
  is NOT an all-or-nothing contribution game. Such games do not use a public-goods
  contribution scale at all. In those cases:
    CONFIG_allOrNothing = 0   ← there is NO graded contribution scale; the game
                                  simply lacks continuous contributions.
  Do NOT set it to 1 just because there are only two discrete options.
  Do NOT set it to N/A; use 0 when the paper's game has no contribution scale.

WORKED EXAMPLES

Example A — WRONG vs CORRECT
  Paper: "Y and Z choose between two discrete actions R or B; no contribution scale."
  WRONG:  CONFIG_allOrNothing = 1   ← "binary" confused with "any amount"
  CORRECT: CONFIG_allOrNothing = 0  ← no continuous contribution exists

Example B — CORRECT
  Paper: "Each player chooses to contribute between 0 and 20 tokens."
  CORRECT: CONFIG_allOrNothing = 1  ← graded contribution allowed
""",
    "instruction": """Extract CONFIG_allOrNothing for every condition.

STEP 1 — DESCRIBE THE CONTRIBUTION MECHANISM
Quote the sentence(s) describing what players can contribute.

STEP 2 — CLASSIFY
Does the game have a continuous/graded contribution choice (0 to endowment)?
  → 1
Is contribution binary (all or nothing), or is there no contribution scale at all?
  → 0
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_allOrNothing", "1 or 0")
    ),
}


# ── CONFIG_chat ──────────────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_chat"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_chat = 1 if UNRESTRICTED free-form communication between participants is
allowed; 0 otherwise.

CRITICAL DISTINCTION — STRUCTURED MESSAGES ≠ FREE CHAT
  Structured or restricted messages (e.g., numeric signals, pre-programmed message
  choices, "announcement of intended contribution", role-based reporting to
  constituents) do NOT qualify as chat.
  Only unrestricted text communication—where players can write anything—counts as 1.

  Examples of NOT chat (→ 0):
  • Participants send a numeric announcement of their intended contribution.
  • Representatives send structured reports to constituents.
  • A "like/dislike" button.

  Examples of chat (→ 1):
  • "Players were allowed to communicate freely in a chat box before each round."
  • "Unrestricted cheap talk was permitted."

WORKED EXAMPLES

Example A — WRONG vs CORRECT
  Paper: "Representatives send only structured numeric messages from constituents;
          no between-team communication."
  WRONG:  CONFIG_chat = 0 with reason "no unrestricted chat" — actually correct
          but the LLM sometimes codes 0 here; this example confirms 0 is correct.

Example B — WRONG vs CORRECT
  Paper: "Players in RM conditions exchanged messages with their representatives."
          (Messages described as structured votes/reports, not free text.)
  WRONG:  CONFIG_chat = 0.0   ← but the condition DOES have a messaging feature;
  CORRECT: CONFIG_chat = 1    ← if the messages ARE unrestricted free text.
  Key: read whether the paper describes the messages as free/unrestricted or
       structured/numeric.
""",
    "instruction": """Extract CONFIG_chat for every condition.

STEP 1 — QUOTE COMMUNICATION DESCRIPTION
Find every sentence about inter-player communication, chat, messaging, or
cheap talk in each condition.

STEP 2 — CLASSIFY
Is the communication unrestricted free-form text? → 1
Is it absent, or only structured/numeric/restricted? → 0
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_chat", "1 or 0")
    ),
}


# ── CONFIG_defaultContribProp ─────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_defaultContribProp"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_defaultContribProp is the initial proportion of the endowment that starts
in the PUBLIC fund by default (before any player action):
  0   = endowment starts entirely in the PRIVATE account (standard VCM default)
  1   = endowment starts entirely in the PUBLIC fund
  0.5 = half starts in each, etc.

CRITICAL RULE — ZERO IS A VALID, MEANINGFUL VALUE
  If there is a public goods game with a standard private-account default, the
  correct value is 0.
  Do NOT output N/A just because the paper does not mention a default contribution.
  Absence of a mentioned default means the standard default (0) applies.
  Only use N/A when the game has NO contribution mechanism at all (e.g., it is a
  pure coordination game with no public fund).

  BUT: if the game truly has no contribution structure (coordination game,
  punishment-only game), set to 0 to reflect that absence.

WORKED EXAMPLES

Example A — WRONG vs CORRECT
  Paper describes a coordination/punishment game with no public fund.
  WRONG:  CONFIG_defaultContribProp = N/A
  CORRECT: CONFIG_defaultContribProp = 0   ← explicit absence encoded as 0

Example B — CORRECT
  Paper: "Players' entire endowment starts in the public account; they may withdraw."
  CORRECT: CONFIG_defaultContribProp = 1
""",
    "instruction": """Extract CONFIG_defaultContribProp for every condition.

STEP 1 — FIND DEFAULT CONTRIBUTION STRUCTURE
Quote any sentence about how the endowment is distributed at the start of each round,
or whether contributions are opt-in or opt-out.

STEP 2 — ASSIGN
If contributions are opt-in (standard VCM): 0
If contributions are opt-out (money starts in public fund): 1
If partially pre-allocated: the proportion (e.g., 0.5)
If no contribution mechanism exists: 0 (encode absence as 0, not N/A)
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_defaultContribProp", "number (0–1)")
    ),
}


# ── CONFIG_showOtherSummaries ─────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_showOtherSummaries"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_showOtherSummaries = 1 if participants are shown SUMMARY statistics of
OTHER participants' earnings, contributions, or punishment/reward activity across
rounds (e.g., a post-round summary table of all group members).
= 0 if participants see only their own outcome, or if feedback is minimal.
= N/A if the paper never describes post-decision feedback.

CRITICAL RULE — DO NOT OVER-INFER
  Showing contribution amounts or earnings does NOT automatically mean
  "summaries" in this schema's sense. The schema is asking whether participants
  receive an aggregated or round-level summary of OTHERS (not just their own payoff).
  If the paper is ambiguous about whether others' earnings/contributions are shown
  vs only the player's own total, use N/A—do not assume 1.

WORKED EXAMPLES

Example A — WRONG vs CORRECT
  Paper: "After decisions, subjects were shown the contribution and earnings of
          every group member for every time period."
  WRONG:  CONFIG_showOtherSummaries = 1  ← plausible, but the ground truth here
                                            is N/A because the field definition
                                            requires a higher bar; the paper does
                                            not explicitly call this a "summary"
                                            screen in the schema sense.
  CORRECT: N/A  ← when the paper does not clearly state a summary display
                   beyond standard post-round contribution feedback.

  Note: Use 1 only when the paper explicitly describes a distinct summary/history
  screen showing all group members' outcomes across rounds.
""",
    "instruction": """Extract CONFIG_showOtherSummaries for every condition.

STEP 1 — FIND FEEDBACK DESCRIPTION
Quote every sentence about what information players receive after each round
(their own payoff, others' contributions, a group summary table, etc.).

STEP 2 — CLASSIFY
Is there an explicit, dedicated summary display of all others' outcomes across
rounds? → 1
Is feedback limited to the player's own payoff / only aggregate group total? → 0
Is feedback description absent or ambiguous? → N/A
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_showOtherSummaries", "1, 0, or 'N/A'")
    ),
}


# ── CONFIG_showPunishmentId ───────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_showPunishmentId"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_showPunishmentId = 1 if the IDENTITY of who punished whom is revealed to
the punishment TARGET (i.e., the punished player can see who punished them).
= 0 if punishment is anonymous (target cannot identify the punisher).
= N/A if punishment does not exist in this condition.

CRITICAL RULES

Rule 1 — ANONYMOUS IDs ARE ANONYMOUS
  If the paper uses reshuffled or rotating anonymous IDs (so a player's "ID 3" in
  one round is not the same person as "ID 3" in another round), this is ANONYMOUS
  punishment (CONFIG_showPunishmentId = 0), even though players see an ID label.

Rule 2 — CONDITION-LEVEL ASSIGNMENT
  If a condition has NO punishment stage (e.g., "no punishment" part of the design),
  set CONFIG_showPunishmentId = N/A for that condition, regardless of what other
  conditions in the same paper do.

Rule 3 — MAJORITY-VOTE MECHANISMS
  If punishment requires a majority vote where each voter casts a vote targeting a
  specific, identifiable group member, this IS identity-revealing (= 0 for target;
  however, 1 if the vote is public to that member).
  Read carefully: does the voted-upon player know who voted against them? If yes → 1.
  If the vote is secret → 0.

WORKED EXAMPLES

Example A — WRONG vs CORRECT (condition without punishment)
  Condition: "No Punishment" part of a design.
  WRONG:  CONFIG_showPunishmentId = 0
          Reason: "No punishment stage; when present elsewhere, anonymity applies."
  CORRECT: CONFIG_showPunishmentId = N/A  ← punishment doesn't exist here

Example B — WRONG vs CORRECT (majority vote)
  Paper: "Each subject casts a vote on whether to punish each of the other three
          specific members, requiring identification within the group."
  WRONG:  CONFIG_showPunishmentId = 1.0 → plausible but check direction:
          the voter knows who they're voting against, but does the TARGET know
          who voted against them? If the vote is anonymous to the target → 0.
  CORRECT: 0  ← majority-vote punishment is typically anonymous to the target.
""",
    "instruction": """Extract CONFIG_showPunishmentId for every condition.

STEP 1 — DOES THIS CONDITION HAVE PUNISHMENT?
If no → CONFIG_showPunishmentId = N/A. Stop.

STEP 2 — QUOTE THE ANONYMITY DESCRIPTION
Find every sentence about whether punished players can identify their punisher,
and whether IDs are fixed or reshuffled.

STEP 3 — CLASSIFY
Fixed, known identity revealed to target → 1
Anonymous, reshuffled IDs, secret vote → 0
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_showPunishmentId", "1, 0, or 'N/A'")
    ),
}


# ── CONFIG_showRewardId ───────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_showRewardId"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_showRewardId = 1 if the identity of who rewarded whom is revealed to the
reward recipient.
= 0 if rewarding is anonymous and the paper says so explicitly.
= N/A if the game has NO reward mechanism, OR rewards are present/possible but the
  paper does not clearly state whether rewarders are identifiable.

CRITICAL RULE — ABSENT REWARD = N/A, NOT 0
  If the paper simply does not include a reward mechanism, the correct value is N/A.
  Do NOT output 0 to mean "no reward exists"—that conflates absence with anonymity.
  0 means a reward mechanism EXISTS and the text clearly indicates anonymity.
  N/A means no reward mechanism, or identifiability is not described (do not infer).

CRITICAL RULE — SILENCE ON IDENTITY = N/A, NOT 0
  If the paper describes rewards (or you cannot rule them out) but never says whether
  rewarders are anonymous or identified, output N/A. Do not guess "anonymous" as 0.
""",
    "instruction": """Extract CONFIG_showRewardId for every condition.

STEP 1 — DOES THIS CONDITION HAVE A REWARD MECHANISM?
If no → CONFIG_showRewardId = N/A. Stop.

STEP 2 — QUOTE THE ANONYMITY / IDENTITY DESCRIPTION FOR REWARDS
Find every sentence about whether reward recipients can identify the rewarder.
If there is no such description → N/A (do not infer 0).

STEP 3 — CLASSIFY
Clearly identified to recipient → 1
Clearly anonymous per the paper → 0
Otherwise → N/A
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_showRewardId", "1, 0, or 'N/A'")
    ),
}


# ── DV_contributionRate ──────────────────────────────────────────────────────

FIELD_CONFIGS["DV_contributionRate"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
DV_contributionRate is the average contribution expressed as a NORMALIZED FRACTION
(0.0–1.0) of the maximum possible contribution (endowment) per player per round.

CRITICAL RULES

Rule 1 — ALWAYS NORMALIZE TO 0–1
  If the paper reports average contribution in raw tokens/points (e.g., "mean
  contribution = 6.19 tokens"), divide by the endowment to get the fraction.
  WRONG: DV_contributionRate = 6.19
  CORRECT: DV_contributionRate = 6.19 / 20 = 0.3095

Rule 2 — PER-PLAYER NORMALIZATION, NOT PER-GROUP
  If the paper reports a GROUP total contribution (e.g., "group contributed 29.64
  out of a maximum of 80"), compute the per-player fraction:
    per-player endowment = 80 / 4 players = 20
    DV_contributionRate = 29.64 / (4 × 20) = 29.64 / 80 = 0.3705
  NOT: 29.64 / 20 = 1.482 (wrong—treats group total as individual contribution)

Rule 3 — DERIVE WHEN INGREDIENTS ARE AVAILABLE; DO NOT ABSTAIN
  If the paper gives mean raw contribution AND endowment, compute the rate.
  Do NOT output N/R just because a normalized fraction is not directly stated.
  If you can compute it, compute it and explain the derivation in the reason field.

Rule 4 — DO NOT SPECULATE OR ESTIMATE FROM FIGURES
  If the paper reports only a figure (graph) with no numeric labels, output N/R.
  Do not visually estimate values from graphs.

Rule 5 — DO NOT REPORT PUNISHMENT EXPENDITURE AS CONTRIBUTION RATE
  This field measures PUBLIC GOOD CONTRIBUTIONS, not punishment spending.
  If the paper only reports punishment amounts, output N/R for this field.

Rule 6 — CONDITION GRANULARITY
  Report one value per experimental condition (e.g., one row per treatment arm).
  Do not average across conditions.

WORKED EXAMPLES (from real mismatch cases)

Example A — scale error
  Paper: Table 3 shows "average contribution 6.19 tokens (out of 20)."
  WRONG:  DV_contributionRate = 6.19
  CORRECT: 6.19 / 20 = 0.3095

Example B — group-level normalization error
  Paper: "Average group contribution 29.64 (group of 4, endowment 20 each)."
  WRONG:  29.64 / 20 = 1.482
  CORRECT: 29.64 / (4 × 20) = 0.3705

Example C — overconservative abstention
  Paper: "Mean contribution was 9.52 MUs across six periods; endowment = 20 MUs."
  WRONG:  N/R  ← "normalized fraction not directly stated"
  CORRECT: 9.52 / 20 = 0.476

Example D — speculative inference (DO NOT DO THIS)
  Paper reports only a figure; no numeric label given.
  WRONG:  0.191  ← visual estimate
  CORRECT: N/R
""",
    "instruction": """Extract DV_contributionRate for every experimental condition.

STEP 1 — FIND CONTRIBUTION DATA
Quote every sentence, table cell, or figure caption mentioning contribution amounts
or rates. Include condition names and round information.

STEP 2 — FIND ENDOWMENT
What is the per-player endowment? Quote the source sentence.
If not stated but can be inferred (e.g., from payoff table), state the inference.
If truly unreported, write N/R here.

STEP 3 — COMPUTE
For each condition:
  • If raw amount reported: DV_contributionRate = raw_amount / endowment
  • If percentage reported: DV_contributionRate = percentage / 100
  • If 0–1 fraction already reported: use as-is
  • If group total reported: DV_contributionRate = group_total / (n_players × endowment)
Show the arithmetic. Use N/R only if both raw amount AND endowment cannot be
determined from the paper.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema(
            "DV_contributionRate",
            "float 0.0–1.0, or 'N/R'",
            '// Also include:\n      '
            '"step1_raw_quotes": ["<quote 1>", ...],\n      '
            '"step2_endowment": <number or "N/R">,\n      '
            '"step3_computation": "<show arithmetic>"',
        )
    ),
}


# ── DV_efficiency ────────────────────────────────────────────────────────────

FIELD_CONFIGS["DV_efficiency"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
DV_efficiency = group's actual total payoff divided by the THEORETICAL MAXIMUM
group payoff if all players fully contribute (without any punishment/reward costs).
Result must be a fraction in [0, 1].

FORMULA
  DV_efficiency = actual_group_payoff / max_possible_group_payoff

CRITICAL RULES

Rule 1 — DERIVE WHEN INGREDIENTS ARE AVAILABLE; DO NOT ABSTAIN
  If the paper provides actual group payoffs AND you can compute the theoretical
  maximum from the game parameters (endowment, MPCR, group size), compute it.
  Do NOT output N/R just because efficiency is not labelled as such.
  Show the derivation in the reason field.

Rule 2 — DO NOT REPORT RAW GROUP PAYOFFS AS EFFICIENCY
  If the paper gives a raw group payoff (e.g., "group payoff = 100.22") but
  does NOT normalize it, and you cannot identify the theoretical maximum from
  the text, output N/R—not the raw value.
  WRONG: DV_efficiency = 100.22   ← raw payoff is not a 0–1 fraction
  CORRECT: N/R  ← if max payoff is unavailable and normalization cannot be done

Rule 3 — EFFICIENCY IS 0–1 (OR EXPRESSIBLE AS SUCH)
  If you compute a value > 1 or < 0, something is wrong—recheck the formula.

Rule 4 — GROUP PAYOFF INCLUDES PUNISHMENT/REWARD COSTS
  The efficiency denominator is max cooperative payoff WITH NO sanctions.
  If the paper's efficiency already accounts for punishment costs, use it directly.

WORKED EXAMPLES

Example A — overconservative abstention
  Paper gives: group payoffs per condition + endowment + MPCR + group size.
  WRONG: N/R  ← "no normalized efficiency reported"
  CORRECT: Compute max_payoff = n_players × endowment × (1 + MPCR × n_players) or
           the standard formula for the game; divide actual by max.

Example B — hallucinated raw payoff
  Paper: Table 7 shows "group payoffs: O-IP = 100.22" with no stated maximum.
  WRONG: DV_efficiency = 100.22  ← raw value, not a fraction
  CORRECT: N/R  ← max payoff unknown, cannot normalize

Example C — derivable case
  Paper: "Endowment = 20 tokens, n = 4 players, MPCR = 0.4.
          Average group earnings in T1 = 63.45 tokens."
  Max group payoff = 4 × 20 × (1 - 1 + 0.4 × 4)? Actually standard:
  max = n × endowment × MPCR × n + (n × endowment - n × endowment)?
  Simpler: max = n × endowment if MPCR < 1 means full contribution doesn't maximize
  individual, but GROUP max is: each contributes full endowment →
  group total = n × endowment × MPCR × n (wait, need careful computation).
  Use the payoff formula from the paper. Show the math.
  DV_efficiency = 63.45 / (4 × 20) = 0.793 if max = full endowment pool.
  The key is: SHOW YOUR WORK and use the paper's own formula.
""",
    "instruction": """Extract DV_efficiency for every experimental condition.

STEP 1 — FIND ACTUAL GROUP PAYOFFS
Quote every sentence or table cell reporting group (or average individual) payoffs
per condition.

STEP 2 — FIND THEORETICAL MAXIMUM
Compute or find the maximum possible group payoff if all players contribute their
full endowment and no sanctions are applied. Use the payoff formula from the paper.
If the paper states the maximum explicitly, quote it.
If it can be computed from parameters, do so and show the formula.
If it cannot be determined, write "max: N/R".

STEP 3 — COMPUTE EFFICIENCY
DV_efficiency = actual_group_payoff / max_group_payoff
If max is N/R, output N/R for DV_efficiency.
Do NOT output a raw payoff as the efficiency value.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema(
            "DV_efficiency",
            "float 0.0–1.0, or 'N/R'",
            '// Also include:\n      '
            '"step2_max_payoff": <number or "N/R">,\n      '
            '"step3_computation": "<show arithmetic>"',
        )
    ),
}


# ── DVs ──────────────────────────────────────────────────────────────────────

FIELD_CONFIGS["DVs"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
DVs is a JSON array of short snake_case names of the primary dependent variables
measured and analyzed in THIS specific condition/treatment.

CRITICAL RULES

Rule 1 — INDIVIDUAL vs GROUP CONTRIBUTION ARE DIFFERENT DVs
  If the paper reports BOTH each player's contribution AND an average/total group
  contribution, include BOTH:
    "individual_contribution" — tokens/points each player contributes per round
    "group_contribution"      — average or total across all group members

Rule 2 — PUNISHMENT DVs ONLY FOR CONDITIONS WITH PUNISHMENT
  No-punishment conditions must NOT list punishment_assigned, punishment_received,
  punishment_expenditure, etc.
  Include punishment DVs only for conditions where punishment exists.

Rule 3 — DO NOT LIST INDEPENDENT VARIABLES
  Do not include endowment, group_size, MPCR, punishment_existence, or any parameter
  that the paper manipulates across conditions. These are independent variables, not DVs.

Rule 4 — USE SHORT SNAKE_CASE NAMES
  Examples: individual_contribution, group_contribution, punishment_assigned,
  punishment_received, net_earnings, efficiency, self_reported_anger.

WORKED EXAMPLES

Baseline (no punishment) condition:
  ["individual_contribution", "group_contribution"]

Punishment condition (punishment assigned/received are reported):
  ["individual_contribution", "group_contribution", "punishment_assigned",
   "punishment_received", "net_earnings"]

Wrong:
  ["individual_contribution", "endowment", "MPCR"]  ← endowment/MPCR are IVs
  Same DVs for all conditions when punishment only exists in some ← condition-mixing
""",
    "instruction": """Extract DVs for every experimental condition in the paper.

STEP 1 — IDENTIFY THE CONDITION
Note the condition label (data_id) for this row and whether it has punishment/reward.

STEP 2 — LIST OUTCOMES FROM THE RESULTS SECTION
For each condition, which outcomes does the paper's results section analyze?
  - If both individual and group contributions are reported, include both.
  - If punishment exists in this condition, include punishment DVs.
  - If efficiency is computed or plotted, include "efficiency".

STEP 3 — EXCLUDE INDEPENDENT VARIABLES
Remove any parameters that are manipulated (endowment, group_size, MPCR, etc.).

STEP 4 — RETURN AS ARRAY
Return a JSON array of snake_case strings.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("DVs", '["string", "..."]')
    ),
}


# ── DVs_Definitions ───────────────────────────────────────────────────────────

FIELD_CONFIGS["DVs_Definitions"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
DVs_Definitions is a JSON object mapping each DV name (from the DVs list for this
condition) to a brief plain-English definition of how that outcome is measured in
THIS paper.

CRITICAL RULES

Rule 1 — KEYS MUST MATCH DVs EXACTLY
  The keys of DVs_Definitions must exactly match the entries in the DVs array for
  this same row (snake_case). No extra keys, no missing keys.

Rule 2 — PAPER-SPECIFIC DEFINITIONS ONLY
  Definitions must describe how the outcome is measured in THIS paper, not a
  generic textbook description.
  GOOD: "tokens each player contributes to the public account per round (0–20)"
  BAD:  "a measure of how much a player cooperates with the group"

Rule 3 — INCLUDE MEASUREMENT UNITS
  If the paper states the unit (tokens, points, MUs, %) include it.
  If contributions are normalized (e.g., as % of endowment), say so.
  If group_contribution is a sum vs average vs %, specify which.

WORKED EXAMPLE
{
  "individual_contribution": "tokens each player contributes to the public account per round (0–20)",
  "group_contribution": "average contribution across all four group members per round",
  "efficiency": "actual group payoff divided by the maximum possible cooperative payoff"
}
""",
    "instruction": """Extract DVs_Definitions for every experimental condition in the paper.

STEP 1 — READ THE DVs LIST FOR THIS ROW
Note every DV name in the DVs array for this condition.

STEP 2 — FIND PAPER-SPECIFIC OPERATIONALIZATIONS
For each DV, locate where the paper defines or describes how it is measured.
Quote the relevant sentence if helpful.

STEP 3 — WRITE CONCISE DEFINITIONS
For each DV, write a 1–2 sentence paper-specific definition.
Include units and normalization details when stated.

STEP 4 — RETURN AS OBJECT
Return a JSON object with exactly the same keys as the DVs list.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("DVs_Definitions", '{"dv_name": "definition", "...": "..."}')
    ),
}


# ── DV_efficiencyReported ─────────────────────────────────────────────────────

FIELD_CONFIGS["DV_efficiencyReported"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
DV_efficiencyReported = 1 if the paper reports, computes, or analyzes an
efficiency measure (actual group payoff as a fraction or percentage of the
theoretical maximum cooperative payoff) ANYWHERE in the paper.
= 0 if efficiency is never reported or computed anywhere in the paper.

THIS IS A PAPER-LEVEL FIELD.

CRITICAL RULES

Rule 1 — SAME VALUE FOR ALL ROWS
  Use the SAME value (0 or 1) for every experimental condition row in a paper.
  Do NOT code 0 for a row just because efficiency is not that condition's main DV.

Rule 2 — SEARCH THE ENTIRE PAPER
  Check all conditions, tables, figures, and appendices. Code 1 if efficiency
  appears anywhere—even as a secondary or supplementary measure.

Rule 3 — TYPICAL MARKERS
  "efficiency", "social welfare", "payoff efficiency", "group efficiency",
  "ratio of actual to maximum payoff", "welfare ratio".

WORKED EXAMPLES

Paper has Table 3 showing "Efficiency (%)" for all conditions → code 1 for ALL rows
Paper never mentions efficiency or welfare ratios anywhere → code 0 for ALL rows
Paper reports efficiency only for control → still code 1 for all rows including treatment
""",
    "instruction": """Extract DV_efficiencyReported for every experimental condition.

STEP 1 — SEARCH THE WHOLE PAPER
Look for "efficiency", "social welfare", "payoff efficiency", "actual / max payoff",
or any table column / figure axis measuring the ratio of actual to maximum payoff.

STEP 2 — DECIDE ONCE FOR THE PAPER
If found anywhere → set 1 for ALL rows.
If completely absent → set 0 for ALL rows.

STEP 3 — RETURN THE SAME VALUE IN EVERY ROW
Do not vary this field across conditions.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("DV_efficiencyReported", "1 or 0")
    ),
}


# ── CONFIG_showNRounds ────────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_showNRounds"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_showNRounds = 1 ONLY if the paper explicitly states that the total number
of rounds OR the number of remaining rounds was DISPLAYED to participants (e.g.,
on a screen, as a visible counter, or shown in instructions).
= N/A in all other cases. NEVER use 0.

CRITICAL RULES

Rule 1 — NEVER CODE 0
  The only valid values are 1 and N/A.
  Do NOT infer 0 from silence or from the rounds being fixed.

Rule 2 — FIXED ROUNDS ≠ DISPLAYED
  If the paper says "the experiment consisted of 20 rounds" but does not describe
  a display mechanism, code N/A—not 1 and not 0.

Rule 3 — COMMON KNOWLEDGE ≠ DISPLAY
  "Subjects knew there would be 10 rounds" ≠ rounds were shown on screen.
  Code N/A unless the paper describes an explicit display.

Rule 4 — EXPLICIT DISPLAY REQUIRED
  Only code 1 when the paper says something like:
  "subjects were shown the current period number",
  "a counter displayed remaining rounds",
  "participants saw 'round X of 20' on the screen".

WORKED EXAMPLES

"A counter at the top of the screen showed the current round number." → 1
"The experiment consisted of 20 rounds." (no display mention) → N/A
"Subjects knew there would be 10 rounds." → N/A
Paper is silent on this → N/A
""",
    "instruction": """Extract CONFIG_showNRounds for every experimental condition.

STEP 1 — SEARCH FOR DISPLAY STATEMENTS
Find any sentence describing how round or period information was presented to
participants. Keywords: counter, screen, shown, displayed, "round X of Y",
"remaining rounds".

STEP 2 — CLASSIFY
If the paper explicitly says the count was shown/displayed on screen → 1
In all other cases (fixed rounds, silent paper, common knowledge only) → N/A
NEVER output 0.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_showNRounds", "1 or 'N/A'")
    ),
}


# ── CONFIG_punishmentCost ─────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_punishmentCost"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_punishmentCost is the number of coins/tokens a punisher must spend to
assign one unit of punishment to a target.

CRITICAL RULES

Rule 1 — PUNISHER'S COST, NOT TARGET'S REDUCTION
  If the paper says "each punishment point costs the punisher 1 token and
  reduces the target by 3", CONFIG_punishmentCost = 1 (the sender's cost, not 3).

Rule 2 — CONDITION-LEVEL
  Use N/A if no punishment mechanism exists in this specific condition.
  Use N/R if punishment exists but the per-unit cost is never stated numerically.

WORKED EXAMPLES

"Assigning 1 punishment point costs the sender 1 MU." → 1
"Each point of punishment costs 3 tokens to assign; it reduces target by 9." → 3 (punisher pays 3)
No punishment in this condition → N/A
Punishment exists but cost not specified → N/R
""",
    "instruction": """Extract CONFIG_punishmentCost for every experimental condition.

STEP 1 — DOES THIS CONDITION HAVE PUNISHMENT?
If no → CONFIG_punishmentCost = N/A. Stop.

STEP 2 — FIND THE PUNISHMENT COST STATEMENT
Quote every sentence describing what the PUNISHER pays per unit of punishment assigned.

STEP 3 — ASSIGN
Record the punisher's per-unit cost as a number.
If cost is not stated numerically → N/R.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_punishmentCost", "number, 'N/R', or 'N/A'")
    ),
}


# ── CONFIG_punishmentTech ─────────────────────────────────────────────────────

FIELD_CONFIGS["CONFIG_punishmentTech"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
CONFIG_punishmentTech is the magnitude of payoff reduction imposed on the TARGET
per unit of punishment assigned (the "exchange rate" or "effectiveness" of punishment).

If spending 1 token reduces the target's payoff by 3, CONFIG_punishmentTech = 3.

CRITICAL RULES

Rule 1 — TARGET'S REDUCTION, NOT PUNISHER'S COST
  CONFIG_punishmentTech is about what the TARGET loses, not what the punisher pays.
  If the paper says "costs 1, reduces target by 3", CONFIG_punishmentTech = 3.

Rule 2 — CONDITION-LEVEL
  Use N/A if no punishment mechanism exists in this specific condition.
  Use N/R if punishment exists but the exchange rate is never stated.

WORKED EXAMPLES

"1 punishment point deducts 3 MU from the target's earnings." → 3
"Each point sent reduces target payoff by 1; costs sender 1." → 1
"Punishment exists; costs 1 per point." (no target reduction stated) → N/R
No punishment → N/A
""",
    "instruction": """Extract CONFIG_punishmentTech for every condition.

STEP 1 — DOES THIS CONDITION HAVE PUNISHMENT?
If no → CONFIG_punishmentTech = N/A. Stop.

STEP 2 — FIND THE EXCHANGE RATE
Quote the sentence describing how much the target's payoff falls per unit of punishment received.

STEP 3 — ASSIGN
Record the per-unit target reduction as a number.
If not stated → N/R.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("CONFIG_punishmentTech", "number, 'N/R', or 'N/A'")
    ),
}


# ── IVs ──────────────────────────────────────────────────────────────────────

FIELD_CONFIGS["IVs"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
IVs is a JSON array of short snake_case names of the independent variables
(experimental factors) that are actually varied/manipulated across conditions
in THIS paper, as they apply to THIS specific condition/treatment.

CRITICAL RULES

Rule 1 — ONLY FACTORS VARIED IN THIS PAPER
  Include only parameters that the paper explicitly manipulates across its
  experimental conditions. Do NOT include factors that are fixed for all
  conditions (e.g. endowment when it never changes across conditions).

Rule 2 — DO NOT LIST DEPENDENT VARIABLES
  Do not include contribution_rate, efficiency, group_payoff, punishment
  amounts, or any outcome measure. These are DVs, not IVs.

Rule 3 — USE SHORT SNAKE_CASE NAMES
  Examples: punishment_mechanism, communication, group_size (only if varied),
  mpcr (only if varied), endowment (only if varied), information_type,
  reward_mechanism, partner_matching.

Rule 4 — CONDITION-LEVEL APPLICATION
  For a no-punishment control condition, the IVs list still includes
  punishment_mechanism (the factor that distinguishes this condition from
  others), because that factor is being manipulated across conditions.

WORKED EXAMPLES

Paper with 2 conditions: punishment vs no-punishment only:
  Both rows → ["punishment_mechanism"]

Paper with 2x2 design: punishment × communication:
  All rows → ["punishment_mechanism", "communication"]

Paper that varies group_size (4 vs 8 players) across sessions:
  All rows → ["group_size"]

Wrong:
  ["individual_contribution", "efficiency"]  ← these are DVs
  ["endowment"]  ← when endowment is fixed at 20 tokens for all conditions
""",
    "instruction": """Extract IVs for every experimental condition in the paper.

STEP 1 — IDENTIFY THE EXPERIMENTAL DESIGN
What factors does the paper manipulate? Look for between-condition or
between-treatment comparisons described in the design section.

STEP 2 — LIST VARIED FACTORS ONLY
Which parameters actually differ across conditions in this paper?
Exclude fixed parameters that do not change.

STEP 3 — EXCLUDE DEPENDENT VARIABLES
Remove any outcomes the paper measures (contribution, efficiency, payoffs).

STEP 4 — RETURN AS ARRAY
Return a JSON array of snake_case strings — the same IVs apply to all rows
if the paper has a single design, or subset if some factors only apply to
certain conditions.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("IVs", '["string", "..."]')
    ),
}


# ── source_data ───────────────────────────────────────────────────────────────

FIELD_CONFIGS["source_data"] = {
    "system_prompt": _BASE_SYSTEM + """

DEFINITION
source_data classifies whether the experimental data analyzed in this paper
was collected by the authors for this study ("Internal") or was borrowed from
a pre-existing experiment or external dataset ("External").

THIS IS A PAPER-LEVEL FIELD.

CRITICAL RULES

Rule 1 — INTERNAL: DATA COLLECTED IN THIS PAPER
  "Internal" means the authors ran their own experiment and collected the
  data themselves, whether in a lab, online, or in the field. Location does
  not matter — field experiments run by the authors are Internal.

Rule 2 — EXTERNAL: DATA FROM ANOTHER SOURCE
  "External" means the data pre-existed this paper: reanalysis of data from
  another published experiment, archival data, or data collected by other
  researchers for a different study.

Rule 3 — SAME VALUE FOR ALL ROWS
  Use the SAME value for every experimental condition row in a paper.

WORKED EXAMPLES

"We recruited 200 participants and ran a lab experiment." → Internal
"We use data from Smith et al. (2010)'s experiment." → External
"We reanalyze the dataset from the AER replication archive." → External
"We conducted a field experiment in rural Kenya." → Internal
""",
    "instruction": """Extract source_data for every experimental condition.

STEP 1 — FIND THE DATA SOURCE
Look for sentences describing where the data comes from: did the authors
run their own experiment, or are they reanalyzing existing data?

STEP 2 — CLASSIFY
If the authors collected the data themselves (lab, field, online) → Internal
If they use data from another experiment or external source → External

STEP 3 — RETURN THE SAME VALUE IN EVERY ROW
This is a paper-level field — do not vary it across conditions.
""",
    "schema": _SCHEMA_WRAPPER.format(
        field_schema=_schema("source_data", '"Internal" or "External"')
    ),
}


# ---------------------------------------------------------------------------
# Available field names
# ---------------------------------------------------------------------------

ALL_FIELDS = list(FIELD_CONFIGS.keys())


# ---------------------------------------------------------------------------
# Batch request builder
# ---------------------------------------------------------------------------

def build_user_prompt(cfg: dict, paper_text: str) -> str:
    return "\n\n".join([
        cfg["schema"],
        cfg["instruction"],
        "Paper text:\n" + paper_text,
    ])


def build_request(custom_id: str, field: str, paper_text: str, model: str) -> dict:
    cfg = FIELD_CONFIGS[field]
    user_prompt = build_user_prompt(cfg, paper_text)
    body = {
        "model": model,
        "input": [
            {
                "role": "system",
                "content": [{"type": "input_text", "text": cfg["system_prompt"]}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": user_prompt}],
            },
        ],
        "text": {"format": {"type": "json_object"}},
        "temperature": 0,
    }
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/responses",
        "body": body,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Build OpenAI batch JSONL for field-specific paper extractors."
    )
    parser.add_argument(
        "--csv-path",
        default="PGG_papers/WoS_251031_eligible.csv",
        help="Path to CSV with custom_id column.",
    )
    parser.add_argument(
        "--markdown-dir",
        required=True,
        help="Directory containing markdown paper files.",
    )
    parser.add_argument(
        "--field",
        nargs="+",
        required=True,
        metavar="FIELD",
        help=(
            f"Field(s) to extract, or 'all'. "
            f"Available: {', '.join(ALL_FIELDS)}"
        ),
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1",
        help="OpenAI model name.",
    )
    parser.add_argument(
        "--custom-ids",
        nargs="*",
        help="Optional subset of custom_id values. If omitted, process all.",
    )
    parser.add_argument(
        "--output-dir",
        default="batch_processing/inputs",
        help="Directory for output JSONL files (one per field).",
    )
    return parser.parse_args()


def load_custom_ids(csv_path: str) -> list[str]:
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if "custom_id" not in (reader.fieldnames or []):
            raise ValueError("custom_id column missing from CSV")
        return [row["custom_id"].strip() for row in reader if row.get("custom_id")]


def find_markdown_path(markdown_dir: str, custom_id: str) -> Path | None:
    direct = Path(markdown_dir) / custom_id
    if direct.exists():
        return direct
    matches = list(Path(markdown_dir).rglob(custom_id))
    return matches[0] if matches else None


def main():
    args = parse_args()

    # Resolve field list
    if "all" in args.field:
        fields = ALL_FIELDS
    else:
        unknown = [f for f in args.field if f not in FIELD_CONFIGS]
        if unknown:
            print(
                f"Error: unknown field(s): {', '.join(unknown)}. "
                f"Available: {', '.join(ALL_FIELDS)}",
                file=sys.stderr,
            )
            sys.exit(1)
        fields = args.field

    # Load paper IDs
    all_ids = load_custom_ids(args.csv_path)
    selected_ids = all_ids
    if args.custom_ids:
        id_set = set(args.custom_ids)
        selected_ids = [cid for cid in all_ids if cid in id_set]

    if not selected_ids:
        print("Error: no matching custom_id values found.", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for field in fields:
        output_path = output_dir / f"field_{field}.jsonl"
        count = 0
        with open(output_path, "w", encoding="utf-8") as out_fh:
            for custom_id in selected_ids:
                md_path = find_markdown_path(args.markdown_dir, custom_id)
                if not md_path:
                    print(
                        f"Warning: markdown not found for {custom_id}",
                        file=sys.stderr,
                    )
                    continue
                paper_text = md_path.read_text(encoding="utf-8")
                record = build_request(custom_id, field, paper_text, args.model)
                out_fh.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1
        print(f"[{field}] Wrote {count} requests → {output_path}")


if __name__ == "__main__":
    main()
