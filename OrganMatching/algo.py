import csv, sys


#TODO: Improve This
def gale_shapley(donorfile, patientfile):

    class Donor:

        def __init(self, information, donor_id):
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

    branches = []
    students = []
    numbranches = 0
    branchmap = {}
    ineligibleStudents = []
    finalList = []
    finalBranchList = []

    with open(donorfile, 'r') as csvfile:
        branchreader = csv.reader(csvfile)
        for row in branchreader:
            if (row[0] == "BranchName"):
                branchheader = row
            else:
                newbranch = Donor(row, numbranches)
                branches.append(newbranch)
                branchmap[newbranch.name] = newbranch.code
                numbranches = numbranches + 1

    # for curbranch in branches:
    #  	print(curbranch.name,curbranch.code,curbranch.sancStrength,curbranch.curStrength,sep = " ")

    with open(patientfile, 'r') as csvfile:
        studentreader = csv.reader(csvfile)
        for row in studentreader:
            if (row[0] == "RollNo"):
                studentheader = row
            else:
                newstudent = Patient(row)
                if (newstudent.is_eligible()):
                    students.append(newstudent)
                else:
                    ineligibleStudents.append(newstudent)

    students = list(reversed(sorted(students, key=lambda x: x.cpi)))

    # for curstudent in students:
    # print(curstudent.name,curstudent.preferences,curstudent.cpi,sep = " ")

    toDelete = []
    tempStudents = students[:]
    changed = len(students)
    # iterations =0
    # while(len(tempstudents) !=0 and iterations!=1):
    # 	iterations=0
    while (len(tempStudents) != 0 and changed != 0):

        # Denotes the no of Students whose branch changed
        changed = 0

        for i, curStudent in enumerate(tempStudents):
            curbranch = curStudent.tempbranch
            branchAlloted = curStudent.allotBranch()

            if (not curStudent.preferences):
                changed = changed + 1
                toDelete.append(i)

            elif (branchAlloted != -1):
                if (curbranch != branchAlloted):
                    changed = changed + 1
                for key in curStudent.preferences:
                    if (key != branchAlloted):
                        branches[key].MaxUnallowedCPI = max(curStudent.cpi, branches[key].MaxUnallowedCPI)
                    else:
                        break
            else:
                for key in curStudent.preferences:
                    branches[key].MaxUnallowedCPI = max(curStudent.cpi, branches[key].MaxUnallowedCPI)

        toDelete = toDelete[::-1]
        for i in toDelete:
            tempStudents.pop(i)
        del toDelete[:]
        for branch in branches:
            branch.resetdata()

    students.extend(ineligibleStudents)
    students = list(sorted(students, key=lambda x: (x.roll, x.name.lower())))
    for curStudent in students:
        finalList.append([curStudent.roll, curStudent.name, branches[curStudent.branch].name, curStudent.finalStatus()])
    for curbranch in branches:
        finalBranchList.append([curbranch.name, curbranch.cutoffCPI(), curbranch.sancStrength, curbranch.origStrength,
                                curbranch.curStrength])


    return finalList, finalBranchList