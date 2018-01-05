import csv, sys


def gale_shapley(donorfile, patientfile):

    class Organ:

        def __init__(self, information, donor_id):
            self.code = donor_id
            self.donor = information[1]
            self.type = information[0]
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
            self.requested = information[6:]
            for requirement in information[6:]:
                if requirement:
                    self.requirements.append(donor_map[requirement])
            self.allocated = []

        def is_eligible(self):
            return self.test == "Positive"

        def final_status(self):
            if not self.is_eligible():
                return "Ineligible"
            elif not self.allocated:
                return "In Wait-List"
            else:
                allocated_list = []
                for i in self.allocated:
                    allocated_list.append(str(donors[i].donor) + " (" + str(donors[i].type) + ") ")
                return allocated_list

        def amend(self, req):
            donors[req].allocated = self.name
            self.allocated.append(req)

        def allot(self):
            status = -1
            flag = 0
            blood_group = self.blood_group
            rhesus_factor = self.rhesus_factor
            for req in self.requirements:
                if donors[req].allocated != 0:
                    continue
                for i in self.allocated:
                    if donors[i].type == donors[req].type:
                        flag = -1
                        break
                if flag == -1:
                    continue
                donor_group = donors[req].blood_group
                donor_factor = donors[req].rhesus_factor
                if blood_group == "O":
                    if rhesus_factor == "-":
                        if donor_group == "O" and donor_factor == "-":
                            self.amend(req)
                            status = req
                    elif donor_group == "O":
                        self.amend(req)
                        status = req
                elif blood_group == "A":
                    if rhesus_factor == "-":
                        if (donor_group == "A" or donor_group == "O") and donor_factor == "-":
                            self.amend(req)
                            status = req
                    elif donor_group == "O" or donor_group == "A":
                        self.amend(req)
                        status = req
                elif self.blood_group == "B":
                    if rhesus_factor == "-":
                        if (donor_group == "B" or donor_group == "O") and donor_factor == "-":
                            self.amend(req)
                            status = req
                    elif donor_group == "B" or donor_group == "O":
                        self.amend(req)
                        status = req
                else:
                    if rhesus_factor == "-":
                        if donor_factor == "-":
                            self.amend(req)
                            status = req
                    else:
                        self.amend(req)
                        status = req

            if status != -1:
                self.requirements = self.requirements[0:self.requirements.index(status)]
            return status

    donors = []
    patients = []
    num_organs = 0
    donor_map = {}
    ineligible_patients = []
    final_list = []
    final_donor_list = []

    with open(donorfile, 'r') as csvfile:
        donor_reader = csv.reader(csvfile)
        for row in donor_reader:
            if row[0] == "DonorName":
                continue
            else:
                allocated_organ = Organ(row, num_organs)
                donors.append(allocated_organ)
                donor_map[allocated_organ.type] = allocated_organ.code
                num_organs = num_organs + 1

    with open(patientfile, 'r') as csvfile:
        patient_reader = csv.reader(csvfile)
        for row in patient_reader:
            if row[0] == "User_ID":
                continue
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

    while len(temp_patients) != 0 and assigned != 0:
        assigned = 0
        for i, current_patient in enumerate(temp_patients):
            current_allotment = current_patient.allocated
            organ_alloted = current_patient.allot()

            if not current_patient.requirements:
                assigned = assigned + 1
                to_delete.append(i)
            elif organ_alloted != -1:
                if organ_alloted not in current_allotment:
                    assigned = assigned + 1
        to_delete = to_delete[::-1]
        for i in to_delete:
            temp_patients.pop(i)
        del to_delete[:]

    patients.extend(ineligible_patients)
    patients = list(sorted(patients, key=lambda x: (x.id, x.name.lower())))

    for current_patient in patients:
        final_list.append([current_patient.id, current_patient.name, current_patient.requested, current_patient.final_status()])
    for current_donor in donors:
        final_donor_list.append([current_donor.type, current_donor.allocated])

    return final_list, final_donor_list
