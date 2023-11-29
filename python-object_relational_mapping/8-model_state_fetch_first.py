#!/usr/bin/python3
"""
Script that prints the first State object
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

    result = session.query(State).order_by(State.id).first()
    if result is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(result.id, result.name))
    
    session.close()
