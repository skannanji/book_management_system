from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/book/{book_id}", response_model=List[schemas.Review])
def read_reviews_for_book(book_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(models.Review.book_id == book_id).all()
    return reviews

