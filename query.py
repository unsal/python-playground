from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import  or_
from database.Rehber import Rehber
from database.Connection import Connect

conn = Connect()
session = conn.session()


# Simple Query Order By
result = session.query(Rehber.rehber_adi, Rehber.rehber_tel).order_by(Rehber.rehber_adi)
for row in result:
    print(row)

# Count Record
record = session.query(func.count(Rehber.rehber_adi).label('count')).first()
print(record.count)

# Filter1
result = session.query(Rehber).filter(Rehber.rehber_adi=='Ugur Unsal').first()
print(result)

# Filter2
result = session.query(Rehber).filter_by(rehber_adi = 'Ugur Unsal').first()
print(result)

# Like
result = session.query(Rehber).filter(Rehber.rehber_adi.like('%Ugur%')).first()
print(result)


# Select Where And
result = session.query(Rehber).filter(
    Rehber.rehber_adi.like('%Ugur%'),
    Rehber.rehber_tel.like('%0532%')
)

for row in result:
    print(row.rehber_adres)

# Select Where OR
result = session.query(Rehber).filter(
    or_(
        Rehber.rehber_adi.like('%Ugur%'),
        Rehber.rehber_adi.like('%Damla%')
    )
)

for row in result:
    print(row.rehber_adi)

session.close()
print ("session Closed Successfully!")