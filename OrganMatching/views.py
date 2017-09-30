from django.http import HttpResponse
from django.shortcuts import render, redirect


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

        ############# UNCOMMENT BELOW  FOR AUTHENTICATION #############
        # (auth,rollno) = doLogin(userLDAP, userPASS)
        ####################################################################

        ### OR ###

        ############### UNCOMMENT FOR NO AUTHENTICATION ################
        rollno = username
        auth = True
        ####################################################################

        if auth:
            if username == ADMIN:
                #request.session['user'] = "admin"
                return redirect("admin")
            else:
                return render(request, "OrganMatching/login.html", {"Username": username, "Error": "branches.csv has not been uploaded by admin!"})
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


#TODO: Improve This
def upload(request):

    if request.method == 'GET':
        return render(request, "OrganMatching/lost.html")
    if request.method == 'POST':
        if len(request.FILES) != 2:
            return render(request, "OrganMatching/admin.html", {"Error": "Choose Both Files!"})
        return render(request, "OrganMatching/uploaded.html")
