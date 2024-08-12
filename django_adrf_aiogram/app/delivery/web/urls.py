from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path, include

from app.config.application import DEBUG
from app.config.web import STATIC_ROOT, STATIC_URL

urlpatterns: list[URLResolver | URLPattern] = [
    path("api/v1/", include("app.apps.api.web.urls")),
    path("admin/", admin.site.urls),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
