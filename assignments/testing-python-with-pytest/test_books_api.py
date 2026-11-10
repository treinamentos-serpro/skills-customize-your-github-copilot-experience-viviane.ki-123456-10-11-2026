import pytest
from fastapi.testclient import TestClient

import books_api

client = TestClient(books_api.app)


@pytest.fixture(autouse=True)
def reset_books():
    books_api.books.clear()
    books_api.next_book_id = 1


def test_serialize_book():
    book = books_api.Book(title="Dune", author="Frank Herbert", year=1965)

    result = books_api.serialize_book(1, book)

    assert result == {
        "id": 1,
        "title": "Dune",
        "author": "Frank Herbert",
        "year": 1965,
    }