from django.conf.urls import url
from . import views
from django.contrib import admin


urlpatterns = [
    url('',views.index, name ='index'),
    url('contact',views.contact,name ='contact')
]