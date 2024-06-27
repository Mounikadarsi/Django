from django.urls import path
from . import views
urlpatterns =[
    path('First/',views.First_view),
    path('Second/',views.Second_view),
    path('Third/',views.Third_view),
]