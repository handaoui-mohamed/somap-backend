from app import db, app
from app.institution_class.models import InstitutionClass
from app.institution_class.forms import InstitutionClassForm
from app.institution_class.controller import createInstitutionClass, updateInstitutionClass, checkInstitutionClassId
from app.user.controller import admin_required
from werkzeug.datastructures import MultiDict
from flask import request, jsonify


@app.route('/api/institution_classes')
def query():
    institutionClasses = InstitutionClass.query.all()
    return jsonify({'elements': [element.to_json_min() for element in institutionClasses]})


@app.route('/api/institution_classes', methods=["POST"])
@admin_required
def post(currentUser):
    data = request.get_json(force=True)
    form = InstitutionClassForm(MultiDict(mapping=data))
    if form.validate():
        institutionClass = createInstitutionClass(data)
        return jsonify({'element': institutionClass.to_json()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institution_classes/<int:id>')
def get(id):
    institutionClass = checkInstitutionClassId(id)
    return jsonify({'element': institution_class.to_json()})


@app.route('/api/institution_classes/<int:id>', methods=["PUT"])
@admin_required
def put(currentUser, id):
    institutionClass = checkInstitutionClassId(id)
    data = request.get_json(force=True)
    form = InstitutionClassForm(MultiDict(mapping=data))
    if form.updateValidate(institutionClass.id):
        updateInstitutionClass(institutionClass, data)
        return jsonify({'element': institutionClass.to_json()})
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institution_classes/<int:id>', methods=["DELETE"])
@admin_required
def delete(currentUser, id):
    institutionClass = checkInstitutionClassId(id)
    db.session.delete(institutionClass)
    db.session.commit()
    return jsonify({'success': 'true'}), 200
