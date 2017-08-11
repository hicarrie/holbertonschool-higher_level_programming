#!/usr/bin/python3
"""
Module for script that prints the State object
with the name passed as an argument
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    name = sys.argv[4]
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

    state_id = session.query(State).filter_by(name=name).first()
    if state_id is None:
        print("Not found")
    else:
        print("{}".format(state_id))
    session.close()
