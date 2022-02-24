from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "support"

urlpatterns = [
    path('', views.notice),
    path('certification', views.certification),
    path('download', views.download),
    path('video', views.video),
    path('contact', views.contact),
    path('contact/<int:id>', views.contact_more),
    path('contact_form', views.contact_form),
    path('notice', views.notice),
    path('notice_more', views.notice_more),
]