from flask import Flask
from infopublic_mail import blueprints
from infopublic_mail.blueprints import auth
from config import config
from infopublic_mail.extensions import bootstrap
from infopublic_mail.extensions import db
from infopublic_mail.extensions import migrate
from infopublic_mail.extensions import email
from infopublic_mail.extensions import login
from infopublic_mail.extensions import moment


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    blueprints.init_app(app)
    auth.init_app(app)
    login.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)
    email.init_app(app)
    moment.init_app(app)
    

    return app

