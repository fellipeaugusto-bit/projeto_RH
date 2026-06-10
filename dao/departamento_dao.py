from database import Database

class DepartamentoDAO:
    def __init__(self):
        self.db = Database()

    def cadastrar(self, departamento):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO departamentos (nome, gerente) VALUES (%s, %s)"
        cursor.execute(query, (departamento.nome, departamento.gerente))
        conn.commit()
        cursor.close()

    def listar_todos(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departamentos")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados



