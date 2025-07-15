from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig 

db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
