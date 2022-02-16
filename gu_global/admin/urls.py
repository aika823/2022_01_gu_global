from django.urls import path

from . import views

app_name = "admin"

urlpatterns = [
    path('', views.products),
    path('login', views.login),
    
    path('category', views.category),
    path('category/create', views.category_create),
    path('category/<int:id>', views.category_view),

    path('product', views.products),
    path('product/create', views.products_create),
    path('product/<int:id>', views.products_view),

    path('contact', views.contact),
    path('contact/create', views.contact_create),
    path('contact/<int:id>', views.contact_view),
    
    path('notice', views.notice),
    path('notice/create', views.create_notice),
    path('notice/<int:id>', views.view_notice),

    path('video', views.video),
    path('video/create', views.video_create),
    path('video/<int:id>', views.video_view),
    
    path('popup', views.popup),
    path('popup/create', views.popup_create),
    path('popup/<int:id>', views.popup_view),

    # path('download', views.download),
    # path('download/create', views.download_create),
    # path('download/<int:id>', views.download_view),

    path('create', views.create),
    path('delete', views.delete),

    path('update_image', views.update_image),
    path('update_detail_image', views.update_detail_image),
]