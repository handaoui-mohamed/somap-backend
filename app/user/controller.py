from app.user.models import User


def createUser(data):
    username = data.get('username').lower()
    password = data.get('password')
    email = data.get('email').lower()
    address = data.get('address')
    phone = data.get('phone')
    wilaya = data.get('wilaya')
    if wilaya:
        wilaya_id = wilaya.get('id')
    user = User(username=username, email=email.lower(), phone=phone,
                address=address, wilaya_id=wilaya_id)
    user.hash_password(password)
    return user


def updateUser(user, data):
    user.username = data.get('username').lower()
    user.email = data.get('email').lower()
    user.address = data.get('address')
    user.phone = data.get('phone')
    wilaya = data.get('wilaya')
    if wilaya:
        user.wilaya_id = wilaya.get('id')
    password = data.get('password')
    if password:
        user.hash_password(password)
