from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model.Connection import Connect
from model.Rehber import Rehber
from flask import Flask

app = Flask(__name__)
app.config.from_object('model.settings.Config')

connStr = "postgresql+psycopg2://" + \
    app.config['USER']+":"+app.config['PASSWORD']+"@" + \
    app.config['HOST']+"/"+app.config['DATABASE']

Base = declarative_base()
engine = create_engine(connStr)

RehberTable = Rehber(Base)

Base.metadata.create_all(engine)
