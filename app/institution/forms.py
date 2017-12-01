# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField,validators
from wtforms.validators import DataRequired, Length, NumberRange
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
from app.commune.models import Commune

class InstitutionForm(FlaskForm):
	name = StringField('name',validators=[
		DataRequired('La denomenation de l\'institution est nécessaire'),
		Length(min=1, max=200, message="La name doit être < 200 caractères")
	])
	description = StringField('description',validators=[
		Length(max=500, message="La description doit être < 500 caractères")
	])
	address = StringField('address',validators=[
		DataRequired('L\'adresse est nécessaire'),
		Length(min=1, max=200, message="L\'adresse doit être < 200 caractères")
	])
	phone = StringField('phone')
	fax = StringField('fax')
	longitude=FloatField('longitude', validators=[
		DataRequired('Longitude est nécessaire')
	])
	latitude=FloatField('latitude', validators=[
		DataRequired('Latitude est nécessaire')
	])
	validated=BooleanField('validated', default=False)


	def validate(self):
		if not FlaskForm.validate(self):
			return False

		# institution_class = InstitutionClass.query.get(self.class_id.data)
		# if institution_class is None:
		# 	self.class_id.errors.append('Le type d\'institution n\'existe pas!')
		# 	return False
		# wilaya = Wilaya.query.get(self.wilaya_id.data)
		# if wilaya is None:
		# 	self.wilaya_id.errors.append('La wilaya n\'existe pas!')
		# 	return False

		# commune = Commune.query.get(self.commune_id.data)
		# if commune is None or commune.wilaya_id is not wilaya.id:
		# 	self.commune_id.errors.append('La commune n\'existe pas!')
		# 	return False
		return True
