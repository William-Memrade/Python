from flask import Blueprint, render_template, redirect
from aplicaciones.modelos.aeropuerto import Aeropuerto
from aplicaciones import db

aeropuertos = Blueprint('aeropuertos', __name__)

@aeropuertos.route('/aeropuertos/')
def login_view():
    return 'Este es mi blueprint de aeropuertos'

@aeropuertos.route('/aeropuertos/lista/')
def aeropuertos_lista():
    aeropuertos_list = Aeropuerto.query.all()
    print(aeropuertos_list)
    return render_template('/aeropuertos/lista-aeropuertos.html',aeropuertos=aeropuertos_list)

@aeropuertos.route('/aeropuertos/insertar/')
def nuevo_Aeropuerto():
    aeropuerto = Aeropuerto('Aeropuerto de Ilopango', 3, "Ilopango")
    db.session.add(aeropuerto)
    db.session.commit()
    return 'El Aeropuerto fue agregado con exito!!!'

@aeropuertos.route('/aeropuertos/modificar/<int:id>/')
def modificar_Aeropuerto(id):
    aeropuerto = Aeropuerto.query.get_or_404(id)
    aeropuerto.ciudad = ('San Luis Talpa')
    db.session.commit()
    return 'El Aeropuerto fue modificado con exito!!!'

@aeropuertos.route('/aeropuertos/eliminar/<int:id>/')
def eliminar_Aeropuerto(id):
    aeropuerto = Aeropuerto.query.get_or_404(id)
    db.session.delete(aeropuerto)
    db.session.commit()
    return redirect('/aeropuertos/lista/')

@aeropuertos.route('/aeropuertos/filtrar/<int:idpais>/')
def aeropuertos_lista_filtrar(idpais):
    aeropuertos_list = Aeropuerto.query.filter_by(pais_id = idpais)
    print(aeropuertos_list)
    return render_template('/aeropuertos/lista-aeropuertos.html',aeropuertos=aeropuertos_list)
