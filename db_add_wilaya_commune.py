#!flask/bin/python
from app import db
from app.wilaya.models import Wilaya
from app.commune.models import Commune
import json

# creation of all wilayas from wilaya.json
with open("wilaya.json", "r") as wilaya_json:
    wilayas = json.load(wilaya_json)

for wilaya in wilayas:
    db.session.add(Wilaya(wilaya_name=wilaya["wilaya"].lower()))
    db.session.commit()

# creation of all communes from communes.json
with open("communes.json", "r") as communes_json:
    communes = json.load(communes_json)

for commune in communes:
    wilaya=Wilaya.query.get(int(commune["wilaya_id"]))
    db.session.add(Commune(name=commune["name"].lower(),wilaya=wilaya))
    db.session.commit()