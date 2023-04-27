import django_filters
from django.forms import widgets
from .models import List

class mylistFilter(django_filters.FilterSet):
    STAT_CHOICES = [
        ('Not Set','Not Set'),
        ('Plan to Watch','Plan to Watch'),
        ('Currently Watching','Currently Watching'),
        ('Already Watched','Already Watched'),
    ]
    user_status = django_filters.ChoiceFilter(choices=STAT_CHOICES, widget=widgets.RadioSelect(attrs={'class':'form-check-inline ml-2 mr-2'}))

    class Meta:
        model = List
        fields = ['user_status']