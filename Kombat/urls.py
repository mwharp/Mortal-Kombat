from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name= "home"),
    url(r'^about/$',views.about, name = 'about'),
    url(r'^character/$',views.character, name = 'character'),
    url(r'^frames/$',views.frames, name = 'frames'),
    url(r'^KanoHome/$',views.KanoHome, name = 'KanoHome'),
    url(r'^NightwolfHome/$',views.NightwolfHome, name = 'NightwolfHome'),
    url(r'^JadeHome/$',views.JadeHome, name = 'JadeHome'),
    url(r'^SubZeroHome/$',views.SubZeroHome, name = 'SubZeroHome'),
]

urlpatterns += staticfiles_urlpatterns()