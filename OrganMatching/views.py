from django.shortcuts import render, redirect


def index(request):

    try:
        del request.session['user']
    except:
        pass

    return render(request, "OrganMatching/login.html")


def admin(request):

    try:
        print (request.session['user'])
        return render(request, "OrganMatching/admin.html")
    except:
        return render(request, "OrganMatching/notadmin.html")
