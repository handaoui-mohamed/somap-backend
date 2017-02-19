from app import db

class Wilaya(db.model)
    id = db.Column(db.Integer, primary_key=True)
    wilaya_name = db.Column(db.String(32), unique=True)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.wilaya_name
        }