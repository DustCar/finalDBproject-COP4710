from django.shortcuts import render, redirect
from .models import Post # from the models files in current package
from .models import mediaAnime
from users.models import List
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    # key is 'post' and the value is the list of posts from the top
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'animemaster/home.html', context) # pass it as our third argument (pass the data into the template)

def about(request):
    return render(request, 'animemaster/about.html', {'title': 'About'})

def anime(request):
    anime_list = mediaAnime.objects.all() 
    
    return render(request, 'animemaster/anime.html', {'anime_list': anime_list})

@login_required
def addToList(request, pk):
    
    list = List()
    anime_db = mediaAnime.objects.get(pk=pk)
    ani_list = List.objects.filter(name=anime_db.name, user=request.user.username).exists()
    if ani_list == False:
        list.user = request.user.username
        list.aid = anime_db.pk
        list.name = anime_db.name
        list.episodesL = anime_db.episodes
        list.genre = anime_db.genre
        list.typeL = anime_db.type
        now = datetime.now()
        list.timeadded = now.strftime('%H:%M:%S')
        list.dateadded = now.date()
        list.save()
        messages.success(request, f'Anime added!')
    else:
        messages.error(request, f'Anime is already added!')
    return redirect('animemaster-anime')