import tempfile
import unittest
from collections import OrderedDict
from pathlib import Path
from unittest.mock import patch

import main
from utils.csvio import read_csv


class TestMainCli(unittest.TestCase):
    def test_ground_truth_command_rebuilds_csv_without_browser(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            human_dir = tmp_path / "humans"
            human_dir.mkdir()
            (human_dir / "annotator_a.csv").write_text(
                (
                    "Filename,Granularity,Empirical,Controled_Or_Observational,Lab_Or_Field\n"
                    "paper_a,,1,0,0\n"
                ),
                encoding="utf-8",
            )
            events_csv = tmp_path / "consensus_events.csv"
            events_csv.write_text("consensus_session_id\n", encoding="utf-8")
            out_csv = tmp_path / "ground_truth.csv"

            exit_code = main.main(
                [
                    "ground-truth",
                    "--session",
                    "default",
                    "--human-datasets-dir",
                    str(human_dir),
                    "--consensus-events-csv",
                    str(events_csv),
                    "--out",
                    str(out_csv),
                ]
            )

            self.assertEqual(exit_code, 0)
            rows = read_csv(out_csv)
            self.assertEqual(rows[0]["Filename"], "paper_a")
            self.assertEqual(rows[0]["Empirical"], "1")
            self.assertEqual(rows[0]["Lab_Or_Field"], "0")

    @patch("cli.commands.mismatch_report.write_mismatch_report_markdown")
    @patch("cli.commands.mismatch_report.build_mismatch_report")
    @patch("scripts.feature_accuracy_matrix.main")
    @patch("utils.consensus.export_ground_truth_csv")
    def test_refresh_eval_command_runs_full_pipeline(
        self,
        mock_export_ground_truth: object,
        mock_feature_matrix: object,
        mock_build_mismatch_report: object,
        mock_write_mismatch_report: object,
    ) -> None:
        ground_truth_path = Path("/tmp/ground_truth.csv")
        mismatch_path = Path("/tmp/mismatch.md")

        mock_export_ground_truth.return_value = ground_truth_path
        mock_build_mismatch_report.return_value = {"summary": {}, "reasons": {}, "analysis": {}}
        mock_write_mismatch_report.return_value = mismatch_path

        exit_code = main.main(
            [
                "refresh-eval",
                "--session",
                "default",
                "--reviewer",
                "alice",
                "--eval-scope",
                "lab-only",
            ]
        )

        self.assertEqual(exit_code, 0)
        mock_export_ground_truth.assert_called_once()
        mock_feature_matrix.assert_called_once()
        self.assertEqual(mock_feature_matrix.call_args.kwargs["eval_scope"], "lab-only")
        self.assertEqual(mock_feature_matrix.call_args.kwargs["ground_truth_csv"], str(ground_truth_path))
        mock_build_mismatch_report.assert_called_once()
        self.assertEqual(mock_build_mismatch_report.call_args.kwargs["eval_scope"], "lab-only")
        self.assertEqual(mock_build_mismatch_report.call_args.kwargs["ground_truth_csv"], ground_truth_path)
        mock_write_mismatch_report.assert_called_once_with(
            {"summary": {}, "reasons": {}, "analysis": {}},
            markdown_out="outputs/mismatch.md",
        )

    @patch("utils.consensus.load_human_datasets")
    @patch("cli.commands.mismatch_report.write_mismatch_report_markdown")
    @patch("cli.commands.mismatch_report.build_mismatch_report")
    @patch("scripts.feature_accuracy_matrix.main")
    @patch("utils.consensus.export_ground_truth_csv")
    def test_evaluate_command_runs_pipeline_after_single_annotator_detect(
        self,
        mock_export_ground_truth: object,
        mock_feature_matrix: object,
        mock_build_mismatch_report: object,
        mock_write_mismatch_report: object,
        mock_load_human_datasets: object,
    ) -> None:
        mock_load_human_datasets.return_value = OrderedDict([("only", [])])
        ground_truth_path = Path("/tmp/ground_truth.csv")
        mismatch_path = Path("/tmp/mismatch.md")
        mock_export_ground_truth.return_value = ground_truth_path
        mock_build_mismatch_report.return_value = {"summary": {}, "reasons": {}, "analysis": {}}
        mock_write_mismatch_report.return_value = mismatch_path

        exit_code = main.main(
            [
                "evaluate",
                "--session",
                "default",
                "--reviewer",
                "alice",
                "--eval-scope",
                "lab-only",
            ]
        )

        self.assertEqual(exit_code, 0)
        mock_load_human_datasets.assert_called_once()
        mock_export_ground_truth.assert_called_once()
        mock_feature_matrix.assert_called_once()
        self.assertEqual(mock_feature_matrix.call_args.kwargs["eval_scope"], "lab-only")
