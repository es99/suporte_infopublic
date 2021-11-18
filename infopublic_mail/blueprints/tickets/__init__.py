from .ticket_views import ticket

def init_app(app):
    app.register_blueprint(ticket)