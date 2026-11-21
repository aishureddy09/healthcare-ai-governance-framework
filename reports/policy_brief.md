# Policy brief: governing AI-assisted skin-lesion triage

**Status:** two-page-style brief from a student desk-research framework. Not legal advice; not a validated standard.

## The decision

A skin-lesion AI that *prioritises images for clinician review* can shorten waits — but only if the evidence, oversight and accountability around it are settled before the first patient is triaged by it. The system must never be framed as making the diagnosis.

## What the risk register shows

This framework tracks 18 risks across 10 lifecycle stages, at 100.0% field completeness. The three highest-scoring risks are:

- **R04 — Class imbalance drives the model to under-detect minority classes** (score 25/25). Harm: False negatives concentrated in rare but serious classes. Mitigation: Class weighting or balanced sampling evaluated as a controlled experiment; report worst-class recall.
- **R01 — Unrepresentative training data under-represents darker skin tones** (score 20/25). Harm: Missed or late melanoma detection in under-represented patients. Mitigation: Set minimum subgroup representation thresholds before training; source additional consented data where gaps exist.
- **R06 — No external validation on data from another site or device** (score 20/25). Harm: Performance collapses silently at a new clinic. Mitigation: Require external validation before deployment at any new site; publish site-specific metrics.

## Three recommendations

1. **Evidence before deployment.** Require external validation and per-class, subgroup-reported sensitivity with uncertainty intervals before go-live at any site — headline accuracy is not assurance.
2. **Humans visibly in charge.** Record the clinician's own judgement before revealing model output for high-risk cases, label the tool as prioritisation support only, and audit override rates.
3. **Monitor or withdraw.** Fund rolling drift and false-negative audits with pre-agreed triggers; a system nobody monitors should not stay live.

## What this brief is not

It does not certify compliance with any law or standard. Decision-makers must check current official guidance and take qualified advice for their own deployment.
