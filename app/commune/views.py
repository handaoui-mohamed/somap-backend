from app import db, app
from app.commune.models import Commune
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify

@app.route('/api/communes')
def get_commune():
    communes = Commune.query.all()
    return jsonify({'elements': [element.to_json_min() for element in communes]})

@app.route('/api/communes/<int:id>')
def get_commune_by_id(id):
    commune = Commune.query.get(id)
    if not commune:
        abort(404)
    return jsonify({'element':commune.to_json()})