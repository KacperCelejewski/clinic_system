from flask import Flask, request, jsonify, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
import local_settings

app = Flask(__name__)

CORS(app)
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
def test():
    return make_response(jsonify({"message": "Works fine!"}))


#! Limits for len of PESEL (sQL integer error)
# create patient
@app.route("/add-patient", methods=["POST"])
def create_patient():
    try:
        data = request.get_json()
        new_patient = Patient(
            pesel=int(data["pesel"]), name=data["name"], surrname=data["surrname"]
        )
        db.session.add(new_patient)
        db.session.commit()

        return make_response(jsonify({"message": "Patient created"}), 201)

    except IntegrityError:
        db.session.rollback()
        return make_response(
            jsonify({"error": "Patient with this PESEL already exists"}), 400
        )
    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return make_response(jsonify({"error": str(e)}), 500)


# get patient
@app.route("/search-patient/<int:pesel>", methods=["GET"])
def get_patient(pesel):
    try:
        patient = Patient.query.filter_by(pesel=pesel).first()
        return make_response(jsonify({"patient": patient.json()}), 200)
    except Exception:
        return make_response(jsonify({"message": "getting patient failed"}), 500)


# update patient
@app.route("/search-patient/<int:pesel>/edit", methods=["PUT"])
def update_patient(pesel):
    try:
        patient = Patient.query.filter_by(pesel=pesel).first()
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
@app.route("/search-patient/<int:id>/delete", methods=["DELETE"])
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
    db.create_all()
with app.app_context():
    if __name__ == "__main__":
        app.run(port=5000, debug=True, use_reloader=False)
