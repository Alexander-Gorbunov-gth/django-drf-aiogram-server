import logging
import os
from logging.handlers import RotatingFileHandler

from app.config.web import STATIC_ROOT

os.makedirs(f"{STATIC_ROOT}/log_file", exist_ok=True)

formatter = logging.Formatter(
    "%(asctime)s, %(levelname)s, %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S"
)

# Общий логгер для отладки в процессе разработки проекта
debug_loger = logging.getLogger("debug_loger")
handler_debug = RotatingFileHandler('static/log_file/debug_loger.log', maxBytes=10000000, backupCount=3)
debug_loger.setLevel(logging.INFO)
debug_loger.addHandler(handler_debug)