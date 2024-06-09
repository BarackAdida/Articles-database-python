from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define your database URL
DB_URL = 'sqlite:///path/to/your/database.db'

# Create the database engine
engine = create_engine(DB_URL)

# Define declarative base
Base = declarative_base()

# Define your models
class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    articles = relationship("Article", back_populates="author")

class Magazine(Base):
    __tablename__ = 'magazines'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)

    articles = relationship("Article", back_populates="magazine")

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))

    author = relationship("Author", back_populates="articles")
    magazine = relationship("Magazine", back_populates="articles")

# Create the tables
Base.metadata.create_all(engine)
