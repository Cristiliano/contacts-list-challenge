from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    numbers = relationship('Number', backref='person', lazy='subquery')

class Number(Base):
    __tablename__ = 'number'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tell = Column(String)
    reference = Column(String)
    person_id = Column(Integer, ForeignKey('person.id')) 