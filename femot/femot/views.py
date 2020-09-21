from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

def boards(request):
    return HttpResponse('Your board is here')

def index(request):
    return HttpResponse('Your index is here')