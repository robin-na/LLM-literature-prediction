from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from batch_processing.hybrid_extract_app import is_derived_markdown_dir, resolve_paper_dir


class HybridExtractAppTests(unittest.TestCase):
    def test_is_derived_markdown_dir_flags_report_paths(self):
        path = Path("literature/output/paper_analysis_reports/broad_all")
        self.assertTrue(is_derived_markdown_dir(path))

    def test_resolve_paper_dir_rejects_derived_markdown(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            derived_dir = Path(temp_dir) / "paper_card_memos" / "strict_predictive_empirical_payoff"
            derived_dir.mkdir(parents=True)

            with self.assertRaisesRegex(ValueError, "derived markdown"):
                resolve_paper_dir(str(derived_dir))

    def test_resolve_paper_dir_accepts_regular_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir = Path(temp_dir) / "raw_markdown"
            raw_dir.mkdir()

            self.assertEqual(resolve_paper_dir(str(raw_dir)), raw_dir)


if __name__ == "__main__":
    unittest.main()
