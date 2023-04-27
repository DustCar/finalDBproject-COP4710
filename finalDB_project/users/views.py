from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, userStatus
from .models import User, List
from datetime import datetime
from animemaster.models import mediaAnime


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

@login_required
def addToList(request, pk):
    
    list = List()
    anime_db = mediaAnime.objects.get(pk=pk)
    ani_list = List.objects.filter(media=anime_db, user=request.user.username).exists()
    if ani_list == False:
        list.user = request.user.username
        list.media = anime_db
        now = datetime.now()
        list.timeadded = now.strftime('%H:%M:%S')
        list.dateadded = now.date()
        list.save()
        messages.success(request, f'Anime added!')
    else:
        messages.error(request, f'Anime is already added!')
    return redirect('animemaster-mylist')

@login_required
def mylist(request):
    listdb = List.objects.select_related().filter(user=request.user.username).order_by('-dateadded', '-timeadded')
    list_count = listdb.count()
    
    return render(request, 'animemaster/mylist.html', {'anime_list' : listdb, 'list_count' : list_count})

def unlist(request, pk):
    list = List.objects.filter(lid=pk)
    list.delete()
    messages.success(request, f'Anime removed successfully!')
    return redirect('animemaster-mylist')

def updateStat(request, pk):
    list = List.objects.get(lid=pk)
    anime = mediaAnime.objects.get(id=list.media_id)
    form = userStatus(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('animemaster-mylist')
    return render(request, 'users/update-list.html', {'form' : form, 'anime' : anime})