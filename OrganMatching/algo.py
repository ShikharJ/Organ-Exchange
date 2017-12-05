import csv, sys


#TODO: Improve This
def gale_shapley(donorfile, patientfile):

    class Donor:

        def __init__(self, information, donor_id):
            self.code = donor_id
            self.name = information[0]


    class Patient:

        def __init__(self, information, patient_id):
            self.code = patient_id
            self.name = information[0]

        def is_eligible(self):
            return False

        def final_status(self):
            if not self.is_eligible():
                return "Ineligible"

        def allot(self):
            status = -1

    return None
