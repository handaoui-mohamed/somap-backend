# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.commune.models import Commune
from app.wilaya.models import Wilaya


class CommuneForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired('Le nom de la commune est nécessaire'),
        Length(max=100, message="Le nom de la commune doit être < 100 caractères")
    ])
    
    def validate(self, data):
        if not FlaskForm.validate(self):
            return False

        wilaya = data.get("wilaya")
        if wilaya:
            wilaya_id = wilaya.get("id")
            wilaya = Wilaya.query.get(wilaya_id)
            if wilaya is None:
                self.wilaya_id.errors.append("La wilaya n\'éxiste pas")
                return False
            return True
        else:
            self.wilaya_id.errors.append("La wilaya n\'éxiste pas")
            return False
