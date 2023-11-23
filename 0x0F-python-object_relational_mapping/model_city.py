#!/usr/bin/python3
"""Module for City Class definition."""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """City Class that inherits from the Base Class
    and defines a `cities` table.

    Attr:
        id (integer): Unique identifier of a state which is NOT NULL and a PK.
        name (string): State's name with a limit of 128 characters.
        state_id (integer): Integer foreign key of the 'States' Table.
    """

    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    states = relationship("State", back_populates="cities")
