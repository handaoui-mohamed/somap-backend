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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message='Missing authorization header')
            response.status_code = 401
            return response

        try:
            payload = parse_token(request)
        except DecodeError:
            response = jsonify(message='Token is invalid')
            response.status_code = 401
            return response
        except ExpiredSignature:
            response = jsonify(message='Token has expired')
            response.status_code = 401
            return response

        g.user_id = payload['sub']
        g.user = User.query.get(g.user_id)
        return f(user, *args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(user, *args, **kwargs):
        if not user.is_admin:
            response = jsonify(message='User do not have the right permission')
            response.status_code = 403
            return response
        return f(user, *args, **kwargs)
    return decorated_function
