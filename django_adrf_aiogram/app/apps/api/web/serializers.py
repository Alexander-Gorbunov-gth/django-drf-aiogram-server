from adrf.serializers import ModelSerializer

from app.apps.api import models
from app.loggers.loggers import debug_loger


class CheckSerializer(ModelSerializer):

    class Meta:
        model = models.CheckServerModel
        fields = "__all__"
