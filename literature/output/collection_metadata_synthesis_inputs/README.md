# Metadata Collection Synthesis Inputs

This directory contains the rendered evidence digests and request manifest for
the metadata-filter collection reports.

Source-of-truth generation spec:

- `literature/METADATA_COLLECTIONS.md`

Key files:

- `*.md`
  One paper-set digest per retained metadata collection.

- `request_manifest.csv`
  One row per synthesis request, including:
  - `collection_id`
  - `custom_id`
  - `n_filters`
  - `filter_label`
  - `count`
  - `bundle_chars`
  - `bundle_path`

- `prompt_previews/metadata_collection_prompt_preview.md`
  Preview of the prompt template used to generate the metadata collection
  synthesis reports.

Prompt-format notes:

- The prompt body intentionally omits collection ids and applied-filter
  metadata.
- The digest header keeps only the paper count:
  - `# Paper Set Evidence Digest`
  - `Number of papers in this paper set: N`
  - `Each item below is a compact paper-level analysis digest. Use only this digest.`

The actual batch JSONL emitted from these digests is:

- `openAI_batch_input/synthesis_collection_metadata_filters.jsonl`
