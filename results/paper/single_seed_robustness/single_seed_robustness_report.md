# Single-Seed Robustness

This report summarizes whether the Figures 3-8 qualitative claims survive when each analysis is run on a single repeat instead of the 5-repeat mean.

## Heterogeneity Across Augmented Inputs
- Papers: single-seed item SD ranges from 0.054 to 0.103; the share of papers above baseline ranges from 0.08 to 0.95.
- Collections: single-seed item SD ranges from 0.065 to 0.101; the share of collections above baseline ranges from 0.03 to 0.96.

## Cross-Model Ranking Agreement
- Papers: mean pairwise Spearman ranges from 0.171 to 0.190 across the five single repeats.
- Collections: mean pairwise Spearman ranges from 0.226 to 0.264 across the five single repeats.
- Collections exceed papers in every single repeat: True.

## Metadata Predictability
- Individual papers: grouped-CV R2 ranges from 0.029 to 0.037; grouped-CV Spearman ranges from 0.158 to 0.183.
- Collections: grouped-CV R2 ranges from 0.052 to 0.069; grouped-CV Spearman ranges from 0.192 to 0.236.
- Collections exceed papers in grouped-CV R2 in every repeat: True.

## Feature-Direction Trends
- Paper empirical effect: negative in 25/25 model-seed fits; significantly negative in 24/25.
- Collection empirical-share effect: negative in 25/25 model-seed fits; significantly negative in 21/25.
- Paper citation effect: negative in 22/25; significantly negative in 8/25.
- Collection citation effect: negative in 25/25; significantly negative in 15/25.
- Paper journal-impact effect: positive in 18/25; significantly positive in 1/25.
- Collection journal-impact effect: positive in 22/25; significantly positive in 6/25.