from pydantic import BaseModel

class ReviewBase(BaseModel):
    book_id: int
    user_id: int
    review_text: str
    rating: float

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
