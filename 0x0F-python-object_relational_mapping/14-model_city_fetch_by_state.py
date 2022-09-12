#!/usr/bin/python3
"""sqlalchemy select all columns statement"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                        argv[1],
                                                        argv[2],
                                                        argv[3]
                                                        )
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
