#!/usr/bin/python3
"""
Module for State class
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ defines State class """

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    city = relationship("City", back_populates="state")

    def __str__(self):
        """ defines __str__ attribute """
        return "{}".format(self.name)
