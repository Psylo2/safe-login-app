import sqlite3
from typing import List



CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    email TEXT UNIQUE,
    blocked INTEGER
);"""

CREATE_PASSWORDS_TABLE = """CREATE TABLE IF NOT EXISTS passwords (
    username TEX UNIQUE,
    current_password TEXT,
    password_1 TEXT,
    password_2 TEXT,
    password_3 TEXT,
    password_4 TEXT,
    password_5 TEXT,
    password_6 TEXT,
    password_7 TEXT,
    password_8 TEXT,
    password_9 TEXT,
    password_10 TEXT,
    FOREIGN KEY(username) REFERENCES users(username)
);"""

INSERT_USER = "INSERT INTO users (username, email,  blocked) VALUES (?, ?, ?);"

INSERT_PASSWORD = "INSERT INTO passwords (username, current_password, password_1, password_2, password_3, password_4, password_5, password_6, password_7, password_8, password_9, password_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

SELECT_ALL_USERS = """SELECT * FROM users;"""

SELECT_ALL_PASSWORDS = "SELECT * FROM passwords;"

SELECT_PASSWORD = "SELECT * FROM passwords WHERE username=(?);"

SELECT_USER = "SELECT * FROM users WHERE (?) IN (username, email);"

UPDATE_PASSWORD = "UPDATE passwords SET current_password = (?), password_1 = (?), password_2 = (?), password_3 = (?), password_4 = (?), password_5 = (?), password_6 = (?), password_7 = (?), password_8 = (?), password_9 = (?), password_10 = (?) WHERE username=(?);"

BLOCK_USER = "UPDATE users SET blocked = (?)  WHERE (?) IN (username, email);"

DROP_TABLE_USERS = "DROP TABLE users;"

DROP_TABLE_PASSWORDS = "DROP TABLE passwords;"
