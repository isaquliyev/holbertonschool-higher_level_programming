#!/usr/bin/python3
"""
    The `First state model` module.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
    """
        States Table for hbtn_0d_usa Database
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
