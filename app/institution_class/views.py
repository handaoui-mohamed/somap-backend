from app import db, app
from app.institution_class.models import InstitutionClass
from app.institution_class.forms import InstitutionClassForm
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify


@app.route('/api/institution_classes')
def query():
    institution_classes = InstitutionClass.query.all()
    return jsonify({'elements': [element.to_json_min() for element in institution_classes]})


@app.route('/api/institution_classes', methods=["POST"])
def post():
    data = request.get_json(force=True)
    form = InstitutionClassForm(MultiDict(mapping=data))
    if form.validate():
        class_denomination = data.get('denomination')
        institution_class = InstitutionClass(denomination=denomination)
        db.session.add(institution_class)
        db.session.commit()
        return jsonify({'element': institution_class.to_json_min()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institution_classes/<int:id>')
def get(id):
    institution_class = InstitutionClass.query.get(id)
    if not institution_class:
        abort(404)
	return jsonify({'element': institution_class.to_json()})


@app.route('/api/institution_classes/<int:id>', methods=["PUT"])
def put(id):
    institution_class = InstitutionClass.query.get(id)
    if not institution_class:
        abort(404)
        data = request.get_json(force=True)
        form = InstitutionClassForm(MultiDict(mapping=data))
        if form.updateValidate():
            institution_class.denomination = data.get('denomination')
            institution_class.icon_url = data.get('icon_url')
            db.session.add(institution_class)
            db.session.commit()
            return jsonify({'element': institution_class.to_json()})
	return jsonify({"form_errors": form.errors}), 400


@app.route('/api/institution_classes/<int:id>', methods=["DELETE"])
def delete(id):
    institution_class = InstitutionClass.query.get(id)
    if not institution_class:
        abort(404)
    db.session.delete(institution_class)
    db.session.commit()
    return jsonify({'success': 'true'}), 200
