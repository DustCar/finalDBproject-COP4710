import django_filters
from django import forms
from .models import mediaAnime

class listFilter(django_filters.FilterSet):
    GENRE_CHOICES = [
        ('', '--------'),
        ('Drama', 'Drama'),
        ('Shounen', 'Shounen'),
    ]
    TYPE_CHOICES = [
        ('TV','TV'),
        ('Movie','Movie'),
        ('OVA','OVA'),
    ]
    genre = django_filters.MultipleChoiceFilter(lookup_expr="contains", conjoined=True,choices = GENRE_CHOICES)
    type = django_filters.ChoiceFilter(choices = TYPE_CHOICES)
    class Meta:
        model = mediaAnime
        fields = ['name', 'genre', 'type']