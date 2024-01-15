#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 9-model_state_filter_a.py
"""script that lists all State objects that contain the letter a from
   the database hbtn_0e_6_usa
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
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
