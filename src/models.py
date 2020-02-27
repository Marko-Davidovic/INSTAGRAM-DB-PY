import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class home(Base):
    __tablename__ = 'Home'
    id = Column(Integer, primary_key=True)
    story = Column(String(250))
    profile = Column(String(250))
    like = Column(String(250))
    picture = Column(String(250), nullable=False)
    home_id = Column(Integer, ForeignKey('home.id'))
    home = relationship(home)

class story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    live = Column(String(250))
    boomerang = Column(String(250))
    superzoom = Column(String(250))
    Filter = Column(String(200))
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship(story)

class profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    posts = Column(String(250))
    fallowers = Column(String(1000))
    following = Column(String(1000))
    messages = Column(String(1000))
    tagged_picture = Column(String(250), nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship(profile)

def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')