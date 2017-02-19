# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.comment.models import Comment
from app.institution.models import Intitution
from app.user.models import User

class CommentForm(FlaskForm):
    comment_content=StringField('comment_content', validators=[
        Length(max=500, message="La denomination doit être < 500 caractères")
    ])
    rating=FloatField('rating', validators=[
        DataRequired('La note d\'évaluation est nécessaire'),
        NumberRange(min=0, max=5)
    ])
    user_id=IntegerField('rating', validators=[
        DataRequired('L\'identifiant de l\'utilisateur est nécessaire')
    ])
    institution_id=IntegerField('rating', validators=[
        DataRequired('L\'identifiant de l\'instiution est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = User.query.get(self.user_id.data)
        institution = institution.query.get(self.institution_id.data)
        if user is None:
            self.user_id.errors.append("L\'identifiant de l\'utilisateur n\'éxiste pas")
            return False
        if institution is None:
            self.institution_id.errors.append("L\'identifiant de l\'instiution n\'éxiste pas")
            return False
        return True
