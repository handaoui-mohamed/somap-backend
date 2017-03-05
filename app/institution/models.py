from app import db
from app.commune.models import Commune
from app.wilaya.models import Wilaya

class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(200))
    description = db.Column(db.String(500))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(30))
    fax = db.Column(db.String(30))
    longitude=db.Column(db.Float)
    latitude = db.Column(db.Float)
    comments = db.relationship('Comment', backref='institution', lazy='dynamic')
    class_id = db.Column(db.Integer, db.ForeignKey('institution_class.id'))
    wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))
    commune_id = db.Column(db.Integer, db.ForeignKey('commune.id'))
    validated = db.Column(db.Boolean, default=False)
    # add user_id for the one who added this

    def to_json_min(self):
        return{
            'id': self.id,
            'denomination': self.denomination,
            'description': self.description,
            'commune': Commune.query.get(self.commune_id).to_json_min(),
            'address': self.address,
            'phone': self.phone,
            'fax': self.fax,
            'position':{
                'lat': self.latitude,
                'lng': self.longitude
            },
            'class_id': self.class_id,
            'wilaya_id': self.wilaya_id,
            'wilaya': Wilaya.query.get(self.wilaya_id).wilaya_name,
        }

    def to_json(self):
        return{
            'id': self.id,
            'denomination': self.denomination,
            'description': self.description,
            'commune': Commune.query.get(self.commune_id).to_json_min(),
            'address': self.address,
            'phone': self.phone,
            'fax': self.fax,
            'position':{
                'lat': self.latitude,
                'lng': self.longitude
            },
            'class_id': self.class_id,
            'wilaya_id': self.wilaya_id,
            'wilaya': Wilaya.query.get(self.wilaya_id).wilaya_name,
            'comments': [element.to_json() for element in self.comments.all()]
        }

    
    def getWilaya(self):
        return Wilaya.query.get(self.wilaya_id).wilaya_name
    
    def getCommune(self):
        return Commune.query.get(self.commune_id).name

    def getClass(self):
        from app.institution_class.models import InstitutionClass
        return InstitutionClass.query.get(self.class_id).denomination