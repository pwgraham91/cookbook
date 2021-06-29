from typing import Optional

import flask_jwt_extended
from sqlalchemy import func
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.libs.model_lib import ModelSetRequiredFieldException, set_property_on_model
from app.models import User


def create_user(user_dict) -> User:
    user = User()
    set_property_on_model(user, user_dict, 'name')
    set_property_on_model(user, user_dict, 'username')
    email = user_dict.get('email')
    if not email:
        raise ModelSetRequiredFieldException('"email" is a required field')
    user.email = email.lower()

    password = user_dict.get('password')
    if not password:
        raise ModelSetRequiredFieldException('"password" is a required field')
    user.password = generate_password_hash(password)

    return user


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    return session.query(User).filter(
        func.lower(User.email) == email.lower()
    ).first()


def get_user_by_jwt(session: Session) -> Optional[User]:
    email = flask_jwt_extended.get_jwt_identity()
    if not email:
        return

    return get_user_by_email(session, email)
