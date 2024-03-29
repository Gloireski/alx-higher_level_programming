#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 10-model_state_my_get.py
"""script that prints the State object with the name
   passed as argument from the database hbtn_0e_6_usa
   args:
        mysql username,
        mysql password,
        database name,
        state name: to search
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
    result = session.query(State).filter(State.name == sys.argv[4])
    try:
        print(result[0].id)
    except IndexError:
        print("Not found")
