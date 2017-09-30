import os, csv

def get_content(user_id):

    with open('static/patients.csv', 'r') as inp:
        for row in csv.reader(inp):
            if row[0] == user_id:
                return row

    return ["", "", "", "", ""]


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
