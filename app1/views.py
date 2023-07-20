from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def starting(request):
    return HttpResponse('<h1>abbulu.........</h1>')

from django.http import HttpResponse
def ending(request):
    return HttpResponse('<h1>come on.......</h1>')