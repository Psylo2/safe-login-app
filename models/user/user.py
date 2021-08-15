from dataclasses import dataclass, field
from typing import List
from flask import current_app


from db.db import add_user, block_user
from models.abc.model import Model


@dataclass(init=False)
class UserModel:
    _name: str
    _email: str
    _blocked: int = field(default=0)

    def __init__(self, username, email, blocked):
        self._name = username
        self._email = email
        self._blocked = blocked


class User(UserModel, Model):
    DATABASE = "users"

    # TODO: How to call password and save him as well each time
    def save_to_db(self) -> None:
        add_user(self._name, self._email, self._blocked)

    def block_user_model(self) -> None:
        if self._name != current_app.config["ADMIN"]:
            block_user(self._name, 1)

    def unblock_user_model(self) -> None:
        if self._name != current_app.config["ADMIN"]:
            block_user(self._name, 0)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        return cls.find_one_by(name, cls.DATABASE)

    @classmethod
    def find_all_from_db(cls) -> List["User"]:
        return cls.find_many_by(cls.DATABASE)

    # TODO: Implement on login_utils
    #@classmethod
    #def valid_login(cls, name_email: str, password: str) -> bool:
     #   user = cls.find_from_db(name_email,)
      #  return hmac.compare_digest(user._password, password)
