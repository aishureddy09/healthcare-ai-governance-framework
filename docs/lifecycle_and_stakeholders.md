# Lifecycle and stakeholder map — AI-assisted skin-lesion triage

**System definition.** A model that receives a dermoscopic image and returns a
priority score used to order a clinician review queue. Intended use:
*prioritisation support only — not autonomous diagnosis, not discharge.*

## Lifecycle (each stage maps to risks in `risk_register.csv`)

| Stage | Key activities | Register risks |
|---|---|---|
| Data collection | Image acquisition, consent, provenance, representation audit | R01, R02 |
| Annotation | Labelling, consensus, disagreement handling | R03 |
| Development | Training, patient-level splits, imbalance handling | R04, R05 |
| Validation | Held-out, subgroup and external validation with intervals | R06, R07 |
| Procurement | Version pinning, contracts, change control | R08 |
| Deployment | Intended-use framing, thresholds, human factors, safety-netting | R09–R12 |
| Monitoring | Drift audits, incident reporting, false-negative sampling | R13, R14 |
| Privacy & security | DPIA, access control, approved processors only | R15, R16 |
| Accountability | Named owners, responsibility matrix, governance board | R17 |
| Retirement | Dependency mapping, exit plan, pathway notification | R18 |

## Stakeholders and what they are owed

- **Patients** — an accurate, fair queue position; privacy; a route to redress.
- **Clinicians (dermatologists, GPs)** — honest uncertainty, the right to override, no silent scope creep.
- **Developers** — clear intended use, confirmed labels, feedback from deployment audits.
- **Data providers / annotators** — consent-respecting use, credit, disagreement preserved not erased.
- **Hospital leadership / service managers** — capacity impact (false positives) and drift reports they can act on.
- **Regulators & commissioners** — traceable evidence: this register, validation reports, incident logs.
- **Affected communities** — representation in the data and in subgroup reporting, especially groups historically under-imaged in dermatology archives.

## How this connects to Project 1

The companion project (`skin-lesion-bias-fairness-evaluation`) supplies the
worked technical evidence this framework asks for: per-class recall, a
class-weighting experiment, and subgroup reporting with confidence intervals.
Governance without those numbers is paperwork; numbers without governance
have no owner. The two projects are designed to be read together.
