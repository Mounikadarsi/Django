from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time(request):
    date=datetime.datetime.now()
    msg="<h1>This Program is used to display the current time in our system </h1><hr>"
    msg += "<h2> Now Server Time is:"+str(date)+"</h2>"
    return HttpResponse(msg)