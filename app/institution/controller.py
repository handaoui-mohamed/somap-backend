def createInstitution(data):
    name = data.get('name').lower()
    description = data.get('description').lower()
    address = data.get('address').lower()
    phone = data.get('phone')
    fax = data.get('fax')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    wilaya = Wilaya.query.get(data.get('wilaya_id'))
    commune = Commune.query.get(data.get('commune_id'))
    institution_class = InstitutionClass.query.get(data.get('class_id'))
    institution = Institution(name=name, description=description, commune=commune, address=address, phone=phone,
                              fax=fax, latitude=latitude, longitude=longitude, wilaya=wilaya, institution_class=institution_class)
    return institution


def updateInstitution(institution, data):
    institution.name = data.get('name').lower()
    institution.description = data.get('description').lower()
    institution.address = data.get('address').lower()
    institution.phone = data.get('phone')
    institution.fax = data.get('fax')
    institution.latitude = data.get('latitude')
    institution.longitude = data.get('longitude')
    institution.wilaya = Wilaya.query.get(data.get('wilaya_id'))
    institution.commune = Commune.query.get(data.get('commune_id'))
    institution.institution_class = InstitutionClass.query.get(
        data.get('class_id'))
    institution.validated = data.get('validated', False)
    return institution
