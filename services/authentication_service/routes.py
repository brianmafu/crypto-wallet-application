"""Routes for authentication service."""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from .models import User, db


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    """User signup."""
    data = request.get_json()
    username = data["username"]
    password = generate_password_hash(data["password"])
    try:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return jsonify({"message": "User already exists!"})
    return jsonify({"message": "User Signed Up successfully!"})


@auth_bp.route("/signin", methods=["POST"])
def login():
    """User login."""
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"error": "Invalid Username or Password!"}), 401


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """User logout."""

    return jsonify({"message": "User logged out successfully!"})
