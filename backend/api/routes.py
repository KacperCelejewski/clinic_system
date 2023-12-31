from flask import make_response, jsonify, request
from .models import Patient
from app.app import app, db
from sqlalchemy.exc import IntegrityError


# create patient
@app.route("/add-patient", methods=["POST"])
def create_patient():
    """
    Create a new patient.

    This function is responsible for creating a new patient in the clinic system.
    It receives the patient data as a JSON object in the request body and adds the patient to the database.
    If the patient with the same PESEL already exists, it returns a 400 error.
    If any other error occurs, it returns a 500 error.

    Returns:
        A response object with a JSON message indicating the success or failure of the operation.
    """
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
    """
    Get patient information by their PESEL number.

    Args:
        pesel (int): The PESEL number of the patient.

    Returns:
        Response: The response containing the patient information in JSON format.

    Raises:
        Exception: If there is an error while retrieving the patient information.
    """
    try:
        patient = Patient.query.filter_by(pesel=pesel).first()
        return make_response(jsonify({"patient": patient.json()}), 200)
    except Exception:
        return make_response(jsonify({"message": "getting patient failed"}), 500)


# update patient
@app.route("/search-patient/<int:pesel>/edit", methods=["PUT"])
def update_patient(pesel):
    """
    Update a patient's information.

    Args:
        pesel (int): The PESEL number of the patient.

    Returns:
        Response: A JSON response indicating the result of the update operation.
    """
    try:
        patient = Patient.query.filter_by(pesel=pesel).first()
        if patient:
            data = request.get_json()
            patient.update(data)
            db.session.commit()
            return make_response(jsonify({"message": "patient updated"}), 200)
        return make_response(jsonify({"message": "patient not found"}), 404)
    except Exception:
        return make_response(jsonify({"message": "updating patient failed"}), 500)


# delete patient
@app.route("/search-patient/<int:id>/delete", methods=["DELETE"])
def delete_patient(id):
    """
    Delete a patient from the database.

    Args:
        id (int): The ID of the patient to be deleted.

    Returns:
        flask.Response: A JSON response indicating the result of the deletion operation.
            - If the patient is found and successfully deleted, returns a response with status code 200 and message "patient deleted".
            - If the patient is not found, returns a response with status code 404 and message "patient not found".
            - If an exception occurs during the deletion operation, returns a response with status code 500 and message "deleting patient failed".
    """
    try:
        patient = Patient.query.filter_by(id=id).first()
        if patient:
            db.session.delete(patient)
            db.session.commit()
            return make_response(jsonify({"message": "patient deleted"}), 200)
        return make_response(jsonify({"message": "patient not found"}), 404)
    except Exception:
        return make_response(jsonify({"message": "deleting patient failed"}), 500)
