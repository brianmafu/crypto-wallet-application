"""
This is the main entry point for the authentication service.
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate
from .models import db
from .config import Config
from .routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# initialize database layer
db.init_app(app)  # Initialize SQLAlchemy with the app
# Initialize Flask-Migrate with the app and SQLAlchemy instance
migrate = Migrate(app, db)
jwt = JWTManager(app)
# Register auth routes
app.register_blueprint(auth_bp, url_prefix="/auth")
# bootstrap the swagger
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

# Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Authentication Service API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
