from typing import List

from fastapi import APIRouter

from app.domain.lead import Lead
from app.domain.prospect_validations import Prospect

router_prospect = APIRouter()


@router_prospect.get("/", response_model=List[Lead])
def valid_prospect() -> List[Lead]:
    """
    Valid if the leads in the system are prospects
    :return: List of prospects
    """
    return Prospect.validate()


@router_prospect.get("/{lead_id}", response_model=List[Lead])
def valid_prospect(lead_id: str) -> List[Lead]:
    """
    Valid if the specific lead is prospect
    :param lead_id: the identification number of lead
    :return: list with the lead updated if pass the prospect validation
    """
    return Prospect.validate(lead_id)
