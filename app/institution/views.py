from app import db, app
from app.wilaya.models import Wilaya
from app.commune.models import Commune
from app.institution_class.models import InstitutionClass
from app.institution.models import Institution
from app.institution.forms import InstitutionForm
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify
from haversine import haversine


@app.route('/api/institutions',methods=["GET","POST"])
def add_get_institutions():
    if request.method == 'GET':        
        institution = Institution.query.filter_by(validated=True).all()
        return jsonify({'elements': [element.to_json_min() for element in institution]})
    elif request.method == 'POST': #POST Methode
        data = request.get_json(force=True)
        form = InstitutionForm(MultiDict(mapping=data))
        if form.validate():
            denomination = data.get('denomination').lower()
            description = data.get('description').lower()
            address = data.get('address').lower()
            phone = data.get('phone')
            fax = data.get('fax')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            wilaya = Wilaya.query.get(data.get('wilaya_id'))
            commune = Commune.query.get(data.get('commune_id'))
            institution_class = InstitutionClass.query.get(data.get('class_id'))
            institution=Institution(denomination=denomination,description=description,\
            commune=commune,address=address,phone=phone,fax=fax,latitude=latitude,\
            longitude=longitude,wilaya=wilaya,institution_class=institution_class)
            db.session.add(institution)
            db.session.commit() 
            return jsonify({'element':institution.to_json_min()}),201
        return jsonify({"form_errors": form.errors}), 400

@app.route('/api/institutions/<int:id>',methods=["GET"])
def get_institution(id):
    institution = Institution.query.get(id)
    if not institution or not institution.validated:
            abort(404)
    return jsonify({'elements': institution.to_json()}),200


def calculate_haversine(location1, location2, search_area):
    pos1 = location1["latitude"], location1["longitude"]
    pos2 = location2["latitude"], location2["longitude"]
    km = haversine(pos1,pos2)
    return km <= search_area