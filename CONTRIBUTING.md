# Contribuindo

## Antes de iniciar

Certifique-se de que está trabalhando com a versão atualizada do projeto:

```
git switch main
git pull
git status
```

## Antes de enviar uma alteração

1. Execute o programa: `python src/main.py`
2. Confira as mudanças: `git status` e `git diff`
3. Execute as análises: `pylint src` e `radon cc src -s`
4. Faça um commit com uma mensagem objetiva.

## Estrutura do projeto

- `src/main.py` → interface de console e coordenação da aplicação
- `src/cadastro.py` → `CadastroPessoas`, gerencia o conjunto de pessoas
- `src/pessoa.py` → `Pessoa`, representa uma pessoa

## Padrões de código

- nomes claros e consistentes
- funções e variáveis em snake_case; métodos das classes em camelCase (ver `.pylintrc`)
- evitar duplicação
- responsabilidade identificável
- tratar entradas inválidas

## Convenções

- Um commit representa uma alteração verificável.
- Não inclua dados reais de pessoas no repositório.
- Registre decisões e resultados relevantes no histórico Git.

## Arquivos que não são versionados

Artefatos gerados automaticamente (`__pycache__/`, `*.pyc`) são recriados pelo
Python a cada execução e dependem da versão do interpretador. Versioná-los só
gera ruído no histórico e conflitos, por isso estão no `.gitignore`.
