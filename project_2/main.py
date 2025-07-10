from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        'title': 'Book 1',
        'author': '<NAME1>',
        'category': 'science',
    },
    {
        'title': 'Book 2',
        'author': '<NAME2>',
        'category': 'anime',
    }
]


@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/{title}")
async def get_book(title: str):
    for book in BOOKS:
        if book['title'].casefold() == title.casefold():
            return book

    return {}

@app.get("/books/")
async def get_books_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book['category'] == category:
            books_to_return.append(book)
    return books_to_return

@app.post("/books/")
async def create_book(book: dict):
    BOOKS.append(book)
    return book

@app.put("/books/")
async def update_book(book: dict):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == book['title'].casefold():
            BOOKS[i] = book
    return BOOKS

@app.delete("/books/{title}")
async def delete_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == title.casefold():
            BOOKS.pop(i)
            break
    return BOOKS