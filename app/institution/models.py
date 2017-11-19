from app import db
from app.wilaya.models import Wilaya
from app.commune.models import Commune
from app.institution_class.models import InstitutionClass


class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String)
    description = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    fax = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    class_id = db.Column(db.Integer, db.ForeignKey('institution_class.id'))
    wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))
    commune_id = db.Column(db.Integer, db.ForeignKey('commune.id'))
    picture = db.relationship('InstitutionPicture',
                              backref='institution', uselist=False)
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
            'position': {
                'lat': self.latitude,
                'lng': self.longitude
            },
            'class_id': self.class_id,
            'wilaya_id': self.wilaya_id,
            'wilaya': Wilaya.query.get(self.wilaya_id).wilaya_name
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
            'position': {
                'lat': self.latitude,
                'lng': self.longitude
            },
            'class_id': self.class_id,
            'wilaya_id': self.wilaya_id,
            'wilaya': Wilaya.query.get(self.wilaya_id).wilaya_name,
            'picture': self.picture.to_json() if self.picture else None
        }

    def getWilaya(self):
        return Wilaya.query.get(self.wilaya_id).wilaya_name

    def getCommune(self):
        return Commune.query.get(self.commune_id).name

    def getClass(self):
        from app.institution_class.models import InstitutionClass
        return InstitutionClass.query.get(self.class_id).denomination

        @staticmethod
        def new(data):
			denomination = data.get('denomination').lower()
			description = data.get('description').lower()
			address = data.get('address').lower()
			phone = data.get('phone')
			fax = data.get('fax')
			latitude = data.get('latitude')
			longitude = data.get('longitude')
			wilaya = Wilaya.query.get(data.get('wilaya_id'))
			commune = Commune.query.get(data.get('commune_id'))
			institution_class = InstitutionClass.query.get(data.get('class_id'))
			institution = Institution(denomination=denomination, description=description, commune=commune, address=address, phone=phone, fax=fax, latitude=latitude, longitude=longitude, wilaya=wilaya, institution_class=institution_class)
			return institution
