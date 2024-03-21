#!/usr/bin/python3
"""
    The `Cities in state`
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
        Cities Table for hbtn_0d_usa Database
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
