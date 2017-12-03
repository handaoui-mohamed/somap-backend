# -*- coding: utf-8 -*-
from app import db, app
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime, timedelta
from config import SECRET_KEY
import jwt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String)
    email = db.Column(db.String(60))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=False)
    wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def create_token(self):
        payload = {
            'sub': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token.decode('unicode_escape')

    def to_json(self):
        from app.wilaya.models import Wilaya
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'isAdmin': self.is_admin,
            "wilaya": Wilaya.query.get(self.wilaya_id or 16).to_json_min()
        }

    def __repr__(self):
        return '<User N=%s username=%s>' % (self.id, self.username)
