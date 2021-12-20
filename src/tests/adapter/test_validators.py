from app.adapter.validator import national_registry, judicial_registry, prospect_qualification
from app.domain.lead import Lead

from tests.fixtures.user import user


def test_national_registry():
    lead = Lead(**user)
    nag_reg = national_registry(lead)
    assert type(nag_reg) == bool


def test_judicial_registry():
    lead = Lead(**user)
    jud_reg = judicial_registry(lead)
    assert type(jud_reg) == bool


def test_prospect_qualification():
    lead = Lead(**user)
    pros_que = prospect_qualification(lead)
    assert type(pros_que) == int
