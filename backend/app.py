from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import api.local_settings as local_settings

app = Flask(__name__)
CORS(app)

pg = local_settings.postgrsql
db_uri = f"postgresql://{pg['pguser']}:{pg['pgpassword']}@{pg['pghost']}:{pg['pgport']}/{pg['pgdb']}"
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)

from api.routes import *

with app.app_context():
    db.create_all()
    if __name__ == "__main__":
        app.run(port=5000, debug=True, use_reloader=False)
