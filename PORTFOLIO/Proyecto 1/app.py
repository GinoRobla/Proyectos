from flask import Flask
from rutas.rutas_bebidas import bp_bebidas
from rutas.rutas_clientes import bp_clientes
#creamos nuestro entorno virtual luego lo activamos y descargamos flask, establecemos flask en nuestro proyecto app.py y lo corremos con los siguiente comandos en consola
#Python -m venv .venv
#.venv\Scripts\activate
#pip install flask
#Set FLASK_APP=app.py
#Flask run --debug

app = Flask(__name__)

app.register_blueprint(bp_bebidas)
app.register_blueprint(bp_clientes)

if __name__ == "__main__":
    app.run(debug=True)