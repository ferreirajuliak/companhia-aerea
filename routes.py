from flask import Blueprint, request, json, jsonify
from sqlalchemy import create_engine, select, update, func, null, insert
from sqlalchemy.orm.session import sessionmaker
import database
import controllers
from flask.helpers import make_response
from models import Clientes, Base, Aeroportos, Voos, Reservas
from flask_login import LoginManager, login_required 

login_manager = LoginManager()
urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/')
def index():
    return "Welcome to Julia's Airline "

@urls_blueprint.route('/init_db', methods = ['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Database are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Database are not created!!"}    
    return ret    


@urls_blueprint.route('/create_tables', methods = ['GET'])
def create_tables():    
    try:
        database.init_tables()
        ret = {"status": "Tables are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Problems to create tables!!"}    
    return ret    

@urls_blueprint.route('/usuarios', methods = ['POST'])
def add_usuario_json():
    req_data = request.get_json()
    usuario_json = {"nome": req_data['nome'],  
                    "email": req_data['email'],
                    "password": req_data['password']}
    ret = controllers.add_usuario_json(usuario_json)
    print(usuario_json)
    return ret

@login_manager.user_loader
def load_user(user_id):
    return controllers.controller_load_user(user_id)

@urls_blueprint.route("/login", methods=["POST"])
def login():
    credentials = request.get_json()
    res = controllers.controller_login(credentials)
    return make_response(jsonify(res))

@urls_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    res = controllers.controller_logout()
    return make_response(jsonify(res))    



@urls_blueprint.route('/aeroportos', methods = ['GET'])
def get_aeroportos():
    ret = controllers.get_aeroportos()
    return json.dumps(ret)

@urls_blueprint.route('/aeroportos/<nome>', methods = ['GET'])
def get_aeroportos_origem(nome):
    ret = controllers.get_aeroportos_origem(nome)
    return json.dumps(ret)

@urls_blueprint.route('/voos/<data>', methods = ['GET'])
def get_voos_data(data):
    ret = controllers.get_voos_data(data)
    return json.dumps(ret)

@urls_blueprint.route('/voos-passageiro/<n>', methods = ['GET'])
def get_voos_preco(n):
    ret = controllers.get_voos_preco(n)
    return json.dumps(ret)

# @urls_blueprint.route('/reservas', methods = ['POST'])
# def comprar():
#     data = request.get_json()
#     ret = controllers.compra(data)
#     return json.dumps(ret)

@urls_blueprint.route('/reserva', methods = ['POST'])
def compra():
    req_data = request.get_json()
    reserva = {"id_voo": req_data['id_voo'],  
                    "id_cliente": req_data['id_cliente']}
    ret = controllers.compra(reserva)
    return json.dumps(ret)