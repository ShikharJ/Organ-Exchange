import csv, sys


#TODO: Improve This
def gale_shapley(donorfile, patientfile):

    class Organ:

        def __init__(self, information, donor_id):
            self.code = donor_id
            self.donor = information[0]
            self.type = information[1]
            self.blood_group = information[2]
            self.rhesus_factor = information[3]
            self.allocated = 0


    class Patient:

        def __init__(self, information):
            self.id = information[0]
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
            return self.test == "Positive"

        def final_status(self):
            if not self.is_eligible():
                return "Ineligible"
            elif self.allocated == "None":
                return "In Wait-List"
            else:
                return donors[self.allocated].name

        def allot(self):
            status = -1
            blood_group = self.blood_group
            rhesus_factor = self.rhesus_factor
            for req in self.requirements:
                if blood_group == "O":
                    if rhesus_factor == "-":

                    else:

                elif blood_group == "A":
                    if rhesus_factor == "-":

                    else:

                elif self.blood_group == "B":
                    if rhesus_factor == "-":

                    else:

                else:
                    if rhesus_factor == "-":

                    else:

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
        donor_reader = csv.reader(csvfile)
        for row in donor_reader:
            if row[0] == "DonorName":
                branch_header = row
            else:
                allocated_organ = Organ(row, num_organs)
                donors.append(allocated_organ)
                donormap[allocated_organ.type].append(allocated_organ.code)
                num_organs = num_organs + 1

    with open(patientfile, 'r') as csvfile:
        patient_reader = csv.reader(csvfile)
        for row in patient_reader:
            if row[0] == "User_ID":
                student_header = row
            else:
                new_patient = Patient(row)
                if new_patient.is_eligible():
                    patients.append(new_patient)
                else:
                    ineligible_patients.append(new_patient)

    patients = list(reversed(sorted(patients, key=lambda x: x.age)))

    to_delete = []
    temp_patients = patients[:]
    assigned = len(patients)

    while (len(temp_patients) != 0 and assigned != 0):
        assigned = 0
        for i, current_patient in enumerate(temp_patients):
            current_allotment = current_patient.allocated
            organ_alloted = current_patient.allot()

            if not current_patient.requirements:
                assigned = assigned + 1
                to_delete.append(i)
            elif organ_alloted != -1:
                if current_allotment != organ_alloted:
                    assigned = assigned + 1
                for key in current_patient.requirements:
                    if key != organ_alloted and key != "None":
                        #TODO: Complete This
                    else:
                        break
            else:
                for key in current_patient.requirements:
                    # TODO: Complete This
        to_delete = to_delete[::-1]
        for i in to_delete:
            temp_patients.pop(i)
        del to_delete[:]
        for donor in donors:
            donor.resetdata()

    patients.extend(ineligible_patients)
    patients = list(sorted(patients, key=lambda x: (x.id, x.name.lower())))

    #TODO: Complete This
    for current_patient in patients:
        final_list.append([current_patient.id, current_patient.name, current_patient.final_status()])
    for current_donor in donors:
        final_donor_list.append([current_donor.type])

    return final_list, final_donor_list
