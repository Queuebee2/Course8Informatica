from flask import Flask
from mysql import connector


def app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')


    with app.app_context():
        from . import routes, errorhandlers


        return app