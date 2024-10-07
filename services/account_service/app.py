"""
This is the main entry point for the account service.
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import account_bp
from .models import db
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
# Initialize Flask-Migrate with the app and SQLAlchemy instance
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
app.register_blueprint(account_bp, url_prefix="/account")
# bootstrap the swagger
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"


# Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Account Service  API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
