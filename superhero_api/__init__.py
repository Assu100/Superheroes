from flask import Flask
from .app import app, db, migrate
from .routes import setup_routes
from .models import db  # Import db from models.py
from .config import Config

def create_app():
    # app = Flask(__name__)
    # app.config.from_object(Config)

    # # initialize the db
    # db.init_app(app)
    app.config.from_object('superhero_api.config.Config')
    db.init_app(app)
    migrate.init_app(app, db)

    setup_routes(app)  # Register routes

    return app

