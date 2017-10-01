import os, csv


#TODO: Improve This
def get_content(user_id):

    with open('static/patients.csv', 'r') as inp:
        for row in csv.reader(inp):
            if row[0] == user_id:
                return row

    return ["", "", "", "", ""]


#TODO: Improve This
def get_donors():

    donors = []
    with open('static/donors.csv', 'r') as inp:
        for row in csv.reader(inp):
            if row[0] != "Name":
                donors.append(row[0])

    return donors


def improvise(x, y):

    with open('static/patients.csv', 'w') as destination:
        for chunk in x.chunks():
            destination.write(chunk)

    with open('static/donors.csv', 'w') as destination:
        for chunk in y.chunks():
            destination.write(chunk)


#TODO: Improve This
def is_correct(post_data):

    if post_data.get("uname") == "":
        return "Please Enter Your Name!"

    cpi = post_data.get("cpi")
    if cpi == "":
        return "You have not entered your CPI! Please enter it correct upto 2 decimal places."

    is_num = True
    count_dot = 0
    for x in range(0, len(cpi)):
        if (not cpi[x].isdigit()) and cpi[x] != '.':
            is_num = False
            break
        elif cpi[x] == '.':
            count_dot += 1
            if count_dot > 1:
                is_num = False
                break

    if is_num:
        val = float(cpi)
        if val > 10:
            return "Your CPI is out of bounds!"
        elif (len(cpi) != 4 and val != 10):
            return "Please follow the standard CPI format and don't add any extra prefix zeroes!"
    else:
        return "Your CPI isn't a positive number!"

    chosen = post_data.get("currb")
    prefs = []

    if len(post_data) == 7:
        return "Please choose at least 1 preference!"

    for i in range(len(post_data) - 7):
        prefs.append(post_data.get("pref" + str(i + 1)))

    for pref in prefs:
        if pref == chosen:
            return "You can't have your current branch as a preference!"

    for i in range(len(prefs)):
        for j in range(i + 1, len(prefs)):
            if prefs[i] == prefs[j]:
                return "No two preferences can be the same!"

    return "none"


#TODO: Improve This
def edit_csv(post_data):
    found = False
    user_data = [post_data.get("rollno"), post_data.get("uname"), post_data.get("currb"), post_data.get("cpi"), post_data.get("category")]

    for i in range(len(post_data) - 7):
        user_data.append(post_data.get("pref" + str(i + 1)))

    if not os.path.isfile("static/patients.csv"):
        f = open("static/patients.csv", "w")
        f.write("RollNo,Name,CurrentBranch,CPI,Category,Options\n")
        f.close()

    with open('static/patients.csv', 'r') as inp, open('static/first_edit.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if found or (row[0] != post_data.get("rollno") and row[1] != post_data.get("uname")):
                writer.writerow(row)
            else:
                found = True
        writer.writerow(user_data)

    os.remove("static/patients.csv")
    os.rename("static/first_edit.csv", "static/patients.csv")
