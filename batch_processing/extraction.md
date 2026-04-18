# Extraction Usage

## Prerequisites: Download Paper Markdown Files

Papers must be available locally as `.md` files in `PGG_papers/papers/` before running extraction. Download them from Google Drive:

```bash
python batch_processing/download_papers_md.py
```

For a new batch of papers, provide a text file with one PDF path per line:

```bash
python batch_processing/download_papers_md.py --pdf-list my_new_papers.txt
```

See `CLAUDE.md` for first-time Google Drive credential setup.

---

Use `batch_processing/extract_papers.py` as the **main human-facing entrypoint**.

It supports three clear modes:

- `simple`: one-shot extraction for all fields
- `hybrid`: one-shot extraction plus agentic overrides for key fields
- `agentic-field`: debug one field on one paper

Before running commands:

```bash
set -a && source .env && set +a
source .venv_agentic/bin/activate
```

## 1. Simple Extraction (real-time)

> **Prefer Batch API** (section 1b) for large runs — same output, ~50% cheaper, results within 24h.


Use this when you want the cheapest and fastest extraction path.

```bash
python batch_processing/extract_papers.py simple \
  --paper-dir PGG_papers/papers \
  --paper-ids 10.1007_s10645-008-9094-1 \
  --output-xlsx batch_processing/output_xlsx/simple_extraction.xlsx
```

What it does:

- runs one model call per paper
- extracts all fields in a single JSON response
- writes an Excel workbook with an `extractions` sheet

## 1b. Simple Extraction via Batch API (~50% cheaper)

The Batch API bundles all requests into one JSONL file, submits it to OpenAI, and returns results within 24h at half the real-time price. Use this for any run with more than ~10 papers.

**Step 1 — Submit** (prints a batch ID, takes seconds):
```bash
python batch_processing/extract_papers.py batch-submit \
  --paper-dir PGG_papers/papers \
  --paper-ids $(ls PGG_papers/papers/*.md | xargs -n1 basename | sed 's/\.md$//') \
  --save-jsonl batch_processing/inputs/batch_input_simple.jsonl
```

**Step 2 — Check status** (run until you see `completed`):
```bash
python batch_processing/extract_papers.py batch-status <batch_id>
```

**Step 3 — Collect results** (once status is `completed`):
```bash
python batch_processing/extract_papers.py batch-collect <batch_id> \
  --output-xlsx batch_processing/output_xlsx/simple_batch_200papers.xlsx \
  --save-jsonl batch_processing/inputs/batch_output_simple.jsonl
```

The output workbook is identical to what `simple` produces.

---

## 2. Hybrid Extraction

Use this when you want the normal production workflow.

```bash
python batch_processing/extract_papers.py hybrid \
  --paper-dir PGG_papers/papers \
  --paper-ids 10.1007_s10645-008-9094-1 \
  --output-xlsx batch_processing/output_xlsx/hybrid_extraction.xlsx
```

What it does:

- runs simple extraction first for all fields
- reruns selected fields with the agentic system
- in `v2` mode, merges agentic values only when the pipeline decision is `accept`
- writes an Excel workbook with `extractions` and `agentic_meta`

Useful options:

- `--agentic-version v2` (default): recommended efficient workflow
- `--agentic-version v1`: legacy always-critic workflow
- `--max-tool-rounds 12`: increase tool budget if a field gets stuck
- `--min-review-confidence 0.9`: stricter merge threshold

## 3. Single-Field Agentic Debugging

Use this when you want to inspect one field on one paper.

```bash
python batch_processing/extract_papers.py agentic-field \
  --field CONFIG_MPCR \
  --paper-id 10.1007_s10645-008-9094-1 \
  --paper-dir PGG_papers/papers \
  --agentic-version v2 \
  --final-only
```

What it does:

- runs only one field
- prints either the full workflow payload or only the final JSON
- is useful for debugging prompts, tools, and critic behavior

## Legacy Entry Points

These still work, but they are no longer the recommended first commands:

- `batch_processing/run_hybrid_agentic_extraction.py`
- `batch_processing/agentic_extract.py`

Prefer `batch_processing/extract_papers.py` for everyday use.
