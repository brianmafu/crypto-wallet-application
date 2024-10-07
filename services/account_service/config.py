"""Flask configuration variables."""

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Config:
    """Set Flask configuration from .env file."""

    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://username:password@db/account_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret")
