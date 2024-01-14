#!/usr/bin/python3
"""Module 8-model_state_fetch_first to list first `State` object
if available."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    url = f'mysql+mysqldb:\
//{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    instances = session.query(State).order_by(State.id)
    if (instances is None):
        print("Nothing")
    else:
        print(f'{instances[0].id}: {instances[0].name}')
