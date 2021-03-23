from abc import ABC, abstractmethod
from smtpd import SMTPServer
from smtplib import SMTP_SSL
from ssl import create_default_context


env_vars = os.environ


class BaseMailer(ABC):
    def __init__(self):
        smtp_local_host = env_vars['SMTP_LOCAL_HOST']
        smtp_local_port = int(env_vars['SMTP_LOCAL_PORT'])
        smtp_remote_host = env_vars['SMTP_REMOTE_HOST']
        smtp_remote_port = int(env_vars['SMTP_REMOTE_PORT'])

        self.smtp_local_address = (smtp_local_host, smtp_local_port)
        self.smtp_remote_address = (smtp_remote_host, smtp_remote_port)

        self.sender_email = env_vars['SENDER_EMAIL']
        self.sender_password = env_vars['SENDER_PASSWORD']
        self.receiver_email = env_vars['RECEIVER_EMAIL']

        self.parsed_data = []

        self.initialize_smtp_server()

    @property
    @abstractmethod
    def email_body(self):
        pass

    def initialize_smtp_server(self):
        SMTPServer(self.smtp_local_address, self.smtp_remote_address)

    def send_email(self, parsed_data):
        self.parsed_data = parsed_data

        context = create_default_context()

        with SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, self.email_body)


class HgBrasilMailer(BaseMailer):
    @property
    def email_body(self):
        plain_text_body = ''

        for stock_data in self.parsed_data:
            stock_display = stock_data[0]

            plain_text_body += stock_display

        return plain_text_body
