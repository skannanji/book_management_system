from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, Book, Review
from llama_integration import llama_model
from recommendation_model import recommendation_model
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int
    content: str

class ReviewCreate(BaseModel):
    user_id: int
    review_text: str
    rating: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books")
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    summary = llama_model.generate_summary(book.content)
    db_book = Book(title=book.title, author=book.author, genre=book.genre, year_published=book.year_published, summary=summary)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books")
async def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{book_id}")
async def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

@app.post("/books/{book_id}/reviews")
async def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db_review = Review(book_id=book_id, user_id=review.user_id, review_text=review.review_text, rating=review.rating)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@app.get("/books/{book_id}/reviews")
async def read_reviews(book_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.book_id == book_id).all()
    return reviews

@app.get("/books/{book_id}/summary")
async def get_book_summary(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    reviews = db.query(Review).filter(Review.book_id == book_id).all()
    avg_rating = sum(review.rating for review in reviews) / len(reviews) if reviews else 0
    return {"summary": book.summary, "average_rating": avg_rating}

@app.get("/recommendations")
async def get_recommendations(book_id: int, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    recommendation_model.train([{"id": book.id, "genre": book.genre} for book in books])
    recommended_book_ids = recommendation_model.get_recommendations(book_id)
    recommended_books = db.query(Book).filter(Book.id.in_(recommended_book_ids)).all()
    return recommended_books

@app.post("/generate-summary")
async def generate_summary(content: str):
    summary = llama_model.generate_summary(content)
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
