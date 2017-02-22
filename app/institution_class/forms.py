# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Length
from app.institution_class.models import InstitutionClass


class InstitutionClassForm(FlaskForm):
    class_denomination = StringField('class_denomination',validators=[
        DataRequired('La denomenation de la classe est nécessaire'),
        Length(min=1, max=32, message="La denomination doit être > 1 et < 100 caractères")
    ])
    icon_url = StringField('icon_url',validators=[
        DataRequired('L\'url de l\'icon est nécessaire'),
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        institution_class = InstitutionClass.query.filter_by(class_denomination=self.class_denomination.data).first()
        if institution_class is not None:
            self.class_denomination.errors.append("Cette classe exite déja, veuillez choisir une autre!")
            return False
        return True
    
    def updateValidate(self):
        if FlaskForm.validate(self):
            return True
