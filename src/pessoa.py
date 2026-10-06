"""Classe Pessoa."""


class Pessoa:
    """Representa uma pessoa cadastrada."""

    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def getIdade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    def getEmail(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    def setNome(self, nome):
        """Altera o nome da pessoa."""
        self.__nome = nome

    def setIdade(self, idade):
        """Altera a idade da pessoa."""
        self.__idade = idade

    def setEmail(self, email):
        """Altera o e-mail da pessoa."""
        self.__email = email
