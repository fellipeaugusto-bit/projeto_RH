from database import Database

class AuthService:
    def __init__(self):
        self.db = Database()

    def login(self, usuario, senha):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM administradores WHERE usuario = %s AND senha = %s"
        cursor.execute(query, (usuario, senha))
        admin = cursor.fetchone()
        cursor.close()
        return admin is not None
