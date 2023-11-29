#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    eng = create_engine(db)
    Base.metadata.create_all(eng)
    session = Session(eng)

    cities = session.query(State.name, City.id, City.name)\
        .join(City).order_by(City.id).all()
    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")

    session.close()
