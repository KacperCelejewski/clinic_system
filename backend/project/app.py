from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ


app = Flask(__name__)
import local_settings

pg = local_settings.postgrsql
db_uri = f"postgresql://{pg['pguser']}:{pg['pgpassword']}@{pg['pghost']}:{pg['pgport']}/{pg['pgdb']}"

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)


class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    pesel = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)
    surrname = db.Column(db.String(100), nullable=False)

    def json(self):
        return {
            "id": self.id,
            "pesel": self.pesel,
            "name": self.name,
            "surrname": self.surrname,
        }


@app.route("/")
def hello():
    return make_response(jsonify({"message": "hello"}), 200)


# create patient
@app.route("/patient", methods=["POST"])
def create_patient():
    try:
        data = request.get_json()
        new_patient = Patient(
            pesel=data["pesel"], name=data["name"], surrname=data["surrname"]
        )
        db.session.add(new_patient)
        db.session.commit()
        return make_response(jsonify({"message": "patient created"}), 201)
    except Exception:
        return make_response(jsonify({"message": "creating patient failed"}), 500)


# get patient
@app.route("/patient/<int:id>", methods=["GET"])
def get_patient(id):
    try:
        patient = Patient.query.filter_by(id=id).first()
        return make_response(jsonify({"patient": patient.json()}), 200)
    except Exception:
        return make_response(jsonify({"message": "getting patient failed"}), 500)


# update patient
@app.route("/patient/<int:id>", methods=["PUT"])
def update_patient(id):
    try:
        patient = Patient.query.filter_by(id=id).first()
        if patient:
            data = request.get_json()

            patient.pesel = data["pesel"]
            patient.name = data["name"]
            patient.surrname = data["surrname"]
            db.session.commit()
            return make_response(jsonify({"message": "patient updated"}), 200)
        return make_response(jsonify({"message": "patient not found"}), 404)
    except Exception:
        return make_response(jsonify({"message": "updating patient failed"}), 500)


# delete patient
@app.route("/patient/<int:id>", methods=["DELETE"])
def delete_patient(id):
    try:
        patient = Patient.query.filter_by(id=id).first()
        if patient:
            db.session.delete(patient)
            db.session.commit()
            return make_response(jsonify({"message": "patient deleted"}), 200)
        return make_response(jsonify({"message": "patient not found"}), 404)
    except Exception:
        return make_response(jsonify({"message": "deleting patient failed"}), 500)


with app.app_context():
    if __name__ == "__main__":
        app.run()
        db.create_all()
