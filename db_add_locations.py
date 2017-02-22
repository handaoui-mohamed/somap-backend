#!flask/bin/python
from app import db
from app.institution.models import Institution
from app.wilaya.models import Wilaya
from app.institution_class.models import InstitutionClass
import json

# creation of all wilayas from wilaya.json
with open("wilaya.json", "r") as wilaya_json:
    wilayas = json.load(wilaya_json)

for wilaya in wilayas:
    db.session.add(Wilaya(wilaya_name=wilaya["wilaya"]))
    db.session.commit()

# creation of insititution classes
with open("institutionsClasses.json", "r") as institution_classes_json:
    institution_classes = json.load(institution_classes_json)

for institution_class in institution_classes:
    db.session.add(InstitutionClass(class_denomination=institution_class["classeDenomination"],icon_url=institution_class["iconUrl"]))
    db.session.commit()


# creation of existing insitution in institution.json file
with open("institutions.json", "r") as institution_json:
    institutions = json.load(institution_json)

for institution in institutions:

    db.session.add(Institution(\
        denomination=institution["denomination"],description=institution["description"],\
        commune=institution["commune"],address=institution["adresse"],phone=institution["tel"],\
        fax=institution["fax"],latitude=institution["position"]["lat"],longitude=institution["position"]["lng"],\
        institution_class=InstitutionClass.query.get(int(institution["typeId"])+1),\
        wilaya=Wilaya.query.get(int(institution["wilayaID"]))))
    db.session.commit()
