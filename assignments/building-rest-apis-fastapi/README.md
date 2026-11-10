# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para cadastrar e consultar livros usando FastAPI. Você praticará rotas HTTP, validação de dados com Pydantic e operações CRUD em uma coleção mantida em memória.

## 📝 Tarefas

### 🛠️ Criar e Executar a API

#### Descrição
Instale as dependências, execute o código inicial e implemente uma rota inicial para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Executar o servidor com `uvicorn starter-code:app --reload`.
- Implementar uma rota `GET /` que retorne uma mensagem indicando que a API de livros está ativa.
- Permitir que a documentação interativa seja acessada em `/docs`.

### 🛠️ Cadastrar e Listar Livros

#### Descrição
Use o modelo Pydantic fornecido no código inicial para validar os dados e implemente as rotas da coleção de livros.

#### Requisitos
O programa concluído deve:

- Aceitar livros com título, autor e ano de publicação; o FastAPI deve rejeitar dados que não correspondam ao modelo.
- Implementar `GET /books` para retornar todos os livros cadastrados.
- Implementar `POST /books` para cadastrar um livro, atribuir um identificador único e retornar o livro criado.
- Manter os livros em memória; os dados podem ser apagados quando o servidor for reiniciado.

### 🛠️ Gerenciar um Livro por ID

#### Descrição
Implemente operações para consultar, atualizar e remover um livro específico. Use a documentação em `/docs` para testar as rotas.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar o livro indicado.
- Implementar `PUT /books/{book_id}` para substituir os dados do livro indicado.
- Implementar `DELETE /books/{book_id}` para remover o livro indicado.
- Retornar o status HTTP `404` quando o identificador não existir nas operações de consulta, atualização ou remoção.
