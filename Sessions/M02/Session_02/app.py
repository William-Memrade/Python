# from flask import Flask, render_template, request
# app = Flask(__name__)

from aplicaciones import app
from flask import render_template, request


@app.route("/primer")
def primer():
    return render_template("primer.html")


@app.route("/lista-ordenada")
def lista_ordenada():
    return render_template("lista_ordenada.html")


@app.route("/lista-desordenada")
def lista_desordenada():
    return render_template("lista_desordenada.html")


@app.route("/image")
def image():
    return render_template("image.html")


@app.route("/login", methods=['GET', 'POST'])
def Login():
    error = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        if usuario == 'admin' and clave == '123456':
            return render_template("principal.html", usuario=usuario)
        else:
            error = 'Usuario y/o contraseña incorrecta!!'

    return render_template("form1.html", error=error)


@app.route("/register")
def Registro():
    return render_template("register.html")


@app.route("/personas")
def personas():
    lista_personas = [
        {'id': 1, 'nombre': 'alicia', 'edad': 30},
        {'id': 2, 'nombre': 'beto', 'edad': 20},
        {'id': 3, 'nombre': 'camila', 'edad': 25},
        {'id': 4, 'nombre': 'diana', 'edad': 22},
    ]

    return render_template('tabla.html', lista=lista_personas)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "main":
    app.run()
