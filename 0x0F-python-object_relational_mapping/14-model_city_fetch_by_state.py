#!/usr/bin/python3
"""Module for Querying the `State` database using SQLAlchemy's ORM."""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    args = sys.argv
    eng_format = "mysql://{}:{}@localhost:3306/{}".format(
                  args[1], args[2], args[3])
    engine = create_engine(eng_format)
    Session = sessionmaker(bind=engine)
    session = Session()
    State.cities = relationship("City", back_populates="states")
    instances = session.query(City).order_by(City.id)

    for instance in instances:
        print(instance.states.name, instance.id, instance.name)
