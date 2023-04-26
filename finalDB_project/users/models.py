from django.db import models
from animemaster.models import mediaAnime

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    
#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

class List(models.Model):
    user = models.CharField(max_length=100, default="Anonymous")
    lid = models.AutoField(primary_key=True)
    timeadded = models.TimeField(blank=True, null=True)
    dateadded = models.DateField(blank=True, null=True)
    media = models.ForeignKey(mediaAnime, on_delete=models.CASCADE, default=-1)
    user_status = models.CharField(max_length=50,null=True, default="Not Set")

