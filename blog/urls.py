
from django.urls import *
from django.conf.urls import include, url
from blog import views

urlpatterns = [
        url('^testblog/$',views.testblog,name='testblog'),
        url('^testjq/$', views.testjquery, name='testjq'),
    ]