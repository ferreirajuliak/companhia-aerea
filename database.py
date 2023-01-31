from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, insert, delete
from models import Clientes, Base, Aeroportos, Voos, Reservas
from sqlalchemy_utils import database_exists, create_database
from settings import DATABASE_URL

print(DATABASE_URL)
engine = create_engine('postgresql+psycopg2://username:postgres@172.17.0.3:5432/companhia-aerea')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
                                         
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Base de dados criada com sucesso!!")
    else:
        print("Base de dados já foi criada!!")
        engine.connect()

def init_tables():
    import models
    Base.metadata.create_all(bind=engine)
    print("Tables has been created!!")
    ret = {"status": "Tables has been created!!"}
    return ret


