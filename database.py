import mysql.connector
from mysql.connector import Error

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='SUA SENHA',
                    database='banco_rh'
                )
            return self.connection
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
