from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def start(request):
    return HttpResponse('<h1>we are developers</h1>')

from django.http import HttpResponse
def end(request):
    return HttpResponse('<h1>vadilestunnava</h1>')