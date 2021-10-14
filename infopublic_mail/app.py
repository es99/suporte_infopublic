from flask import Flask
from infopublic_mail import blueprints
from config import config
from infopublic_mail.extensions import bootstrap
from infopublic_mail.extensions import db
from infopublic_mail.extensions import migrate
from infopublic_mail.extensions import email


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    blueprints.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)
    email.init_app(app)
    

    return app

