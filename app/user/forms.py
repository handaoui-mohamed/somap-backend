# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length
from app.user.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired('Le nom d\'utilisateur est nécessaire'),
        Length(min=1, max=32,
               message="Le nom d\'utilisateur doit être > 1 et < 32 caractères")
    ])
    email = EmailField('email', [
        validators.DataRequired('L\'addresse Email est nécessaire'),
        validators.Email('L\'addresse Email doit être valide')
    ])

    password = PasswordField('password', validators=[
        Length(min=4, message="Le mot de passe doit être >= 4 caractères"),
        DataRequired('Le mot de passe est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            self.username.errors.append(
                "Ce nom d'utilisteur existe déja, veuillez choisir un autre!")
            return False
        return True


class UpdateForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired('Le nom d\'utilisateur est nécessaire'),
        Length(min=1, max=32,
               message="Le nom d\'utilisateur doit être > 1 et < 32 caractères")
    ])
    email = EmailField('email', [
        validators.DataRequired('L\'addresse Email est nécessaire'),
        validators.Email('L\'addresse Email doit être valide')
    ])

    def validate(self, userId):
        if not FlaskForm.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is not None and user.id != userId:
            self.username.errors.append(
                "Ce nom d'utilisteur existe déja, veuillez choisir un autre!")
            return False
        return True


class LoginForm(FlaskForm):
    username=StringField('username', validators=[
        DataRequired('Le nom d\'utilisateur est nécessaire'),
        Length(min=1, max=32,
               message="Le nom d\'utilisateur doit être > 1 et < 32 caractères")
    ])
    password=PasswordField('password', validators=[
        Length(min=4, message="Le nom mot de passe doit être >= 4 caractères"),
        DataRequired('Le mot de passe est nécessaire')
    ])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user=User.query.filter_by(username=self.username.data).first()
        if not user or not user.verify_password(self.password.data):
            return False
        return True
