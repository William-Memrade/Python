from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from aplicaciones.usuarios.views import login, usuarios
from aplicaciones.modelos.rol import Rol
from aplicaciones.modelos.usuario import Usuario

# VISTAS
app.register_blueprint(login)
app.register_blueprint(usuarios)
