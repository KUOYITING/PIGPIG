from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'pigpig'
urlpatterns = [
    path('', views.pigpig, name='pigpig'),
    path('index-cut/', views.indexCut, name='indexCut'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
    path('c/', views.c, name='c'),
    path('d/', views.d, name='d'),
    path('e/', views.e, name='e'),
    path('f/', views.f, name='f'),
    path('g/', views.g, name='g'),
    path('h/', views.h, name='h'),
    path('i/', views.i, name='i'),
    path('j/', views.j, name='j'),
    path('k/', views.k, name='k'),


]