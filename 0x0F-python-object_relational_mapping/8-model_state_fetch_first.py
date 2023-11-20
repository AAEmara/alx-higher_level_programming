#!/usr/bin/python3
"""Module for Querying the `State` database using SQLAlchemy's ORM."""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv
    eng_format = "mysql://{}:{}@localhost:3306/{}".format(
                  args[1], args[2], args[3])
    engine = create_engine(eng_format)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()

    if instance is None:
        print("Nothing")
    else:
        print(f"{instance.id}: {instance.name}")
