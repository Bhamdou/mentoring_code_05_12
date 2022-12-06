from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, select


Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


engine = create_engine('postgresql://postgres:postgres@127.0.0.1:2022/my_blog')
session = Session(engine)


def get_posts():
    posts = session.query(Post).all()
    return [dict(row.to_json()) for row in posts]


def get_authors():
    authors = session.query(Author).all()
    return [dict(row.to_json()) for row in authors]