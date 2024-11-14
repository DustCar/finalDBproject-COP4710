from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.welcome, name='animemaster-welcome'),
    path('home/', views.home, name='animemaster-home'),
    path('anime/', views.anime, name='animemaster-anime'),
    path('add/<int:pk>', user_views.addToList, name='add-media'),
    path('mylist/', user_views.mylist, name='animemaster-mylist'),
    path('unlist/<int:pk>', user_views.unlist, name='unlist-media'),
    path('remove/<int:pk>', views.remove, name='remove-media'),
    path('details/<int:pk>', views.details, name='details-media'),
    path('update/<int:pk>', views.update, name='update-media'),
    path('anime/add/', views.addAnime, name='add-anime'),
    path('mylist/update/<int:pk>', user_views.updateStat, name='update-mylist'),
]