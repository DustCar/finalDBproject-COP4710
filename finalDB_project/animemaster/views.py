from django.shortcuts import render, redirect
from .models import mediaAnime
from users.models import List
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'animemaster/home.html') # pass it as our third argument (pass the data into the template)

def about(request):
    return render(request, 'animemaster/about.html', {'title': 'About'})

def anime(request):
    anime_list = mediaAnime.objects.all() 
    
    return render(request, 'animemaster/anime.html', {'anime_list': anime_list})

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
    return redirect('animemaster-anime')

def mylist(request):

    listdb = List.objects.filter(user=request.user.username)
    return render(request, 'animemaster/mylist', {'anime_list' : listdb})
    