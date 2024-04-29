from db import db

class Pacientes(db.Model):
    tablename = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100)) 