# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length
from app.user.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[
        DataRequired('Le nom d\'utilisateur est nécessaire'),
        Length(min=1, max=32, message="Le nom d\'utilisateur doit être > 1 et < 32 caractères")
    ])
    email = EmailField('email', [
        validators.DataRequired('L\'addresse Email est nécessaire'),
        validators.Email('L\'addresse Email doit être valide')
    ])
    
    full_name = StringField('full_name', validators=[
        Length(max=100, message="Le nom et prénom doivent être < 100 caractères")
    ])
    
    password = PasswordField('password', validators=[
        Length(min=8, message="Le nom mot de passe doit être > 8 caractères"),
        DataRequired('Le mot de passe est nécessaire')
    ])


    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            self.username.errors.append("Ce nom d'utilisteur existe déja, veuillez choisir un autre!")
            return False
        return True


class UpdateForm(FlaskForm):
    full_name = StringField('full_name', validators=[
        Length(max=100, message="Le nom et prénom doivent être < 100 caractères")
    ])
    
    email = EmailField('email', [
        validators.DataRequired('L\'addresse Email est nécessaire'),
        validators.Email('L\'addresse Email doit être valide')
    ])
