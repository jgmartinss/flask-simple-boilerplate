from flask import Flask

from config import app_config
from app.database import db
from app.auth import views, admin


def create_app(name, config_name):
    app = Flask(name, template_folder="templates")
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    views.configure(app)
    admin.configure(app)

    return app
