from sqlalchemy import create_engine
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# Database
from database.Connection import Connect
from database.Rehber import Rehber

conn = Connect()
session = conn.session()

# Select Where And
record = session.query(Rehber).filter(
    Rehber.rehber_id == 1
)

try:
    record.update({Rehber.rehber_adi:'Ugur Unsal'})
    session.commit()
    print("Update Successfull...")
except:
    session.rollback()
    print("DB Error!")
finally:
    session.close()
    print("Session Closed!")