import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.validate_register import REQUIRED, load_register, validate, risk_score

ROOT = Path(__file__).resolve().parents[1]


def test_real_register_is_valid_and_complete():
    rows = load_register(ROOT / "risk_register.csv")
    errors, warnings, stats = validate(rows)
    assert errors == [] and stats["completeness_pct"] == 100.0
    assert stats["n_risks"] >= 15
    assert stats["stages_missing"] == []


def test_empty_field_and_duplicate_id_are_errors():
    rows = load_register(ROOT / "risk_register.csv")
    bad = [dict(r) for r in rows[:2]]
    bad[1]["risk_id"] = bad[0]["risk_id"]
    bad[1]["owner"] = ""
    errors, _, _ = validate(bad)
    assert any("duplicate" in e for e in errors)
    assert any("owner" in e for e in errors)


def test_score_out_of_range_is_error():
    rows = [dict(load_register(ROOT / "risk_register.csv")[0])]
    rows[0]["severity"] = "9"
    errors, _, _ = validate(rows)
    assert any("severity" in e for e in errors)


def test_risk_score_and_required_columns():
    row = load_register(ROOT / "risk_register.csv")[0]
    assert risk_score(row) == int(row["likelihood"]) * int(row["severity"])
    assert set(REQUIRED) <= set(row.keys())
