from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def boards(request):
    #return HttpResponse('Your board is here')
    board = Board.objects.all()
    #create a lit to hold names
    boards_names = list()