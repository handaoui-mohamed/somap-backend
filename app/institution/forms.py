# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
from app.commune.models import Commune

class InstitutionForm(FlaskForm):
    denomination = StringField('denomination',validators=[
        DataRequired('La denomenation de l\'institution est nécessaire'),
        Length(min=1, max=200, message="La denomination doit être < 200 caractères")
    ])
    description = StringField('description',validators=[
        Length(max=500, message="La description doit être < 500 caractères")
    ])
    address = StringField('address',validators=[
        DataRequired('L\'adresse est nécessaire'),
        Length(min=1, max=200, message="L\'adresse doit être < 200 caractères")
    ])
    phone = StringField('phone',validators=[
        Length(max=30, message="La numéro de téléphone doit être < 30 caractères")
    ])
    fax = StringField('fax',validators=[
        Length(max=30, message="La numéro du Fax doit être < 30 caractères")
    ])
    class_id=IntegerField('class_id', validators=[
        DataRequired('Le type d\'institution est nécessaire')
    ])
    wilaya_id=IntegerField('wilaya_id', validators=[
        DataRequired('La wilaya est nécessaire')
    ])
    commune_id=IntegerField('commune_id', validators=[
        DataRequired('La commune est nécessaire')
    ])
    longitude=FloatField('longitude', validators=[
        DataRequired('Longitude est nécessaire')
    ])
    latitude=FloatField('latitude', validators=[
        DataRequired('Latitude est nécessaire')
    ])


    def validate(self):
        if not FlaskForm.validate(self):
            return False

        institution_class = InstitutionClass.query.get(self.class_id.data)
        if institution_class is None:
            self.class_id.errors.append('Le type d\'institution n\'existe pas!')
            return False
        wilaya = Wilaya.query.get(self.wilaya_id.data)
        if wilaya is None:
            self.wilaya_id.errors.append('La wilaya n\'existe pas!')
            return False

        commune = Commune.query.get(self.commune_id.data)
        if commune is None or commune.wilaya_id is not wilaya.id:
            self.commune_id.errors.append('La commune n\'existe pas!')
            return False
        return True
