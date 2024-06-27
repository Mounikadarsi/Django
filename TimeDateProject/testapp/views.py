from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetime_info(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg="<h1> Hello Guest Very Good "
    if h<12:
        msg += "Morning !!!!!"
    elif h<16:
        msg += "Afternoon !!!!!"
    elif h<21:
        msg += "Evening !!!!!"
    else:
        msg += "Night !!!!"
    msg += "<h1> <hr>"
    msg += "<h1> Now The Server Time is :"+str(date)+"</h1>"
    return HttpResponse(msg)