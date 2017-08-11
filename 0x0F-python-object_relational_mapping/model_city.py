#!/usr/bin/python3
"""
Module for City class
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ defines CIty class """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="city")

    def __str__(self):
        """ defines __str__ attribute """
        return "{}".format(self.name)
