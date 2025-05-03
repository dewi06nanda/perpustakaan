from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def list_books():
    return [
        {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
        {"id": 2, "title": "Deep Work", "author": "Cal Newport"},
        {"id": 3, "title": "The Pragmatic Programmer", "author": "Andy Hunt"}
    ]
