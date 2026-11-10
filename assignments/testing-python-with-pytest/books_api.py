from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, Book] = {}
next_book_id = 1


def serialize_book(book_id: int, book: Book) -> dict:
    return {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
    }


@app.get("/")
def read_root():
    return {"message": "Books API is running"}


@app.get("/books")
def list_books():
    return [serialize_book(book_id, book) for book_id, book in books.items()]


@app.post("/books")
def create_book(book: Book):
    global next_book_id
    book_id = next_book_id
    next_book_id += 1
    books[book_id] = book
    return serialize_book(book_id, book)


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return serialize_book(book_id, books[book_id])


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book
    return serialize_book(book_id, book)


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": "Book deleted"}