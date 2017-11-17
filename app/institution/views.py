from app import db, app
from app.institution.models import Institution
from app.institution.forms import InstitutionForm
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify


@app.route('/api/institutions')
def get_institutions():
    institution = Institution.query.filter_by(validated=True).all()
    return jsonify({'elements': [element.to_json_min() for element in institution]})


@app.route('/api/institutions', methods=["POST"])
def add_institution():
    data = request.get_json(force=True)
    form = InstitutionForm(MultiDict(mapping=data))
    if form.validate():
        institution = Institution.new(data)
        db.session.add(institution)
        db.session.commit()
        return jsonify({'element': institution.to_json_min()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institutions/<int:id>')
def get_institution(id):
    institution = Institution.query.get(id)
    if not institution or not institution.validated:
        abort(404)
    return jsonify({'element': institution.to_json()}), 200
