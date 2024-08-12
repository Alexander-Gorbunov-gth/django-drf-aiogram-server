from django.db import models


class BaseModel(models.Model):

    create_date_time = models.DateTimeField(
        "Запись создана", auto_now_add=True, blank=True
    )
    update_date_time = models.DateTimeField(
        "Последнее изменение", auto_now=True, blank=True
    )

    class Meta:
        abstract = True


class CheckServerModel(BaseModel):
    """Чек сервера"""
    text = models.TextField("Some text")
    number = models.IntegerField("Some number", blank=True, null=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Тест сервера"
        verbose_name_plural = "Тест сервера"
