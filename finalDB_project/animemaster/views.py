from django.shortcuts import render
from .models import Post # from the models files in current package

def home(request):
    # key is 'post' and the value is the list of posts from the top
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'animemaster/home.html', context) # pass it as our third argument (pass the data into the template)

def about(request):
    return render(request, 'animemaster/about.html', {'title': 'About'})