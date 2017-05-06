from app import db

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))

    def to_json(self):
        return{
            'id': self.id,
            'content': self.content,
            'date': str(self.timestamp),
        }