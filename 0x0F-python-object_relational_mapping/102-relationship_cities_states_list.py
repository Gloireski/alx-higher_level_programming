#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# 102-relationship_cities_states_list.py
"""
   Lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

#    for state in session.query(State).order_by(State.id):
#        for city in state.cities:
#            print("{}: {} -> {}".format(city.id, city.name, state.name))
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.states.name))
