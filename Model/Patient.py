from Persistency import Persistency


class Patient(Persistency):

    def __init__(self):
        super().__init__()
        self.id = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.DOB = None
        self.email = None
        self.date_created = None

    # return dataframe
    def findPatient(self, name):
        sql = f"select id, fist_name from patient where fist_name like '{name}'"

        return self.execute_select_pandas(sql)
