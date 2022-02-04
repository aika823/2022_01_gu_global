from django.urls import path, include
from company.views import index

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", index),
    path("admin/", include("admin.urls")),
    path("company/", include("company.urls")),
    path("products/", include("products.urls")),
    path("support/", include("support.urls")),
    path("solution/", include("solution.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
