from django.conf.urls import url
from django.contrib import admin
from femot.boards.models import Board

def boards(request):
    #return HttpResponse('Your board is here')
    board = Board.objects.all()
    #create a lit to hold names
    boards_names = list()