from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def mails(request):
    return HttpResponse("mails World")
