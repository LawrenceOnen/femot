
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    #url(r'^users/', views.users, name='users'),
    url(r'^boards/', views.boards, name='boards'),
    #url(r'^topics/', views.topics, name='topics'),
    url(r'^$', views.index,),
]
