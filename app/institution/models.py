from app import db

class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(200))
    description = db.Column(db.String(500))
    commune = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(30))
    fax = db.Column(db.String(30))
    longitude=db.Column(db.Float)
    latitude = db.Column(db.Float)
    comments = db.relationship('Comment', backref='institutiton', lazy='dynamic')
    institution_class_id = db.Column(db.Integer, db.ForeignKey('institution_class.id'))
    wilaya_id = db.Column(db.Integer, db.ForeignKey('wilaya.id'))

    def to_json_min(self):
        return{
            'id': self.id,
            'denomination': self.denomination,
            'description': self.description,
            'commune': self.commune,
            'address': self.address,
            'phone': self.phone,
            'fax': self.fax,
            'position':{
                'lat': self.latitude,
                'lng': self.longitude
            },
            'typeId': self.institution_class_id,
            'wilayaId': self.wilaya_id
        }

    def to_json(self):
        return{
            'id': self.id,
            'denomination': self.denomination,
            'description': self.description,
            'commune': self.commune,
            'address': self.address,
            'phone': self.phone,
            'fax': self.fax,
            'position':{
                'lat': self.latitude,
                'lng': self.longitude
            },
            'typeId': self.institution_class_id,
            'wilayaId': self.wilaya_id,
            'comments': [element.to_json() for element in self.comments.all()]
        }