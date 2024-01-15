#!/usr/bin/python3
"""Module model_city that defines City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State


class City (Base):
    """City Class defined based on Base Class."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    stated_id = Column(ForeignKey('states.id'), Integer, nullable=False)

    state = realtionship("State", back_populates="cities")
