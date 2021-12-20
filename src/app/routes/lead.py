from typing import List

from fastapi import APIRouter

from app.adapter.inmemory_lead_repository import lead_repository
from app.domain.lead import Lead

router_lead = APIRouter()


@router_lead.post("/", response_model=Lead)
def create_lead(lead: Lead) -> Lead:
    return lead.save(lead_repository)


@router_lead.get("/count", response_model=int)
def count_all() -> int:
    return lead_repository.total()


@router_lead.get("/all", response_model=List[Lead])
def get_all() -> List[Lead]:
    return lead_repository.all()
