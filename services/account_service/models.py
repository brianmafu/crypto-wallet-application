"""Account and Transaction models."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    """Define the account table"""

    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, default=0.0)


class Transaction(db.Model):
    """ "Define the transaction table"""

    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # credit or debit
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
