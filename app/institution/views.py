from app import db, app
from app.institution.models import Institution
from app.institution.forms import InstitutionForm
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify
from app.institution.controller import createInstitution, updateInstitution, checkInstitutionId, login_required, admin_required


@app.route('/api/institutions')
def get_institutions():
    institution = Institution.query.filter_by(validated=True).all()
    return jsonify({'elements': [element.to_json_min() for element in institution]})


@app.route('/api/institutions', methods=["POST"])
@login_required
def add_institution():
    data = request.get_json(force=True)
    form = InstitutionForm(MultiDict(mapping=data))
    if form.validate():
        institution = createInstitution(data)
        db.session.add(institution)
        db.session.commit()
        return jsonify({'element': institution.to_json_min()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institutions/<int:id>')
def get_institution(id):
    institution = checkInstitutionId(id)
    return jsonify({'element': institution.to_json()}), 200


@app.route('/api/institutions/<int:id>', methods=["PUT"])
@admin_required
def update_institution(id):
    institution = Institution.query.get(id)
    if not institution:
        abort(404)
    data = request.get_json(force=True)
    form = InstitutionForm(MultiDict(mapping=data))
    if form.validate():
        updateInstitution(institution, data)
        return jsonify({'element': institution.to_json_min()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institutions/<int:id>', methods=["DELETE"])
@admin_required
def delete_institution(id):
    institution = checkInstitutionId(id)
    db.session.delete(institution)
    db.session.commit()
    return jsonify({'success': 'true'}), 200
