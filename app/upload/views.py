from app import app, db
import os
from flask import abort, request, jsonify, g, send_from_directory
from werkzeug import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, basedir
from app.upload.models import InstitutionPicture
from app.institution.models import Institution


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/api/uploads/<int:institution_id>',methods=['POST'])
def uploadPicture(institution_id):
    institution = Institution.query.get(institution_id)
    if not institution_id or not institution:
        abort(400)
    file = request.files.get("file")
    if not file:
        abort(400)
    filename = uploadFile(file, os.path.join(basedir, UPLOAD_FOLDER, str(institution.id)), institution)
    uploaded_picture = InstitutionPicture(name=filename,institution=institution)
    db.session.add(uploaded_picture)
    db.session.commit()
    return jsonify({'element':institution.to_json()}),201

@app.route('/api/uploads/<int:institution_id>',methods=['GET'])
def getPicture(institution_id):
	institution = Institution.query.get(institution_id)
	if not institution_id or not institution or not institution.picture:
		abort(400)
	directory = os.path.join(basedir, UPLOAD_FOLDER, str(institution.id))
	return send_from_directory(directory, institution.picture.name)

# upload files function
def uploadFile(file, path, owner):
    if not file or not allowed_file(file.filename):
        abort(400)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        directory = path
        if os.path.exists(directory):
            old_picture = owner.picture
            if old_picture:
                file_path = os.path.join(directory, old_picture.name)
                db.session.delete(old_picture)
                db.session.commit()
                if os.path.exists(file_path):
                    os.remove(file_path)
        else:
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)
        file.save(file_path)
    return filename