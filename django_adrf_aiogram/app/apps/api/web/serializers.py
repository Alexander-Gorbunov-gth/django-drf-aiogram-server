from adrf.serializers import ModelSerializer

from app.apps.api import models
from .tasks import check_task
from app.loggers.loggers import debug_loger


class CheckSerializer(ModelSerializer):

    async def acreate(self, validated_data):
        debug_loger.info("Start check Calary")
        check_task.delay()
        return await super().acreate(validated_data)

    class Meta:
        model = models.CheckServerModel
        fields = "__all__"
