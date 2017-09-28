from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib import admin
from django.db import models

class Patient(models.Model):
    user = models.OneToOneField(User, primary_key = True)
    adhn = models.CharField(max_length = 9, unique = True)
    birth_date = models.DateField()
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    zip_code = models.CharField(max_length = 6)

    Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length = 1, choices = Gender_Choices)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class PatientAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('user__first_name', 'user__last_name', 'user__adhn')
    list_display = ('__unicode__', 'birth_date', 'adhn',)
