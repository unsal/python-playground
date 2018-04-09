from sqlalchemy import create_engine
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database.Rehber import Rehber
from database.Connection import Connect

conn = Connect()
session = conn.session()
# Select Where And
record = session.query(Rehber).filter(
    Rehber.rehber_id == 1
)

try:
    record.delete()
    session.commit()
    print("Record deleted successfully...")
except:
    session.rollback()
    print("DB Error!")
finally:
    session.close()
    print("Session Closed!")