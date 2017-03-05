from app import db

class Wilaya(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wilaya_name = db.Column(db.String(32), unique=True)
    institutions = db.relationship('Institution', backref='wilaya', lazy='dynamic')
    communes = db.relationship('Commune', backref='wilaya', lazy='dynamic')

    def to_json_min(self):
        return{
            'id': self.id,
            'name': self.wilaya_name
        }

    def to_json(self):
        return{
            'id': self.id,
            'name': self.wilaya_name,
            'communes': [element.to_json_min() for element in self.communes.all()]
        }