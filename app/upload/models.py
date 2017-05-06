from app import db
from config import HOST_URL, UPLOAD_FOLDER


# file upload
class InstitutionPicture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    institution_id = db.Column(db.String, db.ForeignKey('institution.id'))

    def to_json(self):
        return {
            'id': self.id,
            'path': HOST_URL+'/'+UPLOAD_FOLDER+'/'+self.institution_id,
            'name': self.name,
            'institution_id': self.institution_id
        }