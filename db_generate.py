#!flask/bin/python
from app import db
from app.institution.models import Institution
from app.institution_class.models import InstitutionClass
from app.wilaya.models import Wilaya
from app.commune.models import Commune
from app.user.models import User
import json
import argparse


parser = argparse.ArgumentParser(description='A script to generate SoMap data')
parser.add_argument('-i', '--institutions',
                    help='Adds institution data', action="store_true")
parser.add_argument('-c', '--classes',
                    help='Adds institution classes data', action="store_true")
parser.add_argument('-w', '--wilayas',
                    help='Adds wilayas and communes data', action="store_true")
parser.add_argument('-u', '--users', help='Adds users data',
                    action="store_true")
parser.add_argument('-a', '--all', help='Adds all data', action="store_true")
parser.add_argument('-d', '--drop', help='Drops all data', action="store_true")
args = parser.parse_args()

if args.drop or args.all:
    print "Droping all data ..."
    db.drop_all()
    print "Data dropped successfully."
    if args.drop:
        exit()

print "\nCreating data tables..."
db.create_all()
print "Data tables created successfully."

if args.wilayas or args.all:
    print "\nCreating Wilayas..."
    # creation of all wilayas from wilaya.json
    with open("data/wilayas.json", "r") as wilaya_json:
        wilayas = json.load(wilaya_json)

    for wilaya in wilayas:
        db.session.add(
            Wilaya(name=wilaya["wilaya"].lower(), code=(wilaya["id"] + 1)))
    db.session.commit()
    print "Wilayas created successfully."
    # creation of all communes from communes.json
    with open("data/communes.json", "r") as communes_json:
        communes = json.load(communes_json)
    print "\nCreating Communes..."
    for commune in communes:
        wilaya = Wilaya.query.filter_by(code=int(commune["wilaya_id"])).first()
        db.session.add(Commune(name=commune["name"].lower(), zip_code=int(
            commune["code_postal"]), wilaya=wilaya))
    db.session.commit()
    print "Communes created successfully."

if args.classes or args.all:
    print "\nCreating institution classes..."
    # creation of insititution classes
    with open("data/institutionclasses.json", "r") as institution_classes_json:
        institution_classes = json.load(institution_classes_json)

    for institution_class in institution_classes:
        db.session.add(InstitutionClass(
            name=institution_class["classeDenomination"].lower()))
    db.session.commit()
    print "Institution classes created successfully."

if args.institutions or args.all:
    print "\nCreating institutions..."
    # creation of existing insitution in institution.json file
    with open("data/institutions.json", "r") as institution_json:
        institutions = json.load(institution_json)

    for institution in institutions:
        commune = Commune.query.filter_by(
            name=institution["commune"].lower(), wilaya_id=institution["wilayaID"]).first()
        db.session.add(Institution(
            name=institution["denomination"].lower(),
            description=institution["description"].lower(),
            commune=commune,
            address=institution["adresse"],
            phone=institution["tel"],
            fax=institution["fax"],
            latitude=institution["position"]["lat"],
            longitude=institution["position"]["lng"],
            institution_class=InstitutionClass.query.get(
                int(institution["typeId"]) + 1),
            wilaya=Wilaya.query.get(int(institution["wilayaID"])),
            validated=True))
    db.session.commit()
    print "Institution created successfully."

if args.users or args.all:
    print "\nCreating users..."
    user = User(username="admin", email="admin@somap.dz", wilaya_id=16)
    user.hash_password("admin")
    db.session.add(user)
    db.session.commit()
    print "Users created successfully."
