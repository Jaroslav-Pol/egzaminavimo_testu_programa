from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

'''Sukuriame DB'''
emgine = create_engine('sqlite:///testai.db')
Base = declarative_base()

'''Kuriame lenteles'''
class Vartotojai(Base):
    __tablename__ = 'vartotojai'
    id = Column('ID', Integer, primary_key=True)
    vardas = Column('Vardas', String)
    pavarde = Column('Pavardė', String)
    email = Column('El_paštas')

class Klausimai(Base):
    __tablename__ = 'klausimai'
    id = Column('ID', Integer, primary_key=True)
    klausimas = Column('Klausimas', String)
    testo_id = Column('Testo_ID', Integer)

class Atsakymai(Base):
    __tablename__ = 'atsakymai'
    id = Column('ID', Integer, primary_key=True)
    klausimo_id = Column('Klausimo_ID', Integer)
    atsakymas = Column('Atsakymas', String)
    ar_teisingas = Column('Ar_teisingas', Boolean)

class Sprendimai(Base):
    __tablename__ = 'sprendimai'
    id = Column('ID', Integer, primary_key=True)
    vartotojo_id = Column('Vartotojo_ID')
    sprendimo_data = Column('Sprendimo_data', DateTime, default=datetime.datetime.utcnow())

class VartotojuSprendimai(Base):
    __tablename__ = 'vartotoju_sprendimai'
    id = Column('ID', Integer, primary_key=True)
    sprendimo_id = Column('Sprendimo_ID', Integer)
    klausimo_id = Column('Klausimo_ID', Integer)
    atsakymo_id = Column('Atsakymo_ID', Integer)

class Testas(Base):
    __tablename__ = 'testas'
    id = Column('ID', Integer, primary_key=True)
    pavadinimas = Column('Pavadinimas', String)

