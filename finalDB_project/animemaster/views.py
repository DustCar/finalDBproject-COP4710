from django.shortcuts import render, redirect
from .models import mediaAnime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AnimeForm
from .filters import listFilter

def welcome(request):
    return render(request, 'animemaster/welcome.html')

def home(request):
    return render(request, 'animemaster/home.html') # pass it as our third argument (pass the data into the template)

def anime(request):
    anime_list = mediaAnime.objects.all().order_by('-id')
    l_filter = listFilter(request.GET, queryset=anime_list)
    filter_count = l_filter.qs.count()
    if (anime_list.count()==filter_count):
        equal = True
    else:
        equal = False
    return render(request, 'animemaster/anime.html', {'anime_list': l_filter, 'filter_count': filter_count, 'l_equals': equal})

def details(request, pk):
    anime = mediaAnime.objects.get(id=pk)

    return render(request, 'animemaster/details.html', {'curr_anime': anime})


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