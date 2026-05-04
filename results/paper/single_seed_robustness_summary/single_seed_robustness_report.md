# Single-Seed Robustness Summary

This report uses one repeat at a time and asks whether the Figures 3-8 qualitative claims still hold.

## Heterogeneity Across Inputs
- Papers: item SD ranges from 0.054 to 0.103; share above baseline ranges from 0.08 to 0.95.
- Collections: item SD ranges from 0.065 to 0.101; share above baseline ranges from 0.03 to 0.96.

## Cross-Model Ranking Agreement
- Papers: mean pairwise Spearman ranges from 0.171 to 0.190.
- Collections: mean pairwise Spearman ranges from 0.226 to 0.264.
- Collections exceed papers in every repeat: True.

## Metadata Predictability
- Papers: grouped-CV R2 ranges from 0.029 to 0.037; grouped-CV Spearman ranges from 0.158 to 0.183.
- Collections: grouped-CV R2 ranges from 0.052 to 0.069; grouped-CV Spearman ranges from 0.192 to 0.236.
- Collections exceed papers in grouped-CV R2 in every repeat: True.

## Feature Direction Trends (Point Estimates)
- Paper empirical effect is negative in 5/5 model-seed fits.
- Collection empirical-share effect is negative in 5/5 model-seed fits.
- Paper citation effect is negative in 5/5 model-seed fits.
- Collection citation effect is negative in 5/5 model-seed fits.
- Paper journal-impact effect is positive in 5/5 model-seed fits.
- Collection journal-impact effect is positive in 5/5 model-seed fits.