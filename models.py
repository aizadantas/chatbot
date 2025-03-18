from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class FileContent(Base):
    __tablename__ = 'file_contents'
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)