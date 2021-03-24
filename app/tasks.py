import logging
import os

from celery import Celery

from app.fetcher import HgBrasilFetcher
from app.parser import HgBrasilParser
from app.mailer import HgBrasilMailer


env_vars = os.environ

logging.basicConfig(filename='logs/task.log')

celery_app = Celery('tasks', broker='redis://redis:6379')

@celery_app.task
def hg_brasil_task():
        fetcher = HgBrasilFetcher()
        parser = HgBrasilParser()
        mailer = HgBrasilMailer()

        fetched_data = fetcher.fetch_data()
        parsed_data = parser.parse_data(fetched_data)

        mailer.send_email(parsed_data)

def run_tasks():
    default_task_schedule = int(env_vars['TASKS_SCHEDULE_IN_SECONDS'])

    celery_app.conf.beat_schedule = {
        'hg_brasil': {
            'task': 'app.tasks.hg_brasil_task',
            'schedule': default_task_schedule,
        },
    }

run_tasks()
