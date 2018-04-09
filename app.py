from flask import Flask
from flask import jsonify
from flask import Response
from database.Connection import Connect
from database.Rehber import Rehber

app = Flask(__name__)

@app.route('/rehber/<id>', methods=['GET'])
def getRehber(id):
    conn = Connect()
    session = conn.session()
    # result = session.execute("select * from rehber where rehber_id = "+id)
    result = session.query(Rehber).filter(Rehber.rehber_id == id).first()

    a=[]
    for row in result:
        a_list = {}
        a_list["rehber_adi"] = row["rehber_adi"]
        a_list["rehber_tel"] = row["rehber_tel"]
        a_list["rehber_adres"]=row["rehber_adres"]
        a_list["rehber_zamandamgasi"]=row["rehber_zamandamgasi"]
        a.append(a_list)

    session.close()
    if (len(a) == 0):
        return Response("No records found..")
    else:
        return jsonify({"rehber":a})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Server started successfully!")
