from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '41806117-7939-4765-aff2-74607a6ba445'

# SQLAlchemy
local_database = 'postgresql://localhost/cookbook'
docker_database = 'postgresql://postgres@cookbook_postgres_1/cookbook'
local_test_database = 'postgresql://localhost/cookbook_test'


SQLALCHEMY_DATABASE_URI = local_database
SQLALCHEMY_TEST_DATABASE_URI = local_test_database
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ENVIRONMENT = 'dev'
FLASK_ENV = 'development'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=90)
