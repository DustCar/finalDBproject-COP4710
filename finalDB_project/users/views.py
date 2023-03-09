from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.username = form.cleaned_data.get('username')
            new_user.email = request.POST.get('email') 
            new_user.save()
            form.save()
            #display_username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in, fellow weeb!:)')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # decorator: adds functionality to an existing function (user must be logged for this page)
def profile(request):
    return render(request, 'users/profile.html')