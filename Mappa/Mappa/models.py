from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1500), unique=True)
    password = db.Column(db.String(1500))
    username = db.Column(db.String(150))
    Favorites = db.relationship('Favorite')
