#!/usr/bin/python3
"""Module 10-model_state_my_get to list first `State` object
if available."""
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    url = f'mysql+mysqldb:\
//{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    instance = session.query(State).filter(text("name=:value")).\
        params(value=sys.argv[4]).first()

    if (instance is None):
        print("Not found")
    else:
        print(instance.id)
