import csv, sys


#TODO: Improve This
def gale_shapley(donorfile, patientfile):

    class Organ:

        def __init__(self, information, donor_id):
            self.code = donor_id
            self.name = information[0]
            self.strength = int(information[1])


    class Patient:

        def __init__(self, information):
            self.roll = information[0]
            self.name = information[1]
            self.test = information[2]
            self.age = information[3]
            self.blood_group = information[4]
            self.rhesus_factor = information[5]
            self.requirements = []
            for requirement in information[6:]:
                if requirement:
                    self.requirements.append(donormap[requirement])
            self.allocated = "None"

        def is_eligible(self):
            return (self.test == "Positive")

        def final_status(self):
            if not self.is_eligible():
                return "Ineligible"
            elif self.allocated == "None":
                return "In Wait-List"
            else:
                return donors[self.allocated].name

        def allot(self):
            status = -1
            for req in self.requirements:
                self
            if status != -1:
                self.requirements = self.requirements[0:self.requirements.index(status)]
            return status

    donors = []
    patients = []
    num_organs = 0
    donormap = {}
    ineligible_patients = []
    final_list = []
    final_donor_list = []

    with open(donorfile, 'r') as csvfile:
        donor_reader = csv.reader(donorfile)
        for row in donor_reader:
            if row[0] == "DonorName":
                branch_header = row
            else:
                allocated_organ = Organ(row, num_organs)
                donors.append(allocated_organ)
                donormap[allocated_organ.name] = allocated_organ.code
                num_organs = num_organs + 1

    return None
