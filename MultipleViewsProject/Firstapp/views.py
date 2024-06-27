from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Wish1(request):
    return HttpResponse("<h1> This is Fron Fist Application </h1>")