#!/usr/bin/python3
# Belem Gloire BEKOUTOU
# model_state.py
"""class definition of a State and an instance Base = declarative_base():
   .inherits from Base
   .links to the MySQL table states
   .class attribute id: col(auto gen, uniq int, not nul, pk)
   .class attribute name: col(string, max 128, not null)
   Must use sql alchemy
   Server: localhost at port 3306
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """states model class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        "constructor"
        self.name = name
