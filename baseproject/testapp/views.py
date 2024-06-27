from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def First_view(request):
    return HttpResponse("<h1> This is From First View </h1>")
def Second_view(request):
    return HttpResponse("<h1> This is From Second View </h1>")
def Third_view(request):
    return HttpResponse("<h1> This is From Third View </h1>")