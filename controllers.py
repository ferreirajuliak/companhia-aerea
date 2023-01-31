import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, insert, delete
from models import Clientes, Base, Aeroportos, Voos, Reservas
from sqlalchemy_utils import database_exists, create_database
from settings import DATABASE_URL
from datetime import datetime, timedelta
from flask_login import login_user, logout_user

engine = create_engine("postgresql+psycopg2://username:postgres@172.17.0.3:5432/companhia-aerea")

#usuario
def add_usuario_json(json_usuario):
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Clientes).
            values(
                nome = json_usuario['nome'],
                email = json_usuario['email'],
                password = json_usuario['password'])
    )
    print(query)
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "User has been added"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret

#login
def controller_load_user(user_id):
    Session = sessionmaker(engine)
    session = Session()    
    return session.query(Clientes).filter_by(id=user_id).first()

def controller_login(credentials):
    Session = sessionmaker(engine)
    session = Session()    
    user = (
        session.query(Clientes)
        .filter_by(email=credentials["email"], password=credentials["password"])
        .first()
    )
    print(user)
    login_user(user)
    session.close()
    return "Logged In"

def controller_logout():
    logout_user()
    return "Logged Out"

#aeroporto
def get_aeroportos():
    Session = sessionmaker(engine)
    session = Session()     
    
    aeroportos_obj = session.query(Aeroportos).all()
    session.close()
    return [
        {'Aeroporto': airport.nome}
        for airport in aeroportos_obj
        ]

def get_aeroportos_origem(origem):
    Session = sessionmaker(engine)
    session = Session()

    aeroportos_obj = session.query(Voos).filter_by(origem=origem).all()
    session.close()
    return  [
        {'Aeroporto': aeroporto.destino}
        for aeroporto in aeroportos_obj
        ]

#retornar voos
#por data
def get_voos_data(data):
    data2 = datetime.strptime(data, '%Y-%m-%d') + timedelta(1)
    data2 = data2.strftime('%Y-%m-%d')
    Session = sessionmaker(engine)
    session = Session()
    voos_obj = (
        session.query(Voos)
        .filter( (Voos.data >= data) & (Voos.data < data2) )
        .all()
    )
    session.close()
    return [
        {'Origem' : voos.origem, 
        'Destino' : voos.destino, 
        'Preco': str(voos.preco)}
        for voos in voos_obj
    ]
#por preço
def get_voos_preco(n):
    passageiros_n = int(n)
    Session = sessionmaker(engine)
    session = Session()
    voos_obj = (
        session.query(Voos).order_by(Voos.preco.asc()).all()
    )
    session.close()
    return [
        {'Origem' : voos.origem, 
        'Destino' : voos.destino, 
        'Preco': str((voos.preco*passageiros_n))}
        for voos in voos_obj
    ]
#reserva
def compra(data):
    import string 
    import random 
    N = 8
    ticket = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = N)) 
    
    Session = sessionmaker(engine)
    session = Session()
    query = (
            insert(Reservas).
            values(
                id_cliente = data['id_cliente'],
                id_voo = data['id_voo'],
                e_ticket = ticket)
    )
    print(query)
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"Reserva concluida": ticket}

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret
