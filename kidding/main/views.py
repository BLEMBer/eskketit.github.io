from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return render(request, 'main/page2.html')

def login(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about_us.html')

def regist(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password = request.POST['password']

        myuser = User.objects.create_user(email, password, password)
        myuser.save()

        return redirect('main/login.html')

    return render(request, 'main/regist.html')