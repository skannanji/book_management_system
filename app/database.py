from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year_published = Column(Integer)
    summary = Column(String)

    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer)
    review_text = Column(String)
    rating = Column(Float)

    book = relationship("Book", back_populates="reviews")

# Database connection
DATABASE_URL = "postgresql://admin:admin@123@localhost/bookdb"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)
