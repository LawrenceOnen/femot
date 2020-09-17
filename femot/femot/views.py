from django.http import HttpResponse

def boards(request):
    return HttpResponse('Boards page')

def topics(request):
    return HttpResponse('topics')


def users(request):
    return HttpResponse('users')

def index(request):
    return HttpResponse('Homepage')