import abc
from typing import List

from app.domain.lead import Lead


class LeadRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, lead: Lead) -> Lead:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Lead]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
