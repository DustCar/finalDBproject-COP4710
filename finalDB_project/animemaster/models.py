from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
    
class Media(models.Model):
    name = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    media_img = models.ImageField(null=True, upload_to="photos")
    synopsis = models.TextField(null=True)
    
    class Meta:
        abstract = True

class mediaAnime(Media):
    type = models.CharField(max_length=15, blank=True)
    episodes = models.CharField(max_length=10)