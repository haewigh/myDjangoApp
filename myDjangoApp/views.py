from django.shortcuts import render

from django.http import HttpResponse

def index(Response):
    return HttpResponse("HELLO WORLD!")
