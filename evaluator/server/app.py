"""
Local review server (FastAPI).

This server is the persistence layer for the review UI:

- Serves the generated UI (`outputs/comparison.html`) at `/`
- Accepts review actions (e.g., changing a row classification) at `POST /events`
- Stores those actions as an append-only CSV event log at `data/review_events.csv`
- Exposes the current override state at `GET /state` by materializing the event log
"""

from __future__ import annotations

import csv
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from utils.consensus import (
    build_alignment,
    build_consensus_state,
    export_ground_truth_csv as write_ground_truth_export,
    load_human_datasets,
    read_consensus_events,
)
from utils.finalize import FinalizePaths, materialize_final_dataset, write_final_dataset
from utils.paths import (
    COMPARISON_HTML,
    CONSENSUS_EVENTS_CSV,
    CONSENSUS_HTML,
    GROUND_TRUTH_CSV,
    HUMAN_DATASETS_DIR,
    LLM_DATASET_CSV,
    REVIEW_EVENTS_CSV,
    STATE_DIR,
)
from utils.review_state import build_classification_overrides, build_paper_notes


class ReviewEventIn(BaseModel):
    """Schema for a single review event posted by the UI."""

    review_session_id: str = Field(default="default")
    reviewer_id: str = Field(default="anonymous")

    key: str
    action: str = Field(default="set_classification")

    old_classification: Optional[str] = None
    new_classification: Optional[str] = None

    old_value: Optional[str] = None
    new_value: Optional[str] = None

    note: Optional[str] = None


class ConsensusEventIn(BaseModel):
    """Schema for a single consensus event posted by Stage 1 UI."""

    consensus_session_id: str = Field(default="default")
    reviewer_id: str = Field(default="anonymous")

    key: str
    action: str = Field(default="set_ground_truth")

    old_value: Optional[str] = None
    new_value: Optional[str] = None
    source_annotator: Optional[str] = None
    note: Optional[str] = None


def utc_now_iso() -> str:
    """Return current UTC time in ISO8601 format (seconds precision)."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_events_header(path: Path, fieldnames: list[str]) -> None:
    """Create an empty CSV file with a header row if it doesn't exist yet."""
    if path.exists() and path.stat().st_size > 0:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


EVENT_FIELDNAMES = [
    "event_id",
    "timestamp",
    "review_session_id",
    "reviewer_id",
    "key",
    "action",
    "old_classification",
    "new_classification",
    "old_value",
    "new_value",
    "note",
]


CONSENSUS_EVENT_FIELDNAMES = [
    "event_id",
    "timestamp",
    "consensus_session_id",
    "reviewer_id",
    "key",
    "action",
    "old_value",
    "new_value",
    "source_annotator",
    "note",
]


def append_event(event: ReviewEventIn) -> dict[str, Any]:
    """Append a single event row to the CSV event log and return the written row."""
    ensure_events_header(REVIEW_EVENTS_CSV, EVENT_FIELDNAMES)

    row: dict[str, Any] = {
        "event_id": str(uuid.uuid4()),
        "timestamp": utc_now_iso(),
        "review_session_id": event.review_session_id,
        "reviewer_id": event.reviewer_id,
        "key": event.key,
        "action": event.action,
        "old_classification": event.old_classification or "",
        "new_classification": event.new_classification or "",
        "old_value": event.old_value or "",
        "new_value": event.new_value or "",
        "note": event.note or "",
    }

    with REVIEW_EVENTS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EVENT_FIELDNAMES)
        writer.writerow(row)

    return row


def append_consensus_event(event: ConsensusEventIn) -> dict[str, Any]:
    """Append a single event row to the consensus event log and return it."""
    ensure_events_header(CONSENSUS_EVENTS_CSV, CONSENSUS_EVENT_FIELDNAMES)

    row: dict[str, Any] = {
        "event_id": str(uuid.uuid4()),
        "timestamp": utc_now_iso(),
        "consensus_session_id": event.consensus_session_id,
        "reviewer_id": event.reviewer_id,
        "key": event.key,
        "action": event.action,
        "old_value": event.old_value or "",
        "new_value": event.new_value or "",
        "source_annotator": event.source_annotator or "",
        "note": event.note or "",
    }
    with CONSENSUS_EVENTS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CONSENSUS_EVENT_FIELDNAMES)
        writer.writerow(row)
    return row


def read_events(session_id: str) -> list[dict[str, str]]:
    """Read all events for a given session id from the CSV event log."""
    if not REVIEW_EVENTS_CSV.exists() or REVIEW_EVENTS_CSV.stat().st_size == 0:
        return []
    with REVIEW_EVENTS_CSV.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [dict(r) for r in reader if r.get("review_session_id") == session_id]
    return rows


