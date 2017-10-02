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

    if post_data.get("Name") == "":
        return "Please Enter Your Name!"

    age = post_data.get("Age")
    if age == "":
        return "You have not entered your age! Please enter it correct upto 2 decimal places."

    is_num = True
    for x in range(0, len(age)):
        if not age[x].isdigit():
            is_num = False
            break

    if is_num:
        val = int(age)
        if val > 80 or val < 4:
            return "Your age is too advanced / premature for a transplant. Please consult a specialist!"
    else:
        return "Your age isn't a positive integer!"

    return "none"


#TODO: Improve This
def edit_csv(post_data):

    found = False
    user_data = [post_data.get("User_ID"), post_data.get("Name"), post_data.get("Blood_Report"), post_data.get("Age"), post_data.get("Blood_Group")]

    if not os.path.isfile("static/patients.csv"):
        f = open("static/patients.csv", "w")
        f.write("User_ID,Name,Blood_Report,Age,Blood_Group,Options\n")
        f.close()

    with open('static/patients.csv', 'r') as inp, open('static/first_edit.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if found or (row[0] != post_data.get("User_ID") and row[1] != post_data.get("Name")):
                writer.writerow(row)
            else:
                found = True
        writer.writerow(user_data)

    os.remove("static/patients.csv")
    os.rename("static/first_edit.csv", "static/patients.csv")
