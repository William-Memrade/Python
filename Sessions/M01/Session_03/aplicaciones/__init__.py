from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from aplicaciones.usuarios.views import login, usuarios
from aplicaciones.aeropuertos.views import aeropuertos
from aplicaciones.paises.views import paises
from aplicaciones.modelos.rol import Rol
from aplicaciones.modelos.usuario import Usuario
from aplicaciones.modelos.aeropuerto import Aeropuerto

# VISTAS
app.register_blueprint(login)
app.register_blueprint(usuarios)
app.register_blueprint(paises)
app.register_blueprint(aeropuertos)
