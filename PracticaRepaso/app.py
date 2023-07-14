from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL
from models import db

app= Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_Fruteria'
app.secret_key='mysecretkey'
mysql= MySQL(app)


@app.route('/')
def index():
    return '¡Bienvenido a la Frutería!'

if __name__ == '__main__':
    app.run()

db = SQLAlchemy()

class Fruta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruta = db.Column(db.String(50), nullable=False)
    temporada = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, fruta, temporada, precio, stock):
        self.fruta = fruta
        self.temporada = temporada
        self.precio = precio
        self.stock = stock


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar_fruta():
    if request.method == 'POST':
        fruta = request.form['fruta']
        temporada = request.form['temporada']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])

        nueva_fruta = Fruta(fruta=fruta, temporada=temporada, precio=precio, stock=stock)
        db.session.add(nueva_fruta)
        db.session.commit()

        return redirect('/consultar')

    return render_template('IngresoFruta.html')

@app.route('/consultar')
def consultar_frutas():
    frutas = Fruta.query.all()
    return render_template('ConsultaFruta.html', frutas=frutas)

@app.route('/eliminar/<int:id>')
def eliminar_fruta(id):
    fruta = Fruta.query.get(id)
    db.session.delete(fruta)
    db.session.commit()
    return redirect('/consultar')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_fruta(id):
    fruta = Fruta.query.get(id)

    if request.method == 'POST':
        fruta.fruta = request.form['fruta']
        fruta.temporada = request.form['temporada']
        fruta.precio = float(request.form['precio'])
        fruta.stock = int(request.form['stock'])
        db.session.commit()

        return redirect('/consultar')

    return render_template('EditarFruta.html', fruta=fruta)

@app.route('/consultar_nombre', methods=['GET', 'POST'])
def consultar_frutas_nombre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        frutas = Fruta.query.filter(Fruta.fruta.ilike(f'%{nombre}%')).all()
        return render_template('consulta_frutas_nombre.html', frutas=frutas)

    return render_template('ConsultaFrutasNombre.html')


db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
