from abc import ABC, abstractmethod


class UserUseCase(ABC):

    @abstractmethod
    def login(self, name_email: str, password: str):
        ...

    @abstractmethod
    def register(self, username: str, email: str, password: str):
        ...

    @abstractmethod
    def change_password(self, username: str, email: str, password: str):
        ...

    @abstractmethod
    def logout(self) -> None:
        ...
