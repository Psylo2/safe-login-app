import os
import bcrypt as bcrypt
import mysql.connector

from db.queries import (CREATE_USERS_TABLE, CREATE_PASSWORDS_TABLE,
                        BLOCK_USER, INSERT_PASSWORD, INSERT_USER,
                        SELECT_ALL_PASSWORDS, SELECT_ALL_USERS,
                        UPDATE_PASSWORD)
from typing import List, Tuple, Union

connection = mysql.connector.connect(host=os.environ.get('HOST'),
                                     user=os.environ.get('USER'),
                                     password=os.environ.get('PASSWORD'),
                                     database=os.environ.get('DB'),
                                     port=os.environ.get('PORT')
                                     )


def create_tables() -> None:
    with connection.cursor(buffered=True) as conn:
        conn.execute(CREATE_USERS_TABLE)
        conn.execute(CREATE_PASSWORDS_TABLE)


def add_user(username: str, email: str, blocked: int, password: str) -> None:
    with connection.cursor() as conn:
        usern = _encrypt_(username)
        conn.execute(INSERT_USER, (usern, email, blocked))
        li = [None] * 12
        li[0] = usern
        li[1] = _encrypt_(password)
        conn.execute(INSERT_PASSWORD, li)
        connection.commit()


def block_user(name_email: bytes, block_mode: int) -> None:
    with connection.cursor(buffered=True) as conn:
        conn.execute(BLOCK_USER, (
            block_mode,
            name_email), )


def get_all_fields(field: str) -> connection.cursor():
    with connection.cursor(buffered=True) as conn:
        if field == "users":
            conn.execute(SELECT_ALL_USERS)
        if field == "passwords":
            conn.execute(SELECT_ALL_PASSWORDS)
        return conn.fetchall()


def get_field(name_email: str, field: str, origin: bool = None) -> Union[Tuple or None]:
    all_fields = get_all_fields(field)
    for f in all_fields:
        if _decrypt_(name_email, f[0]):
            li = list(f)
            if origin:
                return li
            li[0] = name_email
            return tuple(li)


def update_password(password: tuple) -> None:
    with connection.cursor(buffered=True) as conn:
        conn.execute(UPDATE_PASSWORD, [pas for pas in password])
        connection.commit()


def get_headers(table: str) -> List:
    with connection.cursor(buffered=True) as conn:
        conn.execute(f"select * from {table};")
        return list(map(lambda x: x[0], conn.description))


def _encrypt_(some: str):
    key = int(os.environ.get('SALT_KEY'))
    return bcrypt.hashpw(some.encode("UTF-8"), bcrypt.gensalt(key))


def _decrypt_(x: str, y: bytes) -> bool:
    return bcrypt.checkpw(x.encode("UTF-8"), y)
