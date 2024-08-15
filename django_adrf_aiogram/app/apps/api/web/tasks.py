from time import sleep
from celery import shared_task


@shared_task
def check_task():
    sleep(10)
    print("Celery works")