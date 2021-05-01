from flask import Blueprint, request

# from werkzeug.security import check_password_hash, generate_password_hash

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "GET":
        return "Register User"
    else:
        return "User Registered"
