# Main-Text Figure Set 260427

This folder is the source-of-truth handoff point for the `main_text_260427` figure set.

Its purpose is to let a fresh agent answer four questions without reading prior chat history:

1. Which figures are currently canonical?
2. Which figure number maps to which semantic figure?
3. Where did each figure come from?
4. Which files are exploratory versus main-text?

## Rules

- The canonical mapping lives in `figure_manifest.csv`.
- Figure numbers may change during drafting. Semantic figure identities should stay stable unless the figure's substantive purpose changes.
- Canonical main-text assets belong directly in:
  - `plots/paper/main_text_260427/`
  - `results/paper/main_text_figures_260427/`
- Exploratory or superseded variants belong only in:
  - `plots/paper/main_text_260427/exploratory/`
  - `results/paper/main_text_figures_260427/exploratory/`
- Every canonical figure should eventually have four linked artifacts:
  - one PNG
  - one rows CSV
  - one documentation markdown file
  - one generating script
- Every documentation file should state:
  - the exact estimand
  - the exact input files
  - the exact output files
  - the generating script
  - whether the figure is inherited or adapted from an earlier set

## Current Numbering Shift

For `main_text_260427`, the current numbering shift relative to `main_text_260415` is:

- `260415` Figure 1 -> `260427` Figure 2
- `260415` Figure 2 -> `260427` Figure 3
- `260415` Figure 3 -> `260427` Figure 4
- `260415` Figure 4 -> `260427` Figure 5

Figure 1 is intentionally reserved for a new leading figure and is not yet defined.

## Canonical vs Exploratory

At scaffold time, `260427` does not yet contain regenerated canonical figures. The manifest points to the current parent assets in `260415` so a new agent can see the latest stable predecessor.

Exploratory examples from `260415` that should not be confused with canonical `260427` figures include:

- Figure 1 experiment-bootstrap variant
- Figure 1 adjusted-correlation (`r_adj`) variant
- Figure 2 empirical-split density variant
- Figure 2 heterogeneity and cross-LLM agreement variant
- Figure 3 individual-paper permutation-importance companion plots

## Update Protocol

When a `260427` figure is created or replaced:

1. Update the row in `figure_manifest.csv`.
2. Add or update the figure-specific documentation markdown file.
3. Keep the semantic ID stable if the figure is the same core object under a new number.
4. Move any superseded noncanonical variants into the `exploratory/` subfolder or mark them clearly as noncanonical.

