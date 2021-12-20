from typing import List

from fastapi import APIRouter

from app.domain.lead import Lead
from app.domain.prospect_validations import Prospect

router_prospect = APIRouter()


@router_prospect.get("/all", response_model=List[Lead])
def valid_prospect() -> List[Lead]:
    return Prospect.validate()


@router_prospect.get("/{item_id}", response_model=List[Lead])
def valid_prospect(item_id: str) -> List[Lead]:
    return Prospect.validate(item_id)
