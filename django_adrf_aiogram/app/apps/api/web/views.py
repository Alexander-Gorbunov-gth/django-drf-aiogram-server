from adrf.viewsets import ModelViewSet as aModelView

from app.apps.api.web import serializers
from app.apps.api import models
from app.loggers.loggers import debug_loger


class CheckView(aModelView):
    serializer_class = serializers.CheckSerializer
    queryset = models.CheckServerModel

    async def acreate(self, request, *args, **kwargs):
        debug_loger.info("Start check Calary")
        return super().acreate(request, *args, **kwargs)