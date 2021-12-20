from dataclasses import dataclass
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.lead_repository import LeadRepository


@dataclass
class Lead(BaseModel):
    """
    National identification number, birthdate, first name, last name, email, etc
    """
    identification_number: str
    first_name: str
    last_name: str
    birthdate: str
    email: str
    prospect: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, lead_repository: "LeadRepository"):
        return lead_repository.add(self)

    def __hash__(self):
        return hash(self.identification_number)
