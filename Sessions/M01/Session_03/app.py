from flask import Flask, render_template
from aplicaciones import app

# app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola esta es mi primera funcion con Flash'

@app.route('/inicio/')
def inicio():
    return 'Bienvenido a un inicio'

@app.route('/articulos/')
def articulos():
    return 'Esta es una lista de articulos'

@app.route('/pagina-html/')
@app.route('/pagina-html/<nombre>/')
def pagina_html(nombre = 'alicia'):
    return f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Mi Página Web</title>
            </head>
            <body>

            <header>
                <h1>Bienvenid@ a mi Página Web {nombre}</h1>
            </header>

            <p>Este es un párrafo de ejemplo en mi primera página web.</p>

            <h2>Lista de cosas que me gustan:</h2>
            <ul>
                <li>Programar</li>
                <li>Leer libros</li>
                <li>Escuchar música</li>
            </ul>

            </body>
        </html>
    '''

# @app.route('/primer-template/')
# def primer_template():
#     users = ['alicia', 'beto', 'camila', 'diana']
#     return render_template('primer-template.html', usuarios = users)

if __name__ == '__main__':
    app.run()
