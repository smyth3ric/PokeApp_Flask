from sys import base_exec_prefix
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

#create models based off of ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable =False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250))
    Pokemon = db.relationship("Pokemon", backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self,user):
        db.session.add(user)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String)
    base_exp = db.Column(db.Integer)
    ability = db.Column(db.String)
    base_hp = db.Column(db.Integer)
    base_att = db.Column(db.Integer)
    base_def =db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



    def __init__(self, name, img_url, base_exp, ability, base_hp, base_att, base_def, user_id):
        self.name = name
        self.img_url = img_url
        self.base_exp = base_exp
        self.ability = ability
        self.base_hp = base_hp
        self.base_att = base_att
        self.base_def = base_def
        self.user_id = user_id

        

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.add(self)
        db.session.commit()

    def updateInfo(self):
        db.session.add(self)
        db.session.commit()

    

    