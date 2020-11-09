from django.shortcuts import render,redirect
from .models import *

def home_page(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request,'api/home.html',context)