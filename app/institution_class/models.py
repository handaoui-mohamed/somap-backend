from app import db


class InstitutionClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String, unique=True)
    institutions = db.relationship('Institution', backref='institution_class', lazy='dynamic')

    def to_json_min(self):
        return{
            'id': self.id,
            'name': self.denomination
        }

    def to_json(self):
        return{
            'id': self.id,
            'name': self.denomination,
            'institutions': [element.to_json_min() for element in self.institutions.all()]
        }
