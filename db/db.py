import os
import bcrypt as bcrypt
import sqlite3

from db.queries import (CREATE_USERS_TABLE, CREATE_PASSWORDS_TABLE,
                        BLOCK_USER, INSERT_PASSWORD, INSERT_USER,
                        SELECT_ALL_PASSWORDS, SELECT_ALL_USERS,
                        UPDATE_PASSWORD)
from typing import List, Tuple, Union

connection = sqlite3.connect("login12.db", check_same_thread=False)


def create_tables() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_PASSWORDS_TABLE)


def add_user(username: str, email: str, blocked: int, password: str) -> None:
    with connection:
        usern = _encrypt_(username)
        connection.execute(INSERT_USER, (
            usern,
            _encrypt_(email),
            blocked), )
        li = [None]*12
        li[0] = usern
        li[1] = _encrypt_(password)
        connection.execute(INSERT_PASSWORD, li)


def block_user(name_email: bytes, block_mode: int) -> None:
    with connection:
        connection.execute(BLOCK_USER, (
            block_mode,
            name_email), )

def get_all_fields(field: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        if field == "users":
            cursor.execute(SELECT_ALL_USERS)
        if field == "passwords":
            cursor.execute(SELECT_ALL_PASSWORDS)
        return cursor.fetchall()

def get_field(name_email: str, field: str, origin: bool = None) -> Union[Tuple or None]:
    with connection:
        all_fields = get_all_fields(field)
        for f in all_fields:
            if _decrypt_(name_email, f[0]):
                li = list(f)
                if origin:
                    return li
                li[0] = name_email
                return tuple(li)


def update_password(password: tuple) -> None:
    with connection:
        connection.execute(UPDATE_PASSWORD, [pas for pas in password])
        connection.commit()


def get_headers(database: str) -> List:
    with connection:
        cursor = connection.execute(f"select * from {database};")
        return list(map(lambda x: x[0], cursor.description))


def _encrypt_(some: str):
    key = int(os.environ.get('SALT_KEY'))
    return bcrypt.hashpw(some.encode("UTF-8"), bcrypt.gensalt(key))


def _decrypt_(x: str, y: bytes) -> bool:
    return bcrypt.checkpw(x.encode("UTF-8"), y)
