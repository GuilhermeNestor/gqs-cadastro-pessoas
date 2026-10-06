"""Interface de console do Cadastro de Pessoas.

Este modulo conversa com o usuario (input e print) e coordena a aplicacao.
As regras do cadastro ficam em CadastroPessoas; os dados, em Pessoa.
"""

from cadastro import CadastroPessoas


def exibir_menu():
    """Mostra o menu principal e retorna a opcao escolhida."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoa")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))


def cadastrar_pessoa(cadastro):
    """Le os dados de uma nova pessoa e adiciona no cadastro."""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")
    cadastro.cadastrar(nome, idade, email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def exibir_pessoa(pessoa):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    if pessoa.getIdade() >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def consultar_pessoa(cadastro):
    """Consulta uma pessoa pelo nome e exibe seus dados."""
    procurado = input("Nome para consultar: ")
    pessoa = cadastro.buscarPorNome(procurado)
    if pessoa is None:
        print("Nao encontrado")
    else:
        exibir_pessoa(pessoa)


def alterar_pessoa(cadastro):
    """Altera os dados de uma pessoa localizada pelo nome."""
    procurado = input("Nome para alterar: ")
    if cadastro.buscarPorNome(procurado) is None:
        print("Nao encontrado")
    else:
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        novo_email = input("Novo e-mail: ")
        pessoa = cadastro.alterar(procurado, novo_nome, nova_idade, novo_email)
        print("Pessoa alterada!")
        exibir_pessoa(pessoa)


def classificar_faixa_etaria(idade):
    """Classifica a idade em uma faixa etaria."""
    if idade < 12:
        return "Crianca"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"


def avaliar_email(email):
    """Avalia se o e-mail esta ausente, invalido ou utilizavel."""
    if email == "":
        return "ausente"
    if "@" not in email:
        return "invalido"
    return "utilizavel"


def identificar_provedor(email):
    """Identifica o provedor de e-mail a partir do dominio."""
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    if email.endswith("@hotmail.com"):
        return "Hotmail"
    if email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    return "Outro"


def definir_condicao_contato(idade, email):
    """Define a condicao de contato com base na idade e no e-mail."""
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    if idade >= 18 and email == "":
        return "Maior de idade sem contato"
    if idade < 18 and email != "":
        return "Menor de idade com contato"
    return "Menor de idade sem contato"


def analisar_pessoa(cadastro):
    """Analisa faixa etaria, e-mail e condicao de contato de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Pessoa nao encontrada")
    else:
        idade = pessoa.getIdade()
        email = pessoa.getEmail()

        faixa_etaria = classificar_faixa_etaria(idade)
        print("Faixa etaria: " + faixa_etaria)

        situacao_email = avaliar_email(email)
        if situacao_email == "ausente":
            print("Cadastro incompleto: sem e-mail")
        elif situacao_email == "invalido":
            print("E-mail invalido")
        else:
            provedor = identificar_provedor(email)
            print("Provedor: " + provedor)

        print(definir_condicao_contato(idade, email))


def listar_pessoas(cadastro):
    """Lista todas as pessoas cadastradas."""
    pessoas = cadastro.listar()
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada")
    for pessoa in pessoas:
        exibir_pessoa(pessoa)
        print("-------------------------")
    print("Total: " + str(len(pessoas)))


def executar():
    """Executa o menu principal da aplicacao."""
    cadastro = CadastroPessoas()

    opcao = 0

    while opcao != 6:
        opcao = exibir_menu()

        if opcao == 1:
            cadastrar_pessoa(cadastro)
        elif opcao == 2:
            consultar_pessoa(cadastro)
        elif opcao == 3:
            alterar_pessoa(cadastro)
        elif opcao == 4:
            listar_pessoas(cadastro)
        elif opcao == 5:
            analisar_pessoa(cadastro)
        elif opcao == 6:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    executar()
