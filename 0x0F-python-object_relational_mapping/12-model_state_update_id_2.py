#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 12-model_state_update_id_2.py
"""script that changes the name of a State object
   from the database hbtn_0e_6_usa
   args:
        mysql username,
        mysql password,
        database name,
   Change the name of the State where id = 2 to New Mexico
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
    x = session.query(State).get(2)
    x.name = "New Mexico"
    session.commit()
    session.close()
