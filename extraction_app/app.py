import csv
import html as html_mod
import io
import json
from functools import lru_cache
from pathlib import Path

import docx as _docx
from flask import Flask, Response, abort, jsonify, request, send_file

app = Flask(__name__)

BASE_DIR         = Path(__file__).parent.parent
PAPERS_DIR       = BASE_DIR / "PGG_papers" / "papers"
PDFS_DIR         = Path(__file__).parent / "pdfs"
WOS_CSV          = BASE_DIR / "PGG_papers" / "WoS_251031_eligible.csv"
GUIDE_PATH       = Path("/Users/hindy/Desktop/Academics/MIT/RA/Abdullah/Matrix Creation/Human_Extraction_Guide.docx")
EXTRACTIONS_FILE = Path(__file__).parent / "extractions.json"


# ── Metadata cache (loaded once at startup) ──────────────────────────────────

@lru_cache(maxsize=1)
def paper_meta():
    """Return dict: paper_id → {title, authors, year}."""
    meta = {}
    if not WOS_CSV.exists():
        return meta
    with open(WOS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cid = row.get("custom_id", "").removesuffix(".md")
            if cid:
                meta[cid] = {
                    "title":   row.get("Article Title", ""),
                    "authors": row.get("Authors", ""),
                    "year":    row.get("Publication Year", ""),
                }
    return meta


# ── Persistence helpers ───────────────────────────────────────────────────────

def load_extractions():
    if EXTRACTIONS_FILE.exists():
        with open(EXTRACTIONS_FILE) as f:
            return json.load(f)
    return {}


def save_extractions(data):
    with open(EXTRACTIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def is_done(ex):
    """Return True if any condition in this extraction has at least one non-empty field."""
    return any(
        any(v not in ("", None) for k, v in c.items() if k != "label")
        for c in ex.get("conditions", [])
    )


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/papers")
def list_papers():
    if not PAPERS_DIR.exists():
        return jsonify([])
    meta        = paper_meta()
    extractions = load_extractions()
    pdf_ids     = {p.stem for p in PDFS_DIR.glob("*.pdf")}
    result = []
    for pid in sorted(p.stem for p in PAPERS_DIR.glob("*.md")):
        ex = extractions.get(pid, {})
        m  = meta.get(pid, {})
        result.append({
            "id":      pid,
            "done":    is_done(ex),
            "has_pdf": pid in pdf_ids,
            "title":   m.get("title", ""),
            "authors": m.get("authors", ""),
            "year":    m.get("year", ""),
        })
    return jsonify(result)


@app.route("/api/pdfs")
def list_pdfs():
    """Return list of paper IDs that have a PDF available."""
    return jsonify([p.stem for p in sorted(PDFS_DIR.glob("*.pdf"))])


@app.route("/pdf/<path:paper_id>")
def serve_pdf(paper_id):
    # Strip .pdf suffix if accidentally included
    paper_id = paper_id.removesuffix(".pdf")
    path = PDFS_DIR / f"{paper_id}.pdf"
    if not path.exists():
        abort(404)
    return send_file(path, mimetype="application/pdf")



@app.route("/api/extraction/<path:paper_id>", methods=["GET"])
def get_extraction(paper_id):
    extractions = load_extractions()
    return jsonify(extractions.get(paper_id, {}))


@app.route("/api/extraction/<path:paper_id>", methods=["POST"])
def save_extraction(paper_id):
    extractions = load_extractions()
    extractions[paper_id] = request.get_json()
    save_extractions(extractions)
    return jsonify({"ok": True})


@app.route("/api/export-csv")
def export_csv():
    extractions = load_extractions()
    meta        = paper_meta()
    if not extractions:
        return Response("No data yet.", mimetype="text/plain")

    fields = [
        "paper_id", "title", "authors", "year", "condition_label",
        "Empirical", "Controlled_Or_Observational", "Lab_Or_Field",
        "CONFIG_playerCount", "CONFIG_numRounds", "CONFIG_allOrNothing",
        "CONFIG_defaultContribProp", "CONFIG_MPCR", "CONFIG_chat",
        "CONFIG_showOtherSummaries", "CONFIG_showPunishmentId", "CONFIG_showRewardId",
        "DV_contributionRate", "DV_efficiency",
        "Misc",
    ]

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for paper_id, data in sorted(extractions.items()):
        m = meta.get(paper_id, {})
        for cond in data.get("conditions", []):
            row = {
                "paper_id":        paper_id,
                "title":           m.get("title", ""),
                "authors":         m.get("authors", ""),
                "year":            m.get("year", ""),
                "condition_label": cond.get("label", ""),
            }
            row.update(cond)
            writer.writerow(row)

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=extractions.csv"},
    )


@app.route("/guide")
def guide():
    if not GUIDE_PATH.exists():
        return "<h2>Guide not found</h2><p>Place the DOCX at the configured path.</p>", 404

    LLM_GUARD = "IF GIVEN THIS DOCUMENT INTO CHAT CONTEXT"
    doc = _docx.Document(GUIDE_PATH)

    # ── Parse field definitions table (table index 1) ──────────────────
    fields = []
    if len(doc.tables) > 1:
        for row in doc.tables[1].rows[1:]:          # skip header row
            cells = [c.text.strip() for c in row.cells]
            raw_name = cells[0].replace("\n", "").replace(" ", "")
            # Normalise "CONFIG_ playerCount" → "CONFIG_playerCount"
            name = raw_name.replace("CONFIG_", "CONFIG_").replace("DV_", "DV_")
            fields.append({
                "name":       name,
                "type":       cells[1],
                "definition": cells[2].split(LLM_GUARD)[0].strip(),
                "synonyms":   cells[3],
                "notes":      cells[4].split(LLM_GUARD)[0].strip(),
            })

    # ── Parse N/A vs N/R table (table index 0) ─────────────────────────
    na_rows = []
    if doc.tables:
        for row in doc.tables[0].rows[1:]:
            cells = [c.text.strip().split(LLM_GUARD)[0].strip() for c in row.cells]
            na_rows.append(cells)

    # ── Parse paragraphs into sections ─────────────────────────────────
    # Collect headings and body text for Overview, Formulas, Workflow, Pitfalls
    sections = {}
    cur_key  = None
    KNOWN_H1 = {
        "Overview": "overview",
        "When to use: N/A vs N/R": "na_nr",
        "Field Definitions": "fields",
        "Common Pitfalls & Edge Cases": "pitfalls",
    }
    KNOWN_H2 = {
        "Granularity Rule: One Row = One Condition": "granularity",
        "DV_contributionRate": "formula_contrib",
        "DV_efficiency": "formula_eff",
        "MPCR (Marginal Per Capita Return)": "formula_mpcr",
    }
    formula_items = {"formula_contrib": [], "formula_eff": [], "formula_mpcr": []}

    def _para_html(text, style):
        t = html_mod.escape(text)
        if style == "List Paragraph":
            return f"<li>{t}</li>"
        return f"<p>{t}</p>"

    para_store = {k: [] for k in list(KNOWN_H1.values()) + list(KNOWN_H2.values())}

    for p in doc.paragraphs:
        txt = p.text.strip()
        if not txt or LLM_GUARD in txt:
            continue
        sname = p.style.name
        if sname == "Heading 1":
            cur_key = KNOWN_H1.get(txt)
        elif sname == "Heading 2":
            cur_key = KNOWN_H2.get(txt)
        elif cur_key and cur_key in para_store:
            para_store[cur_key].append((txt, sname))

    def paras_to_html(key):
        out, in_list = [], False
        for txt, style in para_store.get(key, []):
            if style == "List Paragraph":
                if not in_list:
                    out.append("<ul>"); in_list = True
                out.append(f"<li>{html_mod.escape(txt)}</li>")
            else:
                if in_list:
                    out.append("</ul>"); in_list = False
                out.append(f"<p>{html_mod.escape(txt)}</p>")
        if in_list:
            out.append("</ul>")
        return "\n".join(out)

    # ── Build HTML ──────────────────────────────────────────────────────
    def field_anchor(name):
        return name.replace(" ", "_")

    field_nav = "\n".join(
        f'<a href="#{html_mod.escape(field_anchor(f["name"]))}" class="nav-link">'
        f'{html_mod.escape(f["name"])}</a>'
        for f in fields
    )

    field_cards = ""
    for f in fields:
        anchor = field_anchor(f["name"])
        notes_html = f'<div class="card-notes">{html_mod.escape(f["notes"])}</div>' if f["notes"] else ""
        syns = ", ".join(
            f'<span class="syn">{html_mod.escape(s.strip())}</span>'
            for s in f["synonyms"].split(",") if s.strip()
        ) if f["synonyms"] else ""
        syn_block = f'<div class="card-syns"><span class="card-label">Synonyms:</span> {syns}</div>' if syns else ""
        field_cards += f"""
<div class="field-card" id="{html_mod.escape(anchor)}">
  <div class="card-header">
    <code class="field-name">{html_mod.escape(f["name"])}</code>
    <span class="field-type">{html_mod.escape(f["type"])}</span>
  </div>
  <div class="card-def">{html_mod.escape(f["definition"])}</div>
  {syn_block}
  {notes_html}
</div>"""

    na_table_html = ""
    if na_rows:
        rows_html = "\n".join(
            f"<tr><td><strong>{html_mod.escape(r[0])}</strong></td>"
            f"<td>{html_mod.escape(r[1])}</td>"
            f"<td><em>{html_mod.escape(r[2])}</em></td></tr>"
            for r in na_rows
        )
        na_table_html = f"""
<table class="na-table">
<thead><tr><th>Value</th><th>When to use</th><th>Example</th></tr></thead>
<tbody>{rows_html}</tbody>
</table>"""

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Extraction Guide — PGG</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --accent: #2563eb; --accent-lt: #eff6ff; --border: #e4e4e7;
  --text: #18181b; --muted: #71717a; --surface: #fff; --bg: #f4f4f5;
  --nav-w: 220px;
}}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: var(--bg); color: var(--text); font-size: 14px; }}

