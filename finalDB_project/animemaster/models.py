from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Media(models.Model):
    name = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    
    class Meta:
        abstract = True

class mediaAnime(Media):
    type = models.CharField(max_length=15, blank=True)
    episodes = models.CharField(max_length=10)