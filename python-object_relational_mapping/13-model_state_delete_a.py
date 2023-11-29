#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    eng = create_engine(db)
    Base.metadata.create_all(eng)
    session = Session(eng)

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
