from app import db

class InstitutionClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_denomination = db.Column(db.String(200), unique=True)
    icon_url = db.Column(db.String)
    institutions = db.relationship('Institution', backref='institution_class', lazy='dynamic')

    def to_json_min(self):
        return{
            'id': self.id,
            'denomination': self.class_denomination,
            'icon_url': self.icon_url
        }

    def to_json(self):
        return{
            'id': self.id,
            'denomination': self.class_denomination,
            'icon_url': self.icon_url,
            'institutions': [element.to_json_min() for element in self.institutions.all()]
        }