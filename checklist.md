# Checklist - Analise Estatica com PyLint

Disciplina: Gestao da Qualidade de Software
Projeto: gqs-cadastro-pessoas
Branch: `pylint-analise`

## Etapas da pratica

- [x] Criar/utilizar a branch `pylint-analise` a partir de `main`
- [x] Criar o arquivo `checklist.md` e registrar o commit
- [x] Executar o PyLint pela primeira vez (baseline, antes das correcoes)
- [x] Analisar os apontamentos (nao buscar apenas a nota, entender a causa)
- [x] Corrigir o codigo com base na analise
- [x] Executar o PyLint novamente e comparar com a execucao anterior
- [x] Registrar os commits de cada etapa
- [x] Conferir o historico final com `git log --oneline`

## Arquivo analisado

- `Cadastro.py`

## Comando utilizado

```
python -m pylint Cadastro.py
```

## Observacoes

A analise estatica foi usada como apoio a melhoria do codigo (nomes de variaveis,
docstrings, tratamento de excecoes, comparacoes redundantes, uso de builtins como
nome de variavel, complexidade), e nao apenas para perseguir uma nota alta da
ferramenta.
