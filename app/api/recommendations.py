from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db
from app.services.recommendation_model import get_recommendations

router = APIRouter()

@router.get("/{book_id}", response_model=List[schemas.Book])
def get_book_recommendations(book_id: int, db: Session = Depends(get_db)):
    recommended_book_ids = get_recommendations(book_id)
    recommended_books = db.query(models.Book).filter(models.Book.id.in_(recommended_book_ids)).all()
    return recommended_books
