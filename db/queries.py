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

INSERT_USER = "INSERT INTO users (username, email,  blocked) VALUES (?, ?, ?);"

INSERT_PASSWORD = "INSERT INTO passwords (username, current_password, password_1, password_2, password_3, password_4, password_5, password_6, password_7, password_8, password_9, password_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

SELECT_ALL_USERS = """SELECT * FROM users;"""

SELECT_ALL_PASSWORDS = "SELECT * FROM passwords;"

UPDATE_PASSWORD = "UPDATE passwords SET current_password = (?), password_1 = (?), password_2 = (?), password_3 = (?), password_4 = (?), password_5 = (?), password_6 = (?), password_7 = (?), password_8 = (?), password_9 = (?), password_10 = (?) WHERE username=(?);"

BLOCK_USER = "UPDATE users SET blocked = (?)  WHERE username = (?);"

DROP_TABLE_USERS = "DROP TABLE users;"

DROP_TABLE_PASSWORDS = "DROP TABLE passwords;"
