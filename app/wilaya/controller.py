from app import db
from flask import abort
from app.wilaya.models import Wilaya


def checkWilayaId(id):
    wilaya = Wilaya.query.get(id)
    if not wilaya:
        abort(404)
    return wilaya


def createWilaya(data):
    name = data.get('name')
    code = data.get('code')
    wilaya = Wilaya(name=name, code=code)
    db.session.add(wilaya)
    db.session.commit()
    return wilaya


def updateWilaya(wilaya, data):
    wilaya.name = data.get('name')
    wilaya.code = data.get('code')
    db.session.add(wilaya)
    db.session.commit()
