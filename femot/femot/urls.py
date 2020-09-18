
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from femot.boards.views import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    #url(r'^users/', views.users, name='users'),
    url(r'^boards/', boards.views, name='boards'),
    #url(r'^topics/', views.topics, name='topics'),
    #url(r'^$', views.index,),
]
