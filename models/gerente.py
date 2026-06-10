from models.funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, email, telefone, cargo_id, salario, departamento_id, id=None, data_admissao=None):
        super().__init__(nome, cpf, email, telefone, cargo_id, salario, departamento_id, id, data_admissao)

    def mostrar_detalhes(self):
        return f"Gerente: {self.nome} | CPF: {self.cpf} | Departamento ID: {self.departamento_id}"
