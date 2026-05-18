from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLOTS_ROOT = ROOT / "plots"

VALIDATION_PLOTS = PLOTS_ROOT / "validation"
VALIDATION_NO_AUGMENTATION_MODEL_COMPARISON_PLOTS = (
    VALIDATION_PLOTS / "no_augmentation_model_comparison"
)
VALIDATION_AUGMENTATION_DELTA_MODEL_PLOTS = (
    VALIDATION_PLOTS / "augmentation_delta_by_model"
)
VALIDATION_AUGMENTATION_DELTA_MODEL_SPLIT_PLOTS = (
    VALIDATION_PLOTS / "augmentation_delta_by_model_split"
)
VALIDATION_AUGMENTATION_CONVERGENCE_PLOTS = (
    VALIDATION_PLOTS / "augmentation_convergence"
)
VALIDATION_REASONING_REPEAT_SUMMARY_PLOTS = (
    VALIDATION_PLOTS / "reasoning_repeat_summary"
)
VALIDATION_MODEL_SUITE_COMPREHENSIVE_PLOTS = (
    VALIDATION_PLOTS / "model_suite_comprehensive"
)
VALIDATION_PAPER_ONLY_NARRATIVE_DECISION_PLOTS = (
    VALIDATION_PLOTS / "paper_only_narrative_decision"
)
VALIDATION_LITERATURE_DESIGN_SPACE_PLOTS = (
    VALIDATION_PLOTS / "literature_design_space"
)
VALIDATION_LITERATURE_AUGMENTATION_BACKBONE_PLOTS = (
    VALIDATION_PLOTS / "literature_augmentation_backbone"
)
VALIDATION_POSITIVE_CASE_PLOTS = VALIDATION_PLOTS / "positive_case"
VALIDATION_POSITIVE_CASE_LITERATURE_DESIGN_SPACE_PLOTS = (
    VALIDATION_POSITIVE_CASE_PLOTS / "literature_design_space"
)
LEARNING_PLOTS = PLOTS_ROOT / "learning"
CROSSWAVE_PLOTS = PLOTS_ROOT / "crosswave"
GRANULAR_PLOTS = PLOTS_ROOT / "granular"
POSITIVE_CASE_PLOTS = PLOTS_ROOT / "positive_cases"


def ensure_plot_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path
