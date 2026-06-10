from database import Database

class CargoDAO:
    def __init__(self):
        self.db = Database()

    def cadastrar(self, cargo):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO cargos (nome, salario_base) VALUES (%s, %s)"
        cursor.execute(query, (cargo.nome, cargo.salario_base))
        conn.commit()
        cursor.close()

    def listar_todos(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cargos")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
