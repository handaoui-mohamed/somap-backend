# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Length
from app.institution_class.models import InstitutionClass


class InstitutionClassForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired('La denomenation est nécessaire'),
        Length(min=1, max=200, message="La name doit être > 1 et < 100 caractères")
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        name = InstitutionClass.query.filter_by(name=self.name.data).first()
        if name is not None:
            self.name.errors.append(
                "Ce type exite déja, veuillez choisir une autre!")
            return False
        return True

    def updateValidate(self, institutionClassId):
        if not FlaskForm.validate(self):
            return False

        institutionClass = InstitutionClass.query.filter_by(
            name=self.name.data).first()
        if institutionClass is not None and institutionClass.id != institutionClassId:
            self.name.errors.append(
                "Ce type exite déja, veuillez choisir une autre!")
            return False
        return True
