# PGG Paper Extraction App

A local web app for manually extracting structured data from PGG (Public Goods Game) papers into a shared CSV. It replaces the Excel-based workflow with a three-panel interface: paper list, PDF viewer, and extraction form.

---

## How to run

```bash
cd extraction_app
bash run.sh
```

Then open **http://localhost:5050** in your browser.

Requirements (one-time install if missing):

```bash
pip install flask python-docx --break-system-packages
```

---

## Setup: adding PDFs

The app reads PDFs from `extraction_app/pdfs/`. Name each file after the paper's DOI-based ID, replacing `/` with `_`:

```
extraction_app/pdfs/
  10.1002_bdm.1810.pdf
  10.1016_j.jebo.2014.03.001.pdf
  ...
```

The paper ID matches the `.md` filename in `PGG_papers/papers/`. Papers without a matching PDF show a "no PDF" badge in the sidebar and a placeholder in the viewer.

---

## Interface

### Sidebar (left)
- Lists all papers from `PGG_papers/papers/`; titles come from `WoS_251031_eligible.csv`
- Green dot = extraction started; grey = not yet touched
- Search box filters by title, authors, or DOI
- Progress bar shows overall completion

### PDF viewer (center)
- Displays the PDF for the selected paper using the browser's native renderer
- Scroll, zoom, and navigate pages normally

### Extraction form (right)
- One form per paper; add multiple **conditions** (tabs) when a paper reports several treatment arms
- Fields are grouped into Study Type, Game Configuration (`CONFIG_*`), and Outcomes (`DV_*`)
- Auto-saves 2 seconds after the last edit; also saves when you navigate to another paper
- Press **Save** (or `S`) to save immediately

### Keyboard shortcuts
| Key | Action |
|-----|--------|
| `→` or `J` | Next paper |
| `←` or `K` | Previous paper |
| `S` | Save now |

---

## Fields

| Field | Type | Notes |
|-------|------|-------|
| `Empirical` | 0/1 | 1 = has human subjects; 0 = theory/simulation. Setting to 0 auto-fills all CONFIG_ and DV_ fields as N/A. |
| `Controlled_Or_Observational` | 0/1 | 1 = controlled experiment; 0 = observational |
| `Lab_Or_Field` | 0/1 | 1 = real-world field; 0 = lab or online |
| `CONFIG_playerCount` | text | Players per group |
| `CONFIG_numRounds` | text | Total rounds; use `N/R` if unknown/hidden |
| `CONFIG_allOrNothing` | 0/1 | 1 = binary threshold game; 0 = continuous |
| `CONFIG_defaultContribProp` | 0/1/N/A | 0 = opt-in; 1 = opt-out; N/A = non-human |
| `CONFIG_MPCR` | text | Fund multiplier ÷ group size |
| `CONFIG_chat` | 0/1/N/A | Pre-game communication allowed |
| `CONFIG_showOtherSummaries` | 0/1 | Individual contributions/earnings visible |
| `CONFIG_showPunishmentId` | 0/1/N/A | Punisher identity revealed; N/A = no punishment condition |
| `CONFIG_showRewardId` | 0/1/N/A | Rewarder identity revealed; N/A = no reward condition |
| `DV_contributionRate` | text | Mean contribution ÷ endowment (0–1), or `N/R` |
| `DV_efficiency` | text | Actual group payoff ÷ max payoff (0–1), or `N/R` |
| `Misc` | text | Source notes, table/figure refs, ambiguities |

See the in-app guide at **http://localhost:5050/guide** for full definitions, formulas, and pitfalls.

---

## Exporting results

Click **Export CSV** in the top bar (or visit `/api/export-csv`). The download contains one row per condition across all papers with all fields plus paper metadata.

---

## Data storage

Extractions are saved to `extraction_app/extractions.json` automatically. This file is the source of truth — back it up if needed. The Export CSV is generated from this file on demand.

---

## Configuring the extraction guide path

The in-app guide (`/guide`) is built from a DOCX file. The default path is:

```
/Users/hindy/Desktop/Academics/MIT/RA/Abdullah/Matrix Creation/Human_Extraction_Guide.docx
```

To override it without editing code, set the environment variable before running:

```bash
GUIDE_DOCX="/path/to/your/guide.docx" bash run.sh
```
