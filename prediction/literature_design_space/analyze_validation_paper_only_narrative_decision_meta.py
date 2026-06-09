from __future__ import annotations

import sys
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).resolve().parents[1]
if str(ANALYSIS_ROOT) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_ROOT))

from plot_paths import VALIDATION_LITERATURE_DESIGN_SPACE_PLOTS  # noqa: E402
from positive_case.literature_design_space.analyze_validation_paper_only_narrative_decision_meta import (  # noqa: E402
    configure_context,
    main,
)
from result_paths import VALIDATION_LITERATURE_DESIGN_SPACE_RESULTS  # noqa: E402


configure_context(
    results_dir=VALIDATION_LITERATURE_DESIGN_SPACE_RESULTS,
    plots_dir=VALIDATION_LITERATURE_DESIGN_SPACE_PLOTS,
    output_stem_prefix="validation_literature_design_space",
    plot_context_label="Literature Design Space",
)


if __name__ == "__main__":
    main()
