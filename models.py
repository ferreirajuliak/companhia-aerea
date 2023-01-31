from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Float
from flask_login import UserMixin

Base = declarative_base()

class Aeroportos(Base):
    __tablename__ = 'aeroportos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(64), unique=True)
    cidade = Column(String(64))

class Voos(Base):
    __tablename__ = 'voos'
    id = Column(Integer, primary_key=True)
    origem = Column(String(64), ForeignKey("aeroportos.nome"))
    destino = Column(String(64), ForeignKey("aeroportos.nome"))
    data = Column(DateTime)
    preco = Column(Float)
    capacidade = Column(Integer)
    passageiros = Column(Integer)


class Clientes(UserMixin, Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(128))
    email = Column(String(128))
    password = Column(String(64))


class Reservas(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True)
    e_ticket = Column(String(32))
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    id_voo = Column(Integer, ForeignKey("voos.id"))
