from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/page2.html')

def login(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h4>страница о нас</h4>")