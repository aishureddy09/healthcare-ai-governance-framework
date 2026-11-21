# Responsible AI Governance & Risk Assessment Framework for Healthcare AI

A worked governance framework for one concrete system — **AI-assisted
skin-lesion triage** (a model that orders a clinician's review queue;
prioritisation support only, never autonomous diagnosis) — built around a
machine-readable risk register and a validator that generates the assurance
paperwork from it.

**Research question.** Which risks should developers, healthcare organisations
and decision-makers assess before deploying an AI-assisted skin-lesion system,
and what evidence or controls could reduce those risks?

## What's here

| File | What it is |
|---|---|
| `risk_register.csv` | 18 risks across all 10 lifecycle stages. Each row: harm, affected group, likelihood & severity (1–5) with a written rationale, evidence needed, named owner role, mitigation, monitoring indicator |
| `src/validate_register.py` | Loads and validates the register (required fields, unique IDs, 1–5 scores), scores completeness/traceability, and generates the two reports below |
| `reports/assurance_report.md` | Generated: completeness score, highest-priority risks (score ≥ 15), pre-deployment evidence gate |
| `reports/policy_brief.md` | Generated two-page-style brief: the decision, what the register shows, three recommendations |
| `docs/lifecycle_and_stakeholders.md` | Lifecycle map and stakeholder analysis, cross-referenced to risk IDs |
| `docs/assurance_checklist.md` | Pre- and post-deployment evidence checklist |

## Results (actual run)

```
Risks: 18 | completeness: 100.0% | stages covered: 10/10
high-priority (likelihood x severity >= 15): R01, R04, R05, R06, R09, R10, R11, R13
```

The top of the register is dominated by evidence problems, not exotic ones:
unrepresentative training data (R01, 20/25), class imbalance suppressing
minority-class detection (R04, 25/25), train/test leakage (R05), and deploying
at a new site without external validation (R06). The framework's pre-deployment
gate blocks go-live until those have evidence on file — external validation,
per-class and subgroup sensitivity with intervals, a signed responsibility
matrix (R17), and the intended-use statement (R10).

It pairs with the companion evaluation project
(`skin-lesion-bias-fairness-evaluation`), which produces exactly the per-class
and subgroup evidence this framework demands.

## Run it

```bash
pip install -r requirements.txt
python -m src.validate_register   # regenerates reports/
python -m pytest tests -q         # 4 tests
```

## Limitations — read this before citing it

This is a **desk-research framework written by a student**: it has not been
expert-reviewed, field-tested, or validated against a live deployment. It is
**not legal advice** and does not certify compliance with any law, regulation
or standard. Likelihood/severity scores are reasoned judgements with their
rationales recorded in the register — challenge them there, in the open,
rather than treating the totals as measurements.

## Responsible use

Use it to structure questions and assign owners before a deployment decision.
Do not present a completed checklist as proof that a system is safe.

## Author

Thikkam Aiswarya — MSc Artificial Intelligence with Healthcare, Aston
University. Draws on her dissertation's discussion of false negatives, class
imbalance and explainability in skin-lesion AI, and on her team-lead
experience coordinating data-annotation work. Prepared for the GovAI UK
Summer Fellowship 2027 portfolio.
