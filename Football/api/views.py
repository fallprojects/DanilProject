from django.shortcuts import render,redirect
from .models import *

def home_page(request):
    games = Games.objects.all()
    news = News.objects.all().order_by('-date_created')
    context = {'news':news,'games':games}
    return render(request,'api/home.html',context)

def news_page(request):
    context = {}
    return render(request,'api/news.html',context)

def games_page(request):
    game = Games.objects.all()
    context = {'game':game}
    return render(request,'api/games.html',context)

def about_game_page(request,pk):
    context = {}
    return render(request,'api/about_game.html',context)

def table_page(request):
    team = Teams.objects.all()
    context = {'team':team}
    return render(request,'api/table.html',context)

def team_page(request,pk):
    command = Teams.objects.get(id=pk)
    context = {'command':command}
    return render(request,'api/team.html',context)