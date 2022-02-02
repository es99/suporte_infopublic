from .views import servidor

def init_app(app):
    app.register_blueprint(servidor, url_prefix='/servidores')