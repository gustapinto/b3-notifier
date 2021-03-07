from abc import ABC, abstractmethod

from requests import get

from app.app import flask_app

class BaseFetcher(ABC):
    def __init__(self):
        self.fetched_data = []

    @property
    @abstractmethod
    def api_base_url(self):
        pass

    @property
    @abstractmethod
    def stocks_list(self):
        pass

    def fetch_data(self):
        for stock in self.stocks_list:
            url = self.api_base_url + stock

            json_response = get(url).json()

            self.fetched_data.append(json_response)

        return self.fetched_data


class HgBrasilFetcher(BaseFetcher):
    @property
    def api_base_url(self):
        self.base_url = flask_app.env_vars['HG_BRASIL_BASE_URL']
        self.key = flask_app.env_vars['HG_BRASIL_KEY']

        return self.base_url + '?key=' + self.key + '&symbol='

    @property
    def stocks_list(self):
        self.stocks_string = flask_app.env_vars['HG_BRASIL_STOCK']

        return self.stocks_string.split('.')
