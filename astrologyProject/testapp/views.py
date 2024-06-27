from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    date=datetime.datetime.now()
    my_list=['The golden days a head',
             'Better to read more',
             'Study Hard To get a job',
             'propose u r girlfriend ']
    names_list=['Samyuktha','Sravya','Swetha','Anushka','Prajwal']
    h=int(date.strftime('%H'))
    if h < 12:
        s = "Good Morning"
    elif h < 16:
        s = "Good Afternoon"
    elif h <21:
        s="Good Evening"
    else :
        s="Good Night"
    name=random.choice(names_list)
    msg=random.choice(my_list)
    my_dict={'time':date,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astro.html',my_dict)