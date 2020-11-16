from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('news/',news_page,name='news'),
    path('games/',games_page,name='games'),
    path('table/',table_page,name='table'),
    path('team/<int:pk>/',team_page,name='team'),
    path('about_game/',about_game_page,name='about_game'),
]
