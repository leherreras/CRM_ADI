import names

from app.adapter.inmemory_lead_repository import InMemoryLeadRepository
from app.domain.lead import Lead

user = {
    "identification_number": "123456789",
    "first_name": names.get_first_name(),
    "last_name": names.get_last_name(),
    "email": "test@test.com",
    "birthdate": "01/01/2000"
}


def test_lead_save():
    lead = Lead(**user)
    lead_repository = InMemoryLeadRepository()

    assert lead.save(lead_repository).identification_number == lead.identification_number


def test_lead_repository_all():
    lead_repository = InMemoryLeadRepository()
    lead1 = Lead(**user).save(lead_repository)
    lead2 = Lead(**user).save(lead_repository)

    assert set(lead_repository.all()) == {lead1, lead2}


def test_lead_repository_total():
    lead_repository = InMemoryLeadRepository()
    Lead(**user).save(lead_repository)
    Lead(**user).save(lead_repository)

    assert lead_repository.total() == 2
