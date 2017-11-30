from app import db


class Wilaya(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    code = db.Column(db.Integer)
    institutions = db.relationship(
        'Institution', backref='wilaya', lazy='dynamic')
    communes = db.relationship('Commune', backref='wilaya', lazy='dynamic')
    users = db.relationship('User', backref='wilaya', lazy='dynamic')

    def to_json_min(self):
        return{
            'id': self.id,
            'name': self.name,
            'code': self.code
        }

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'communes': [element.to_json_min() for element in self.communes.all()]
        }
