from app import db


class Commune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))
    institutions = db.relationship(
        'Institution', backref='commune', lazy='dynamic')

    def to_json_min(self):
        return{
            "id": self.id,
            "name": self.name,
            "zip_code": self.zip_code
        }

    def to_json(self):
        from app.wilaya.models import Wilaya
        return{
            "id": self.id,
            "name": self.name,
            "zip_code": self.zip_code,
            "wilaya": Wilaya.query.get(self.wilaya_id).to_json_min() if self.wilaya_id else {}
        }
