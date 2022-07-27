from Persistency import Persistency

class Appointment(Persistency):

    def __init__(self, patient_id=None,  doctor_id=None, date=None, slot=None, appointment_id =None):
        super().__init__()
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.slot = slot
        self.appointment_id = appointment_id

    def insert(self, new_slot):
        self.insertAppointment(self.patient_id, self.doctor_id, self.date, self.slot, new_slot)

    def update(self,  removed_slot, prior_date, returned_slot):
        self.updateAppointment(self.appointment_id, self.doctor_id, self.date, self.slot,
                               removed_slot, prior_date, returned_slot)

    def findAppointmentDoctor(self, doctor):
        return self.findAppointmentByDoctor(doctor)

    def findAppointmentPatient(self, patient):
        return self.findAppointmentByPatient(patient)






