from app import db, app
from app.comment.models import Comment
from app.institution.models import Institution
from app.user.models import User
from app.comment.forms import CommentForm
import datetime
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify

@app.route('/api/comments',methods=["POST"])
def add_comment():
    data = request.get_json(force=True)
    form = CommentForm(MultiDict(mapping=data))
    if form.validate():
        content = data.get('content')
        institution = Institution.query.get(data.get('institution_id'))
        comment=Comment(content=content,timestamp=datetime.datetime.utcnow(),institution=institution)
        db.session.add(comment)
        db.session.commit() 
        return jsonify({'element':comment.to_json()}),201
    return jsonify({"form_errors": form.errors}), 400

@app.route('/api/comments/<int:id>',methods=["DELETE","PUT"])
def modify_comment(id):
    comment = Comment.query.get(id)
    if not comment:
            abort(404)
    if request.method == 'DELETE':
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'success': 'true'}), 200
    else: #PUT method
        data = request.get_json(force=True)
        form = CommentForm(MultiDict(mapping=data))
        if form.validate():
            comment.comment_content = data.get('content')
            comment.timestamp=datetime.datetime.utcnow()
            db.session.add(comment)
            db.session.commit() 
            return jsonify({'element':comment.to_json()})
        return jsonify({"form_errors": form.errors}), 400