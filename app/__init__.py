from flask import Flask

from config import get_config

from app.database import db
from app.auth import views, admin


def create_app(name, config_name):
    app = Flask(name, template_folder='templates')
    app.config.from_object(get_config())

    db.init_app(app)
    views.configure(app)
    admin.configure(app)

    return app
