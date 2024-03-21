#!/usr/bin/python3
"""
    The `First state model` module.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
import MySQLdb
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    MySQLdb.connect(host="localhost",
                    port=3306,)
