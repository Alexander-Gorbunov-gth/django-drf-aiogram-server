from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.apps.api import models


@admin.register(models.CheckServerModel)
class ChecAdmin(ModelAdmin[models.CheckServerModel]):
    pass
