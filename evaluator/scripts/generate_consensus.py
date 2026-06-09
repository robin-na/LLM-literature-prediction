from __future__ import annotations

import html
import json
from collections import OrderedDict

from utils.consensus import FIELD_MAP, build_alignment, load_human_datasets
from utils.paths import CONSENSUS_HTML, HUMAN_INPUT_DIR


def esc(value: object) -> str:
    return html.escape(str(value)) if value is not None else ""


def render_sidebar(papers: list[tuple[str, list[dict[str, object]]]]) -> str:
    parts: list[str] = ['<div class="sidebar">', "<h3>Papers</h3>"]
    parts.append('<input type="text" id="paperSearch" placeholder="Search papers..." onkeyup="filterPapers()">')
    for idx, (paper_id, rows) in enumerate(papers):
        cls = "paper-link active" if idx == 0 else "paper-link"
        parts.append(
            f'<div class="{cls}" data-idx="{idx}" onclick="showPaper({idx})">'
            f'<span class="paper-doi">{esc(paper_id)}</span>'
            f'<span class="paper-counts">Rows: {len(rows)}</span>'
            "</div>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def render_paper_section(idx: int, paper_id: str, rows: list[dict[str, object]], annotators: list[str]) -> str:
    display = "block" if idx == 0 else "none"
    parts: list[str] = [
        f'<div class="paper-section" id="paper-{idx}" data-paper-id="{esc(paper_id)}" style="display:{display}">',
        f"<h2>{esc(paper_id)}</h2>",
        f'<div class="summary">Aligned rows: <b>{len(rows)}</b></div>',
    ]
    for row in rows:
        row_index = int(row["row_index"])
        alignment_type = str(row["alignment_type"])
        parts.append(f'<div class="pair-header">Row {row_index + 1} ({esc(alignment_type)})</div>')
        parts.append('<table class="comp-table"><thead><tr><th>Field</th>')
        for annotator in annotators:
            parts.append(f"<th>{esc(annotator)}</th>")
        parts.append("<th>Ground Truth</th></tr></thead><tbody>")
        for cell in row["cells"]:
            key = str(cell["key"])
            auto = bool(cell["auto_accepted"])
            auto_value = str(cell["auto_value"])
            row_cls = "auto-cell" if auto else "needs-resolution"
            parts.append(
                f'<tr class="{row_cls}" data-key="{esc(key)}" '
                f'data-auto="{esc(auto_value)}" data-locked="{"1" if auto else "0"}">'
                f'<td class="field-name">{esc(cell["field_label"])}</td>'
            )
            values_by_annotator: dict[str, str] = cell["values_by_annotator"]
            for annotator in annotators:
                parts.append(f'<td class="h-val">{esc(values_by_annotator.get(annotator, ""))}</td>')
            gt_attrs = f'data-key="{esc(key)}"'
            parts.append(
                "<td>"
                f'<div class="gt-wrap">'
                f'<div class="gt-value" {gt_attrs}></div>'
                f'<div class="gt-controls" {gt_attrs}>'
            )
            if auto:
                parts.append('<span class="auto-badge">Auto-suggested</span>')
            parts.append(
                f'<div class="custom-wrap">'
                f'<input class="custom-input" data-key="{esc(key)}" placeholder="Edit ground truth value">'
                f'<button class="clear-selection" data-key="{esc(key)}">Reset</button>'
                f"</div>"
            )
            parts.append("</div></div></td></tr>")
        parts.append("</tbody></table>")
    parts.append("</div>")
    return "\n".join(parts)


def build_view_payload() -> tuple[list[str], list[tuple[str, list[dict[str, object]]]], list[dict[str, object]]]:
    datasets = load_human_datasets(HUMAN_INPUT_DIR)
    annotators, aligned_rows, cells = build_alignment(datasets)
    cells_by_key = {cell.key: cell for cell in cells}

    papers: "OrderedDict[str, list[dict[str, object]]]" = OrderedDict()
    for aligned in aligned_rows:
        paper_rows = papers.setdefault(aligned.paper_id, [])
        paper_rows.append({"row_index": aligned.row_index, "alignment_type": aligned.alignment_type, "cells": []})

    for paper_id, rows in papers.items():
        for row in rows:
            row_index = int(row["row_index"])
            for field_label in FIELD_MAP.keys():
                key = f"{paper_id}|{row_index}|{field_label}"
                cell = cells_by_key[key]
                row["cells"].append(
                    {
                        "key": cell.key,
                        "field_label": cell.field_label,
                        "values_by_annotator": cell.values_by_annotator,
                        "auto_accepted": cell.auto_accepted,
                        "auto_value": cell.auto_value,
                    }
                )

    flat_cells: list[dict[str, object]] = []
    for cell in cells:
        flat_cells.append(
            {
                "key": cell.key,
                "paper_id": cell.paper_id,
                "row_index": cell.row_index,
                "field_label": cell.field_label,
                "values_by_annotator": cell.values_by_annotator,
                "auto_accepted": cell.auto_accepted,
                "auto_value": cell.auto_value,
            }
        )
    return annotators, list(papers.items()), flat_cells


def build_html() -> str:
    annotators, papers, cells = build_view_payload()
    sidebar = render_sidebar(papers)
    main_sections = [render_paper_section(i, pid, rows, annotators) for i, (pid, rows) in enumerate(papers)]
    payload = json.dumps({"annotators": annotators, "cells": cells})
    return (
        HTML_HEAD
        + sidebar
        + '<div class="main">'
        + "".join(main_sections)
        + '</div><script id="consensusPayload" type="application/json">'
        + payload
        + "</script>"
        + HTML_FOOT
    )


HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Human Consensus Review</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; height: 100vh; background: #f5f6fa; color: #2d3436; }
.sidebar { width: 280px; min-width: 280px; background: #2d3436; color: #dfe6e9; overflow-y: auto; padding: 16px 0; }
.sidebar h3 { padding: 0 16px 12px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #74b9ff; }
#paperSearch { width: calc(100% - 32px); margin: 0 16px 12px; padding: 8px 12px; border: 1px solid #636e72; border-radius: 6px; background: #353b48; color: #dfe6e9; font-size: 13px; }
#paperSearch::placeholder { color: #636e72; }
.paper-link { padding: 10px 16px; cursor: pointer; border-left: 3px solid transparent; transition: all 0.15s; }
.paper-link:hover { background: #353b48; }
.paper-link.active { background: #353b48; border-left-color: #74b9ff; }
.paper-doi { display: block; font-size: 12px; font-weight: 600; word-break: break-all; }
.paper-counts { display: block; font-size: 11px; color: #636e72; margin-top: 2px; }
.main { flex: 1; overflow-y: auto; padding: 24px 32px; }
h2 { font-size: 20px; margin-bottom: 8px; color: #2d3436; }
.summary { font-size: 13px; color: #636e72; margin-bottom: 16px; }
.pair-header { font-size: 14px; font-weight: 600; margin: 20px 0 8px; padding: 8px 12px; background: #dfe6e9; border-radius: 6px; }
.comp-table { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 13px; }
.comp-table th { background: #2d3436; color: #fff; padding: 8px 12px; text-align: left; position: sticky; top: 0; }
.comp-table td { padding: 7px 12px; border-bottom: 1px solid #dfe6e9; vertical-align: top; max-width: 420px; word-wrap: break-word; }
.field-name { font-weight: 600; width: 220px; min-width: 220px; background: #f8f9fa; }
.h-val { background: #eef7ff; }
tr.auto-cell td { background: #eceff1; color: #636e72; }
tr.needs-resolution td { background: #fff7e6; }
.gt-wrap { display: flex; flex-direction: column; gap: 8px; }
.gt-value { min-height: 20px; font-weight: 700; color: #2d3436; }
.gt-controls { display: flex; flex-direction: column; gap: 6px; }
#downloadGroundTruth { padding: 6px 10px; border: 1px solid #0984e3; border-radius: 6px; background: #0984e3; color: #fff; cursor: pointer; font-size: 12px; }
.clear-selection { padding: 6px 10px; border: 1px solid #b2bec3; border-radius: 6px; background: #fff; color: #2d3436; cursor: pointer; font-size: 12px; }
.custom-wrap { display: flex; gap: 6px; }
.custom-input { flex: 1; min-width: 140px; padding: 6px 8px; border: 1px solid #b2bec3; border-radius: 6px; font-size: 12px; }
.auto-badge { display: inline-block; width: fit-content; align-self: flex-start; padding: 2px 7px; border-radius: 999px; background: #b2bec3; color: #2d3436; font-size: 10px; font-weight: 700; }
.topbar { position: fixed; top: 0; left: 280px; right: 0; display: flex; align-items: center; gap: 10px; background: #f5f6fa; padding: 10px 32px; border-bottom: 1px solid #dfe6e9; z-index: 10; }
.topbar .meta { font-size: 12px; color: #636e72; }
</style>
</head>
<body>
<div class="topbar">
  <button id="downloadGroundTruth">Download Ground Truth CSV</button>
</div>
"""


HTML_FOOT = """
<script>
const payload = JSON.parse(document.getElementById('consensusPayload').textContent);
const CELLS = payload.cells || [];
const CELL_MAP = {};
for (const cell of CELLS) CELL_MAP[cell.key] = cell;
const SELECTIONS = {};

function getSessionId() {
  const params = new URLSearchParams(location.search);
  return params.get('session') || 'default';
}

function getReviewerId() {
  const key = 'consensus_reviewer_id';
  let rid = localStorage.getItem(key);
  if (!rid) {
    rid = prompt('Reviewer id:', '') || 'anonymous';
    localStorage.setItem(key, rid);
  }
  return rid || 'anonymous';
}

function apiBase() {
  return (location.protocol === 'file:') ? 'http://127.0.0.1:8000' : '';
}

async function loadState() {
  const url = apiBase() + '/consensus/state?consensus_session_id=' + encodeURIComponent(getSessionId()) + '&reviewer_id=' + encodeURIComponent(getReviewerId());
  const res = await fetch(url);
  if (!res.ok) throw new Error('state load failed');
  const data = await res.json();
  for (const [k, v] of Object.entries(data.selections || {})) SELECTIONS[k] = v;
  renderSelections();
}

function renderSelections() {
  for (const cell of CELLS) {
    const el = document.querySelector('.gt-value[data-key="' + cssEsc(cell.key) + '"]');
    if (!el) continue;
    let value = SELECTIONS[cell.key];
    if (!value && cell.auto_accepted) value = cell.auto_value;
    if (
      cell.field_label === 'Controled_Or_Observational' &&
      Object.values(cell.values_by_annotator || {}).every(v => String(v || '').trim() === '')
    ) {
      value = '';
    }
    el.textContent = value || '';
    const input = document.querySelector('.custom-input[data-key="' + cssEsc(cell.key) + '"]');
    if (input && document.activeElement !== input) input.value = value || '';
  }
}

function cssEsc(s) { return String(s).replace(/"/g, '\\\\\"'); }

async function persistSelection(key, value, sourceAnnotator) {
  const oldValue = SELECTIONS[key] || '';
  const payload = {
    consensus_session_id: getSessionId(),
    reviewer_id: getReviewerId(),
    key: key,
    action: value ? 'set_ground_truth' : 'clear_ground_truth',
    old_value: oldValue,
    new_value: value || '',
    source_annotator: sourceAnnotator || '',
    note: '',
  };
  const res = await fetch(apiBase() + '/consensus/events', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error('persist failed');
  if (value) SELECTIONS[key] = value;
  else delete SELECTIONS[key];
  renderSelections();
}

function getEffectiveCellValue(key) {
  const cell = CELL_MAP[key];
  if (!cell) return '';
  let value = SELECTIONS[key];
  if (!value && cell.auto_accepted) value = cell.auto_value;
  if (
    cell.field_label === 'Controled_Or_Observational' &&
    Object.values(cell.values_by_annotator || {}).every(v => String(v || '').trim() === '')
  ) {
    value = '';
  }
  return value || '';
}

function persistFromInput(inputEl) {
  if (!inputEl) return;
  const key = inputEl.dataset.key;
  const value = (inputEl.value || '').trim();
  if (value === getEffectiveCellValue(key)) return;
  persistSelection(key, value, '__custom__');
}

document.addEventListener('click', function(e) {
  const clear = e.target.closest('.clear-selection');
  if (clear) {
    persistSelection(clear.dataset.key, '', '__clear__');
  }
});

document.addEventListener('change', function(e) {
  const input = e.target.closest('.custom-input');
  if (!input) return;
  persistFromInput(input);
});

document.addEventListener('keydown', function(e) {
  if (e.key !== 'Enter') return;
  const input = e.target.closest('.custom-input');
  if (!input) return;
  e.preventDefault();
  persistFromInput(input);
});

document.getElementById('downloadGroundTruth').addEventListener('click', function() {
  const url = apiBase() + '/export/ground_truth.csv?consensus_session_id=' + encodeURIComponent(getSessionId()) + '&reviewer_id=' + encodeURIComponent(getReviewerId());
  fetch(url).then(r => {
    if (!r.ok) throw new Error('download failed');
    return r.blob();
  }).then(blob => {
    const link = document.createElement('a');
    const obj = URL.createObjectURL(blob);
    link.href = obj;
    link.download = 'ground_truth.csv';
    link.click();
    URL.revokeObjectURL(obj);
  });
});

function showPaper(idx) {
  document.querySelectorAll('.paper-section').forEach(s => s.style.display = 'none');
  document.getElementById('paper-' + idx).style.display = 'block';
  document.querySelectorAll('.paper-link').forEach(l => l.classList.remove('active'));
  document.querySelector('.paper-link[data-idx="' + idx + '"]').classList.add('active');
}

function filterPapers() {
  const query = document.getElementById('paperSearch').value.toLowerCase();
  document.querySelectorAll('.paper-link').forEach(link => {
    const doi = link.querySelector('.paper-doi').textContent.toLowerCase();
    link.style.display = doi.includes(query) ? 'block' : 'none';
  });
}

loadState().then(() => {
}).catch(() => {
  renderSelections();
});

document.querySelector('.main').style.paddingTop = '64px';
</script>
</body>
</html>
"""


def main() -> None:
    out = build_html()
    CONSENSUS_HTML.parent.mkdir(parents=True, exist_ok=True)
    CONSENSUS_HTML.write_text(out, encoding="utf-8")
    print(f"Generated {CONSENSUS_HTML}")


if __name__ == "__main__":
    main()
