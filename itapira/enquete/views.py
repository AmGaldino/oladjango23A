from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Olha, se você não me ama</h1><h2>caneta azul, azul caneta</h2>")

def index(request):
    return HttpResponse("<h1>Caneta azul</h1><h2>azul caneta</h2>")