def stage2_ground_truth_csv() -> Path:
    """Resolve the configured ground-truth CSV path for Stage 2."""
    raw = os.environ.get("STAGE2_GROUND_TRUTH_CSV", "").strip()
    if not raw:
        return GROUND_TRUTH_CSV
    return Path(raw).expanduser().resolve()


app = FastAPI(title="RA Review Server", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint used for smoke tests."""
    return {"status": "ok"}


@app.get("/")
def index():
    """Serve the generated comparison UI HTML."""
    if not COMPARISON_HTML.exists():
        raise HTTPException(
            status_code=404,
            detail="comparison.html not found. Run `python3 -m scripts.generate_comparison` first.",
        )
    return FileResponse(COMPARISON_HTML)


@app.post("/events")
def post_event(event: ReviewEventIn):
    """Persist a single UI action (event) to the CSV event log."""
    row = append_event(event)
    return JSONResponse({"ok": True, "event": row})


@app.get("/state")
def get_state(review_session_id: str = "default", reviewer_id: str = "anonymous") -> dict[str, Any]:
    """Return the materialized state for a review session.

    Notes are returned per reviewer (using the provided reviewer_id).
    """
    events = read_events(review_session_id)
    overrides = build_classification_overrides(events)
    notes = build_paper_notes(events, reviewer_id=reviewer_id)
    return {
        "review_session_id": review_session_id,
        "overrides": overrides,
        "notes": notes,
        "reviewer_id": reviewer_id,
        "n_events": len(events),
    }


@app.get("/export/overrides.csv")
def export_overrides(review_session_id: str = "default"):
    """Export the current override state as a CSV file (derived from events)."""
    events = read_events(review_session_id)
    overrides = build_classification_overrides(events)

    out_path = STATE_DIR / f"review_overrides__{review_session_id}.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["review_session_id", "key", "classification"])
        writer.writeheader()
        for key, cls in overrides.items():
            writer.writerow({"review_session_id": review_session_id, "key": key, "classification": cls})

    return FileResponse(out_path)


@app.get("/export/final_dataset.csv")
def export_final_dataset(review_session_id: str = "default", reviewer_id: str = "anonymous"):
    """Export a materialized final dataset CSV for analysis."""
    out_path = STATE_DIR / f"final_review_dataset__{review_session_id}__{reviewer_id}.csv"
    ground_truth_csv = stage2_ground_truth_csv()
    rows = materialize_final_dataset(
        FinalizePaths(
            human_csv=ground_truth_csv,
            llm_csv=LLM_DATASET_CSV,
            review_events_csv=REVIEW_EVENTS_CSV,
            out_csv=out_path,
        ),
        review_session_id=review_session_id,
        reviewer_id=reviewer_id,
    )
    write_final_dataset(rows, out_path)
    return FileResponse(out_path)


@app.get("/consensus")
def consensus_index():
    """Serve the generated consensus UI HTML."""
    if not CONSENSUS_HTML.exists():
        raise HTTPException(
            status_code=404,
            detail="consensus.html not found. Run `python3 main.py consensus` first.",
        )
    return FileResponse(CONSENSUS_HTML)


@app.post("/consensus/events")
def post_consensus_event(event: ConsensusEventIn):
    """Persist one Stage 1 consensus event."""
    row = append_consensus_event(event)
    return JSONResponse({"ok": True, "event": row})


@app.get("/consensus/state")
def get_consensus_state(consensus_session_id: str = "default", reviewer_id: str = "anonymous") -> dict[str, Any]:
    """Materialize current consensus selections from the append-only log."""
    _ = reviewer_id
    datasets = load_human_datasets(HUMAN_DATASETS_DIR)
    annotators, aligned_rows, cells = build_alignment(datasets)
    events = read_consensus_events(consensus_session_id)
    selections = build_consensus_state(cells, events)
    return {
        "consensus_session_id": consensus_session_id,
        "annotators": annotators,
        "n_rows": len(aligned_rows),
        "n_cells": len(cells),
        "n_events": len(events),
        "selections": selections,
    }


@app.get("/export/ground_truth.csv")
def export_ground_truth_csv(consensus_session_id: str = "default", reviewer_id: str = "anonymous"):
    """Export materialized consensus selections as ground truth CSV."""
    _ = reviewer_id
    path = write_ground_truth_export(consensus_session_id=consensus_session_id)
    return FileResponse(path)

