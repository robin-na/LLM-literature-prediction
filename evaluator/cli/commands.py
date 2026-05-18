from __future__ import annotations

import argparse
import os
import unittest
import webbrowser
from dataclasses import dataclass
from pathlib import Path

from scripts import llm_error_analysis_report, mismatch_reason_report, mismatch_report
from utils.paths import GROUND_TRUTH_CSV, LLM_DATASET_CSV


@dataclass(frozen=True)
class UiArgs:
    host: str
    port: int
    reload: bool
    open_browser: bool
    ground_truth: Path


def cmd_build(_: argparse.Namespace) -> int:
    from scripts import generate_comparison

    ground_truth = Path(str(getattr(_, "ground_truth", GROUND_TRUTH_CSV))).expanduser().resolve()
    generate_comparison.main(ground_truth_csv=ground_truth)
    return 0


def cmd_analyze(_: argparse.Namespace) -> int:
    from scripts import meta_analysis

    meta_analysis.main()
    return 0


def cmd_test(_: argparse.Namespace) -> int:
    suite = unittest.TestLoader().discover("tests", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


def cmd_finalize(ns: argparse.Namespace) -> int:
    from utils.finalize import FinalizePaths, materialize_final_dataset, write_final_dataset
    from utils.paths import REVIEW_EVENTS_CSV, STATE_DIR

    out_path = STATE_DIR / f"final_review_dataset__{ns.session}__{ns.reviewer}.csv"
    if ns.out:
        out_path = Path(str(ns.out)).expanduser().resolve()
    ground_truth = Path(str(getattr(ns, "ground_truth", GROUND_TRUTH_CSV))).expanduser().resolve()

    rows = materialize_final_dataset(
        FinalizePaths(
            human_csv=ground_truth,
            llm_csv=LLM_DATASET_CSV,
            review_events_csv=REVIEW_EVENTS_CSV,
            out_csv=out_path,
        ),
        review_session_id=str(ns.session),
        reviewer_id=str(ns.reviewer),
    )
    write_final_dataset(rows, out_path)
    print(str(out_path))
    return 0


def cmd_clean(ns: argparse.Namespace) -> int:
    from scripts.clean_generated_datasets import clean_generated_datasets

    dry_run = not bool(ns.yes)
    affected = clean_generated_datasets(dry_run=dry_run)
    action = "Would remove" if dry_run else "Removed"
    if not affected:
        print("No generated dataset artifacts found.")
        return 0

    for path in affected:
        print(f"{action}: {path}")
    print(f"{action} {len(affected)} file(s).")
    if dry_run:
        print("Dry run only. Re-run with --yes to delete these files.")
    return 0


def cmd_feature_matrix(_: argparse.Namespace) -> int:
    from scripts import feature_accuracy_matrix
    from utils.eval_scope import EVAL_SCOPE_ALL

    feature_accuracy_matrix.main(
        image_out=getattr(_, "image_out", ""),
        review_session_id=str(getattr(_, "session", "default")),
        reviewer_id=str(getattr(_, "reviewer", "")),
        ground_truth_csv=str(getattr(_, "ground_truth", "")),
        eval_scope=str(getattr(_, "eval_scope", EVAL_SCOPE_ALL)),
    )
    return 0


def cmd_mismatch_summary(ns: argparse.Namespace) -> int:
    from utils.eval_scope import EVAL_SCOPE_ALL
    from utils.paper_mismatches import mismatch_summary, render_mismatch_summary_report, write_mismatch_summary_report

    summary = mismatch_summary(
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "anonymous")),
        ground_truth_csv=str(getattr(ns, "ground_truth", "")),
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
    )
    out_path = write_mismatch_summary_report(summary, getattr(ns, "out", ""))
    print(render_mismatch_summary_report(summary))
    print("")
    print(f"Saved mismatch summary: {out_path}")
    return 0


