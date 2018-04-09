# using
#
# conn = Connect()
# session = conn.session()
# session.execute(SQL) or result = session.query(...) SQLAlchemy..
# session.close()

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConfig:
      def __init__(self, configfile):

        with open(configfile, encoding="utf-8-sig") as f:
            data = json.load(f)
            item = data["postgres"]

            self.host = item["host"]
            self.database = item["database"]
            self.user = item["user"]
            self.password = item["password"]
            f.close()

class Connect:
    def __init__(self):
        dbconfig = DBConfig("./database/config.json")
        self.host = dbconfig.host
        self.database = dbconfig.database
        self.user = dbconfig.user
        self.password = dbconfig.password
        connStr = "postgresql+psycopg2://"+self.user+":"+self.password+"@"+self.host+"/"+self.database
        engine = create_engine(connStr)
        self.session = sessionmaker(bind=engine)


if __name__ == "__main__":
    print("Class working successfully..")

