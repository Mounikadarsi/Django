from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hydjobs(request):
    s="<h1>Hyderabad Jobs Information </h1>"
    return HttpResponse(s)
def Bngjobs(request):
    s="<h1>Bangloore Jobs Information </h1>"
    return HttpResponse(s)
def punejobs(request):
    s="<h1>Pune Jobs Information </h1>"
    return HttpResponse(s)
def Delhijobs(request):
    s="<h1>Delhi Jobs Information </h1>"
    return HttpResponse(s)
def Noidajobs(request):
    s="<h1>Noida Jobs Information </h1>"
    return HttpResponse(s)