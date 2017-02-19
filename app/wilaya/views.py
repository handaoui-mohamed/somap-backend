from app import db, app
from app.wilaya.models import Wilaya

@app.route('/api/wilayas')
def get_wilayas():
    wilayas = Wilaya.query.all()
    return jsonify({'elements': [element.to_json() for element in wilayas]})

@app.route('/api/wilayas/<int:id>')
def get_wilayas_by_id(id):
    wilaya = Wilaya.query.get(id)
    if not wilaya:
        abort(404)
    return jsonify({'element':wilaya.to_json()})