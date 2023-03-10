from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    
#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)