import os
from infopublic_mail.app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')