from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def First(request):
    return HttpResponse('<title> First Function</title><h1>Hellow world</h1><h2> Hello All</h2><button><a href="Secound">Secound</a></button>')

def Secound(request):
    return HttpResponse('<title> Secound Function</title><h1> its working</h1> <h2> All ok</h2>')