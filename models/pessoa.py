from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, email, telefone):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @abstractmethod
    def mostrar_detalhes(self):
        pass
