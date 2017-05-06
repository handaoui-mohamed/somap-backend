# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.comment.models import Comment
from app.institution.models import Institution
from app.user.models import User

class CommentForm(FlaskForm):
    comment_content=StringField('comment_content', validators=[
        Length(max=500, message="La denomination doit être < 500 caractères")
    ])
    institution_id=IntegerField('institution_id', validators=[
        DataRequired('L\'identifiant de l\'instiution est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        institution = Institution.query.get(self.institution_id.data)
        if institution is None:
            self.institution_id.errors.append("L\'identifiant de l\'instiution n\'éxiste pas")
            return False
        return True
