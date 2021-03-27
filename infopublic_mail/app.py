from flask import Flask, render_template
from infopublic_mail import blueprints
from infopublic_mail.extensions import bootstrap
from infopublic_mail.extensions import config
from infopublic_mail.extensions import db
from infopublic_mail.extensions import migrate


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    blueprints.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)
    

    return app

