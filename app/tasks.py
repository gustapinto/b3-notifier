import logging

from celery import Celery

from app.fetcher import HgBrasilFetcher
from app.parser import HgBrasilParser
from app.mailer import HgBrasilMailer


logging.basicConfig(filename='logs/task.log')

celery_app = Celery('tasks', broker='redis://redis:6379')

@celery_app.task
def hg_brasil_task():
    try:
        fetcher = HgBrasilFetcher()
        parser = HgBrasilParser()
        mailer = HgBrasilMailer()

        fetched_data = fetcher.fetch_data()
        parsed_data = parser.parse_data(fetched_data)

        mailer.send_email(parsed_data)
    except Exception as e:
        logging.info(e)

def run_tasks():
    hg_brasil_task.delay()

run_tasks()
