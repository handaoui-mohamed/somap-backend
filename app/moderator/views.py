# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from flask_login import LoginManager
from app.user.forms import LoginForm
from app.user.models import User
from app.institution.models import Institution


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'index'
lm.login_message = 'Veuillez vous connecter pour acceder a cette page.'


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/admin/', methods=['GET', 'POST'])
@app.route('/admin/index', methods=['GET', 'POST'])
@app.route('/admin/login', methods=['GET', 'POST'])
def index():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('institution'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data)
        return redirect(request.args.get('next') or url_for('institution'))
    flash("Nom d\'utilisateur ou mot de passe érroné")
    return render_template('index.html', title='Connexion', form=form)


@app.route('/admin/institution')
@login_required
def institution():
    institutions = Institution.query.filter_by(validated=False).all()
    return render_template('institution.html', title='Validation des Institutions', institutions=institutions)


@app.route('/admin/institution/<int:id>/validate')
@login_required
def validate_institution(id):
    institution = Institution.query.get(id)
    institution.validated = True
    db.session.add(institution)
    db.session.commit()
    flash("L\'institution a été valider avec succée")
    return redirect(url_for('institution'))


@app.route('/admin/institution/<int:id>/delete')
@login_required
def delete_institution(id):
    institution = Institution.query.get(id)
    db.session.delete(institution)
    db.session.commit()
    flash("L\'institution a été supprimer avec succée")
    return redirect(url_for('institution'))


@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.errorhandler(404)
def client(e):
    return app.send_static_file("index.html")
