# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from flask_cors import CORS
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

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
from app.comment import views
from app.commune import views
from app.moderator import views

# import models
from app.user.models import User
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
from app.comment.models import Comment
from app.commune.models import Commune
