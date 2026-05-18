from __future__ import annotations

import argparse

from cli.commands import (
    cmd_analyze,
    cmd_build,
    cmd_build_dv_taxonomy,
    cmd_clean,
    cmd_consensus,
    cmd_error_analysis,
    cmd_evaluate,
    cmd_feature_matrix,
    cmd_finalize,
    cmd_ground_truth,
    cmd_mismatch_reasons,
    cmd_mismatch_report,
    cmd_mismatch_summary,
    cmd_refresh_eval,
    cmd_test,
    cmd_ui,
)
from utils.eval_scope import EVAL_SCOPE_LAB_ONLY, VALID_EVAL_SCOPES
from utils.paths import CONSENSUS_EVENTS_CSV, FEATURE_MATRIX_SVG, GROUND_TRUTH_CSV, HUMAN_INPUT_DIR


def _add_eval_scope_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--eval-scope",
        default=EVAL_SCOPE_LAB_ONLY,
        choices=list(VALID_EVAL_SCOPES),
        help="Evaluation paper scope (default: lab-only)",
    )


def _add_eval_pipeline_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--session", default="default", help="Session id for consensus and review data")
    parser.add_argument(
        "--reviewer",
        default="",
        help="Reviewer id for refined classifications (default: auto-detect where supported)",
    )
    parser.add_argument(
        "--human-datasets-dir",
        default=str(HUMAN_INPUT_DIR),
        help=f"Human inputs directory (default: {HUMAN_INPUT_DIR})",
    )
    parser.add_argument(
        "--consensus-events-csv",
        default=str(CONSENSUS_EVENTS_CSV),
        help=f"Consensus event log CSV (default: {CONSENSUS_EVENTS_CSV})",
    )
    parser.add_argument(
        "--ground-truth-out",
        default=str(GROUND_TRUTH_CSV),
        help=f"Ground truth CSV output path (default: {GROUND_TRUTH_CSV})",
    )
    parser.add_argument(
        "--image-out",
        default="",
        help=f"Optional matrix image output path (default: {FEATURE_MATRIX_SVG})",
    )
    parser.add_argument(
        "--mismatch-markdown-out",
        default="outputs/mismatch.md",
        help="Optional combined mismatch markdown output path (default: outputs/mismatch.md)",
    )
    parser.add_argument(
        "--max-examples-per-pattern",
        type=int,
        default=5,
        help="Maximum detailed examples to include for each error pattern (default: 5)",
    )
    _add_eval_scope_arg(parser)


