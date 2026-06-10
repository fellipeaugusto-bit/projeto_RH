from models.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, email, telefone, cargo_id, salario, departamento_id, id=None, data_admissao=None):
        super().__init__(nome, cpf, email, telefone)
        self.id = id
        self.cargo_id = cargo_id
        self.salario = salario
        self.departamento_id = departamento_id
        self.data_admissao = data_admissao

    def mostrar_detalhes(self):
        return f"Funcionário: {self.nome} | CPF: {self.cpf} | Salário: R$ {self.salario:.2f}"
