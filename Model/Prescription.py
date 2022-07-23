from Persistency import Persistency
import PersistencyDML


class Prescription(Persistency):

    def __init__(self):
        super().__init__()
        self.patient_id = None
        self.doctor_id = None
        self.medication = None
        self.observation = None

    def __init__(self, patient_id, doctor_id, medication, observation=None):
        super().__init__()
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication = medication
        self.observation = observation

    def insertPrescription(self):
        statement = self.insert_statement_byDict(self.__dict__, 'Prescription')
        self.execute_command(statement)












