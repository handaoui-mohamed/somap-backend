from app import db
from flask import abort
from app.institution_class.models import InstitutionClass


def checkInstitutionClassId(id):
    institutionClass = InstitutionClass.query.get(id)
    if not institutionClass:
        abort(404)
    return institutionClass


def createInstitutionClass(data):
    name = data.get('name')
    description = data.get('description')
    institutionClass = InstitutionClass(
        name=name, description=description)
    db.session.add(institutionClass)
    db.session.commit()
    return institutionClass


def updateInstitutionClass(institutionClass, data):
    institutionClass.name = data.get('name')
    institutionClass.description = data.get('description')
    db.session.add(institutionClass)
    db.session.commit()
