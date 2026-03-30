from __future__ import annotations

import unittest

from batch_processing.extraction_pipeline import (
    DEFAULT_HYBRID_AGENTIC_FIELDS,
    merge_agentic_fields_into_rows,
    simple_fields,
)


class ExtractionPipelineTests(unittest.TestCase):
    def test_simple_fields_excludes_agentic_fields(self):
        result = simple_fields()
        for field in DEFAULT_HYBRID_AGENTIC_FIELDS:
            self.assertNotIn(field, result)
        self.assertIn("CONFIG_chat", result)

    def test_merge_agentic_fields_overrides_target_field_only(self):
        rows = [
            {
                "custom_id": "paper-1",
                "data_id": "Control",
                "CONFIG_MPCR": "N/R",
                "CONFIG_MPCR_reason": "",
                "CONFIG_MPCR_confidence": 0,
                "CONFIG_chat": 0,
                "CONFIG_chat_reason": "simple extraction",
                "CONFIG_chat_confidence": 0.8,
            }
        ]
        agentic_results = {
            "CONFIG_MPCR": {
                "final_output": {
                    "experiments": [
                        {
                            "data_id": "Control",
                            "CONFIG_MPCR": 0.4,
                            "CONFIG_MPCR_reason": "coefficient on the public-good term",
                            "CONFIG_MPCR_confidence": 0.95,
                        }
                    ]
                },
                "validation": {"ok": True, "errors": [], "warnings": []},
                "critic_rounds": [],
            }
        }

        merged_rows, metadata_rows = merge_agentic_fields_into_rows(
            simple_rows=rows,
            agentic_results=agentic_results,
        )

        self.assertEqual(merged_rows[0]["CONFIG_MPCR"], 0.4)
        self.assertEqual(merged_rows[0]["CONFIG_MPCR_confidence"], 0.95)
        self.assertEqual(merged_rows[0]["CONFIG_chat"], 0)
        self.assertEqual(len(metadata_rows), 1)
        self.assertEqual(metadata_rows[0]["field"], "CONFIG_MPCR")


if __name__ == "__main__":
    unittest.main()
