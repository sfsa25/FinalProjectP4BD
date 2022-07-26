from Persistency import Persistency

class Appointment(Persistency):

    def __init__(self, patient_id=None,  doctor_id=None, date=None, slot=None):
        super().__init__()
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.slot = slot

    def insert(self):
        self.insertAppointment(self.patient_id, self.doctor_id,self.date, self.slot)

    def findAppointmentDoctor(self, doctor):
        return self.findAppointmentByDoctor(doctor)

    def findAppointmentPatient(self, patient):
        return self.FindAppointmentPatient(patient)

    def findFreeDate(self, doctor):
        return self.findFreeDateByDoctor(doctor)




