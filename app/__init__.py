#!/usr/bin/env python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from flask_cors import CORS

# initialization
app = Flask(__name__)
app.config.from_object('config')
# extensions
db = SQLAlchemy(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# import APIs
from app.user import views
from app.institution import views
from app.institution_class import views
from app.wilaya import views
from app.contact import views

# import models
from app.user.models import User
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
