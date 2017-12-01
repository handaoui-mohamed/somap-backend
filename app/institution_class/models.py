from app import db


class InstitutionClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    institutions = db.relationship(
        'Institution', backref='institution_class', lazy='dynamic')

    def to_json_min(self):
        return{
            'id': self.id,
            'name': self.name
        }

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
