from app.domain.lead import Lead
from tests.fixtures.user import user


def test_lead_existing_lead_id():
    assert Lead(**user).identification_number == user["identification_number"]


def test_lead_defaults():
    assert Lead(**user).identification_number
