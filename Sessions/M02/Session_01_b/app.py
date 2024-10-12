from flask import Flask, render_template

app = Flask(__name__)


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


@app.route("/login")
def Login():
    return render_template("form1.html")


@app.route("/register")
def Registro():
    return render_template("register.html")


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "main":
    app.run()
