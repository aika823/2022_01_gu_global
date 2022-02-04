from django.urls import path

from . import views

app_name = "admin"

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    
    path('product', views.products),
    path('product/create', views.products_create),
    path('product/<int:id>', views.products_view),

    path('contact', views.contact),
    
    path('notice', views.notice),
    path('notice/create', views.create_notice),
    path('notice/<int:id>', views.view_notice),

    path('download', views.download),
    path('video', views.video),
    path('popup', views.popup),

    path('create', views.create),

    path('update_image', views.update_image),
    path('update_detail_image', views.update_detail_image),

    path('delete', views.delete)
]