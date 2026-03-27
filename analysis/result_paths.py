from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS_ROOT = ROOT / "results"

VALIDATION_RESULTS = RESULTS_ROOT / "validation"
VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_RESULTS = (
    VALIDATION_RESULTS / "no_augmentation_model_comparison"
)
VALIDATION_AUGMENTATION_DELTA_MODEL_RESULTS = (
    VALIDATION_RESULTS / "augmentation_delta_by_model"
)
VALIDATION_AUGMENTATION_CONVERGENCE_RESULTS = (
    VALIDATION_RESULTS / "augmentation_convergence"
)
VALIDATION_MODEL_SUITE_COMPREHENSIVE_RESULTS = (
    VALIDATION_RESULTS / "model_suite_comprehensive"
)
VALIDATION_REASONING_REPEAT_SUMMARY_RESULTS = (
    VALIDATION_RESULTS / "reasoning_repeat_summary"
)
VALIDATION_PAPER_ONLY_41FAMILY_RESULTS = (
    VALIDATION_RESULTS / "paper_only_41family"
)
VALIDATION_PAPER_ONLY_NARRATIVE_DECISION_RESULTS = (
    VALIDATION_RESULTS / "paper_only_narrative_decision"
)
VALIDATION_LITERATURE_DESIGN_SPACE_RESULTS = (
    VALIDATION_RESULTS / "literature_design_space"
)
VALIDATION_LITERATURE_AUGMENTATION_BACKBONE_RESULTS = (
    VALIDATION_RESULTS / "literature_augmentation_backbone"
)
VALIDATION_POSITIVE_CASE_RESULTS = VALIDATION_RESULTS / "positive_case"
VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_RESULTS = (
    VALIDATION_POSITIVE_CASE_RESULTS / "literature_design_space"
)

LEARNING_RESULTS = RESULTS_ROOT / "learning"
CROSSWAVE_RESULTS = RESULTS_ROOT / "crosswave"
GRANULAR_RESULTS = RESULTS_ROOT / "granular"
POSITIVE_CASE_RESULTS = RESULTS_ROOT / "positive_cases"


def ensure_results_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path
