# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.commune.models import Commune
from app.wilaya.models import Wilaya

class CommentForm(FlaskForm):
    name=StringField('name', validators=[
        DataRequired('Le nom de la commune est nécessaire'),
        Length(max=100, message="Le nom de la commune doit être < 100 caractères")
    ])
    wilaya_id=IntegerField('wilaya_id', validators=[
        DataRequired('L\'identifiant de la wilaya est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        wilaya = Wilaya.query.get(self.wilaya_id.data)
        if wilaya is None:
            self.wilaya_id.errors.append("La wilaya n\'éxiste pas")
            return False
        return True
