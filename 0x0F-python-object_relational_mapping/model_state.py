#!/usr/bin/python3
"""Module for State Class definition and Base instance."""

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class that inherits from the Base Class
    and defines a `States` table.

    Attr:
        id (integer): Unique identifier of a state which is NOT NULL and a PK.
        name (string): State's name with a limit of 128 characters.
    """

    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
