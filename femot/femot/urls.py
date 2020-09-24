
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from 

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^users/', views.users, name='users'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    #url(r'^topics/', views.topics, name='topics'),
    url(r'^$', views.index,),
]
