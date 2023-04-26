from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='animemaster-welcome'),
    path('home/', views.home, name='animemaster-home'),
    path('about/', views.about, name='animemaster-about'), #animemaster urls will handle anything in animemaster
    path('anime/', views.anime, name='animemaster-anime'),
    path('add/<int:pk>', views.addToList, name='add-media'),
    path('mylist/', views.mylist, name='animemaster-mylist'),
    path('unlist/<int:pk>', views.unlist, name='unlist-media'),
    path('remove/<int:pk>', views.remove, name='remove-media'),
    path('details/<int:pk>', views.details, name='details-media'),
    path('update/<int:pk>', views.update, name='update-media'),
    path('anime/add/', views.addAnime, name='add-anime')
]