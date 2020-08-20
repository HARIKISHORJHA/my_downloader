from django.contrib import admin
from django.urls import path
from home import views
from django.views.static import serve
from my_downloader import settings
urlpatterns = [
    path("",views.home,name="home"), 
    path("home",views.home,name="home"),
    path("index",views.index,name='index'),
    path("service", views.service,name="service"),
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),


]
