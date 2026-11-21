# Assurance checklist — before and after deployment

A checklist organises evidence; ticking it does **not** certify compliance or
safety. Each item should link to a document a reviewer can open.

## Pre-deployment

- [ ] Intended use written in one sentence and shown in the UI ("prioritisation support only")
- [ ] Dataset audit on file: provenance, class balance, subgroup composition (R01)
- [ ] Test labels histopathology- or consensus-confirmed; label source recorded (R02)
- [ ] Patient-level split audit signed off; near-duplicate check run (R05)
- [ ] Per-class sensitivity reported, including worst-class recall (R04)
- [ ] Subgroup metrics reported **with confidence intervals** and minimum-n rules (R07)
- [ ] External validation on an independent site/device dataset (R06)
- [ ] Operating threshold chosen for sensitivity, with a safety net for low-priority cases (R11)
- [ ] Human-factors check: clinician judgement recorded before model output is shown (R09)
- [ ] DPIA completed; access controls and approved-processor list verified (R15, R16)
- [ ] Installed model version hash matches the validated version (R08)
- [ ] Responsibility matrix signed by named owners (R17)

## Post-deployment

- [ ] Referral volume and positive predictive value reviewed weekly (R12)
- [ ] Sampled false-negative audit every month (R11)
- [ ] Drift metrics reviewed monthly against pre-agreed re-validation triggers (R13)
- [ ] AI-flagged incidents reviewed monthly; themes fed back to developers (R14)
- [ ] Override rates audited quarterly (R09)
- [ ] Access logs reviewed quarterly; DPIA refreshed annually (R15)
- [ ] Exit plan and pathway dependency map kept current (R18)
