from flask import Flask
from flask.ext.stormpath import StormpathManager
from config import config

stormpath_manager = StormpathManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    stormpath_manager.init_app(app)

    # register blueprint
    from .accounts import accounts as accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    return app