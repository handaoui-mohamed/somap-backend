from app import db
from app.institution.models import Institution
from flask import abort


def checkInstitutionId(id):
    institution = Institution.query.get(id)
    if not institution or not institution.validated:
        abort(404)
    return institution


def createInstitution(data):
    name = data.get('name').lower()
    description = data.get('description').lower()
    address = data.get('address').lower()
    phone = data.get('phone')
    fax = data.get('fax')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    wilaya_id = data["wilaya"]["id"]
    commune_id = data["commune"]["id"]
    class_id = data["class"]["id"]
    institution = Institution(name=name, description=description, address=address, phone=phone,
                              fax=fax, latitude=latitude, longitude=longitude, commune_id=commune_id, wilaya_id=wilaya_id, class_id=class_id)
    return institution


def updateInstitution(institution, data):
    institution.name = data.get('name').lower()
    institution.description = data.get('description').lower()
    institution.address = data.get('address').lower()
    institution.phone = data.get('phone')
    institution.fax = data.get('fax')
    institution.latitude = data.get('latitude')
    institution.longitude = data.get('longitude')
    institution.wilaya_id = data["wilaya"]["id"]
    institution.commune_id = data["commune"]["id"]
    institution.class_id = data["class"]["id"]
    institution.validated = data.get('validated', False)
    db.session.add(institution)
    db.session.commit()
