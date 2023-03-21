from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    
#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

class List(models.Model):
    user = models.CharField(max_length=100, default="Anonymous")
    name = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    lid = models.AutoField(primary_key=True)
    aid = models.PositiveIntegerField(default=0)
    typeL = models.CharField(max_length=200, blank=True)
    episodesL = models.CharField(max_length=10, blank=True)
    timeadded = models.TimeField(blank=True, null=True)
    dateadded = models.DateField(blank=True, null=True)
