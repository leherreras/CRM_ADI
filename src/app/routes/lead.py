from typing import List

from fastapi import APIRouter

from app.adapter.inmemory_lead_repository import lead_repository
from app.domain.lead import Lead

router_lead = APIRouter()


@router_lead.post("/", response_model=Lead)
def create_lead(lead: Lead) -> Lead:
    """
    Create lead
    :param lead: lead data
    :return: Lead created in the system
    """
    return lead.save(lead_repository)


@router_lead.get("/count", response_model=int)
def count_all() -> int:
    """
    Number of leads in the system
    :return: int with the number of leads
    """
    return lead_repository.total()


@router_lead.get("/all", response_model=List[Lead])
def get_all() -> List[Lead]:
    """
    Get all leas in the system
    :return: List of leads
    """
    return lead_repository.all()
