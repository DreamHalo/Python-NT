import mysql.connector

class MySQL:
    def __init__(self) -> None:
        self.__ConnectDB()
        self.__CreateDB()
        self.CreateTB()

    def __ConnectDB(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="23030601"
        )

        self.cursor = self.connection.cursor()
    
    def __CreateDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS airport;")
        self.cursor.execute("USE airport;")
    
    def CreateTB(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ") 