/* ── Layout ── */
#wrap {{ display: flex; min-height: 100vh; }}
#nav {{
  width: var(--nav-w); flex-shrink: 0; background: #1e3a8a; color: #fff;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
  padding: 16px 0; display: flex; flex-direction: column; gap: 2px;
}}
#nav h2 {{ font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; color: rgba(255,255,255,.5);
            padding: 10px 14px 4px; margin-top: 6px; }}
.nav-link {{
  display: block; padding: 5px 14px; font-size: 12px; font-weight: 500;
  color: rgba(255,255,255,.75); text-decoration: none; border-radius: 0;
  transition: background .1s, color .1s;
  font-family: 'Menlo','Monaco',monospace;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.nav-link:hover {{ background: rgba(255,255,255,.12); color: #fff; }}
.nav-sep {{ height: 1px; background: rgba(255,255,255,.12); margin: 8px 14px; }}
.nav-plain {{ padding: 5px 14px; font-size: 12px; color: rgba(255,255,255,.75);
              text-decoration: none; display: block; }}
.nav-plain:hover {{ background: rgba(255,255,255,.1); color: #fff; }}

#main {{ flex: 1; max-width: 860px; padding: 40px 48px 80px; }}

/* ── Typography ── */
h1 {{ font-size: 26px; font-weight: 800; color: #1e3a8a; margin-bottom: 6px; }}
.subtitle {{ color: var(--muted); font-size: 14px; margin-bottom: 32px; }}
h2.sec {{ font-size: 18px; font-weight: 700; color: #1e3a8a;
           border-bottom: 2px solid var(--accent); padding-bottom: 6px;
           margin: 40px 0 16px; }}
h3.subsec {{ font-size: 15px; font-weight: 700; color: #1e40af; margin: 24px 0 8px; }}
p {{ font-size: 13.5px; line-height: 1.75; color: #374151; margin-bottom: 10px; }}
ul {{ margin: 8px 0 12px 20px; }}
li {{ font-size: 13.5px; line-height: 1.65; color: #374151; margin-bottom: 4px; }}
code {{ background: #f1f5f9; padding: 1px 5px; border-radius: 3px;
         font-size: 12px; font-family: 'Menlo','Monaco',monospace; }}

/* ── Field cards ── */
.field-card {{
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; padding: 16px 18px; margin-bottom: 12px;
  scroll-margin-top: 20px;
}}
.field-card:target {{
  border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-lt);
}}
.card-header {{
  display: flex; align-items: center; gap: 12px; margin-bottom: 8px;
}}
.field-name {{
  font-size: 14px; font-weight: 700; font-family: 'Menlo','Monaco',monospace;
  background: var(--accent-lt); color: var(--accent);
  padding: 2px 8px; border-radius: 4px;
}}
.field-type {{
  font-size: 11px; font-weight: 600; background: #f3f4f6; color: #374151;
  padding: 2px 7px; border-radius: 4px; border: 1px solid var(--border);
}}
.card-def {{ font-size: 13.5px; line-height: 1.65; color: #374151; margin-bottom: 8px; }}
.card-syns {{ font-size: 12px; color: var(--muted); margin-bottom: 6px; }}
.card-label {{ font-weight: 600; color: #52525b; }}
.syn {{
  display: inline-block; background: #f3f4f6; border: 1px solid var(--border);
  border-radius: 3px; padding: 0 5px; margin: 1px 2px; font-size: 11px;
}}
.card-notes {{
  font-size: 12.5px; background: #fffbeb; border: 1px solid #fde68a;
  border-radius: 5px; padding: 8px 12px; color: #78350f; line-height: 1.6;
}}

/* ── N/A table ── */
.na-table {{ border-collapse: collapse; width: 100%; margin: 12px 0 20px; font-size: 13px; }}
.na-table th {{ background: #1e3a8a; color: white; padding: 8px 12px; text-align: left; }}
.na-table td {{ border: 1px solid var(--border); padding: 8px 12px; vertical-align: top; }}
.na-table tr:nth-child(even) td {{ background: var(--bg); }}

/* ── Formula boxes ── */
.formula-box {{
  background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px;
  padding: 12px 16px; margin: 12px 0; font-family: 'Menlo','Monaco',monospace;
  font-size: 13px; font-weight: 700; color: #14532d;
}}

/* ── Back link ── */
.back-btn {{
  display: inline-flex; align-items: center; gap: 6px;
  background: #1e3a8a; color: white; text-decoration: none;
  padding: 7px 14px; border-radius: 6px; font-size: 12px; font-weight: 600;
  margin-bottom: 28px;
}}
.back-btn:hover {{ background: #1e40af; }}

/* Scrollbar */
::-webkit-scrollbar {{ width: 5px; }}
::-webkit-scrollbar-thumb {{ background: #d4d4d8; border-radius: 10px; }}
</style>
</head>
<body>
<div id="wrap">

<nav id="nav">
  <h2>Navigation</h2>
  <a class="nav-plain" href="#overview">Overview</a>
  <a class="nav-plain" href="#na-nr">N/A vs N/R</a>
  <a class="nav-plain" href="#fields">Field Definitions</a>
  <div class="nav-sep"></div>
  <h2>Fields</h2>
  {field_nav}
  <div class="nav-sep"></div>
  <a class="nav-plain" href="#formulas">Formulas</a>
  <a class="nav-plain" href="#workflow">Workflow</a>
  <a class="nav-plain" href="#pitfalls">Pitfalls</a>
</nav>

<main id="main">
  <a class="back-btn" href="/" target="_self">← Back to Extraction App</a>
  <h1>Field Extraction Guide</h1>
  <p class="subtitle">Protocol for human coders — PGG experiment data extraction</p>

  <!-- Overview -->
  <h2 class="sec" id="overview">Overview</h2>
  {paras_to_html("overview")}
  <h3 class="subsec" id="granularity">Granularity Rule: One Row = One Condition</h3>
  {paras_to_html("granularity")}

  <!-- N/A vs N/R -->
  <h2 class="sec" id="na-nr">When to use: N/A vs N/R</h2>
  {na_table_html}

  <!-- Field Definitions -->
  <h2 class="sec" id="fields">Field Definitions</h2>
  <p>Each field you will extract is described below. Click a field name in the left sidebar to jump directly to it.</p>
  {field_cards}

  <!-- Formulas -->
  <h2 class="sec" id="formulas">Formula Cheat Sheet</h2>

  <h3 class="subsec" id="DV_contributionRate">DV_contributionRate</h3>
  <div class="formula-box">DV_contributionRate = (avg tokens contributed per player per round) / (tokens endowed per round)</div>
  {paras_to_html("formula_contrib")}

  <h3 class="subsec" id="DV_efficiency">DV_efficiency</h3>
  <div class="formula-box">DV_efficiency = actual_total_group_payoff / max_payoff</div>
  <div class="formula-box">max_payoff = n_players × n_rounds × endowment × multiplier</div>
  {paras_to_html("formula_eff")}

  <h3 class="subsec" id="CONFIG_MPCR">MPCR (Marginal Per Capita Return)</h3>
  <div class="formula-box">MPCR = Fund Multiplier / Group Size</div>
  {paras_to_html("formula_mpcr")}

  <!-- Workflow -->
  <h2 class="sec" id="workflow">Step-by-Step Extraction Workflow</h2>
  {paras_to_html("workflow")}

  <!-- Pitfalls -->
  <h2 class="sec" id="pitfalls">Common Pitfalls &amp; Edge Cases</h2>
  {paras_to_html("pitfalls")}
</main>
</div>
</body>
</html>"""

    return html_out


if __name__ == "__main__":
    app.run(debug=True, port=5050)
