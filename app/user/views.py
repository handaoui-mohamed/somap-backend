from app import db, app
from app.user.models import User
from app.user.forms import RegistrationForm, UpdateForm, LoginForm
from app.user.controller import createUser, updateUser, checkUserId, admin_required, login_required
from flask import abort, request, jsonify
from werkzeug.datastructures import MultiDict


@app.route('/api/users')
@admin_required
def get_users(currentUser):
    users = User.query.all()
    return jsonify({'elements': [element.to_json() for element in users]})


@app.route('/api/users', methods=['POST'])
@admin_required
def new_user(currentUser):
    data = request.get_json(force=True)
    form = RegistrationForm(MultiDict(mapping=data))
    if form.validate():
        user = createUser(data)
        return jsonify({'element': user.to_json()}), 201
    return jsonify({"form_errors": form.errors}), 400


@app.route('/api/users/<int:id>')
@login_required
def get_user_by_id(currentUser, id):
    user = checkUserId(id)
    return jsonify({'element': user.to_json()})


@app.route('/api/users/<int:id>', methods=["DELETE"])
@admin_required
def delete_user(currentUser, id):
    user = checkUserId(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': 'true'}), 200


@app.route('/api/users/<int:id>', methods=["PUT"])
@admin_required
def update_user(currentUser, id):
    user = checkUserId(id)
    data = request.get_json(force=True)
    form = UpdateForm(MultiDict(mapping=data))
    if form.validate(user.id):
        updateUser(user, data)
        return jsonify({'element': user.to_json()})
    return jsonify({"form_errors": form.errors}), 400


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
        token = user.create_token()
        return jsonify({'token': token, 'user': user.to_json()})
    return jsonify({"form_errors": form.errors}), 400
