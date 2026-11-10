# 📘 Assignment: Testing Python with pytest

## 🎯 Objective

Aprenda a escrever testes automatizados com `pytest` para funções e rotas de uma API FastAPI. Use o `TestClient` para verificar respostas corretas, dados inválidos e recursos inexistentes.

## 📝 Tasks

### 🛠️ Escrever um Teste Unitário

#### Descrição
Instale as dependências e execute o teste de exemplo fornecido. Em seguida, escreva mais um teste para a função `serialize_book` em `books_api.py`.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx`.
- Executar os testes com `pytest -q`.
- Verificar que `serialize_book` retorna o ID, título, autor e ano do livro recebido.

### 🛠️ Testar as Rotas da API

#### Descrição
Use o `TestClient` do FastAPI para testar as rotas da API de livros sem iniciar um servidor. Escreva os testes em `test_books_api.py`.

#### Requisitos
O programa concluído deve:

- Verificar que `GET /` retorna status `200` e a mensagem de que a API está ativa.
- Verificar que `GET /books` retorna uma lista vazia quando não há livros cadastrados.
- Criar um livro com `POST /books` e verificar o status `200`, o ID atribuído e os dados retornados.
- Confirmar que `GET /books` e `GET /books/{book_id}` retornam o livro criado.
- Atualizar o livro com `PUT /books/{book_id}` e removê-lo com `DELETE /books/{book_id}`.
- Isolar os testes limpando a coleção de livros antes de cada teste.

### 🛠️ Verificar Erros e Dados Inválidos

#### Descrição
Acrescente testes para confirmar que a API rejeita dados incompletos e informa quando um livro solicitado não existe.

#### Requisitos
O programa concluído deve:

- Enviar um livro sem um campo obrigatório e verificar o status `422`.
- Verificar o status `404` ao consultar, atualizar ou remover um ID inexistente.
- Executar toda a suíte com `pytest -q` e confirmar que os testes passam.