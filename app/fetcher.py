import os
from abc import ABC, abstractmethod

from requests import get


env_vars = os.environ


class BaseJsonFetcher(ABC):
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

        return (self.fetched_data, self.stocks_list)


class HgBrasilFetcher(BaseJsonFetcher):
    @property
    def api_base_url(self):
        self.base_url = env_vars['HG_BRASIL_BASE_URL']
        self.key = env_vars['HG_BRASIL_KEY']

        return f'{self.base_url}?key={self.key}&symbol='

    @property
    def stocks_list(self):
        self.stocks_string = env_vars['HG_BRASIL_STOCKS']

        return self.stocks_string.split('.')
