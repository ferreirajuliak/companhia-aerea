FROM python
RUN apt-get update -y && apt-get install python3-pip -y && apt-get install python-dev -y
WORKDIR /projetoFlask
COPY app.py database.py models.py routes.py settings.py controllers.py requerimentos.txt /projetoFlask/
WORKDIR /projetoFlask
RUN pip install -r requerimentos.txt 
RUN pip install flask
#CMD ["python","app.py"]
CMD ["flask","run","--host=0.0.0.0"]