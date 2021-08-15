from db.queries import (sqlite3, CREATE_USERS_TABLE, CREATE_PASSWORDS_TABLE,
                        BLOCK_USER, INSERT_PASSWORD, INSERT_USER,
                        SELECT_ALL_PASSWORDS, SELECT_ALL_USERS, SELECT_PASSWORD,
                        SELECT_USER, UPDATE_PASSWORD)
from typing import List

connection = sqlite3.connect("login.db", check_same_thread=False)


def create_tables() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_PASSWORDS_TABLE)


def add_user(username: str, email: str, blocked: int) -> None:
    with connection:
        connection.execute(INSERT_USER, (username, email, blocked))


def add_password(password: tuple) -> None:
    with connection:
        connection.execute(INSERT_PASSWORD, [str(pas) for pas in password])


def block_user(name_email: str, block_mode: int) -> None:
    with connection:
        connection.execute(BLOCK_USER, (block_mode, name_email))


def get_user(name_email: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (name_email,))
        return cursor.fetchone()


def get_all_users() -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_USERS)
        return cursor.fetchall()


def get_password(username: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_PASSWORD, (username,))
        return cursor.fetchone()


def get_all_passwords() -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_PASSWORDS)
        return cursor.fetchall()


def update_password(password: tuple) -> None:
    with connection:
        connection.execute(UPDATE_PASSWORD, [str(pas) for pas in password])
        connection.commit()


def get_headers(database: str) -> List:
    with connection:
        cursor = connection.execute(f"select * from {database};")
        return list(map(lambda x: x[0], cursor.description))
