from flask import Flask
from project import app, db
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from project.model import Patient
import json


@app.route("/", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def get_user_info():
    print("endpoint")
    #!Functionality doesnt work
    pesel = request.json["pesel"]
    patient = Patient.query.get(pesel)
    patient_json = {
        "pesel": patient["pesel"],
        "name": patient["name"],
        "surrname": patient["surrname"],
    }

    return str(patient_json)


# Start the app
if __name__ == "__main__":
    with app.app_context():
        app.run()
        db.create_all()
