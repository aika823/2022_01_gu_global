from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "solution"

urlpatterns = [
    path('', views.vc),
    path('VC', views.vc),
    path('YM', views.ym),
    path('MS', views.ms),
    path('YMS', views.yms),
    path('SONY', views.sony),
    path('USB', views.usb),
    path('MS_PHONE',views.ms_phone),
]