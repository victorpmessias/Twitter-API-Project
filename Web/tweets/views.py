from django.shortcuts import render, redirect
from sys import path
path.append('../')
from main import get_trends_route, get_trends_att




# Create your views here.
def tweets(request):
    trends = get_trends_route()
    if not trends:
        get_trends_att()
        trends = get_trends_route()
    trends = trends[-51:-1]
    return render(request, 'tweets/tweets.html', {"trends": trends})


def atualizar(request):
    get_trends_att()
    trends = get_trends_route()

    return redirect('tweets_index')
