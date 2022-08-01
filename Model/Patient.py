from Persistency import Persistency


class Patient(Persistency):

    def __init__(self, patient_first_name=None, patient_last_name=None, patient_gender=None, patient_dob=None, patient_email=None):
        super().__init__()
        # self.id = None
        self.patient_first_name = patient_first_name
        self.patient_last_name = patient_last_name
        self.patient_gender = patient_gender
        self.patient_dob = patient_dob
        self.patient_email = patient_email
        # self.date_created = None

    # return dataframe
    def findPatient(self, name):
        sql = f"select id, first_name from patient where first_name like '{name}'"

        return self.execute_select_pandas(sql)

    def insert(self):
        self.insertPatient(self.patient_first_name, self.patient_last_name, self.patient_gender, self.patient_dob,
                           self.patient_email)

    def findPatientByFullName(self, patient_first_name, patient_last_name):

        return self.findPatientByFullNameS(patient_first_name, patient_last_name)
