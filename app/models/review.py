from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer)
    review_text = Column(String)
    rating = Column(Float)

    book = relationship("Book", back_populates="reviews")
