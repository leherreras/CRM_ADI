import names

from app.domain.lead import Lead

user = {
    "identification_number": "123456789",
    "first_name": names.get_first_name(),
    "last_name": names.get_last_name(),
    "email": "test@test.com",
    "birthdate": "01/01/2000"
}


def test_lead_existing_lead_id():

    assert Lead(**user).identification_number == user["identification_number"]


def test_lead_defaults():
    assert Lead(**user).identification_number
