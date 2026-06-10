from database import Database

class LogDAO:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario, acao):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO logs (usuario, acao, data_hora) VALUES (%s, %s, NOW())"
        cursor.execute(query, (usuario, acao))
        conn.commit()
        cursor.close()

    def listar_ultimos(self, limite=5):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM logs ORDER BY data_hora DESC LIMIT %s"
        cursor.execute(query, (limite,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def listar_todos(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM logs ORDER BY data_hora DESC"
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

