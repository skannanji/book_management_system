from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_book():
    response = client.post(
        "/books",
        json={"title": "Test Book", "author": "Test Author", "genre": "Fiction", "year_published": 2024, "content": "This is a test book content."}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

