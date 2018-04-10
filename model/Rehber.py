from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rehber(Base):
    __tablename__ = 'rehber'
    rehber_id = Column(Integer(), primary_key=True)
    rehber_adi = Column(String(50))
    rehber_tel = Column(String(60))
    rehber_adres = Column(String(255))

    # print(Rehber) deyince bu bolum basilir ekrana
    def __repr__(self):
        return "Rehber(rehber_id='{self.rehber_id}', " \
            "rehber_adi='{self.rehber_adi}', " \
            "rehber_tel='{self.rehber_tel}', " \
            "rehber_adres='{self.rehber_adres}')".format(self=self)

