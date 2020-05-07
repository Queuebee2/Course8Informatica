from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://anonymous:@ensembldb.ensembl.org/homo_sapiens_core_91_38'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug
    SQLALCHEMY_ECHO = True

