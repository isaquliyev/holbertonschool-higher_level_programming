#!/usr/bin/python3
"""
    The `List relationship` module
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
    cities = session.query(City, State.name.label('state'))\
                    .join(State, City.state_id == State.id).all()

    i = 0
    while i < len(cities):
        try:
            current_state = cities[i][1]
            print("{}: {}".format(cities[i][0].state_id, current_state))
            while cities[i][1] == current_state:
                print("    {}: {}".format(cities[i][0].id, cities[i][0].name))
                i += 1
        except Exception:
            break
    session.close()
