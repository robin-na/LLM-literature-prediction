import unittest

from utils.review_state import (
    build_classification_overrides,
    build_paper_notes,
)


class TestReviewState(unittest.TestCase):
    def test_latest_override_wins(self) -> None:
        events = [
            {"action": "set_classification", "key": "a", "new_classification": "match"},
            {"action": "set_classification", "key": "a", "new_classification": "mismatch"},
        ]
        self.assertEqual(build_classification_overrides(events), {"a": "mismatch"})

    def test_auto_clears_override(self) -> None:
        events = [
            {"action": "set_classification", "key": "a", "new_classification": "match"},
            {"action": "set_classification", "key": "a", "new_classification": "__auto"},
        ]
        self.assertEqual(build_classification_overrides(events), {})

    def test_latest_note_wins_per_reviewer(self) -> None:
        events = [
            {
                "action": "set_paper_note",
                "reviewer_id": "alice",
                "key": "paper1",
                "new_value": "first",
            },
            {
                "action": "set_paper_note",
                "reviewer_id": "alice",
                "key": "paper1",
                "new_value": "second",
            },
            {
                "action": "set_paper_note",
                "reviewer_id": "bob",
                "key": "paper1",
                "new_value": "bob-note",
            },
        ]
        self.assertEqual(build_paper_notes(events, "alice"), {"paper1": "second"})
        self.assertEqual(build_paper_notes(events, "bob"), {"paper1": "bob-note"})

    def test_clear_note(self) -> None:
        events = [
            {"action": "set_paper_note", "reviewer_id": "alice", "key": "paper1", "new_value": "x"},
            {"action": "set_paper_note", "reviewer_id": "alice", "key": "paper1", "new_value": ""},
        ]
        self.assertEqual(build_paper_notes(events, "alice"), {})

