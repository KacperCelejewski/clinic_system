from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import local_settings as settings

pg = settings.postgrsql

app = Flask(__name__)

# Set up the database URI
db_uri = f"postgresql://{pg['pguser']}:{pg['pgpassword']}@{pg['pghost']}:{pg['pgport']}/{pg['pgdb']}"
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# # Initialize Marshmallow
# ma = Marshmallow(app)

# Set DEBUG mode if needed
app.config["DEBUG"] = True


# Start the app
if __name__ == "__main__":
    app.run()
