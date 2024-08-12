from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from app.apps.api.web import views

router = DefaultRouter()

router.register("check", views.CheckView, basename="check")

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", auth_views.obtain_auth_token),
]
