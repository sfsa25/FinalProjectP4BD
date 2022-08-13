# reporting
import numpy as np
import matplotlib.pyplot as plt
from Patient import Patient
from Appointment import Appointment
import pandas as pd


class Reporting:

    def patientByAge(self):
        patient = Patient().reportPatientByAge()
        if not patient.empty:

            patient['Age-Range'] = patient['age'].apply(
                lambda x: 'Less than 12 years old' if x < 12 else ('Between 12 and 19 years old'
                                                                   if (x >= 12 and x <= 19) else (
                    'Between 19 e 55 years old' if (x >= 19 and x <= 55) else 'Bigger than 55 years old')))

            df = patient.groupby(['Age-Range']).count()
            fig = df.plot.bar( title='Report 1: Count patient by Age Range', rot=15, figsize=(16, 9), colormap='summer', legend=False)
            fig.bar_label(fig.containers[0], label_type='edge')
            plt.show(block=True)

        input("Press Enter to go back to Menu.")
        plt.close()

    def appointmentBySpecialty(self):
        app = Appointment().reportBySpecialty()
        if not app.empty:
            plt.figure(figsize=(16, 8))
            plt.title('Report 2: Appointment by Specialty \n', fontsize=18)
            plt.pie(app["count"], labels=app["SPECIALTY"], autopct='%1.1f%%')
            plt.show(block=True)

        input("Press Enter to go back to Menu.")
        plt.close()

    def appointmentByDayOfWeek(self):
        app = Appointment().reportByDayOfWeek()
        if not app.empty:
            app = app.sort_values(by='sort')
            app.plot.line(x='day_of_week', y= 'count', figsize=(16, 8), color='navy', linewidth=2.5, marker = 'o',
                          title='Report 3: Appointment by Day of week.')

            plt.show(block=True)



