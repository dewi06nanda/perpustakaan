from fastapi import FastAPI
import requests

app = FastAPI()

# Provider: Menyediakan data user
@app.get("/users")
def list_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

# Consumer: Mengambil data buku dari BookService
@app.get("/users/books")
def get_books_from_book_service():
    try:
        response = requests.get("http://127.0.0.1:5001/books")
        response.raise_for_status()
        return {
            "status": "success",
            "books": response.json()
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }
