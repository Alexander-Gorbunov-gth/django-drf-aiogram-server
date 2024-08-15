from adrf.serializers import ModelSerializer

from app.apps.api import models
from .tasks import check_task


class CheckSerializer(ModelSerializer):

    async def acreate(self, validated_data):
        print("Start check Calary")
        check_task()
        return await super().acreate(validated_data)

    class Meta:
        model = models.CheckServerModel
        fields = "__all__"
