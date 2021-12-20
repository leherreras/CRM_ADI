import logging
import threading
from typing import List

from app.adapter.inmemory_lead_repository import InMemoryLeadRepository
from app.adapter.inmemory_lead_repository import lead_repository
from app.adapter.validator import national_registry, judicial_registry, prospect_qualification
from app.domain.lead import Lead

logger = logging.getLogger(__name__)


class Prospect:
    @staticmethod
    def validate(identification_number: str = None) -> List[Lead]:
        """
        Validate in different platforms if the leads can be prospects
        :param identification_number: identification number of lead (optional)
        :return: List with leads that pass to prospect
        """
        logger.info("Validate the leads")
        leads_resp = []

        # Get one or many leads from the repository
        if not identification_number:
            leads = lead_repository.all_leads()
        else:
            leads = [InMemoryLeadRepository().get(identification_number)]

        # Validate leads to pass to prospect
        for lead in leads:
            national_threading = threading.Thread(target=national_registry, args=[lead])

            judicial_threading = threading.Thread(target=judicial_registry, args=[lead])
            national_threading.start()
            judicial_threading.start()
            national_threading.join()
            judicial_threading.join()
            if national_threading and judicial_threading and prospect_qualification(lead) > 60:
                lead.prospect = True
                lead = lead_repository.update(lead)
                leads_resp.append(lead)
        return leads_resp
