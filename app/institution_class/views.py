from app import db, app
from app.institution_class.models import InstitutionClass

@app.route('/api/institution_classes',["GET","POST"])
def get_intitution_classes():
    if request.method == 'GET':        
        institution_classes = InstitutionClass.query.all()
        return jsonify({'elements': [element.to_json() for element in institution_classes]})
    else: #POST method
        data = request.get_json(force=True)
        form = InstitutionClassForm(MultiDict(mapping=data))
        if form.validate():
            class_denomination = data.get('class_denomination')
            icon_url = data.get('icon_url')
            institution_class=InstitutionClass(class_denomination=class_denomination,icon_url=icon_url)
            db.session.add(institution_class)
            db.session.commit() 
            return jsonify({'element':institution_class.to_json()})
        return jsonify({"form_errors": form.errors}), 400

@app.route('/api/institution_classes/<int:id>',["GET","PUT"])
def get_wilayas_by_id(id):
    institution_class = InstitutionClass.query.get(id)
    if not institution_class:
            abort(404)
    if request.method == 'GET':
        return jsonify({'element':institution_class.to_json()})
    else: #PUT method
        data = request.get_json(force=True)
        form = InstitutionClassForm(MultiDict(mapping=data))
        if form.validate():
            institution_class.class_denomination=data.get('class_denomination')
            institution_class.icon_url=data.get('icon_url')
            db.session.add(institution_class)
            db.session.commit() 
            return jsonify({'element':institution_class.to_json()})
        return jsonify({"form_errors": form.errors}), 400