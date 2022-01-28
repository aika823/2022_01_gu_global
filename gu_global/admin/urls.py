from django.urls import path

from . import views

app_name = "admin"

urlpatterns = [
    path('', views.index),
    path('login', views.login),

    path('products', views.products),
    path('contact', views.contact),
    
    path('notice', views.notice),
    path('notice/create', views.create_notice),
    path('notice/<int:id>', views.view_notice),

    path('download', views.download),
    path('video', views.video),
    path('popup', views.popup),

    

    path('create', views.create),


    # path('create/<str:table>', views.create_type),
    # path('create/<str:table>/<int:id>', views.create_room),
    
    # path('update_image', views.update_image),
    
    # path('<str:table>/<str:id>', views.detail),

    # path('reservation/room/<int:room_id>', views.reservation),

    # path('peak_season', views.peak_season),
    # path('notification', views.notification),
    # path('delete', views.delete),
]