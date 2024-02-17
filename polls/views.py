from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("I'm looking for a way to understand")


def home(request):
    return HttpResponse('This is a gateway to the unknown world')

# Create your views here.
