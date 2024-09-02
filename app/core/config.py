from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Book Management System"
    DATABASE_URL: str = "postgresql://user:password@localhost/bookdb"

    class Config:
        env_file = ".env"

settings = Settings()
