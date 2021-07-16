import sqlite3
from sqlite3.dbapi2 import Connection


def createTable():
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL, PASSWORD TEXT, Date_of_birth DATE)") 
    connection.execute("INSERT INTO USERS VALUES(?, ?, ?)", ('Sergey', 'qwerty', '14/23/2033'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Username: ", data[0])
        print("Pssword: ", data[1])

    connection.close()

createTable()
