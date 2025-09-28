import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_DEVELOPMENT_URI")
    API_URI = os.getenv("API_URI")
    CLIENT_ID = os.getenv("CLIENT_ID")