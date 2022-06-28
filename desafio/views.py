from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def una_vista(request):
    return HttpResponse("<h1> MI PERRO DINAMITA <h1/>  ")
