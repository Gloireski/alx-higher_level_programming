#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 7-model_state_fetch_all.py
"""script that lists all State objects from the database hbtn_0e_6_usa
   args:
        mysql username,
        mysql password,
        database name
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print(state.id, state.name, sep=": ")
