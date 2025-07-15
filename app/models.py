from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storage = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    location = db.Column(db.String(50))
    domain = db.Column(db.String(100))
    db_name = db.Column(db.String(50))
    db_user = db.Column(db.String(50))
    db_password = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
