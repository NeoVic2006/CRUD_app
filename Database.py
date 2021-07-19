import sqlite3
from sqlite3.dbapi2 import Connection


def createTable():
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL, PASSWORD TEXT, Date_of_birth DATE, UNIQUE(USERNAME, PASSWORD))") 
    connection.execute("INSERT INTO USERS VALUES(?, ?, ?)", ('ser', '123', '2019-10-14'))

    connection.execute("CREATE TABLE CLIENTS (USERNAME TEXT NOT NULL, PHONE INT, Date_of_birth DATE, UNIQUE(USERNAME, PHONE))") 
    connection.execute("INSERT INTO CLIENTS VALUES(?, ?, ?)", ('Sergey', 3435626542, '2019-10-14'))

    connection.commit()
    connection.close()

createTable()