def _add_common_parsers(subparsers: argparse._SubParsersAction) -> None:
    subparsers.add_parser("build", help="Regenerate outputs/comparison.html").set_defaults(func=cmd_build)
    subparsers.add_parser("analyze", help="Run meta-analysis into data/").set_defaults(func=cmd_analyze)

    finalize = subparsers.add_parser("finalize", help="Write final reviewed dataset CSV into data/")
    finalize.add_argument("--session", default="default", help="Review session id (default: default)")
    finalize.add_argument("--reviewer", default="anonymous", help="Reviewer id for notes (default: anonymous)")
    finalize.add_argument("--out", default="", help="Optional output path (overrides default)")
    finalize.add_argument(
        "--ground-truth",
        default=str(GROUND_TRUTH_CSV),
        help=f"Ground truth CSV for finalize (default: {GROUND_TRUTH_CSV})",
    )
    finalize.set_defaults(func=cmd_finalize)

    ground_truth = subparsers.add_parser(
        "ground-truth",
        help="Rebuild outputs/ground_truth.csv from inputs/human/ and consensus events",
    )
    ground_truth.add_argument("--session", default="default", help="Consensus session id (default: default)")
    ground_truth.add_argument(
        "--human-datasets-dir",
        default=str(HUMAN_INPUT_DIR),
        help=f"Human dataset directory (default: {HUMAN_INPUT_DIR})",
    )
    ground_truth.add_argument(
        "--consensus-events-csv",
        default=str(CONSENSUS_EVENTS_CSV),
        help=f"Consensus event log CSV (default: {CONSENSUS_EVENTS_CSV})",
    )
    ground_truth.add_argument(
        "--out",
        default=str(GROUND_TRUTH_CSV),
        help=f"Ground truth CSV output path (default: {GROUND_TRUTH_CSV})",
    )
    ground_truth.set_defaults(func=cmd_ground_truth)

    clean = subparsers.add_parser("clean", help="Clean generated analysis dataset artifacts (dry-run by default)")
    clean.add_argument("--yes", action="store_true", help="Delete files. Without this flag, only print what would be removed.")
    clean.set_defaults(func=cmd_clean)

    subparsers.add_parser("feature-matrix", help="Print per-feature LLM vs human accuracy matrix in terminal")
    feature_matrix = subparsers.choices["feature-matrix"]
    feature_matrix.add_argument("--image-out", default="", help=f"Optional output path for matrix image (default: {FEATURE_MATRIX_SVG})")
    feature_matrix.add_argument("--session", default="default", help="Review session id to use for refined classifications (default: default)")
    feature_matrix.add_argument("--reviewer", default="", help="Reviewer id to use for refined classifications (default: auto-detect latest reviewer for session)")
    feature_matrix.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV to use (default: {GROUND_TRUTH_CSV})")
    _add_eval_scope_arg(feature_matrix)
    feature_matrix.set_defaults(func=cmd_feature_matrix)

    mismatch_summary = subparsers.add_parser("mismatch-summary", help="Write per-field mismatch summary into outputs/")
    mismatch_summary.add_argument("--session", default="default", help="Review session id to use for refined classifications (default: default)")
    mismatch_summary.add_argument("--reviewer", default="anonymous", help="Reviewer id to use for refined classifications (default: anonymous)")
    mismatch_summary.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV to use (default: {GROUND_TRUTH_CSV})")
    mismatch_summary.add_argument("--out", default="outputs/mismatch_summary.md", help="Optional output path for summary report (default: outputs/mismatch_summary.md)")
    _add_eval_scope_arg(mismatch_summary)
    mismatch_summary.set_defaults(func=cmd_mismatch_summary)

    mismatch_reasons = subparsers.add_parser("mismatch-reasons", help="Write mismatch examples with LLM reasons into outputs/")
    mismatch_reasons.add_argument("--session", default="default", help="Review session id to use for refined classifications (default: default)")
    mismatch_reasons.add_argument("--reviewer", default="", help="Reviewer id to use for refined classifications (default: auto-detect latest reviewer for session)")
    mismatch_reasons.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV to use (default: {GROUND_TRUTH_CSV})")
    mismatch_reasons.add_argument("--markdown-out", default="outputs/mismatch_reason_report.md", help="Optional markdown output path (default: outputs/mismatch_reason_report.md)")
    mismatch_reasons.add_argument("--csv-out", default="outputs/mismatch_reason_examples.csv", help="Optional CSV output path (default: outputs/mismatch_reason_examples.csv)")
    _add_eval_scope_arg(mismatch_reasons)
    mismatch_reasons.set_defaults(func=cmd_mismatch_reasons)

    error_analysis = subparsers.add_parser("error-analysis", help="Write a prompt-oriented analysis of LLM error patterns into outputs/")
    error_analysis.add_argument("--session", default="default", help="Review session id to use for refined classifications (default: default)")
    error_analysis.add_argument("--reviewer", default="", help="Reviewer id to use for refined classifications (default: auto-detect latest reviewer for session)")
    error_analysis.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV to use (default: {GROUND_TRUTH_CSV})")
    error_analysis.add_argument("--markdown-out", default="outputs/llm_error_analysis_report.md", help="Optional markdown output path (default: outputs/llm_error_analysis_report.md)")
    error_analysis.add_argument("--max-examples-per-pattern", type=int, default=5, help="Maximum detailed examples to include for each error pattern (default: 5)")
    _add_eval_scope_arg(error_analysis)
    error_analysis.set_defaults(func=cmd_error_analysis)

    mismatch_report_parser = subparsers.add_parser("mismatch-report", help="Write one combined mismatch report into outputs/")
    mismatch_report_parser.add_argument("--session", default="default", help="Review session id to use for refined classifications (default: default)")
    mismatch_report_parser.add_argument("--reviewer", default="", help="Reviewer id to use for refined classifications (default: auto-detect latest reviewer for session)")
    mismatch_report_parser.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV to use (default: {GROUND_TRUTH_CSV})")
    mismatch_report_parser.add_argument("--markdown-out", default="outputs/mismatch.md", help="Optional markdown output path (default: outputs/mismatch.md)")
    mismatch_report_parser.add_argument("--max-examples-per-pattern", type=int, default=5, help="Maximum detailed examples to include for each error pattern (default: 5)")
    _add_eval_scope_arg(mismatch_report_parser)
    mismatch_report_parser.set_defaults(func=cmd_mismatch_report)

    evaluate = subparsers.add_parser("evaluate", help="Auto-detect annotator count; write ground truth + matrix + mismatch report")
    _add_eval_pipeline_args(evaluate)
    evaluate.set_defaults(func=cmd_evaluate)

    refresh_eval = subparsers.add_parser("refresh-eval", help="Refresh ground truth, feature matrix, and mismatch reports")
    _add_eval_pipeline_args(refresh_eval)
    refresh_eval.set_defaults(func=cmd_refresh_eval)

    subparsers.add_parser("test", help="Run unit tests under tests/").set_defaults(func=cmd_test)

    build_dv_taxonomy = subparsers.add_parser("build-dv-taxonomy", help="Build or refresh the DV canonical taxonomy JSON via GPT-4.1")
    build_dv_taxonomy.add_argument("--model", default="gpt-4.1", help="OpenAI model to use for taxonomy building (default: gpt-4.1)")
    build_dv_taxonomy.set_defaults(func=cmd_build_dv_taxonomy)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Human vs LLM extraction comparison tools.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    ui = sub.add_parser("ui", help="Build UI then start local review server")
    ui.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    ui.add_argument("--port", type=int, default=8000, help="Port to bind (default: 8000)")
    ui.add_argument("--reload", action="store_true", help="Auto-reload server on code changes")
    ui.add_argument("--open", action="store_true", help="Open the UI in your browser")
    ui.add_argument("--ground-truth", default=str(GROUND_TRUTH_CSV), help=f"Ground truth CSV for Stage 2 review (default: {GROUND_TRUTH_CSV})")
    ui.set_defaults(func=cmd_ui)

    consensus = sub.add_parser("consensus", help="Build consensus UI then start local server")
    consensus.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    consensus.add_argument("--port", type=int, default=8000, help="Port to bind (default: 8000)")
    consensus.add_argument("--reload", action="store_true", help="Auto-reload server on code changes")
    consensus.add_argument("--open", action="store_true", help="Open the consensus UI in your browser")
    consensus.set_defaults(func=cmd_consensus)

    _add_common_parsers(sub)
    return parser
