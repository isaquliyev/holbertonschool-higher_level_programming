#!/usr/bin/python3
"""
    The `City relationship` module.
"""

from sys import argv
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='California')
    city = City(name='San Francisco', state=state)
    session.add(city)
    session.commit()
    session.close()
