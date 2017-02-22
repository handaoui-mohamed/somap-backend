from app import db, app
from app.institution_class.models import InstitutionClass
from app.institution_class.forms import InstitutionClassForm
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify

@app.route('/api/institution_classes',methods=["GET","POST"])
def get_intitution_classes():
    if request.method == 'GET':        
        institution_classes = InstitutionClass.query.all()
        return jsonify({'elements': [element.to_json_min() for element in institution_classes]})
    elif request.method == 'POST': #POST method
        data = request.get_json(force=True)
        form = InstitutionClassForm(MultiDict(mapping=data))
        if form.validate():
            class_denomination = data.get('class_denomination')
            icon_url = data.get('icon_url')
            institution_class=InstitutionClass(class_denomination=class_denomination,icon_url=icon_url)
            db.session.add(institution_class)
            db.session.commit() 
            return jsonify({'element':institution_class.to_json_min()}),201
        return jsonify({"form_errors": form.errors}), 400

@app.route('/api/institution_classes/<int:id>',methods=["GET","DELETE","PUT"])
def get_institution_class_by_id(id):
    institution_class = InstitutionClass.query.get(id)
    if not institution_class:
            abort(404)
    if request.method == 'GET':
        return jsonify({'element':institution_class.to_json()})
    elif request.method == "PUT": #PUT method
        data = request.get_json(force=True)
        form = InstitutionClassForm(MultiDict(mapping=data))
        if form.updateValidate():
            institution_class.class_denomination=data.get('class_denomination')
            institution_class.icon_url=data.get('icon_url')
            db.session.add(institution_class)
            db.session.commit() 
            return jsonify({'element':institution_class.to_json()})
        return jsonify({"form_errors": form.errors}), 400
    elif request.method == "DELETE":
        db.session.delete(institution_class)
        db.session.commit()
        return jsonify({'success': 'true'}), 200