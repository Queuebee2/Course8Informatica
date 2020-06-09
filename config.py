from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('mysql://anonymous:@ensembldb.ensembl.org/homo_sapiens_core_91_38')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug
    SQLALCHEMY_ECHO = True