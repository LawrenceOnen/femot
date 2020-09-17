
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^users/', views.home, name='users'),
    url(r'^boards/', views.board, name='boards'),
]
