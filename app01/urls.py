from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views


urlpatterns = patterns('',

    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^hostlist/', views.hostlist),
    url(r'^addhost/', views.addhost),
)
