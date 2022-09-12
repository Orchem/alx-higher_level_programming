#!/usr/bin/python3
"""sqlalchemy select all columns statement"""
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

    query = session.query(State).order_by(State.id)

    result = query.all()
    for row in result:
        print("{}: {}".format(row.id, row.name))

    session.close()
