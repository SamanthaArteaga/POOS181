from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fruta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruta = db.Column(db.String(50), nullable=False)
    temporada = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def _init_(self, fruta, temporada, precio, stock):
        self.fruta = fruta
        self.temporada = temporada
        self.precio = precio
        self.stock = stock