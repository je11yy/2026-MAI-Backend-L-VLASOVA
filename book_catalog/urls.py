from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("web/", include("catalog.urls_web")),
    path("api/", include("catalog.urls_api")),
]