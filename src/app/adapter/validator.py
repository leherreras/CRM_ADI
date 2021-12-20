import os
from urllib.parse import urljoin

import requests

from app.domain.lead import Lead


def national_registry(lead: Lead) -> bool:
    """
    Validates the lead's national registry number.
    """
    url = urljoin(os.environ.get("URL_NATIONAL"), lead.identification_number)
    response = requests.get(url)
    resp_lead = [
        response.json()["identification_number"] == lead.identification_number,
        response.json()["first_name"] == lead.first_name,
        response.json()["last_name"] == lead.last_name,
        response.json()["birthdate"] == lead.birthdate
    ]
    if all(resp_lead):
        return True
    return False


def judicial_registry(lead: Lead) -> bool:
    """
    Validates the lead's juditial registry number.
    """
    url = urljoin(os.environ.get("URL_JUDICIAL"), lead.identification_number)
    response = requests.get(url)
    if response.json()["status"] != "success":
        return False
    return True


def prospect_qualification(lead: Lead) -> bool:
    """
    Validates the lead's prospect qualification.
    """
    url = urljoin(os.environ.get("URL_QUALIFICATION"), lead.identification_number)
    response = requests.post(url)
    return response.json()["qualification"]
