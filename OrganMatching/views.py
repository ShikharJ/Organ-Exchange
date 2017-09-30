from django.http import HttpResponse
from django.shortcuts import render, redirect
from .misc import *

def index(request):

    try:
        del request.session['user']
    except:
        pass

    return render(request, "OrganMatching/login.html")


def admin(request):

    try:
        #print (request.session['user'])
        return render(request, "OrganMatching/admin.html")
    except:
        return render(request, "OrganMatching/notadmin.html")


#TODO: Improve This
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
        ####################################################################

        if auth:
            if username == ADMIN:
                request.session['user'] = "admin"
                return redirect("admin")
            else:
                old_pref = get_content(user_id)
                donors = get_donors()

                if not donors:
                    return render(request, "OrganMatching/login.html", {"Username": username, "Error": "donors.csv has not been uploaded by the admin."})

                return render(request, "OrganMatching/index.html", {"Username": username, "User_ID": user_id, "old_pref": old_pref, "donors": donors, "range": range(len(old_pref) - 5), "bcpref": old_pref[5:]})
        else:
            return render(request, "OrganMatching/login.html", {"Username": username, "Error": "Your credentials are incorrect!"})


#TODO: Improve This
def resultview(request):

    try:
        #print (request.session['user'])
        return render(request, "OrganMatching/result.html")
    except:
        return render(request, "OrganMatching/notadmin.html")


#TODO: Improve This
def resultcsv(request):

    try:
        #print (request.session['user'])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="results.csv"'
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


#TODO: Improve This
def saved(request):

    if request.method == 'GET':
        return render(request, "OrganMatching/lost.html")

    if request.method == 'POST':
        post_data = request.POST
        error = is_correct(post_data)

        if error == "None":
            edit_csv(post_data)
            warn = ""
