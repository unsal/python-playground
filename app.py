from flask import Flask
from flask import jsonify
from database.Connection import Connect

app = Flask(__name__)

@app.route('/rehber', methods=['GET'])
def getRehber():
    return rehberListesi()

def rehberListesi():
    conn = Connect()
    session = conn.session()

    result = session.execute("Select * from Rehber")
    a=[]
    for row in result:
        a_list = {}
        a_list["rehber_adi"] = row["rehber_adi"]
        a_list["rehber_tel"] = row["rehber_tel"]
        a_list["rehber_adres"]=row["rehber_adres"]
        a_list["rehber_zamandamgasi"]=row["rehber_zamandamgasi"]
        a.append(a_list)

    session.close()
    return jsonify({"rehber":a})


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Server started successfully!")