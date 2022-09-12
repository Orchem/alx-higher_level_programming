#!/usr/bin/python3
"""module to add to state"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
                                                        argv[1],
                                                        argv[2],
                                                        argv[3]
                                                        )
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    row = session.query(State).filter(State.id == 2).first()
    row.name = "New Mexico"
    session.commit()
    session.close()
