from django.urls import path
from . import views

urlpatterns = [
    path('page', views.index),
    path('about', views.about),
    path('login', views.login),
    path('', views.regist),
]
