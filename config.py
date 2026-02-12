import os

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev_secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads"
