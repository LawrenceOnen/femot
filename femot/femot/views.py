from django.http import HttpResponse

def boards(request):
    return HttpResponse('about')

def topics(request):
    return HttpResponse('topics')


def users(request):
    return HttpResponse('users')