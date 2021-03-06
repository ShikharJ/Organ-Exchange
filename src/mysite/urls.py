"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from OrganMatching import views


urlpatterns = [
    url(r'^OrganMatching/', views.index, name = "index"),
    url(r'^admin/$', views.admin, name = "admin"),
    url(r'^submit/$', views.submit, name = "index"),
    url(r'^saved/$', views.saved, name="saved"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^resultview/$', views.resultview, name="resultview"),
    url(r'^resultcsv/$', views.resultcsv, name="resultcsv"),
]

handler404 = "views.error404"