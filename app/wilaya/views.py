from app import db, app
from app.wilaya.models import Wilaya
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify

@app.route('/api/wilayas')
def get_wilayas():
    wilayas = Wilaya.query.all()
    return jsonify({'elements': [element.to_json_min() for element in wilayas]})

@app.route('/api/wilayas/<int:id>')
def get_wilayas_by_id(id):
    wilaya = Wilaya.query.get(id)
    if not wilaya:
        abort(404)
    return jsonify({'element':wilaya.to_json()})