from django.urls import path
from django.shortcuts import render

from mcapp import views


urlpatterns = [    
    path('', views.checklist),
    path('afisha', views.afisha, name="afisha"),
    path('music', views.music, name="music"),
    path('video', views.video, name="video"),
    path('merch', views.merch, name="merch"),
    path('youtube', views.youtube, name="youtube"),
]