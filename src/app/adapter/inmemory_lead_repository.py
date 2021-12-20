from typing import List

from app.domain.lead import Lead
from app.domain.lead_repository import LeadRepository


class InMemoryLeadRepository(LeadRepository):
    """
    Simulates a repository of leads.
    The information is stored in memory.
    """

    def __init__(self):
        self.leads = []

    def get(self, identification_number: str) -> Lead:
        """
        Get a lead by its identification number.
        :param identification_number: the identification number of the lead
        :return: Lead if was found, None otherwise.
        """
        for lead in self.leads:
            if lead.identification_number == identification_number:
                return lead

    def update(self, lead: Lead) -> Lead:
        """
        Update a lead.
        :param lead: Lead to update.
        :return: Lead if was updated, None otherwise.
        """
        for index, l in enumerate(self.leads):
            if l.identification_number == lead.identification_number:
                self.leads[index] = lead
                return lead

    def add(self, lead: Lead) -> Lead:
        """
        Add a lead.
        :param lead: Lead to add.
        :return: Lead added
        """
        self.leads.append(lead)
        return lead

    def all(self) -> List[Lead]:
        """
        Get all leads in the system.
        :return: List with all leads
        """
        return self.leads

    def all_leads(self) -> List[Lead]:
        """
        Get all leads without prospects
        :return: List with leads
        """
        return [lead for lead in self.leads if not lead.prospect]

    def total(self) -> int:
        """
        Count leads in the system
        :return: int with the total
        """
        return len(self.leads)


# Leads are only stored in memory in this variable.
lead_repository = InMemoryLeadRepository()
