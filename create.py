from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from database.Connection import Connect
from database.Rehber import Rehber

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://unsal:Qaz1wsx2!@u2y.cnyxtuppiqxw.eu-west-1.rds.amazonaws.com:5432/gfox_dev')

RehberTable = Rehber(Base)

Base.metadata.create_all(engine)
