from app.celery import celery_app
from app.utils.fetchers import HgBrasilFetcher
from app.utils.parsers import HgBrasilParser
from app.utils.mailers import HgBrasilMailer


@celery_app.task
def email_notifier():
    fetcher = HgBrasilFetcher()
    parser = HgBrasilParser()
    mailer = HgBrasilMailer()

    fetched_data = fetcher.fetch_data()
    parsed_data = parser.parse_data(fetched_data)

    mailer.send_email(parsed_data)
