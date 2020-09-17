from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def board(request):
    return HttpResponse('Your board is here')