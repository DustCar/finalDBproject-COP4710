from django import forms
from .models import List
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class userStatus(forms.ModelForm):
    STAT_CHOICES = [
        ('Not Set','Not Set'),
        ('Plan to Watch', 'Plan to Watch'),
        ('Currently Watching', 'Currently Watching'),
        ('Already Watched', 'Already Watched'),
    ]
    user_status = forms.ChoiceField(label='Select Status', widget=forms.RadioSelect, choices=STAT_CHOICES)

    class Meta:
        model = List
        fields = ['user_status']