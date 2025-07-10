from typing import Optional

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
import uuid

app = FastAPI()

class BookRequest(BaseModel):
    id: Optional[str] = Field(default="")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=1000)
    rating: Optional[int] = Field(default=None, gt=-1, lt=11)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book title",
                "author": "author name",
                "description": "The book description",
                "rating": 5,
            }
        }
    }

class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    author: str
    description: str
    rating: Optional[int] = None

BOOKS = [
    Book(title="Python Programming", author="a1", description="python book", rating=6),
    Book(title="Ruby Programming", author="a2", description="ruby book", rating=3),
    Book(title="Js Programming", author="a3", description="js book", rating=9),
    Book(title="C++ Programming", author="a4", description="c++ book", rating=8),
]

@app.get("/books")
async def get_books(rating: Optional[int] = Query(default=None, gt=-1, lt=11),):
    filtered_books = []
    if rating:
        for book in BOOKS:
            if book.rating == rating:
                filtered_books.append(book)
        return filtered_books
    return BOOKS

@app.get("/books/{id}")
async def get_book(id: str):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@app.post("/books")
async def create_book(book: BookRequest):
    new_book = Book(**book.model_dump())
    BOOKS.append(new_book)
    return new_book

@app.put("/books")
async def update_book(book: BookRequest):
    book_changes = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changes = True
            break

    if book_changes:
        return BOOKS
    raise HTTPException(status_code=404, detail="book not found")

@app.delete("/books/{id}")
async def delete_book(id: str):
    book_changes = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            break
    if book_changes:
        return BOOKS
    raise HTTPException(status_code=404, detail="book not found")
