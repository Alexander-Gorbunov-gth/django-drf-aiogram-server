from app.config import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL", cast=str, default="redis://localhost:6379")
CELERY_RESULT_BACKEND = env("CELERY_BROKER_URL", cast=str, default="redis://localhost:6379")
