# using
#
# conn = Connect()
# session = conn.session()
# session.execute(SQL) or result = session.query(...) SQLAlchemy..
# session.close()

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('model.settings.Config')

class Connect:
    def __init__(self):
        connStr = "postgresql+psycopg2://"+app.config['USER']+":"+app.config['PASSWORD']+"@"+app.config['HOST']+"/"+app.config['DATABASE']
        engine = create_engine(connStr)
        self.session = sessionmaker(bind=engine)
        # print(connStr)


if __name__ == "__main__":
    print("Class working successfully..")

