import logging
import os
import traceback
from urllib.parse import urljoin

import requests

from app.domain.lead import Lead

logger = logging.getLogger(__name__)


def national_registry(lead: Lead) -> bool:
    """
    Validates the lead's national registry number.
    """
    try:
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
    except Exception:
        logger.error(f"Error: cannot get information from national registry e - {traceback.format_exc()}")
        return False


def judicial_registry(lead: Lead) -> bool:
    """
    Validates the lead's juditial registry number.
    """
    try:
        url = urljoin(os.environ.get("URL_JUDICIAL"), lead.identification_number)
        response = requests.get(url)
        if response.json()["status"] != "success":
            return False
        return True
    except Exception:
        logger.error(f"Error: cannot get information from judicial registry. e - {traceback.format_exc()}")
        return False


def prospect_qualification(lead: Lead) -> int:
    """
    Validates the lead's prospect qualification.
    """
    try:
        url = urljoin(os.environ.get("URL_QUALIFICATION"), lead.identification_number)
        response = requests.post(url)
        return response.json()["qualification"]
    except Exception:
        logger.error(f"Error: cannot get information from prospect. e - {traceback.format_exc()}")
        return 0
