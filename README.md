# projeto-sofware-movimentacao

A aplicação é uma API Rest simples, que faz o cadastro de movimentações de compra e venda de ações, ela acessa a API stocks desenvolvida nas aulas anteriores para validar que uma ação é válida.

Para executar a aplicação, execute:

pip install -r requirements.txt
python app.py

Para executar os testes e verificar a cobertura, execute o comando

pytest --cov=. --cov-report=xml --cov-report=term --cov-report=html

Esse commando irá mostrar a cobertura no terminal e também montar um report HTML.

---

## Exercícios

1) Gerar os testes para os arquivos app.py e app_service.py, atingir pelo menos 80% de cobertura
2) Escrever um pipeline para executar os testes e escrever a cobertura de testes sempre que um PR for aberto

Algumas coisas que vocês irão precisar:

- Verificar PR com o coverage:
https://github.com/marketplace/actions/pytest-coverage-comment

- Para fazer mocks no geral -> usar o patch, pode ser o decorator @patch, com ele é possível definir mocks estáticos diretamente no decorator, ou mocks dinâmicos com a função side_effect

- Para fazer mocks de objetos, usar o MagicMock, necessário para mockar o retorno da api requests

