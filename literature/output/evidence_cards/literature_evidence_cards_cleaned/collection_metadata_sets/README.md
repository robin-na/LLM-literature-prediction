# Metadata Collection Sets

This directory contains the generated metadata-filter collection artifacts.

Source-of-truth documentation:

- `literature/METADATA_COLLECTIONS.md`

Key files:

- `collection_metadata_catalog.csv`
  Enriched paper catalog used to build all metadata-filter collections.

- `collection_metadata_summary.csv`
  One row per retained collection, including `collection_id`, `filter_label`,
  paper count, and the path to the per-collection `custom_id` list.

- `collection_metadata_summary.json`
  Run-level metadata including:
  - exclusion rules
  - quartile split thresholds
  - bucket counts
  - retained collection counts by filter depth

- `sets/*.csv`
  One `custom_id` list per retained collection.

Current generation settings in this workspace:

- `max_filters = 3`
- `min_papers = 2`
- `PGG_MS_202502` excluded globally
- citation source: `Times Cited, All Databases`
- discipline source: `WoS Categories`

The retained collection universe is not disjoint. In particular,
`discipline_coarse` is multi-label, so a paper may appear in multiple
discipline-filtered collections.
