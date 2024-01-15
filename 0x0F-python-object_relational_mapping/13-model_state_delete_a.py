#!/usr/bin/python3
"""Module 13-model_state_delete_a to delete State Objects that include
 'a' character."""
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

    instances = session.query(State).filter(State.name.like('%a%'))
    for instance in instances:
        session.delete(instance)
    session.commit()
