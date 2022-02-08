from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.list),
    path('detail', views.detail),
    path('detail/<str:product_name>', views.detail),
    path('<str:main_category>/<str:category_name>', views.category_list)
]