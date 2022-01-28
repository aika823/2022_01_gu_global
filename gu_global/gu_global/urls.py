from django.urls import path, include
from company.views import index

urlpatterns = [
    path("", index),
    path("admin/", include("admin.urls")),
    path("company/", include("company.urls")),
    path("products/", include("products.urls")),
    path("support/", include("support.urls")),
    path("solution/", include("solution.urls")),
]
