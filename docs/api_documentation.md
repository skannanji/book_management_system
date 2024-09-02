# Book Management System API Documentation

## Endpoints

### Books

- `POST /books/`: Create a new book
- `GET /books/`: Get all books
- `GET /books/{book_id}`: Get a specific book

### Reviews

- `POST /reviews/`: Create a new review
- `GET /reviews/book/{book_id}`: Get all reviews for a specific book

### Recommendations

- `GET /recommendations/{book_id}`: Get book recommendations based on a book

## Authentication

This API uses JWT for authentication. Include the JWT token in the Authorization header for protected endpoints.

## Models

### Book

- id: int
- title: string
- author: string
- genre: string
- year_published: int
- summary: string

### Review

- id: int
- book_id: int
- user_id: int
- review_text: string
- rating: float

For more detailed information on request/response formats, please refer to the OpenAPI documentation available at `/docs` when running the server.
