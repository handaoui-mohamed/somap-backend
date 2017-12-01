from app import db
from app.user.models import User


def checkUserId(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return user


def createUser(data):
    username = data.get('username').lower()
    password = data.get('password')
    email = data.get('email').lower()
    address = data.get('address')
    phone = data.get('phone')
    wilaya_id = data["wilaya"]["id"]
    user = User(username=username, email=email.lower(), phone=phone,
                address=address, wilaya_id=wilaya_id)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return user


def updateUser(user, data):
    user.username = data.get('username').lower()
    user.email = data.get('email').lower()
    user.address = data.get('address')
    user.phone = data.get('phone')
    user.wilaya_id = data["wilaya"]["id"]
    password = data.get('password')
    if password:
        user.hash_password(password)
        db.session.add(user)
    db.session.commit()
