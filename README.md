# Book Management System

This is a FastAPI-based Book Management System with Llama3 integration for book summaries and a recommendation system.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with the necessary environment variables
4. Initialize the database: `python scripts/init_db.py`
5. Run the server: `uvicorn app.main:app --reload`

## Features

- CRUD operations for books and reviews
- Book summary generation using Llama3
- Book recommendations
- JWT authentication

## API Documentation

API documentation is available at `/docs` when running the server.

## Testing

Run tests using pytest: `pytest`

## Docker

To run the application using Docker:

1. Build the image: `docker-compose build`
2. Run the containers: `docker-compose up`

The API will be available at `http://localhost:8000`.


`
**Folder creation commands**
mkdir -p book_management_system/{app/{models,schemas,api,services,core},tests,scripts,docs}

cd book_management_system

touch app/{__init__.py,main.py,database.py}
touch app/models/{__init__.py,book.py,review.py}
touch app/schemas/{__init__.py,book.py,review.py}
touch app/api/{__init__.py,books.py,reviews.py,recommendations.py}
touch app/services/{__init__.py,llama_integration.py,recommendation_model.py}
touch app/core/{__init__.py,config.py,security.py,auth.py}

touch tests/{__init__.py,test_main.py,test_books.py,test_reviews.py}

touch scripts/init_db.py

touch docs/api_documentation.md

touch .env .gitignore Dockerfile docker-compose.yml requirements.txt README.md
`