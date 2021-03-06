from django.http import HttpResponse
from django.shortcuts import render, redirect
from OrganMatching.misc import *
from OrganMatching.algo import *

blood_groups = ["A", "B", "AB", "O"]
rhesus_factors = ["+", "-"]
reports = ["Positive", "Negative"]


def index(request):

    try:
        del request.session['user']
    except:
        pass

    return render(request, "OrganMatching/login.html")


def admin(request):

    try:
        return render(request, "OrganMatching/admin.html")
    except:
        return render(request, "OrganMatching/notadmin.html")


def submit(request):

    if request.method == 'GET':
        return render(request, "OrganMatching/lost.html")

    if request.method == 'POST':

        username = request.POST.get("Username")
        password = request.POST.get("Password")

        if username == "" or password == "":
            return render(request, "OrganMatching/lost.html", {"Username": username, "Error": "Both fields must be filled!"})

        ADMIN = "Shikhar"

        ############### UNCOMMENT FOR NO AUTHENTICATION ################
        user_id = username
        auth = True
        ################################################################

        if auth:
            if username == ADMIN:
                request.session['user'] = "admin"
                return redirect("admin")
            else:
                patient = get_content(user_id)
                donors = get_donors()

                if not donors:
                    return render(request, "OrganMatching/login.html", {"Username": username, "Error": "donors.csv has not been uploaded by the admin."})

                return render(request, "OrganMatching/index.html", {"Username": username, "User_ID": user_id, "patient": patient, "donors": donors, "blood_groups": blood_groups, "rhesus_factors": rhesus_factors, "reports": reports, "range":range(len(patient) - 6), "orgreq":patient[6:]})
        else:
            return render(request, "OrganMatching/login.html", {"Username": username, "Error": "Your credentials are incorrect!"})


def resultview(request):

    try:
        final_list, donor_list = gale_shapley("static/donors.csv", "static/patients.csv")
        return render(request, "OrganMatching/result.html", {"final_list": final_list})
    except:
        return render(request, "OrganMatching/notadmin.html")


def resultcsv(request):

    try:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="results.csv"'
        final_list, donor_list = gale_shapley("static/donors.csv", "static/patients.csv")
        writer = csv.writer(response)
        writer.writerows(final_list)
        return response
    except:
        return render(request, "OrganMatching/notadmin.html")


def upload(request):

    if request.method == 'GET':
        return render(request, "OrganMatching/lost.html")

    if request.method == 'POST':
        if len(request.FILES) != 2:
            return render(request, "OrganMatching/admin.html", {"Error": "Choose Both Files!"})

        improvise(request.FILES['file1'], request.FILES['file2'])
        return render(request, "OrganMatching/uploaded.html")


def saved(request):

    if request.method == 'GET':
        return render(request, "OrganMatching/lost.html")

    if request.method == 'POST':
        post_data = request.POST
        error = is_correct(post_data)

        if error == "None":
            edit_csv(post_data)
            warn = ""

            if int(post_data.get("Age")) < 18:
                warn = "Your age is below the legally permitted age, but the form was submitted!"

            return render(request, "OrganMatching/saved.html", {"Warn": warn})
        else:
            user_id = post_data.get("User_ID")
            username = post_data.get("Username")
            patient = [user_id, post_data.get("Name"), post_data.get("Blood_Report"), post_data.get("Age"), post_data.get("Blood_Group"), post_data.get("Rhesus_Factor")]
            for i in range(len(post_data) - 8):
                patient.append(post_data.get("Organ_Requirement" + str(i + 1)))
            donors = get_donors()

            return render(request, "OrganMatching/index.html", {"Username": username, "User_ID": user_id, "patient": patient, "donors": donors, "blood_groups": blood_groups, "rhesus_factors": rhesus_factors, "reports": reports, "range":range(len(patient) - 6), "orgreq":patient[6:], "Error": error})
