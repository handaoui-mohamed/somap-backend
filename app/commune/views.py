from app import db, app
from app.commune.models import Commune
from app.commune.forms import CommuneForm
from app.commune.controller import checkCommuneId, createCommune, updateCommune
from app.user.controller import admin_required
from werkzeug.datastructures import MultiDict
from flask import request, jsonify


@app.route('/api/communes')
def get_communes():
    communes = Commune.query.all()
    return jsonify({'elements': [element.to_json() for element in communes]})


@app.route('/api/communes', methods=["POST"])
@admin_required
def add_commune(currentUser):
    data = request.get_json(force=True)
    form = CommuneForm(MultiDict(mapping=data))
    if form.validate(data):
        commune = createCommune(data)
        return jsonify({'element': commune.to_json()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/communes/<int:id>')
def get_commune_by_id(id):
    commune = checkCommuneId(id)
    return jsonify({'element': commune.to_json()})


@app.route('/api/communes/<int:id>', methods=["PUT"])
@admin_required
def update_commune(currentUser, id):
    commune = checkCommuneId(id)
    data = request.get_json(force=True)
    form = CommuneForm(MultiDict(mapping=data))
    if form.validate(data):
        updateCommune(commune, data)
        return jsonify({'element': commune.to_json()})
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/communes/<int:id>', methods=["DELETE"])
@admin_required
def delete_commune(currentUser, id):
    commune = checkCommuneId(id)
    db.session.delete(commune)
    db.session.commit()
    return jsonify({'success': 'true'}), 200
