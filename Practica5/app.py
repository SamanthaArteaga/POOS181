#importación del framework
from flask import Flask

#Inicialización del APP
app= Flask(__name__)

#Declaración de ruta http://localhost:5000
@app.route('/')
def index():
    return"Hola Mundo FLASK"


@app.route('/guardar')
def guardar():
    return"Se guardo en la BD"


@app.route('/eliminar')
def eliminar():
    return"Se elimino en la BD"


#Ejecución del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)