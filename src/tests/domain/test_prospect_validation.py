from app.domain.prospect_validations import Prospect
from tests.fixtures.user import user


def test_validation():
    assert type(Prospect.validate()) == list


def test_validation_with_id():
    assert type(Prospect.validate(user["identification_number"])) == list
