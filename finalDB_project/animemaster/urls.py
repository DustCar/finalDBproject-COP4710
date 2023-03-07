from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='animemaster-home'),
    path('about/', views.about, name='animemaster-about'), #animemaster urls will handle anything in animemaster
]