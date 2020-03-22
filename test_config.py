from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'aebf703f-9d98-44f4-abe6-4ac5d8fa070b'

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/cookbook'
SQLALCHEMY_TEST_DATABASE_URI = 'postgresql://localhost/cookbook_test'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ENVIRONMENT = 'dev'
FLASK_ENV = 'test'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=90)
TESTING = True
