from flask import Blueprint, render_template
from aplicaciones.modelos.rol import Rol
from aplicaciones.modelos.usuario import Usuario
from aplicaciones import db

login = Blueprint('login', __name__)
usuarios = Blueprint('usuarios', __name__)

@login.route('/login/')
def login_view():
    return 'Este es mi blueprint de login'

@usuarios.route('/usuarios/lista/')
def usuarios_lista():
    users = Usuario.query.all()
    return render_template('Este es mi blueprint de usuarios', usuarios = users)

@usuarios.route('/usuarios/insertar/')
def nuevo_usuario():
    user = Usuario('beto', 'beto', 'perez', 'beto@gmail.com', '123456', 1)
    db.session.add(user)
    db.session.commit()
    return 'El usuario fue agregado con exito!!!'

@usuarios.route('/usuarios/modificar/<int:id>/')
def modificar_usuario(id):
    user = Usuario.query.get_or_404(id)
    user.correo = ('alicia2024@gmail.com')
    db.session.commit()
    return 'El usuario fue modificado con exito!!!'

@usuarios.route('/usuarios/eliminar/<int:id>/')
def eliminar_usuario(id):
    user = Usuario.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return 'El usuario fue eliminado con exito!!!'