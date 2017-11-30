from app import db
from app.wilaya.models import Wilaya
from app.commune.models import Commune
from app.institution_class.models import InstitutionClass


class Institution(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	address = db.Column(db.String)
	phone = db.Column(db.String)
	fax = db.Column(db.String)
	longitude = db.Column(db.Float)
	latitude = db.Column(db.Float)
	class_id = db.Column(db.Integer, db.ForeignKey('institution_class.id'))
	wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))
	commune_id = db.Column(db.Integer, db.ForeignKey('commune.id'))
	picture = db.relationship('InstitutionPicture', backref='institution', uselist=False)
	validated = db.Column(db.Boolean, default=False)

	def to_json_min(self):
		return{
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'commune': Commune.query.get(self.commune_id).name,
			'commune_id': self.commune_id,
			'address': self.address,
			'phone': self.phone,
			'fax': self.fax,
			'position': {
				'lat': self.latitude,
				'lng': self.longitude
			},
			'class_id': self.class_id,
			'wilaya_id': self.wilaya_id,
			'class': InstitutionClass.query.get(self.class_id).name,
			'wilaya': Wilaya.query.get(self.wilaya_id).name,
			'validated': self.validated
		}

	def to_json(self):
		return{
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'commune': Commune.query.get(self.commune_id).name,
			'commune_id': self.commune_id,
			'address': self.address,
			'phone': self.phone,
			'fax': self.fax,
			'position': {
				'lat': self.latitude,
				'lng': self.longitude
			},
			'class_id': self.class_id,
			'wilaya_id': self.wilaya_id,
			'class': InstitutionClass.query.get(self.class_id).name,
			'wilaya': Wilaya.query.get(self.wilaya_id).name,
			'picture': self.picture.to_json() if self.picture else None,
			'validated': self.validated
		}


	def getWilaya(self):
		return Wilaya.query.get(self.wilaya_id).name

	def getCommune(self):
		return Commune.query.get(self.commune_id).name

	def getClass(self):
		from app.institution_class.models import InstitutionClass
		return InstitutionClass.query.get(self.class_id).name
