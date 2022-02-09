from abc import ABC, abstractmethod

class UserLogicService(ABC):

    @abstractmethod
    def _is_valid_register(self, username: str, email: str, password: str, re_password: str) -> bool:
        ...

    @abstractmethod
    def _is_valid_login(self, name_email: str, password: str) -> bool:
        ...

    @abstractmethod
    def _valid_login(self, name_email: str, password: str) -> bool:
        ...

    @abstractmethod
    def _valid_register(self, username: str, email: str, password: str, re_password: str) -> bool:
        ...
