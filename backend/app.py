from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize the database and migration objects
db.init_app(app)
migrate = Migrate(app, db)

# Import routes after app and db initialization
from routes import register_routes

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
