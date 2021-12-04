from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets, name='tweets_index'),
    path('atualizar/', views.atualizar, name='atualizar')
]
