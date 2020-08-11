from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.home,name="home"), 
    path("home",views.home,name="home"),
    path("index",views.index,name='index'),
    path("service", views.service,name="service"),
    

]
