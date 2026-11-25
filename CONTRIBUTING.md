# Como contribuir

## Preparar um fork

Fa�a um fork de `gkauac-droid/gqs-cadastro-pessoas` na sua conta. Substitua `SEU-USUARIO` pelo seu usu�rio do GitHub nos comandos abaixo.

```console
git clone https://github.com/SEU-USUARIO/gqs-cadastro-pessoas.git
cd gqs-cadastro-pessoas
git remote add upstream https://github.com/gkauac-droid/gqs-cadastro-pessoas.git
git fetch upstream
git switch -c docs/readme-contributing upstream/main
```

Escolha um nome de branch que descreva sua contribui�ao. O exemplo acima cria uma branch de documenta�ao a partir da versao atual da `main` do projeto.

## Preparar e conferir a mudan�a

Use dados fict�cios nos exemplos. Mantenha a intera�ao com o terminal em `src/main.py`, as opera�oes em `src/cadastro.py` e o armazenamento nas classes de reposit�rio. Siga os nomes usados no projeto e as conven�oes da configura�ao do Pylint. Deixe os arquivos gerados pelo Python, como `__pycache__/` e `*.pyc`, fora do commit.

Prepare o ambiente conforme o [README](README.md). Para altera�oes de c�digo, execute na raiz:

```console
python -m pytest -v
python -m pylint src
python src/main.py
```

O projeto tamb�m configura hooks de pytest e Pylint. Para ativ�-los no seu clone, execute `pre-commit install` com o ambiente virtual ativo. Para uma an�lise adicional de complexidade com Radon, instale-o com `python -m pip install radon` e execute `radon cc src -s`.

## Publicar e abrir o Pull Request

Confira os arquivos e fa�a um commit que descreva a altera�ao. Para a contribui�ao de documenta�ao deste exemplo:

```console
git status
git diff
git add README.md CONTRIBUTING.md
git diff --cached
git commit -m "docs: explica a execu�ao do cadastro e o fluxo de contribui�ao"
git push -u origin HEAD
```

No GitHub, abra **Compare & pull request**. Selecione a `main` de `gkauac-droid/gqs-cadastro-pessoas` como destino e a branch do seu fork como origem. Descreva o que mudou e como voc� conferiu o resultado. O respons�vel pelo projeto revisa e integra o PR.

Para registrar a autoria na atividade da disciplina, consulte o hist�rico da `main` atualizada ap�s o merge:

```console
git log --format="%h | %an <%ae> | %s"
```
