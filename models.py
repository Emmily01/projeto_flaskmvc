from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    local_encontrado = db.Column(db.String(100), nullable=False)
    data_registro = db.Column(db.DateTime, default=datetime.now) 
    status = db.Column(db.String(20), default='Ativo')
    retirado_por = db.Column(db.String(100), nullable=True)
    data_devolucao = db.Column(db.DateTime, nullable=True)