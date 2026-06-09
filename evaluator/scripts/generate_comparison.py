from __future__ import annotations

import html
from collections import OrderedDict
from pathlib import Path
from typing import Optional

from utils.columns import COLUMN_MAP
from utils.csvio import Row, read_csv
from utils.helpers import group_by_paper, normalize_paper_id
from utils.matching import classify_match, to_html_class
from utils.paths import COMPARISON_HTML, GROUND_TRUTH_CSV, LLM_DATASET_CSV
from utils.row_alignment import align_rows, human_alignment_label, llm_alignment_label


def esc(value: object) -> str:
    return html.escape(str(value)) if value else ""


def matching_label(field_label: str) -> str:
    return "Lab / Experiment" if field_label == "Lab_Or_Field" else field_label


def canon_stage2_classification(value: str) -> str:
    value = (value or "").strip().replace("-", "_")
    if value in {"match", "close", "both_empty"}:
        return "match"
    if value in {"mismatch", "one_empty", "missing_row"}:
        return "mismatch"
    return value


def validate_columns(ground_truth_rows: list[Row], llm_rows: list[Row]) -> None:
    human_cols = set(ground_truth_rows[0].keys()) if ground_truth_rows else set()
    llm_cols = set(llm_rows[0].keys()) if llm_rows else set()
    required_human = {"Filename"} | {human for human, _ in COLUMN_MAP.values()}
    required_llm = {"custom_id"} | {llm for _, llm in COLUMN_MAP.values()}
    missing_human = sorted(required_human - human_cols)
    missing_llm = sorted(required_llm - llm_cols)
    if missing_human:
        raise ValueError(f"Ground truth CSV missing required columns: {', '.join(missing_human)}")
    if missing_llm:
        raise ValueError(f"LLM CSV missing required columns: {', '.join(missing_llm)}")


def build_pairs(ground_truth_rows: list[Row], llm_rows: list[Row]) -> list[tuple[Optional[Row], Optional[Row]]]:
    return [(h, l) for h, l in align_rows(ground_truth_rows, llm_rows, column_map=COLUMN_MAP)]


def gather_papers_data(
    ground_truth_groups: dict[str, list[Row]],
    llm_groups: dict[str, list[Row]],
) -> list[tuple[str, list[tuple[Optional[Row], Optional[Row]]]]]:
    all_papers = list(OrderedDict.fromkeys(list(ground_truth_groups.keys()) + list(llm_groups.keys())))
    return [(pid, build_pairs(ground_truth_groups.get(pid, []), llm_groups.get(pid, []))) for pid in all_papers]


