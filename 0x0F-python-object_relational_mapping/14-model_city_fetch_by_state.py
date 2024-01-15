#!/usr/bin/python3
"""Module 14-model_city_fetch_by_state to list all `City` objects."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    url = f'mysql+mysqldb:\
//{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    State.cities = relationship("City", back_populates="state")
    instances = session.query(City).order_by(City.id)
    for instance in instances:
        print(f'{instance.state.name}: ({instance.id}) {instance.name}')
