import os
from flask import Flask, Blueprint
from .extensions import db
from flask_cors import CORS
from .routes.url_shortener import url_shortener_blueprint



def create_app(config_file='settings.py'):
    """Initialize Flask app with the DB config and blueprints

    Returns:
        app : Initalized Flask app 
    """
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(url_shortener_blueprint)

    CORS(app)

    return app
