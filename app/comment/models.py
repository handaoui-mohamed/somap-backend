from app import db

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    comment_content=db.Column(db.String(500))
    rating=db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    intitution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    #TODO: see ho to prevent the many version allow one comment

    def to_json(self):
        from app.user.models import User
        return{
            'id': self.id,
            'content': self.comment_content,
            'rating': self.rating,
            'date': self.timestamp,
            'user': User.query.get(user_id).to_json()
        }