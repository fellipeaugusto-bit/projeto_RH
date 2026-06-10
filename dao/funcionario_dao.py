from database import Database
from models.funcionario import Funcionario

class FuncionarioDAO:
    def __init__(self):
        self.db = Database()

    def cadastrar(self, funcionario):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = """INSERT INTO funcionarios (nome, cpf, email, telefone, cargo_id, salario, departamento_id, data_admissao) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())"""
        values = (funcionario.nome, funcionario.cpf, funcionario.email, funcionario.telefone, 
                  funcionario.cargo_id, funcionario.salario, funcionario.departamento_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def listar_todos(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.*, c.nome as cargo_nome, d.nome as depto_nome 
                   FROM funcionarios f
                   JOIN cargos c ON f.cargo_id = c.id
                   JOIN departamentos d ON f.departamento_id = d.id"""
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def pesquisar_por_nome(self, nome):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.*, c.nome as cargo_nome, d.nome as depto_nome 
                   FROM funcionarios f
                   JOIN cargos c ON f.cargo_id = c.id
                   JOIN departamentos d ON f.departamento_id = d.id
                   WHERE f.nome LIKE %s"""
        cursor.execute(query, (f"%{nome}%",))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def pesquisar_por_cpf(self, cpf):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.*, c.nome as cargo_nome, d.nome as depto_nome 
                   FROM funcionarios f
                   JOIN cargos c ON f.cargo_id = c.id
                   JOIN departamentos d ON f.departamento_id = d.id
                   WHERE f.cpf = %s"""
        cursor.execute(query, (cpf,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def atualizar(self, id, cargo_id, salario, departamento_id, telefone, email):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = """UPDATE funcionarios SET cargo_id=%s, salario=%s, departamento_id=%s, 
                   telefone=%s, email=%s WHERE id=%s"""
        cursor.execute(query, (cargo_id, salario, departamento_id, telefone, email, id))
        conn.commit()
        cursor.close()

    def excluir(self, id):
        conn = self.db.connect()
        cursor = conn.cursor()
        query = "DELETE FROM funcionarios WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()

