from adrf.serializers import ModelSerializer

from app.apps.api import models


class CheckSerializer(ModelSerializer):
    class Meta:
        model = models.CheckServerModel
        fields = "__all__"
