# Metadata Collection Analysis Reports

This directory contains the synthesized literature reports produced from the
metadata-filter collection digests.

Upstream inputs:

- `openAI_batch_output/synthesis_collection_metadata_filters.jsonl`
- `literature/output/collection_metadata_synthesis_inputs/request_manifest.csv`

Source-of-truth generation spec:

- `literature/METADATA_COLLECTIONS.md`

Key files:

- `*.md`
  One synthesized report per retained metadata collection.

- `report_index.csv`
  Index mapping each rendered report back to its originating `custom_id`,
  collection description, and count.

These reports are the augmentation source for the prediction batch files:

- `openAI_batch_input/prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41.jsonl`
- `openAI_batch_input/prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_41mini.jsonl`
- `openAI_batch_input/prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt51.jsonl`
- `openAI_batch_input/prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5mini.jsonl`
- `openAI_batch_input/prediction_literature_collection_analysis_report_metadata_filters_joint_reps1to5_gpt5nano.jsonl`
