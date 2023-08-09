from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1> Welcome to the help desk ticket service <h1>')

def about(request):
    return HttpResponse('<h1> About this page <h1>')




