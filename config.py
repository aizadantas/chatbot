import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/chatbot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False