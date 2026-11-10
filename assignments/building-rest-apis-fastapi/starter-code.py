from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, Book] = {}


@app.get("/")
def read_root():
    # TODO: Return a message confirming the API is running.
    pass


@app.get("/books")
def list_books():
    # TODO: Return all books, including each book's ID.
    pass


@app.post("/books")
def create_book(book: Book):
    # TODO: Assign an ID, store the book, and return the created book.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the book or raise HTTPException with status code 404.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Replace the book or raise HTTPException with status code 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTPException with status code 404.
    pass
