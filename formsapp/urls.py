from django.contrib import admin
from django.urls import path, include
from formsapp import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    url('saveCriteria', views.saveCriteria, name='saveCriteria'),
    url('getRecom', views.getRecom, name='getRecom')
]
