from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def forum(request):
    return HttpResponse("Hello World")
