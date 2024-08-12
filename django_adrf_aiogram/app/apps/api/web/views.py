from adrf.viewsets import ModelViewSet as aModelView

from app.apps.api.web import serializers
from app.apps.api import models


class CheckView(aModelView):
    serializer_class = serializers.CheckSerializer
    queryset = models.CheckServerModel
