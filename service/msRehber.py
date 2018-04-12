from flask import Flask
from flask import jsonify
from flask import Response
from model.Connection import Connect
from model.Rehber import Rehber
import sqlalchemy

def getRehber(kodu):
    conn = Connect()
    session = conn.session()
    # result = session.execute("select * from rehber where rehber_id = 01")
    result = session.query(Rehber).filter(Rehber.rehber_id == kodu).first()

    a = []
    for row in result:
        a_list = {}
        a_list["rehber_adi"] = row["rehber_adi"]
        a_list["rehber_tel"] = row["rehber_tel"]
        a_list["rehber_adres"] = row["rehber_adres"]
        a_list["rehber_zamandamgasi"] = row["rehber_zamandamgasi"]
        a.append(a_list)

    session.close()
    if (len(a) == 0):
        return Response("No records found..")
    else:
        return jsonify({"rehber": a})

