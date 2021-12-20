from typing import List

from app.domain.lead import Lead
from app.domain.lead_repository import LeadRepository


class InMemoryLeadRepository(LeadRepository):
    def __init__(self):
        self.leads = []

    def get(self, identification_number: str) -> Lead:
        for lead in self.leads:
            if lead.identification_number == identification_number:
                return lead

    def update(self, lead: Lead) -> Lead:
        for index, l in enumerate(self.leads):
            if l.identification_number == lead.identification_number:
                self.leads[index] = lead
                return lead

    def add(self, lead: Lead) -> Lead:
        self.leads.append(lead)
        return lead

    def all(self) -> List[Lead]:
        return self.leads

    def all_leads(self) -> List[Lead]:
        return [lead for lead in self.leads if not lead.prospect]

    def total(self) -> int:
        return len(self.leads)


lead_repository = InMemoryLeadRepository()