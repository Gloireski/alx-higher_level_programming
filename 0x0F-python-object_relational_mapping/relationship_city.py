#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# relationship_city.py
"""class definition of a State and an instance Base = declarative_base():
   .inherits from Base
   .links to the MySQL table cities
   .class attribute id: col(auto gen, uniq int, not nul, pk)
   .class attribute name: col(string, max 128, not null)
   Must use sql alchemy
   Server: localhost at port 3306
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base




class City(Base):
    """city model class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
