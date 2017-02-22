from app import db

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    comment_content=db.Column(db.String(500))
    rating=db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_min(self):
        from app.user.models import User
        return{
            'id': self.id,
            'content': self.comment_content,
            'rating': self.rating,
            'date': self.timestamp
        }

    def to_json(self):
        from app.user.models import User
        return{
            'id': self.id,
            'content': self.comment_content,
            'rating': self.rating,
            'date': self.timestamp,
            'user': User.query.get(self.user_id).to_json_min()
        }