def cmd_mismatch_reasons(ns: argparse.Namespace) -> int:
    from utils.eval_scope import EVAL_SCOPE_ALL

    report = mismatch_reason_report.build_mismatch_reason_report(
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "")),
        ground_truth_csv=str(getattr(ns, "ground_truth", "")),
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
    )
    markdown_path, csv_path = mismatch_reason_report.write_mismatch_reason_outputs(
        report,
        markdown_out=str(getattr(ns, "markdown_out", "")),
        csv_out=str(getattr(ns, "csv_out", "")),
    )
    print(mismatch_reason_report.render_mismatch_reason_markdown(report))
    print("")
    print(f"Saved mismatch reason report: {markdown_path}")
    print(f"Saved mismatch reason CSV: {csv_path}")
    return 0


def cmd_error_analysis(ns: argparse.Namespace) -> int:
    from utils.eval_scope import EVAL_SCOPE_ALL

    report = llm_error_analysis_report.build_error_analysis_report(
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "")),
        ground_truth_csv=str(getattr(ns, "ground_truth", "")),
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
        max_examples_per_pattern=int(getattr(ns, "max_examples_per_pattern", 5)),
    )
    markdown_path = llm_error_analysis_report.write_error_analysis_markdown(
        report,
        markdown_out=str(getattr(ns, "markdown_out", "")),
    )
    print(llm_error_analysis_report.render_error_analysis_markdown(report))
    print("")
    print(f"Saved error analysis report: {markdown_path}")
    return 0


def cmd_mismatch_report(ns: argparse.Namespace) -> int:
    from utils.eval_scope import EVAL_SCOPE_ALL

    report = mismatch_report.build_mismatch_report(
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "")),
        ground_truth_csv=str(getattr(ns, "ground_truth", "")),
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
        max_examples_per_pattern=int(getattr(ns, "max_examples_per_pattern", 5)),
    )
    markdown_path = mismatch_report.write_mismatch_report_markdown(
        report,
        markdown_out=str(getattr(ns, "markdown_out", "")),
    )
    print(mismatch_report.render_mismatch_report_markdown(report))
    print("")
    print(f"Saved mismatch report: {markdown_path}")
    return 0


def cmd_build_dv_taxonomy(ns: argparse.Namespace) -> int:
    from scripts.build_dv_taxonomy import build_taxonomy, print_taxonomy

    model = str(getattr(ns, "model", "gpt-4.1"))
    taxonomy = build_taxonomy(model=model)
    print_taxonomy(taxonomy)
    return 0


def cmd_ground_truth(ns: argparse.Namespace) -> int:
    from utils.consensus import export_ground_truth_csv
    from utils.paths import CONSENSUS_EVENTS_CSV

    out_path = export_ground_truth_csv(
        consensus_session_id=str(getattr(ns, "session", "default")),
        human_datasets_dir=Path(str(getattr(ns, "human_datasets_dir", ""))).expanduser().resolve(),
        consensus_events_csv=Path(str(getattr(ns, "consensus_events_csv", ""))).expanduser().resolve(),
        out_csv=Path(str(getattr(ns, "out", ""))).expanduser().resolve(),
    )
    print(str(out_path))
    return 0


def _ensure_dv_taxonomy() -> None:
    from utils.dv_taxonomy import TAXONOMY_PATH

    if TAXONOMY_PATH.exists():
        return
    print("DV taxonomy not found — building automatically (requires OPENAI_API_KEY)...")
    try:
        from scripts.build_dv_taxonomy import build_taxonomy

        build_taxonomy()
        print("DV taxonomy built and saved.")
    except Exception as exc:
        print(f"Warning: could not build DV taxonomy ({exc}).")
        print("DVs/DVs_Definitions comparison will use word-vector fallback matching.")


