from app import db, app
from app.comment.models import Comment
from app.institution.models import Institution
from app.user.models import User
from app.comment.forms import CommentForm
import datetime
from werkzeug.datastructures import MultiDict
from flask import abort, request, jsonify

@app.route('/api/comment',methods=["POST"])
def add_comment():
    data = request.get_json(force=True)
    form = CommentForm(MultiDict(mapping=data))
    if form.validate():
        comment_content = data.get('comment_content')
        rating = data.get('rating')
        user = User.query.get(data.get('user_id'))
        intitution = Institution.query.get(data.get('intitution_id'))
        comment=Comment(comment_content=comment_content,rating=rating,\
        timestamp=datetime.datetime.utcnow(),user=user,institution=institution)
        db.session.add(comment)
        db.session.commit() 
        return jsonify({'element':comment.to_json()})
    return jsonify({"form_errors": form.errors}), 400

@app.route('/api/comment/<int:id>',methods=["DELETE","PUT"])
def modify_comment(id):
    comment = comment.query.get(id)
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
            comment.comment_content = data.get('comment_content')
            comment.rating = data.get('rating')
            comment.timestamp=datetime.datetime.utcnow()
            db.session.add(comment)
            db.session.commit() 
            return jsonify({'element':comment.to_json()})
        return jsonify({"form_errors": form.errors}), 400