from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Wish2(request):
    return HttpResponse("<h1> This is Fron Second Application </h1>")