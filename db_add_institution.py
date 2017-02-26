#!flask/bin/python
from app import db
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
from app.commune.models import Commune
import json

# creation of insititution classes
with open("institutionsClasses.json", "r") as institution_classes_json:
    institution_classes = json.load(institution_classes_json)

for institution_class in institution_classes:
    db.session.add(InstitutionClass(class_denomination=institution_class["classeDenomination"].lower(),icon_url=institution_class["iconUrl"].lower()))
    db.session.commit()


# creation of existing insitution in institution.json file
with open("institutions.json", "r") as institution_json:
    institutions = json.load(institution_json)

for institution in institutions:
    commune = Commune.query.filter_by(name=institution["commune"].lower(),wilaya_id=institution["wilayaID"]).first()
    db.session.add(Institution(\
        denomination=institution["denomination"].lower(),description=institution["description"].lower(),\
        commune=commune,address=institution["adresse"],phone=institution["tel"],\
        fax=institution["fax"],latitude=institution["position"]["lat"],longitude=institution["position"]["lng"],\
        institution_class=InstitutionClass.query.get(int(institution["typeId"])+1),\
        wilaya=Wilaya.query.get(int(institution["wilayaID"]))))
    db.session.commit()
