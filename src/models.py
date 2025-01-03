import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(50))
    users = relationship('Favorites', backref='users', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    diameter = Column(Integer)
    favorites = relationship('Favorites', backref='planets', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    favorites = relationship('Favorites', backref='characters', lazy=True)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))


    






render_er(Base, 'diagram.png')