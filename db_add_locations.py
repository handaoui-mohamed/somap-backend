#!flask/bin/python
from app import db
from app.institution.models import Institution
import json

# creation of all wilayas from wilaya.json
with open("wilaya.json", "r") as wilaya_json:
    wilayas = json.load(wilaya_json)

or wilaya in wilayas:
    db.session.add(Wilaya(wilaya_name=wilaya["wilaya"])))
    db.session.commit()

# creation of insititution classes
with open("institutionClasses.json", "r") as instritution_classe_json:
    institution_classes = json.load(institution_classe_json)

or institution_classe in institution_classes:
    db.session.add(InstitutionClasse(class_denomination=institution_classe["classe_denomination"],icon_url=institution["iconUrl"]))
    db.session.commit()


# creation of existing insitution in institution.json file
with open("institution.json", "r") as instritution_json:
    institutions = json.load(institution_json)

for institution in institutions:

    new_institution=Institution(\
        denomination=institution["denomination"],description=institution["description"],\
        commune=institution["commune"],address=institution["adresse"],phone=institution["tel"],\
        fax=institution["fax"],latitude=institution["position"]["lat"],longitude=institution["position"]["lng"])
    new_institution.add_position(position.id)
    new_insitution.add_wilaya(Number(institution["wilayaId"])+1)
    new_insitution.add_classe(Number(Institution["typeId"])+1)
    db.session.add(new_institution)
    db.session.commit()
