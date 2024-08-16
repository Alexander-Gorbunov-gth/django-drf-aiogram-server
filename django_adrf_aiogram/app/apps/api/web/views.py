from adrf.viewsets import ViewSet as aView
from rest_framework.response import Response

from app.apps.api.web import serializers
from app.apps.api import models
from app.loggers.loggers import debug_loger
from .tasks import check_task


class CheckView(aView):

    async def retrieve(self, request, pk):
        debug_loger.info("Start Celery Check")
        check_task.apply_async(
            kwargsrepr={"name": "Чек функции"}
        )
        return Response({"check": "Get request - True"})

    