from flask import Blueprint, jsonify, make_response

from app.auth import models


user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1/')


@user_bp.route("/users", methods=['GET'])
def get_users():
    users = [u.as_dict() for u in models.User.query.all()]
    resp = make_response(jsonify(users))

    return resp


def configure(app):
    app.register_blueprint(user_bp)
