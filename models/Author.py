from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///orms.db', echo=True)
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    articles = relationship('Article', back_populates='author')

    def __init__(self, name):
        self.name = name
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot modify name after it has been set.")
        if not isinstance(value, str):
            raise TypeError("Name must be of type str.")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """
        with engine.connect() as connection:
            connection.execute(sql)

    def articles(self):
        session = Session()
        articles = session.query(Article).filter(Article.author_id == self.id).all()
        session.close()
        return articles

    def magazines(self):
        session = Session()
        magazines = session.query(Magazine).join(Article).filter(Article.author_id == self.id).all()
        session.close()
        return magazines

Author.create_table()
Session = sessionmaker(bind=engine)
