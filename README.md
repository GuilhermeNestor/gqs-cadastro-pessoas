# Cadastro de Pessoas

Aplica�ao de console em Python desenvolvida na disciplina Gestao da Qualidade de Software. O menu permite cadastrar, consultar por nome, alterar e listar pessoas. A op�ao de an�lise mostra a faixa et�ria, avalia o e-mail e informa a condi�ao de contato.

## Executar

Na raiz do projeto, execute:

```console
python src/main.py
```

Para experimentar, escolha **1**, informe um nome fict�cio, a idade e um e-mail. Escolha **2** e digite o mesmo nome para consultar o registro. A op�ao **6** encerra a sessao. O reposit�rio padrao guarda os dados em mem�ria durante essa execu�ao.

## Ambiente de desenvolvimento no Windows

No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
```

## Organiza�ao

| Caminho | Responsabilidade |
| --- | --- |
| `src/main.py` | Menu e intera�ao pelo terminal |
| `src/cadastro.py` | Opera�oes do cadastro |
| `src/pessoa.py` | Dados de uma pessoa |
| `src/repositorio_pessoas.py` | Contrato de armazenamento |
| `src/repositorio_pessoas_memoria.py` | Armazenamento em mem�ria |
| `tests/` | Testes automatizados de cadastro e busca |

## Laborat�rio MySQL

O arquivo `infra/compose.yaml` define dois servi�os de MySQL para as pr�ticas de banco de dados. Para inici�-los e consultar o estado dos cont�ineres, use:

```console
docker compose -f infra/compose.yaml up -d
docker compose -f infra/compose.yaml ps
```

O servi�o `principal` usa a porta local 3307 e o servi�o `replica` usa a 3308. A aplica�ao de console continua usando o reposit�rio em mem�ria quando esses servi�os estao ativos.

Para configurar o canal de replicação e testar a persistência e a retomada após uma parada, siga o [laboratório da Aula 11](infra/LABORATORIO.md).

Para enviar melhorias, consulte o [guia de contribui�ao](CONTRIBUTING.md).
