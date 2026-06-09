import unittest

from utils.eval_scope import EVAL_SCOPE_ALL, EVAL_SCOPE_LAB_ONLY, resolve_evaluation_scope


def _human_row(paper_id: str, *, lab_or_field: str) -> dict[str, str]:
    return {
        "Filename": paper_id,
        "Lab_Or_Field": lab_or_field,
    }


class TestEvalScope(unittest.TestCase):
    def test_all_scope_keeps_requested_papers(self) -> None:
        scope = resolve_evaluation_scope(
            human_rows=[
                _human_row("paper_a", lab_or_field="0"),
                _human_row("paper_b", lab_or_field="1"),
            ],
            requested_paper_ids=["paper_a", "paper_b"],
            eval_scope=EVAL_SCOPE_ALL,
        )

        self.assertEqual(scope.paper_ids, ["paper_a", "paper_b"])
        self.assertEqual(scope.excluded_non_lab_papers, [])

    def test_lab_only_scope_filters_to_lab_papers(self) -> None:
        scope = resolve_evaluation_scope(
            human_rows=[
                _human_row("paper_a", lab_or_field="0"),
                _human_row("paper_b", lab_or_field="1"),
                _human_row("paper_c", lab_or_field="lab"),
            ],
            requested_paper_ids=["paper_a", "paper_b", "paper_c"],
            eval_scope=EVAL_SCOPE_LAB_ONLY,
        )

        self.assertEqual(scope.paper_ids, ["paper_a", "paper_c"])
        self.assertEqual(scope.excluded_non_lab_papers, ["paper_b"])
