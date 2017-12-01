from app import db, app
from app.wilaya.models import Wilaya
from app.wilaya.forms import WilayaForm
from app.wilaya.controller import checkWilayaId, createWilaya, updateWilaya
from werkzeug.datastructures import MultiDict
from flask import request, jsonify


@app.route('/api/wilayas')
def get_wilayas():
    wilayas = Wilaya.query.all()
    return jsonify({'elements': [element.to_json_min() for element in wilayas]})


@app.route('/api/wilayas', methods=["POST"])
def add_wilaya():
    data = request.get_json(force=True)
    form = WilayaForm(MultiDict(mapping=data))
    if form.validate():
        wilaya = createWilaya(data)
        return jsonify({'element': wilaya.to_json_min()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/wilayas/<int:id>')
def get_wilaya_by_id(id):
    wilaya = checkWilayaId(id)
    return jsonify({'element': wilaya.to_json()})


@app.route('/api/wilayas/<int:id>', methods=["PUT"])
def update_wilaya(id):
    wilaya = checkWilayaId(id)
    data = request.get_json(force=True)
    form = WilayaForm(MultiDict(mapping=data))
    if form.updateValidate(wilaya.id):
        updateWilaya(wilaya, data)
        return jsonify({'element': wilaya.to_json_min()})
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/wilayas/<int:id>', methods=["DELETE"])
def delete_wilaya(id):
    wilaya = checkWilayaId(id)
    db.session.delete(wilaya)
    db.session.commit()
    return jsonify({'success': 'true'}), 200
