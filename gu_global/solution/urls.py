from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "solution"

urlpatterns = [
    path('', views.vc),
    path('ym', views.ym),
    path('ms', views.ms),
    path('yms', views.yms),
    path('sony', views.sony),
]