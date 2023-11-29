#!/usr/bin/python3
"""
List all State objects that contain the letter a
from the database hbtn_0e_6_usa
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

    result = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for row in result:
        print('{0}: {1}'.format(row.id, row.name))
