from app import db, app
from app.user.models import User
from app.user.forms import RegistrationForm, LoginForm
from app.user.controller import createUser, updateUser
from flask import abort, request, jsonify
from werkzeug.datastructures import MultiDict


@app.route('/api/users')
def get_users():
    users = User.query.all()
    return jsonify({'elements': [element.to_json() for element in users]})


@app.route('/api/users', methods=['POST'])
def new_user():
    data = request.get_json(force=True)
    form = RegistrationForm(MultiDict(mapping=data))
    if form.validate():
        user = createUser(data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'element': user.to_json()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/users/<int:id>')
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return jsonify({'element': user.to_json()})


@app.route('/api/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': 'true'}), 200


@app.route('/api/users/<int:id>', methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    data = request.get_json(force=True)
    form = RegistrationForm(MultiDict(mapping=data))
    if form.validate():
        user = updateUser(user, data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'element': user.to_json()})
    return jsonify({'element': user.to_json()})


@app.route('/api/login', methods=["POST"])
def login():
    data = request.get_json(force=True)
    form = LoginForm(MultiDict(mapping=data))
    if form.validate():
        username = data.get('username').lower()
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            abort(404)
        token = user.generate_auth_token()
        return jsonify({'token': token.decode('ascii'), 'user': user.to_json()})
    return jsonify({"form_errors": form.errors}), 400
