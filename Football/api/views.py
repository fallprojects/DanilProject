from django.shortcuts import render,redirect
from .models import *

def home_page(request):
    games = Games.objects.all()
    news = News.objects.all()
    context = {'news':news,'games':games}
    return render(request,'api/home.html',context)

def news_page(request):
    context = {}
    return render(request,'api/news.html',context)

def games_page(request):
    context = {}
    return render(request,'api/games.html',context)

def teams_page(request):
    teams = Teams.objects.all()
    context = {'teams':teams}
    return render(request,'api/teams.html',context)
