from sqlalchemy import create_engine
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc
from database.Connection import Connect
from database.Rehber import Rehber


conn = Connect()
session = conn.session()

rehber1 = Rehber(
    rehber_id=1,
    rehber_adi='Ugur Unsal',
    rehber_tel='0532 620 1000',
    rehber_adres='Maltepe IStanbul'
)

rehber2 = Rehber(
    rehber_id=2,
    rehber_adi='Jago Fishman',
    rehber_tel='0530 940 5522',
    rehber_adres='Bahçelievler'
)


# session.add(rehber1)
session.add(rehber1)

try:
    session.commit()
    print("insert successfull")
except exc.SQLAlchemyError:
    session.rollback()
    print("DB Error occured...")
    # raise
finally:
    print("Session Closed!")
    session.close()


