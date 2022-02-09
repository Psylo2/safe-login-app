from abc import ABC, abstractmethod
from typing import Dict


class AdminLogicService(ABC):

    @abstractmethod
    def configure_regex(self, data: Dict) -> str:
        ...

    @abstractmethod
    def extract_configuration_fields(self, data: dict) -> Dict:
        ...
