from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "company"

urlpatterns = [
    path('', views.intro),
    path('org', views.org),
    path('history', views.history),
    path('partner', views.partner),
    path('works', views.works),
    path('contact', views.contact),
]