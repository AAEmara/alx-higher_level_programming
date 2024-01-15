#!/usr/bin/python3
"""Module 11-model_state_insert to add State Object 'Louisiana'."""
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
    state_name = "Louisiana"
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()

    instance = session.query(State).filter(text("name=:value")).\
        params(value=state_name).first()

    print(instance.id)
