from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_review():
    response = client.post(
        "/reviews/",
        json={"book_id": 1, "user_id": 1, "review_text": "Great book!", "rating": 5.0}
    )
    assert response.status_code == 200
    assert response.json()["review_text"] == "Great book!"

def test_read_reviews_for_book():
    response = client.get("/reviews/book/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
