# Extraction App

A small Flask app that lets a human annotator extract structured PGG experimental parameters from paper PDFs, one condition at a time.

## Run

```bash
cd extraction_app
bash run.sh
# → http://localhost:5050
```

Or directly: `python3 app.py`.

## Data files (not in the repo)

This PR ships only the code (`app.py`, `static/index.html`, `run.sh`). At runtime the app reads/writes three data inputs that are gitignored and delivered separately (via Google Drive):

| Path | Purpose |
|---|---|
| `extraction_app/pdfs/*.pdf` | One PDF per paper, named by paper ID (e.g. `10.1111_ecin.12713.pdf`) |
| `extraction_app/extractions.json` | Annotation store. The app reads it at startup and writes back on every save. If absent, the app starts with empty annotations. |
| `extraction_app/Human_Extraction_Guide.docx` | Field definitions parsed at startup and served at `/guide`. Optional — point at a Drive-downloaded copy via `GUIDE_DOCX=/path/to/guide.docx` |

The papers' Markdown source (used for keyword search) lives at `../PGG_papers/papers/` and is also gitignored.

## Endpoints

| Path | What |
|---|---|
| `/` | Annotation form |
| `/guide` | Renders `Human_Extraction_Guide.docx` to HTML with field cards + formulas |
| `/api/papers` | List of papers + filled/empty status |
| `/api/extraction/<paper_id>` | GET / POST the annotation for one paper |
| `/api/validate` | Reports mandatory fields that are empty in any condition (used by Export CSV) |
| `/api/export-csv` | Download all annotations as CSV |
| `/pdf/<paper_id>` | PDF served through a local PDF.js viewer |

## Form features

- 22-field schema (Empirical, Lab/Field, all `CONFIG_*`, `number_IVs`, `number_DVs`, `source_data`, Misc)
- Mandatory fields with empty values get an **orange outline**
- Auto-N/A: when `Empirical = 0` or `Lab_Or_Field = 1`, all `CONFIG_*` fields are locked at N/A
- Hover tooltips with the field definition
- Export to CSV runs the validator first and warns if anything is empty

## Config

| Env var | Default | What |
|---|---|---|
| `GUIDE_DOCX` | `extraction_app/Human_Extraction_Guide.docx` | Override path to the guide |
