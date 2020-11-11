from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('news/',news_page,name='news'),
    path('games/',games_page,name='games'),
    path('teams/',teams_page,name='teams')
]
