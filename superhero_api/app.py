from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # Import the Config class
from .routes import setup_routes  # Import your routes setup function

# Initialize the app
app = Flask(__name__)
app.config.from_object(Config)  # Use the Config class for app config

# Initialize database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register routes
setup_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if not already created
        seed_data() #populate the db
    app.run(debug=True)


