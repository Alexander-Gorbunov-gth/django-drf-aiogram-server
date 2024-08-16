import json

from flower.utils.template import humanize

from app.loggers.loggers import debug_loger

persistent = True
enable_events = True
tasks_columns = "name,uuid,state,received,started,runtime"
state_save_interval = 120000

def format_task(task):
    name = task.kwargs.get("name")
    if name:
        task.name = name
        task.kwargs = ""
    return task