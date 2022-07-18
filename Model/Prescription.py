class Prescription():


    def __init__(self):
        self.appointment_id = None
        self.data_created = None
        self.medication = None
        self.dose = None
        self.observation = None

    def __init__(self, appointment_id, data_created, medication,dose=None, observation=None):
        self.appointment_id = appointment_id
        self.data_created = data_created
        self.medication = medication
        self.dose = dose
        self.observation = observation


        
