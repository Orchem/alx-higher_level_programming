#!/usr/bin/python3
"""state class for state  ORM"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """states class for table state"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City", cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
