
import json
from database.Connection import Connect

class Query():

    def __init__(self):
        conn = Connect()
        self.session = conn.session()

    def execute(self, SQL):
        # try:
            result = self.session.execute(SQL)

            items =  []
            for row in result:
               items.append({'rehber_id':row['rehber_id'],'rehber_adi':row['rehber_adi'],'rehber_adres':row['rehber_adres']})

            result_json = json.dumps({'rehber':items})

            print(result_json)
            print("Connection Closed Successfully")
            self.session.close()

if __name__ == "__main__":
    query = Query()
    query.execute("Select * from Rehber")

