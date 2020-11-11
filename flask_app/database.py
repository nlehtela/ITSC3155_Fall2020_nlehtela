from database import db
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask-SQLAlchemy extension instance
db = SQLAlchemy()

# Import the database instance

# Configure the database connection, Set the name and location of the database file.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'

# Set the SQLALCHEMY_TRACK_MODIFICATIONS configuration option to False to disable a feature of
# Flask-SQLAlchemy that we do not need, which is to signal the application every time a change is about to be made in the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context
