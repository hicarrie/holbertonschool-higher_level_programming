#!/usr/bin/python3
"""
Module for script that changes the name of a State object
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                                   passwd,
                                                                   host, port,
                                                                   database))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).one()
    state.name = "New Mexico"
    session.commit()
    session.close()
