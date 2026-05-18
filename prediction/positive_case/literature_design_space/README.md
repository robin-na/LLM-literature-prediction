# Positive Case -> Literature Design Space

This folder is the canonical handoff location for the current positive-case analysis that defines the design space we want to carry into the published-paper augmentation study.

What this folder means:

- this is still a `positive case`
- the augmentation source is a known informative paper
- the purpose is to decide which model / report style / elicitation combinations are worth carrying forward when the vector store is switched to published paper(s)

Current design-space scope:

- models: `GPT-4.1`, `GPT-4.1 Mini`, `GPT-4.1 Nano`
- report styles: `paper_only_narrative`, `paper_only_decision`
- elicitation modes analyzed:
  - `single w/o explanation`
  - `single with explanation`
  - `joint w/o explanation`
  - `joint with explanation`
- explanation-included modes use the metric of the predictor formed by averaging 5 repeated runs

Scripts:

- `plot_validation_paper_only_narrative_decision.py`
  Builds the main rows table, delta plots, convergence plot, dumbbell plot, and paired-bootstrap correlation significance table.

- `analyze_validation_paper_only_narrative_decision_meta.py`
  Pools the explanation-mode correlation gains with a random-effects meta-analysis and writes the forest plot.

Run:

```bash
python analysis/positive_case/literature_design_space/plot_validation_paper_only_narrative_decision.py
python analysis/positive_case/literature_design_space/analyze_validation_paper_only_narrative_decision_meta.py
```

Convenience wrappers also exist:

```bash
python analysis/plot_validation_paper_only_narrative_decision.py
python analysis/analyze_validation_paper_only_narrative_decision_meta.py
```

Outputs:

- results: `results/validation/positive_case/literature_design_space/`
- plots: `plots/validation/positive_case/literature_design_space/`

Why this folder exists:

- a new thread should not be assumed to retain the chat context from this one
- this README plus the results/plots READMEs are the intended restart point
- the next extension is swapping from the single-paper vector store to the literature vector store and varying paper-level inclusion filters
