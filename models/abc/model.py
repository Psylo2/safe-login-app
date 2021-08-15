import uuid
from abc import ABCMeta
from typing import TypeVar, Type, List, Union

from db.db import (get_user, get_all_users, get_password,
                   get_all_passwords, get_headers)

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], one: str, header: str = None) -> T:
        if header == "users":
            database = get_user(one)
        else:
            database = get_password(one)
        headers = get_headers(header)  # "passwords" or "users"
        return cls(**cls.strip_tup(headers, database))

    @classmethod
    def find_many_by(cls: Type[T], header: str = None) -> List[T]:
        if header == "users":
            database = get_all_users()
        else:
            database = get_all_passwords()
        headers = get_headers(header)  # "passwords" or "users"
        return [cls(**i) for i in cls.strip_tup(headers, database)]

    @classmethod
    def strip_tup(cls: Type[T], headers: List, database: List) -> Union[list, dict]:
        ret = {}
        ret_dict = {}

        if type(database) is list:
            for data in database:
                for j in range(len(data)):
                    ret_dict.update({headers[j]: data[j]})
                ret.update({uuid.uuid4().int: ret_dict})
                ret_dict = {}
            return list(ret.values())
        else:
            for i in range(len(database)):
                ret.update({headers[i]: database[i]})
            return ret
