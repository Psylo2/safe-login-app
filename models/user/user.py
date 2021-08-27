from dataclasses import dataclass, field
from typing import List
from flask import current_app

from db.db import add_user, block_user, _decrypt_
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

    def save_to_db(self, password: str) -> None:
        add_user(self._name, self._email, self._blocked, password)

    def block_user_model(self, block) -> None:
        block = bytes(block.encode())
        if not _decrypt_(current_app.config["ADMIN"], block):
            block_user(block, 1)

    def unblock_user_model(self, unblock) -> None:
        unblock = bytes(unblock.encode())
        if not _decrypt_(current_app.config["ADMIN"], unblock):
            block_user(unblock, 0)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        return cls.find_one_by(name, cls.DATABASE)

    @classmethod
    def find_all_from_db(cls) -> List["User"]:
        return cls.find_many_by(cls.DATABASE)
