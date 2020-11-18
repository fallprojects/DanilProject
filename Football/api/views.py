from django.shortcuts import render,redirect
from .filters import TableFilterSet
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

def about_game_page(request):
    context = {}
    return render(request,'api/about_game.html',context)

def table_page(request):
    team = Teams.objects.all().order_by('-points')
    filterset= TableFilterSet(request.GET,queryset=team)
    team = filterset.qs
    context = {'team':team,'filterset':filterset}
    return render(request,'api/table.html',context)

def team_page(request,pk):
    team = Teams.objects.get(id=pk)
    command = team.players_set.all()
    context = {'command':command,'team':team}
    return render(request,'api/team.html',context)

def rates_page(request,pk):
    rates = Rates.objects.get(id=pk)
    if rates.results == 'draw':
        rates.money = rates.money * 2
    context = {'rates':rates}
    return render(request,'api/rates.html',context)