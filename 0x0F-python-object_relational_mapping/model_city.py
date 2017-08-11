#!/usr/bin/python3
"""
Module for City class
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ defines City class """

    __tablename__ = "cities"
    id = Column("id", Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey("states.id"),
                      nullable=False)

    state = relationship("State", back_populates="city")

    def __str__(self):
        """ defines __str__ attribute """
        return "{}".format(self.name)
