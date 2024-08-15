from time import sleep
from celery import shared_task

from app.loggers.loggers import debug_loger


@shared_task
def check_task():
    sleep(20)
    debug_loger.info("Celery works correct")