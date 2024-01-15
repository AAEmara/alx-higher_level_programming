#!/usr/bin/python3
"""Module 12-model_state_update_id_2 to change State Object
with id = 2 into 'New Mexico'."""
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

    instance = session.query(State).filter(text("id=:value")).\
        params(value=2).first()
    instance.name = "New Mexico"

    session.commit()
