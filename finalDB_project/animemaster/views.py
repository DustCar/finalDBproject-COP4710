from django.shortcuts import render, redirect
from .models import mediaAnime
from users.models import List
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import AnimeForm

def welcome(request):
    return render(request, 'animemaster/welcome.html')

def home(request):
    return render(request, 'animemaster/home.html') # pass it as our third argument (pass the data into the template)

def about(request):
    return render(request, 'animemaster/about.html', {'title': 'About'})

def anime(request):
    anime_list = mediaAnime.objects.order_by('-id')
    
    return render(request, 'animemaster/anime.html', {'anime_list': anime_list})

def details(request, pk):
    anime = mediaAnime.objects.get(id=pk)

    return render(request, 'animemaster/details.html', {'curr_anime': anime})

# user functions
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
    listdb = List.objects.select_related().filter(user=request.user.username)
    return render(request, 'animemaster/mylist.html', {'anime_list' : listdb})

def unlist(request, pk):
    list = List.objects.filter(lid=pk)
    list.delete()
    messages.success(request, f'Anime removed successfully!')
    return redirect('animemaster-mylist')

# admin functions
def remove(request, pk):
    anime = mediaAnime.objects.get(id=pk)
    anime.delete()
    messages.success(request, f'{anime.name} removed')
    return redirect('animemaster-anime')

def update(request, pk):
    init_anime = mediaAnime.objects.get(pk=pk)
    
    form = AnimeForm(request.POST or None, request.FILES or None, instance=init_anime)
    if form.is_valid():
        form.save()
        return redirect('details-media', pk)
    return render(request, 'animemaster/update.html', {'form' : form})

def addAnime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            new_anime = mediaAnime()
            new_anime.name = form.cleaned_data.get('name')
            new_anime.genre = form.cleaned_data.get('genre')
            new_anime.media_img = form.cleaned_data.get('media_img')
            new_anime.synopsis = form.cleaned_data.get('synopsis')
            new_anime.type = form.cleaned_data.get('type')
            new_anime.episodes = form.cleaned_data.get('episodes')
            new_anime.save()
            return redirect('animemaster-anime')
    else:
        form = AnimeForm()
    return render(request, 'animemaster/add-anime.html', {'form' : form})