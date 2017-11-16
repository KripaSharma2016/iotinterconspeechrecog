'''
Created on Nov 16, 2017

@author: kripa
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.home)
]

