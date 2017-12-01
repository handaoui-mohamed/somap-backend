from app import db
from flask import abort
from app.commune.models import Commune


def checkCommuneId(id):
    commune = Commune.query.get(id)
    if not commune:
        abort(404)
    return commune


def createCommune(data):
    name = data.get('name')
    zip_code = data.get('zip_code')
    wilaya = data.get('wilaya')
    if wilaya:
        wilaya_id = wilaya.get('id')
    commune = Commune(name=name, zip_code=zip_code, wilaya_id=wilaya_id)
    db.session.add(commune)
    db.session.commit()
    return commune


def updateCommune(commune, data):
    commune.name = data.get('name')
    commune.zip_code = data.get('zip_code')
    wilaya = data.get('wilaya')
    if wilaya:
        commune.wilaya_id = wilaya.get('id')
    db.session.add(commune)
    db.session.commit()
