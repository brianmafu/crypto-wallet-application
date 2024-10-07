"""Flask Routes."""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Account, Transaction, db

account_bp = Blueprint("account", __name__)


@account_bp.route("/balance", methods=["GET"])
@jwt_required()
def get_balance():
    """Get account balance."""
    user_id = get_jwt_identity()
    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({"error": "Account not found!"}), 404

    return jsonify({"balance": account.balance})


@account_bp.route("/credit", methods=["POST"])
@jwt_required()
def credit_account():
    """Credit account."""
    user_id = get_jwt_identity()
    data = request.get_json()
    amount = data["amount"]

    account = Account.query.filter_by(user_id=user_id).first()
    if not account:
        return jsonify({"error": "Account not found!"}), 404

    account.balance += amount
    transaction = Transaction(account_id=account.id, amount=amount, type="credit")
    db.session.add(transaction)
    db.session.commit()

    return jsonify(
        {"message": "Account credited successfully!", "balance": account.balance}
    )


@account_bp.route("/debit", methods=["POST"])
@jwt_required()
def debit_account():
    """Debit account."""
    user_id = get_jwt_identity()
    data = request.get_json()
    amount = data["amount"]

    account = Account.query.filter_by(user_id=user_id).first()
    if not account:
        return jsonify({"error": "Account not found!"}), 404

    if account.balance < amount:
        return jsonify({"error": "Insufficient balance!"}), 400

    account.balance -= amount
    transaction = Transaction(account_id=account.id, amount=amount, type="debit")
    db.session.add(transaction)
    db.session.commit()

    return jsonify(
        {"message": "Account debited successfully!", "balance": account.balance}
    )


@account_bp.route("/create", methods=["POST"])
@jwt_required()
def create_account():
    """Create Account."""
    user_id = get_jwt_identity()
    account = Account.query.filter_by(user_id=user_id).first()

    if account:
        return jsonify({"error": "Account already exists!"}), 400
    account = Account(user_id=user_id, balance=0)
    db.session.add(account)
    db.session.commit()

    return jsonify({"message": "Account created successfully!"})


@account_bp.route("/transactions", methods=["GET"])
@jwt_required()
def get_transaction_history():
    """Get transaction history."""
    user_id = get_jwt_identity()
    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({"error": "Account not found!"}), 404

    transactions = Transaction.query.filter_by(account_id=account.id).all()
    history = [
        {"amount": t.amount, "type": t.type, "date": t.created_at} for t in transactions
    ]

    return jsonify({"transactions": history})
