from flask import Blueprint, render_template

login = Blueprint('login', __name__)
usuarios = Blueprint('usuarios', __name__)

@login.route('/login/')
def login_view():
    return 'Este es mi blueprint de login'

@usuarios.route('/usuarios/lista/')
def usuarios_lista():
    return 'Este es mi blueprint de usuarios'
