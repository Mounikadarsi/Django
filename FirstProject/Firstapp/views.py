from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(res):
    s="Hello"
    return HttpResponse(s)