def render_sidebar(papers_data: list[tuple[str, list[tuple[Optional[Row], Optional[Row]]]]]) -> str:
    parts: list[str] = ['<div class="sidebar">', "<h3>Papers</h3>"]
    parts.append('<input type="text" id="paperSearch" placeholder="Search papers..." onkeyup="filterPapers()">')
    for idx, (paper_id, pairs) in enumerate(papers_data):
        h_count = sum(1 for h, _ in pairs if h)
        l_count = sum(1 for _, l in pairs if l)
        cls = "paper-link active" if idx == 0 else "paper-link"
        parts.append(
            f'<div class="{cls}" data-idx="{idx}" onclick="showPaper({idx})">'
            f'<span class="paper-doi">{esc(paper_id)}</span>'
            f'<span class="paper-counts">GT:{h_count} / L:{l_count}</span>'
            "</div>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def render_comparison_table(paper_id: str, pair_idx: int, gt_row: Optional[Row], llm_row: Optional[Row]) -> str:
    parts: list[str] = []
    h_label = human_alignment_label(gt_row) or "(no ground-truth row)"
    l_label = llm_alignment_label(llm_row) or "(no LLM row)"
    parts.append(
        f'<div class="pair-header">Row {pair_idx + 1}: '
        f'<span class="human-label">{esc(h_label)}</span> vs '
        f'<span class="llm-label">{esc(l_label)}</span></div>'
    )
    parts.append(
        '<table class="comp-table"><thead><tr><th>Ground Truth Field</th><th>Ground Truth</th><th>LLM</th>'
        "<th>LLM Field</th></tr></thead><tbody>"
    )
    for field_label, (h_col, l_col) in COLUMN_MAP.items():
        h_val = ((gt_row.get(h_col) if gt_row else "") or "").strip()
        l_val = ((llm_row.get(l_col) if llm_row else "") or "").strip()
        cls = classify_match(matching_label(field_label), h_val, l_val, gt_row is not None, llm_row is not None)
        cls = canon_stage2_classification(cls)
        html_cls = to_html_class(cls)
        row_key = f"{paper_id}|{pair_idx}|{field_label}"
        parts.append(
            f'<tr class="{html_cls}" data-key="{esc(row_key)}" data-auto="{html_cls}">'
            f'<td class="field-name">{esc(h_col)}</td>'
            f'<td class="h-val">{esc(h_val)}</td>'
            f'<td class="l-val">{esc(l_val)}</td>'
            f'<td class="field-name">{esc(l_col)}</td>'
            "</tr>"
        )
    parts.append("</tbody></table>")
    return "\n".join(parts)


def render_reasons_table(pair_idx: int, llm_row: Optional[Row]) -> str:
    if not llm_row:
        return f'<div class="pair-header">Row {pair_idx + 1}: No LLM data</div>'
    l_label = llm_alignment_label(llm_row)
    parts: list[str] = [f'<div class="pair-header">Row {pair_idx + 1}: {esc(l_label)}</div>']
    parts.append(
        '<table class="comp-table reason-table"><thead><tr><th>Field</th><th>Reason / Confidence</th>'
        "</tr></thead><tbody>"
    )
    for col, val in llm_row.items():
        if not (col.endswith("_reason") or col.endswith("_confidence")):
            continue
        s = (val or "").strip()
        if not s:
            continue
        parts.append(f'<tr><td class="field-name">{esc(col)}</td><td class="reason-val">{esc(s)}</td></tr>')
    parts.append("</tbody></table>")
    return "\n".join(parts)


def render_paper_section(
    idx: int, paper_id: str, pairs: list[tuple[Optional[Row], Optional[Row]]]
) -> str:
    display = "block" if idx == 0 else "none"
    gt_count = sum(1 for h, _ in pairs if h)
    llm_count = sum(1 for _, l in pairs if l)
    parts: list[str] = [
        f'<div class="paper-section" id="paper-{idx}" data-paper-id="{esc(paper_id)}" style="display:{display}">'
    ]
    parts.append(f"<h2>{esc(paper_id)}</h2>")
    parts.append(f'<div class="summary">Ground-truth rows: <b>{gt_count}</b> | LLM rows: <b>{llm_count}</b></div>')
    parts.append('<div class="tab-bar">')
    parts.append(
        f'<button class="tab-btn active" onclick="switchTab({idx}, \'comparison\')">Side-by-Side Comparison</button>'
    )
    parts.append(f'<button class="tab-btn" onclick="switchTab({idx}, \'reasons\')">LLM Reasons &amp; Confidence</button>')
    parts.append(f'<button class="tab-btn" onclick="switchTab({idx}, \'notes\')">Notes</button>')
    parts.append("</div>")
    parts.append(f'<div class="tab-content comparison" id="tab-comparison-{idx}">')
    for pair_idx, (h, l) in enumerate(pairs):
        parts.append(render_comparison_table(paper_id, pair_idx, h, l))
    parts.append("</div>")
    parts.append(f'<div class="tab-content reasons" id="tab-reasons-{idx}" style="display:none">')
    for pair_idx, (_, l) in enumerate(pairs):
        parts.append(render_reasons_table(pair_idx, l))
    parts.append("</div>")
    parts.append(f'<div class="tab-content notes" id="tab-notes-{idx}" style="display:none">')
    parts.append(
        '<div style="display:flex;flex-direction:column;gap:10px;margin-top:6px;">'
        '<div style="font-size:13px;color:#636e72;">Private notes for this paper (saved per reviewer).</div>'
        f'<textarea class="paper-note" data-paper-id="{esc(paper_id)}" '
        'style="width:100%;min-height:160px;padding:10px;border:1px solid #b2bec3;border-radius:8px;'
        'font-size:13px;line-height:1.4;resize:vertical;" placeholder="Write notes here..."></textarea>'
        f'<div style="display:flex;gap:10px;align-items:center;">'
        f'<button class="note-save" data-paper-id="{esc(paper_id)}" '
        'style="padding:8px 14px;border:1px solid #0984e3;border-radius:8px;background:#0984e3;'
        'color:#fff;cursor:pointer;font-size:13px;font-weight:600;">Save</button>'
        f'<span class="note-status" data-paper-id="{esc(paper_id)}" style="font-size:12px;color:#636e72;"></span>'
        "</div></div>"
    )
    parts.append("</div>")
    parts.append("</div>")
    return "\n".join(parts)


def build_html(ground_truth_rows: list[Row], llm_rows: list[Row]) -> str:
    validate_columns(ground_truth_rows, llm_rows)
    gt_groups = group_by_paper(ground_truth_rows, "Filename")
    llm_groups = group_by_paper(llm_rows, "custom_id", strip_md=True)
    papers_data = gather_papers_data(gt_groups, llm_groups)
    html_parts: list[str] = [HTML_HEAD, render_sidebar(papers_data), '<div class="main">']
    for idx, (paper_id, pairs) in enumerate(papers_data):
        html_parts.append(render_paper_section(idx, paper_id, pairs))
    html_parts.append("</div>")
    html_parts.append(HTML_FOOT)
    return "\n".join(html_parts)


HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ground Truth vs LLM Data Extraction Comparison</title>
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
.tab-bar { display: flex; gap: 4px; margin-bottom: 20px; flex-wrap: wrap; }
.tab-btn { padding: 8px 16px; border: 1px solid #b2bec3; border-radius: 6px; background: #fff; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.15s; }
.tab-btn:hover { background: #dfe6e9; }
.tab-btn.active { background: #0984e3; color: #fff; border-color: #0984e3; }
.pair-header { font-size: 14px; font-weight: 600; margin: 20px 0 8px; padding: 8px 12px; background: #dfe6e9; border-radius: 6px; }
.human-label { color: #0984e3; }
.llm-label { color: #6c5ce7; }
.comp-table { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 13px; }
.comp-table th { background: #2d3436; color: #fff; padding: 8px 12px; text-align: left; position: sticky; top: 0; }
.comp-table td { padding: 7px 12px; border-bottom: 1px solid #dfe6e9; vertical-align: top; max-width: 420px; word-wrap: break-word; }
.field-name { font-weight: 600; white-space: nowrap; width: 220px; min-width: 220px; background: #f8f9fa; }
.h-val { background: #eef7ff; }
.l-val { background: #f3eeff; }
tr.match .h-val, tr.match .l-val { background: #d4edda; }
tr.close .h-val, tr.close .l-val { background: #fff3cd; }
tr.mismatch .h-val, tr.mismatch .l-val { background: #f8d7da; }
tr.one-empty .h-val, tr.one-empty .l-val { background: #ffeaa7; }
tr.both-empty .h-val, tr.both-empty .l-val { background: #f8f9fa; color: #b2bec3; }
tr.missing-row td { background: #f8f9fa; color: #b2bec3; font-style: italic; }
.reason-table td { font-size: 12px; }
.reason-val { color: #636e72; line-height: 1.5; }
.legend { display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; font-size: 12px; }
.legend-item { display: flex; align-items: center; gap: 4px; }
.legend-swatch { width: 16px; height: 16px; border-radius: 3px; border: 1px solid #ccc; }
tr[data-key] { cursor: pointer; }
tr.override .field-name::after { content: ' *'; color: #e17055; font-weight: bold; }
#colorMenu { position: fixed; z-index: 1000; display: none; background: #fff; border: 1px solid #b2bec3; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.18); padding: 6px 0; min-width: 170px; }
#colorMenu .cm-item { display: flex; align-items: center; gap: 8px; padding: 7px 16px; cursor: pointer; font-size: 13px; transition: background 0.1s; }
#colorMenu .cm-item:hover { background: #dfe6e9; }
#colorMenu .cm-swatch { width: 14px; height: 14px; border-radius: 3px; border: 1px solid #ccc; flex-shrink: 0; }
#colorMenu .cm-divider { height: 1px; background: #dfe6e9; margin: 4px 0; }
</style>
</head>
<body>
"""


HTML_FOOT = """
<div id="colorMenu">
    <div class="cm-item" data-cls="match"><span class="cm-swatch" style="background:#d4edda"></span>Match</div>
    <div class="cm-item" data-cls="mismatch"><span class="cm-swatch" style="background:#f8d7da"></span>Mismatch</div>
    <div class="cm-divider"></div>
    <div class="cm-item" data-cls="__auto"><span class="cm-swatch" style="background:linear-gradient(135deg,#eef7ff,#f3eeff)"></span>Reset to auto</div>
</div>
<script>
const ALL_CLASSES = ['match','mismatch'];
const LEGACY_STORAGE_KEY = 'comparison_overrides';
const LEGACY_NOTES_KEY_PREFIX = 'comparison_notes__';
const REVIEWER_ID_KEY = 'reviewer_id';

function resolveApiBase() {
    const params = new URLSearchParams(location.search);
    const override = (params.get('api_base') || params.get('api') || '').trim();
    if (override) return override.replace(/\\/+$/, '');
    return (location.protocol === 'file:') ? 'http://127.0.0.1:8000' : '';
}

const API_BASE = resolveApiBase();
let USE_LEGACY_LOCAL_STORAGE = false;
let OVERRIDES = {};
let NOTES = {};
let ACTIVE_REVIEWER_ID = 'anonymous';

function getSessionId() {
    const params = new URLSearchParams(location.search);
    return params.get('session') || 'default';
}

function getReviewerId() {
    try {
        let rid = localStorage.getItem(REVIEWER_ID_KEY);
        if (!rid) {
            rid = prompt('Reviewer id (stored in browser):', '') || 'anonymous';
            localStorage.setItem(REVIEWER_ID_KEY, rid);
        }
        return rid || 'anonymous';
    } catch (e) {
        return 'anonymous';
    }
}

function getLegacyOverrides() {
    try { return JSON.parse(localStorage.getItem(LEGACY_STORAGE_KEY) || '{}'); } catch(e) { return {}; }
}
function saveLegacyOverrides(obj) {
    localStorage.setItem(LEGACY_STORAGE_KEY, JSON.stringify(obj));
}
function legacyNotesKey(reviewerId) {
    return LEGACY_NOTES_KEY_PREFIX + (reviewerId || 'anonymous');
}
function getLegacyNotes(reviewerId) {
    try { return JSON.parse(localStorage.getItem(legacyNotesKey(reviewerId)) || '{}'); } catch(e) { return {}; }
}
function saveLegacyNotes(reviewerId, obj) {
    localStorage.setItem(legacyNotesKey(reviewerId), JSON.stringify(obj));
}

function getCurrentOverrides() {
    return USE_LEGACY_LOCAL_STORAGE ? getLegacyOverrides() : OVERRIDES;
}
function getCurrentNotes() {
    return USE_LEGACY_LOCAL_STORAGE ? getLegacyNotes(ACTIVE_REVIEWER_ID) : NOTES;
}

function applyOverride(tr, cls) {
    ALL_CLASSES.forEach(c => tr.classList.remove(c));
    tr.classList.remove('override');
    if (cls === '__auto' || !cls) tr.classList.add(tr.dataset.auto);
    else { tr.classList.add(cls); tr.classList.add('override'); }
}

function applyAllOverrides() {
    const ov = getCurrentOverrides();
    document.querySelectorAll('tr[data-key]').forEach(tr => {
        const key = tr.dataset.key;
        if (ov[key]) applyOverride(tr, ov[key]);
    });
}

async function loadStateFromServer() {
    const url = `${API_BASE}/state?review_session_id=${encodeURIComponent(getSessionId())}&reviewer_id=${encodeURIComponent(ACTIVE_REVIEWER_ID)}`;
    const res = await fetch(url, { method: 'GET' });
    if (!res.ok) throw new Error(`state fetch failed: ${res.status}`);
    const data = await res.json();
    OVERRIDES = data.overrides || {};
    NOTES = data.notes || {};
}

async function persistEvent(payload) {
    const res = await fetch(`${API_BASE}/events`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });
    if (!res.ok) throw new Error(`event post failed: ${res.status}`);
}

async function setOverride(key, oldCls, newCls) {
    if (USE_LEGACY_LOCAL_STORAGE) {
        const ov = getLegacyOverrides();
        if (newCls === '__auto') delete ov[key];
        else ov[key] = newCls;
        saveLegacyOverrides(ov);
        return;
    }
    const payload = {
        review_session_id: getSessionId(),
        reviewer_id: getReviewerId(),
        key: key,
        action: 'set_classification',
        old_classification: oldCls || '',
        new_classification: newCls || '',
    };
    try {
        await persistEvent(payload);
        if (newCls === '__auto') delete OVERRIDES[key];
        else OVERRIDES[key] = newCls;
    } catch (e) {
        USE_LEGACY_LOCAL_STORAGE = true;
        const ov = getLegacyOverrides();
        if (newCls === '__auto') delete ov[key];
        else ov[key] = newCls;
        saveLegacyOverrides(ov);
    }
}

async function setPaperNote(paperId, oldNote, newNote) {
    if (USE_LEGACY_LOCAL_STORAGE) {
        const n = getLegacyNotes(ACTIVE_REVIEWER_ID);
        if (!newNote) delete n[paperId];
        else n[paperId] = newNote;
        saveLegacyNotes(ACTIVE_REVIEWER_ID, n);
        return;
    }
    const payload = {
        review_session_id: getSessionId(),
        reviewer_id: ACTIVE_REVIEWER_ID,
        key: paperId,
        action: 'set_paper_note',
        old_value: oldNote || '',
        new_value: newNote || '',
    };
    try {
        await persistEvent(payload);
        if (!newNote) delete NOTES[paperId];
        else NOTES[paperId] = newNote;
    } catch (e) {
        USE_LEGACY_LOCAL_STORAGE = true;
        const n = getLegacyNotes(ACTIVE_REVIEWER_ID);
        if (!newNote) delete n[paperId];
        else n[paperId] = newNote;
        saveLegacyNotes(ACTIVE_REVIEWER_ID, n);
    }
}

let activeRow = null;
const menu = document.getElementById('colorMenu');

document.addEventListener('click', function(e) {
    const tr = e.target.closest('tr[data-key]');
    if (tr && tr.closest('.tab-content.comparison')) {
        e.preventDefault();
        activeRow = tr;
        const rect = e.target.getBoundingClientRect();
        let top = rect.bottom + 4;
        let left = rect.left;
        if (top + 250 > window.innerHeight) top = rect.top - 250;
        if (left + 180 > window.innerWidth) left = window.innerWidth - 190;
        menu.style.top = top + 'px';
        menu.style.left = left + 'px';
        menu.style.display = 'block';
        return;
    }
    if (!e.target.closest('#colorMenu')) {
        menu.style.display = 'none';
        activeRow = null;
    }
});

menu.querySelectorAll('.cm-item[data-cls]').forEach(item => {
    item.addEventListener('click', function() {
        if (!activeRow) return;
        const cls = this.dataset.cls;
        const key = activeRow.dataset.key;
        const ov = getCurrentOverrides();
        const oldCls = ov[key] || '__auto';
        const newCls = (cls === '__auto') ? '__auto' : cls;
        applyOverride(activeRow, newCls);
        setOverride(key, oldCls, newCls).then(updateProgress);
        menu.style.display = 'none';
        activeRow = null;
    });
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') { menu.style.display = 'none'; activeRow = null; }
});

function showPaper(idx) {
    document.querySelectorAll('.paper-section').forEach(s => s.style.display = 'none');
    document.getElementById('paper-' + idx).style.display = 'block';
    document.querySelectorAll('.paper-link').forEach(l => l.classList.remove('active'));
    document.querySelector('.paper-link[data-idx="' + idx + '"]').classList.add('active');
}

function switchTab(paperIdx, tabName) {
    const section = document.getElementById('paper-' + paperIdx);
    section.querySelectorAll('.tab-content').forEach(t => t.style.display = 'none');
    section.querySelector('#tab-' + tabName + '-' + paperIdx).style.display = 'block';
    section.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
}

function filterPapers() {
    const query = document.getElementById('paperSearch').value.toLowerCase();
    document.querySelectorAll('.paper-link').forEach(link => {
        const doi = link.querySelector('.paper-doi').textContent.toLowerCase();
        link.style.display = doi.includes(query) ? 'block' : 'none';
    });
}

function exportFinalDataset() {
    const session = getSessionId();
    const reviewer = ACTIVE_REVIEWER_ID || getReviewerId();
    const url = API_BASE + '/export/final_dataset.csv?review_session_id=' + encodeURIComponent(session) + '&reviewer_id=' + encodeURIComponent(reviewer);
    fetch(url)
        .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.blob(); })
        .then(blob => downloadBlob(blob, 'final_review_dataset.csv'))
        .catch(() => {
            const csv = buildFinalDatasetCsvClient(session, reviewer);
            downloadBlob(new Blob([csv], {type: 'text/csv;charset=utf-8;'}), 'final_review_dataset.csv');
            alert('Could not reach server, exported a client-side fallback.');
        });
}

function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename || 'download.csv';
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function buildFinalDatasetCsvClient(sessionId, reviewerId) {
    const ov = getCurrentOverrides();
    const notes = getCurrentNotes();
    const noteEmitted = new Set();
    const header = ['review_session_id','reviewer_id','key','paper_id','row_index','field','human_col','llm_col','human_value','llm_value','auto_classification','final_classification','paper_note'];
    const rows = [header];
    document.querySelectorAll('tr[data-key]').forEach(tr => {
        const key = tr.dataset.key || '';
        const parts = key.split('|');
        const paperId = parts[0] || '';
        const rowIndex = parts[1] || '';
        const field = parts.slice(2).join('|');
        const tds = tr.querySelectorAll('td');
        const humanCol = tds[0] ? (tds[0].textContent || '').trim() : '';
        const humanVal = tds[1] ? (tds[1].textContent || '').trim() : '';
        const llmVal = tds[2] ? (tds[2].textContent || '').trim() : '';
        const llmCol = tds[3] ? (tds[3].textContent || '').trim() : '';
        const autoCls = tr.dataset.auto || '';
        const finalCls = ov[key] || autoCls;
        const note = noteEmitted.has(paperId) ? '' : (notes[paperId] || '');
        noteEmitted.add(paperId);
        rows.push([csvEsc(sessionId || ''),csvEsc(reviewerId || ''),csvEsc(key),csvEsc(paperId),csvEsc(rowIndex),csvEsc(field),csvEsc(humanCol),csvEsc(llmCol),csvEsc(humanVal),csvEsc(llmVal),csvEsc(autoCls),csvEsc(finalCls),csvEsc(note)]);
    });
    return rows.map(r => r.join(',')).join('\\n');
}

function applyAllNotes() {
    const notes = getCurrentNotes();
    document.querySelectorAll('textarea.paper-note').forEach(el => {
        const pid = el.dataset.paperId;
        el.value = notes[pid] || '';
    });
}

function setNoteStatus(paperId, text) {
    const el = document.querySelector(`.note-status[data-paper-id="${cssEsc(paperId)}"]`);
    if (el) el.textContent = text || '';
}
function cssEsc(s) { return String(s).replace(/"/g, '\\\\\"'); }

document.addEventListener('click', function(e) {
    const btn = e.target.closest('button.note-save');
    if (!btn) return;
    const paperId = btn.dataset.paperId;
    const ta = document.querySelector(`textarea.paper-note[data-paper-id="${cssEsc(paperId)}"]`);
    if (!ta) return;
    const notes = getCurrentNotes();
    const oldNote = notes[paperId] || '';
    const newNote = (ta.value || '').trim();
    setNoteStatus(paperId, 'Saving...');
    setPaperNote(paperId, oldNote, newNote).then(() => setNoteStatus(paperId, 'Saved'));
});

function csvEsc(s) {
    if (s == null) return '';
    s = String(s);
    if (s.includes(',') || s.includes('"') || s.includes('\\n')) return '"' + s.replace(/"/g, '""') + '"';
    return s;
}

function updateProgress() {
    const ov = getCurrentOverrides();
    const total = document.querySelectorAll('tr[data-key]').length;
    const reviewed = Object.keys(ov).length;
    const el = document.getElementById('reviewProgress');
    if (el) el.textContent = reviewed + ' / ' + total + ' reviewed';
}

(async function initPersistence() {
    ACTIVE_REVIEWER_ID = getReviewerId();
    try { await loadStateFromServer(); USE_LEGACY_LOCAL_STORAGE = false; }
    catch (e) { USE_LEGACY_LOCAL_STORAGE = true; }
    applyAllOverrides();
    applyAllNotes();
    updateProgress();
})();
</script>
</body>
</html>
"""


def main(ground_truth_csv: Path | None = None):
    gt_path = ground_truth_csv or GROUND_TRUTH_CSV
    if not gt_path.exists():
        raise FileNotFoundError(
            f"Ground truth CSV not found at {gt_path}. Run `python3 main.py evaluate` or `python3 main.py ground-truth` first."
        )
    ground_truth_rows = read_csv(gt_path)
    llm_rows = read_csv(LLM_DATASET_CSV)
    global HTML_HEAD
    HTML_HEAD += """
    <div class="main" id="legend-container" style="position:fixed;top:0;right:0;left:280px;z-index:10;background:#f5f6fa;padding:10px 32px;border-bottom:1px solid #dfe6e9;">
    <div class="legend">
        <b>Legend:</b>
        <span class="legend-item"><span class="legend-swatch" style="background:#d4edda"></span> Match</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#f8d7da"></span> Mismatch</span>
        <span class="legend-item"><span class="legend-swatch" style="background:linear-gradient(135deg,#eef7ff,#f3eeff)"></span> Reset to auto</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#f3eeff"></span> LLM val</span>
        <span style="margin-left:auto; display:flex; gap:8px; align-items:center;">
            <span id="reviewProgress" style="font-size:12px; color:#636e72;"></span>
            <button onclick="exportFinalDataset()" style="padding:6px 14px;border:1px solid #2d3436;border-radius:6px;background:#2d3436;color:#fff;cursor:pointer;font-size:12px;font-weight:600;">Export Final Dataset</button>
        </span>
    </div>
    </div>
    """
    out = build_html(ground_truth_rows, llm_rows)
    out = out.replace('<div class="main">', '<div class="main" style="padding-top: 64px;">', 1)
    COMPARISON_HTML.parent.mkdir(parents=True, exist_ok=True)
    COMPARISON_HTML.write_text(out, encoding="utf-8")
    print(f"Generated {COMPARISON_HTML}")


if __name__ == "__main__":
    main()
