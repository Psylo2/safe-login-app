import uuid
from abc import ABCMeta
from typing import TypeVar, Type, List, Union

from db.db import (get_field, get_all_fields,
                   get_headers)

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    @classmethod
    def find_one_by(cls: Type[T], one: str, header: str) -> T:
        database = get_field(one, header)
        headers = get_headers(header)
        return cls(**cls.strip_tup(headers, database))

    @classmethod
    def find_list(cls: Type[T], one: str, header: str, origin: bool = False) -> List:
        if origin:
            return get_field(one, header, origin=True)
        return get_field(one, header, origin=False)

    @classmethod
    def find_many_by(cls: Type[T], header: str) -> List[T]:
        database = get_all_fields(header)
        headers = get_headers(header)
        return [cls(**i) for i in cls.strip_tup(headers, database)]

    @classmethod
    def strip_tup(cls: Type[T], headers: List,
                  database: List) -> Union[list, dict]:
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
