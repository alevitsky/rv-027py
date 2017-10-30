# Rename this file to config.py and fill db_credentials with your's data.
import os


class Config(object):
    DEBUG = False

    SECRET_KEY = 'SECRET_OR_NOT_KEY'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'SECRET_OR_NOT_KEY'
    # Change database credentials to yours.
    db_credentials = 'postgres://user:password@localhost/db_name'
    if 'DATABASE_URL' in os.environ:
    	db_credentials = os.environ['DATABASE_URL']
    	
    SQLALCHEMY_DATABASE_URI = db_credentials
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True