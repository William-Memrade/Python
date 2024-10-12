from flask import Flask
from aplicaciones.login.views import login

app = Flask(__name__)
app.register_blueprint(login)
