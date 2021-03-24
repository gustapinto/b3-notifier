import logging
import os

from celery import Celery


env_vars = os.environ

DEFAULT_SCHEDULE = int(env_vars['TASKS_SCHEDULE_IN_SECONDS'])

celery_app = Celery('taks', broker='redis://redis:6379', include=[
    'app.tasks.hg_brasil'
])

celery_app.conf.beat_schedule = {
    'hg_brasil_email_notifier': {
        'task': 'app.tasks.hg_brasil.email_notifier',
        'schedule': DEFAULT_SCHEDULE,
    },
}
