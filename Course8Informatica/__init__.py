from flask import Flask
from .database_clasess import  EnsembleDbHandler

ensemble_db = EnsembleDbHandler()

def create_app():
    """Construct the core Course8Informatica."""

def app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    ensemble_db.init_app(app)


    with app.app_context():
        from . import routes, errorhandlers


        return app