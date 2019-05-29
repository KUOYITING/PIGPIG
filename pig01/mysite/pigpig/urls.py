from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'pigpig'
urlpatterns = [
    path('', views.pigpig, name='pigpig'),
    path('index-cut/', views.indexCut, name='indexCut'),
    path('inner/', views.inner, name='inner'),
]