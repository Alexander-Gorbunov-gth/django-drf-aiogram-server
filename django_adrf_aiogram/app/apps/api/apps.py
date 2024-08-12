from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.apps.api"

    def ready(self) -> None:
        # Without this import, admin panel will not include this app
        from app.apps.api.web import admin  # noqa: F401 (unused-import)
