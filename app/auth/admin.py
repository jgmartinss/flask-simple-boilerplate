from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.database import db
from app.auth.models import User


def configure(app):
    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