def _run_feature_matrix_and_mismatch(*, ground_truth_path: Path, ns: argparse.Namespace) -> Path:
    from scripts import feature_accuracy_matrix
    from utils.eval_scope import EVAL_SCOPE_ALL

    feature_accuracy_matrix.main(
        image_out=str(getattr(ns, "image_out", "")),
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "")),
        ground_truth_csv=str(ground_truth_path),
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
    )

    report = mismatch_report.build_mismatch_report(
        review_session_id=str(getattr(ns, "session", "default")),
        reviewer_id=str(getattr(ns, "reviewer", "")),
        ground_truth_csv=ground_truth_path,
        eval_scope=str(getattr(ns, "eval_scope", EVAL_SCOPE_ALL)),
        max_examples_per_pattern=int(getattr(ns, "max_examples_per_pattern", 5)),
    )
    return mismatch_report.write_mismatch_report_markdown(
        report,
        markdown_out=str(getattr(ns, "mismatch_markdown_out", "")),
    )


def cmd_refresh_eval(ns: argparse.Namespace) -> int:
    _ensure_dv_taxonomy()
    from utils.consensus import export_ground_truth_csv

    ground_truth_path = export_ground_truth_csv(
        consensus_session_id=str(getattr(ns, "session", "default")),
        human_datasets_dir=Path(str(getattr(ns, "human_datasets_dir", ""))).expanduser().resolve(),
        consensus_events_csv=Path(str(getattr(ns, "consensus_events_csv", ""))).expanduser().resolve(),
        out_csv=Path(str(getattr(ns, "ground_truth_out", ""))).expanduser().resolve(),
    )
    print(f"Refreshed ground truth: {ground_truth_path}")

    markdown_path = _run_feature_matrix_and_mismatch(ground_truth_path=ground_truth_path, ns=ns)
    print(f"Saved mismatch report: {markdown_path}")
    return 0


def cmd_evaluate(ns: argparse.Namespace) -> int:
    _ensure_dv_taxonomy()
    from utils.consensus import export_ground_truth_csv, load_human_datasets

    human_dir = Path(str(getattr(ns, "human_datasets_dir", ""))).expanduser().resolve()
    try:
        datasets = load_human_datasets(human_dir)
    except ValueError as exc:
        print(str(exc))
        return 1

    n = len(datasets)
    if n == 1:
        print("Single annotator detected — materializing that file as ground truth.")
    else:
        print(f"Multiple annotators ({n}) detected — building consensus ground truth from inputs and saved events.")

    ground_truth_path = export_ground_truth_csv(
        consensus_session_id=str(getattr(ns, "session", "default")),
        human_datasets_dir=human_dir,
        consensus_events_csv=Path(str(getattr(ns, "consensus_events_csv", ""))).expanduser().resolve(),
        out_csv=Path(str(getattr(ns, "ground_truth_out", ""))).expanduser().resolve(),
    )
    print(f"Wrote ground truth: {ground_truth_path}")

    markdown_path = _run_feature_matrix_and_mismatch(ground_truth_path=ground_truth_path, ns=ns)
    print(f"Saved mismatch report: {markdown_path}")
    return 0


def _parse_ui_args(ns: argparse.Namespace) -> UiArgs:
    return UiArgs(
        host=str(ns.host),
        port=int(ns.port),
        reload=bool(ns.reload),
        open_browser=bool(ns.open),
        ground_truth=Path(str(ns.ground_truth)).expanduser().resolve(),
    )


def _run_uvicorn(host: str, port: int, reload: bool) -> None:
    import uvicorn

    uvicorn.run(
        "server.app:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info",
    )


def cmd_ui(ns: argparse.Namespace) -> int:
    args = _parse_ui_args(ns)
    os.environ["STAGE2_GROUND_TRUTH_CSV"] = str(args.ground_truth)
    cmd_build(ns)

    url = f"http://{args.host}:{args.port}"
    if args.open_browser:
        webbrowser.open(url)

    _run_uvicorn(host=args.host, port=args.port, reload=args.reload)
    return 0


def cmd_consensus(ns: argparse.Namespace) -> int:
    from scripts import generate_consensus

    generate_consensus.main()

    host = str(ns.host)
    port = int(ns.port)
    reload = bool(ns.reload)
    open_browser = bool(ns.open)
    url = f"http://{host}:{port}/consensus"
    if open_browser:
        webbrowser.open(url)
    _run_uvicorn(host=host, port=port, reload=reload)
    return 0
