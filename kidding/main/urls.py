from django.urls import path
from . import views

urlpatterns = [
    path('page', views.index, name='page'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('', views.regist, name='regist'),
]
