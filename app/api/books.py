from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db
from app.services.llama_integration import generate_summary

router = APIRouter()

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db_book.summary = generate_summary(book.title)  # Generate summary using Llama3
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Implement other CRUD operations as needed
