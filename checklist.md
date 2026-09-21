# Checklist — Análise Estática com PyLint

Disciplina: Gestão da Qualidade de Software
Projeto: gqs-cadastro-pessoas
Branch: `pylint-analise`

## Etapas da prática

- [x] Criar/utilizar a branch `pylint-analise` a partir de `main`
- [x] Criar o arquivo `checklist.md` e registrar o commit
- [x] Executar o PyLint pela primeira vez (baseline, antes das correções)
- [x] Analisar os apontamentos (não buscar apenas a nota, entender a causa)
- [x] Corrigir o código com base na análise
- [x] Executar o PyLint novamente e comparar com a execução anterior
- [x] Registrar os commits de cada etapa
- [x] Conferir o histórico final com `git log --oneline`

## Arquivo analisado

- `Cadastro.py`

## Comando utilizado

```
python -m pylint Cadastro.py
```

## Observações

A análise estática foi usada como apoio à melhoria do código (nomes de variáveis,
docstrings, tratamento de exceções, comparações redundantes, uso de builtins como
nome de variável, complexidade), e não apenas para perseguir uma nota alta da
ferramenta.
