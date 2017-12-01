# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Length
from app.wilaya.models import Wilaya


class WilayaForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired('Le nom de la wilaya est nécessaire'),
        Length(min=1, max=100, message="La name doit être > 1 et < 100 caractères")
    ])

    code = StringField('code', validators=[
        DataRequired('Le code est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        wilaya = Wilaya.query.filter_by(name=self.name.data).first()
        if wilaya is not None:
            self.name.errors.append(
                "Ce nom exite déja, veuillez choisir une autre!")
            return False
        return True

    def updateValidate(self, wilayaId):
        if not FlaskForm.validate(self):
            return False

        wilaya = Wilaya.query.filter_by(
            name=self.name.data).first()
        if wilaya is not None and wilaya.id != wilayaId:
            self.name.errors.append(
                "Ce nom exite déja, veuillez choisir une autre!")
            return False
        return True
