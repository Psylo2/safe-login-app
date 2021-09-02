CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username BLOB PRIMARY KEY,
    email BLOB UNIQUE,
    blocked INTEGER
);"""

CREATE_PASSWORDS_TABLE = """CREATE TABLE IF NOT EXISTS passwords (
    username BLOB UNIQUE,
    current_password BLOB,
    password_1 BLOB,
    password_2 BLOB,
    password_3 BLOB,
    password_4 BLOB,
    password_5 BLOB,
    password_6 BLOB,
    password_7 BLOB,
    password_8 BLOB,
    password_9 BLOB,
    password_10 BLOB,
    FOREIGN KEY(username) REFERENCES users(username)
);"""
INSERT_USER = "INSERT INTO users (username, email,  blocked) VALUES (%s, %s, %s)"

INSERT_PASSWORD = "INSERT INTO passwords (username, current_password, password_1, password_2, password_3, password_4, password_5, password_6, password_7, password_8, password_9, password_10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

SELECT_ALL_USERS = """SELECT * FROM users;"""

SELECT_ALL_PASSWORDS = "SELECT * FROM passwords;"

UPDATE_PASSWORD = "UPDATE passwords SET current_password = (%s), password_1 = (%s), password_2 = (%s), password_3 = (%s), password_4 = (%s), password_5 = (%s), password_6 = (%s), password_7 = (%s), password_8 = (%s), password_9 = (%s), password_10 = (%s) WHERE username=(%s);"

BLOCK_USER = "UPDATE users SET blocked = (%s)  WHERE username = (%s);"
