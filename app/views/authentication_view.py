import flask
from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from app import app, db
from app.libs.model_lib import ModelSetRequiredFieldException
from app.libs.user_lib import create_user, get_user_by_email


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return flask.jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return flask.jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return flask.jsonify({"msg": "Missing password parameter"}), 400

    session = db.session
    user = get_user_by_email(session, email)

    if not user:
        return flask.jsonify({"msg": "No user with that email"}), 400
    if not check_password_hash(user.password, password):
        return flask.jsonify({"msg": "Wrong password"}), 400

    # Identity can be any data that is json serializable
    return_dict = user.dict
    return_dict['access_token'] = create_access_token(identity=email)
    return flask.jsonify(return_dict), 200


@app.route('/create_user', methods=['POST'])
def create_user_view():
    session = db.session

    data: dict = request.get_json()

    try:
        user = create_user(data)
        session.add(user)
        session.commit()
    except ModelSetRequiredFieldException as e:
        return str(e), 400
    except IntegrityError as e:
        return e.orig.diag.message_detail, 400

    return_dict = user.dict
    return_dict['access_token'] = create_access_token(identity=user.email)
    return flask.jsonify(return_dict), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    app.logger.info('This message goes to stderr and app.log from the auth view!')
    return flask.jsonify(logged_in_as=current_user)
