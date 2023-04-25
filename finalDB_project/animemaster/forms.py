from django import forms
from .models import mediaAnime

class AnimeForm(forms.ModelForm):

    class Meta:
        model = mediaAnime
        fields = ['name', 'genre', 'media_img', 'synopsis', 'type', 'episodes']

