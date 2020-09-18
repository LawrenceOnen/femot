
# Create your views here.
from django.http import HttpResponse

def posts(request):
    return HttpResponse('Your post is here')