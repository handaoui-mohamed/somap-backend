from app import db

class InstitutionClass(db.model)
    id = db.Column(db.Integer, primary_key=True)
    class_denomination = db.Column(db.String(200), unique=True)
    icon_url = db.Column(db.String)

    def to_json(self):
        return{
            'id': self.id,
            'denomination': self.class_denomination,
            'icon_url': self.icon_url
        }