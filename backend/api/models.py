from app.app import db


class Patient(db.Model):
    """
    Represents a patient in the clinic system.

    Attributes:
        id (int): The unique identifier of the patient.
        pesel (int): The PESEL number of the patient.
        name (str): The name of the patient.
        surrname (str): The surname of the patient.
    """

    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    pesel = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)
    surrname = db.Column(db.String(100), nullable=False)

    def json(self):
        """
        Returns the patient data in JSON format.

        Returns:
            dict: The patient data in JSON format.
        """
        return {
            "id": self.id,
            "pesel": self.pesel,
            "name": self.name,
            "surrname": self.surrname,
        }

    def update(self, data):
        """
        Updates the patient data with the provided data.

        Args:
            data (dict): The data to update the patient with.
        """
        for key, item in data.items():
            setattr(self, key, item)
