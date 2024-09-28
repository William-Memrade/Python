from flask import Blueprint, render_template, redirect
from aplicaciones.modelos.pais import Pais
from aplicaciones import db

paises = Blueprint('paises', __name__)

@paises.route('/paises/')
def login_view():
    return 'Este es mi blueprint de paises'

@paises.route('/paises/lista/')
def paises_lista():
    paises = Pais.query.all()
    print(paises)
    return render_template('/paises/lista-paises.html',paises=paises)

@paises.route('/paises/insertar/')
def nuevo_Pais():
    pais = Pais("El Savador")
    db.session.add(pais)
    db.session.commit()
    return 'El Pais fue agregado con exito!!!'

@paises.route('/paises/modificar/<int:id>/')
def modificar_Pais(id):
    pais = Pais.query.get_or_404(id)
    pais.pais = ('El Salvador')
    db.session.commit()
    return 'El Pais fue modificado con exito!!!'

@paises.route('/paises/eliminar/<int:id>/')
def eliminar_Pais(id):
    pais = Pais.query.get_or_404(id)
    db.session.delete(pais)
    db.session.commit()
    return redirect('/paises/lista/')