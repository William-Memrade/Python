from flask import Flask
from aplicaciones.usuarios.views import login, usuarios

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(login)
app.register_blueprint(usuarios)
