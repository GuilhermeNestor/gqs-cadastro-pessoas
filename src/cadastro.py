"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa


class CadastroPessoas:
    """Mantem e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cria uma nova pessoa e adiciona ao cadastro."""
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Retorna a pessoa com o nome informado, ou None se nao existir."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        """Retorna a lista de pessoas cadastradas."""
        return self.__pessoas

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera os dados da pessoa localizada pelo nome."""
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa
