from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='animemaster-home'),
    path('about/', views.about, name='animemaster-about'), #animemaster urls will handle anything in animemaster
    path('anime/', views.anime, name='animemaster-anime'),
    path('add/<int:pk>', views.addToList, name='addToList'),
    path('mylist/', views.mylist, name='animemaster-mylist'),
    path('unlist/<int:pk>', views.unlist, name='unlist-media'),

]