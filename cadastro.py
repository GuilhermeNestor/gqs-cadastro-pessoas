"""Sistema de Cadastro de Pessoas - versao 2.

Novos requisitos: menu, consulta, alteracao e listagem.
"""


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


def cadastrar_pessoa(nomes, idades, emails):
    """Le os dados de uma nova pessoa e adiciona nas listas."""
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def exibir_pessoa(nomes, idades, emails, pos):
    """Exibe os dados da pessoa na posicao informada."""
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def buscar_pessoa(nomes, nome_procurado):
    """Retorna a posicao de nome_procurado em nomes, ou -1 se nao existir."""
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1


def consultar_pessoa(nomes, idades, emails):
    """Consulta uma pessoa pelo nome e exibe seus dados."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)


def alterar_pessoa(nomes, idades, emails):
    """Altera os dados de uma pessoa localizada pelo nome."""
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        nomes[pos] = input("Novo nome: ")
        idades[pos] = int(input("Nova idade: "))
        emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(nomes, idades, emails, pos)


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


def analisar_pessoa(nomes, idades, emails):
    """Analisa faixa etaria, e-mail e condicao de contato de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

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


def listar_pessoas(nomes, idades, emails):
    """Lista todas as pessoas cadastradas."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(nomes)))


def main():
    """Executa o loop principal do cadastro de pessoas."""
    nomes = []
    idades = []
    emails = []

    opcao = 0

    while opcao != 6:
        opcao = exibir_menu()

        if opcao == 1:
            cadastrar_pessoa(nomes, idades, emails)
        elif opcao == 2:
            consultar_pessoa(nomes, idades, emails)
        elif opcao == 3:
            alterar_pessoa(nomes, idades, emails)
        elif opcao == 4:
            listar_pessoas(nomes, idades, emails)
        elif opcao == 5:
            analisar_pessoa(nomes, idades, emails)
        elif opcao == 6:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    main()
