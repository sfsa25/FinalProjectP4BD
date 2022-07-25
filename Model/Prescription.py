from Persistency import Persistency
import PersistencyDML


class Prescription(Persistency):

    def __init__(self, patient_id=None, doctor_id=None, medication=None, observation=None):
        super().__init__()
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication = medication
        self.observation = observation

    def insertPrescription(self):

        self.insertPrescribe(self.patient_id, self.doctor_id, self.medication, self.observation)

    def findPrescription(self):

        return self.findPrescriptionbyDoctor(self.doctor_id, self.patient_id)












