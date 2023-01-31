Protótipo de uma aplicação RESTful API de um sistema de vendas de passagens aéreas usando Python, Flask, PostgreSQL e docker

ROTAS:
-> Adicionar usuarios	
URL:5000/usuarios	Método POST

-> Login	
URL:5000/login	Método POST

-> Logout	
URL:5000/logout	Método GET

-> Retornar aeroportos	
URL:5000/aeroportos	Método GET

-> Retornar aeroportos por origem	
URL:5000/aeroportos/<nome>	Método GET

-> Retornar voos por data	
URL:5000/voos/<data>	Método GET

-> Retornar voos com menor tarifa por número de passageiros 	
URL:5000/voos-passageiro/<n> Método GET

-> Efetuar reserva	
URL:5000/reserva	Método POST
